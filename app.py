from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
from langchain.document_loaders import DataFrameLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_openai import AzureOpenAIEmbeddings, AzureChatOpenAI
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA

app = Flask(__name__)
CORS(app)

# Load documents only once (optional optimization)
def load_documents():
    file_paths = {
        "stakeholders": "", # xlsx file loaction
        "requirements": "",
        "processes": "",
        "change_impact": "",
        "reports": ""
    }

    all_docs = []

    for name, path in file_paths.items():
        df = pd.read_excel(path)
        loader = DataFrameLoader(df.astype(str), page_content_column=df.columns[0])
        docs = loader.load()
        for doc in docs:
            doc.metadata["source"] = name
        all_docs.extend(docs)

    splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    return splitter.split_documents(all_docs)

# Initialize LLM and vector store
def initialize_chain():
    documents = load_documents()

    embedding = AzureOpenAIEmbeddings(
        deployment="text-embedding-3-large-2",
        model="text-embedding-3-large",
        azure_endpoint="",
        openai_api_key="",
        openai_api_version="2024-12-01-preview"
    )

    vectorstore = FAISS.from_documents(documents, embedding)
    retriever = vectorstore.as_retriever()

    llm = AzureChatOpenAI(
        deployment_name="gpt-4o",
        model="gpt-4o",
        azure_endpoint="",
        openai_api_key="",
        openai_api_version="2024-12-01-preview",
        temperature=0
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True
    )

    return qa_chain

# Instantiate chain once
qa_chain = initialize_chain()

@app.route('/analyze', methods=['POST'])
def analyze_custom_query():
    try:
        data = request.get_json()
        title = data.get("title")
        desc = data.get("desc")
        summary = data.get("summary")
        reqType = data.get("reqType")
        priority = data.get("priority")
        roles = data.get("roles")
        departments = data.get("departments")

        required_fields = ['title', 'desc', 'summary', 'reqType', 'priority', 'roles', 'departments']

        if not all(field in data and data[field] for field in required_fields):
            return jsonify({"error": "Missing or empty parameter"}), 400
        
        query = f"""
            You are an AI-powered Change Impact Analyzer.

            A user has submitted a change related to process automation. Based on the details below, analyze and return a structured response.

            Input Data:
            {{
                "statement": "We are automating the compliance validation steps using an AI-powered monitoring system.",
                "types": "{reqType}",
                "priority": "{priority}",
                "role": "{roles}",
                "department": "{departments}",
                "description": "{desc}",
                "title": "{title}",
                "summary": "{summary}"
            }}

            Your tasks:

            1. Classify the "RiskLevel" (Low, Medium, High)
            2. Provide a numeric "ImpactScore" (0–100)
            3. Identify and list:
            - "ImpactedStakeholderRoles"
            - "ImpactedDepartments"
            - "AffectedProcesses" (name + status)
            - "RelatedRequirements" (summarized)
            4. Explain the "ReasonForImpact"
            5. Estimate the "TimeToImplement" as a *list of objects*, each with:
            - ["requirementsGathering", "modelIntegration", "stakeHolderTraining", "systemTesting"]
            - "estimate": time duration in days/weeks/months  
            6. Generate a "ShortSummary" of the risk assessment
            7. Optionally include a "ChartData" section for visualizing Risk vs Impact Dimensions
            8. Indicate the "InputDataRelevancePercentage" (0–100) — how much of the output is based directly on the dataset to the model versus AI’s general reasoning to complete the response.

            *Output Format*:
            - Respond with a valid *JSON object only*
            - *Do not* include any markdown, backticks, explanations, or additional formatting
            - Output must be strictly raw JSON
            """


        
        response = qa_chain(query)

        return jsonify({
            "result": response['result']
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)