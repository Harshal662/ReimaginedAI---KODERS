# RiskIQ.AI - Project Overview

Our project, AI-Powered Change Impact Analyzer, addresses the inefficiencies in project change management. Currently, change requests are evaluated manually across disconnected systems, leading to delays, reduced productivity, and high-risk approvals.

We aim to solve this by building an AI-driven tool that provides real-time impact analysis, contextual insights, and predictive risk assessment—enabling faster, smarter, and safer decision-making by leveraging various technologies such as Groq AI, Pinecone, Azure OpenAI to improve stakeholder engagement and satisfaction by providing relevant information and proactive timelines and graphs.

### Problem Statement

Change decisions in projects are made without real-time impact analysis, leading to delays, inefficiencies, and blind spots.

**Process:** Change requests are manually evaluated across fragmented systems, causing delays and inconsistencies.

**Colleague:** Teams spend excessive time analyzing changes without contextual insights, reducing productivity.

**Risk:** Lack of predictive analytics leads to high-risk changes being approved, jeopardizing compliance and stability.

### Solution introduction

We are building an AI-powered Change Impact Analyzer that automates the assessment of change requests. By integrating with existing systems and leveraging Azure OpenAI, the tool provides real-time insights, highlights affected stakeholders and processes, and predicts risk levels—enabling faster, data-driven, and safer change decisions.

### Explanation of Each File

- **embed_data_from_pickle.py**: Reads data from a `.pkl` file, generates embeddings using Azure OpenAI API, and stores the embeddings in Pinecone.
- **embed_data.py**: Reads data from a different source and generates embeddings using Azure OpenAI API.
- **embed_jsonl_data.py**: Reads data from a `.jsonl` file, generates embeddings using Azure OpenAI API, and stores the embeddings in Pinecone.
- **llama_inference.py**: Contains functions to initialize the ChatGroq client and generate responses using the ChatGroq model.
- **app.py**: The main entry point for the Flask application. Sets up the Flask server, Sets up the Flask server, handles socket connections, and defines API endpoints.
- **main.py**: Sets up the Flask server for json response directly from model
- **package.json**: Contains the dependencies required for the project.
- **pinecone_setup.py**: Contains the function to initialize the Pinecone index.
- **query_bot.py**: Contains functions to generate embeddings using Azure OpenAI API and to generate responses using the ChatGroq model. Integrates with Pinecone to query relevant documents.
- **readme.md**: Provides an overview of the project and instructions on how to run it.
- **static/**: Contains static files for the frontend interface.
    - **css/**: Contains the CSS file for styling the frontend interface.
        - **style.css**: The CSS file for styling the chatbot interface.
    - **js/**: Contains the JavaScript files for the frontend interface.
        - **script.js**: The JavaScript file for handling user input and displaying responses.
    - **index.html**: The HTML file for the model interface.
- **user_interface.py**: Contains the function to start the chatbot and handle user interactions.

## How the Project Works

### File Flow

1. **Data Embedding**:
    - **embed_data_from_pickle.py**: Reads data from a `.pkl` file, generates embeddings using Azure OpenAI API, and stores the embeddings in Pinecone.
    - **embed_data.py**: Reads data from a different source and generates embeddings using Azure OpenAI API.
    - **embed_jsonl_data.py**: Reads data from a `.jsonl` file, generates embeddings using Azure OpenAI API, and stores the embeddings in Pinecone.

2. **Query and Response Generation**:
    - **query_bot.py**: Contains functions to generate embeddings using Azure OpenAI API and to generate responses using the ChatGroq model. Integrates with Pinecone to query relevant documents.
    - **llama_inference.py**: Contains functions to initialize the ChatGroq client and generate responses using the ChatGroq model.

3. **Flask Application**:
    - **app.py**: The main entry point for the Flask application. Sets up the Flask server, handles socket connections, and defines API endpoints.

4. **Frontend Interface**:
    - **static/index.html**: The HTML file for the chatbot interface.
    - **static/css/style.css**: The CSS file for styling the chatbot interface.
    - **static/js/script.js**: The JavaScript file for handling user input and displaying responses.

### Preprocessing Steps

1. **Data Loading**:
    - Load data from various sources such as `.pkl` files, JSONL files, etc.

2. **Embedding Generation**:
    - Use Azure OpenAI API to generate embeddings for the loaded data.

3. **Storing Embeddings**:
    - Store the generated embeddings in Pinecone for efficient querying.

### Sample Data

To simulate real-world scenarios and validate the AI-Powered Change Impact Analyzer, a comprehensive set of test data has been created across five key domains:

**change_impact.xlsx**: Contains sample change requests with associated metadata such as change type, description, priority, and expected impact areas.

**processes.xlsx**: Lists business processes potentially affected by changes, including their IDs, names, owners, and criticality levels.

**reports.xlsx**: Includes reports and dashboards impacted by various changes, enabling traceability and dependency analysis.

**requirements.xlsx**: Represents functional and non-functional requirements linked to changes, useful for assessing scope and validation criteria.

**stakeholders.xlsx:** Maps stakeholders to processes and reports, helping identify impacted users and teams for notifications and approvals.

This structured dataset supports testing of end-to-end impact analysis, risk prediction, and stakeholder communication workflows in the prototype.


### Technologies Used
**Groq AI:** Used for generating responses using the ChatGroq model.
**Pinecone:** Used for storing and querying embeddings.
**Azure OpenAI:** Used for generating embeddings.
**Flask:** Used for setting up the backend server.
**Socket.IO:** Used for real-time communication between the frontend and backend.
**HTML/CSS:** Used for creating the frontend interface.

### RAG-Based Approach
This project uses a Retrieval-Augmented Generation (RAG) approach. The RAG model combines the strengths of retrieval-based and generation-based models. It retrieves relevant documents from a knowledge base (using Pinecone) and uses them to generate more accurate and contextually relevant responses (using Groq AI and Azure OpenAI).

### Architecture
The AI-Powered Change Impact Analyzer is designed using a robust, scalable pipeline combining Azure services, OpenAI models, and modern frameworks like LangChain and Flask. Below is a step-by-step breakdown of the architecture:

>Refer [this](input_output.md) file for detailed architecture diagram and explanation.

![alt text](<Pictures/arct dig.jpg>)

### Sample Input / Output 
>Refer [input_output.md](input_output.md) file for sample input/output.

### Project Features

- **Real-Time Impact Analysis** : Automatically evaluates the impact of change requests on processes, departments, and stakeholders.

- **AI-Powered Matching** :  Uses OpenAI embeddings to semantically match change inputs with internal documents.

- **Risk Scoring**  :   Generates impact scores and classifies changes as Low, Medium, or High risk.

- **Effort Estimation**  :   Provides timelines for requirements gathering, integration, training, and testing.

- **Automated Justification** :  Explains the reason for impact and relevance using AI-generated summaries.

- **Stakeholder Alerts**  :   Sends notifications via Power Automate to affected roles for faster response.

- **Natural Language Interface** :   GPT-4o answers user queries with context-aware insights from internal data.

- **User-Friendly Dashboard**  :   Simple UI for submitting requests and viewing results.



### Conclusion

The AI-Powered Change Impact Analyzer streamlines how organizations evaluate the impact of change requests. By combining semantic search, risk analysis, and natural language understanding, the system delivers fast, accurate, and actionable insights. It reduces manual effort, improves decision-making, and enhances compliance by automatically identifying affected processes, departments, and stakeholders. 