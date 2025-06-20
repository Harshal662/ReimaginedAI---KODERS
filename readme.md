# AI-Powered Change Impact Analyzer (RiskIQ.AI)

In today's fast-paced enterprise environments, change decisions are often made without real-time impact analysis, leading to significant inefficiencies, blind spots, and potential risks. Our project aims to address this critical gap in the change management process through the integration of AI and data-driven automation.

Currently, change requests are evaluated manually across fragmented systems, resulting in delays, inconsistencies, and an increased likelihood of oversight. Colleagues spend hours manually analyzing the impact of proposed changes without access to contextual insights, which drastically reduces overall productivity. Moreover, the absence of predictive analytics in the decision-making process leads to high-risk changes being approved, jeopardizing compliance, operational stability, and strategic alignment.

To solve these challenges, we are building a centralized, AI-powered Change Impact Analyzer that will:

- Automatically evaluate change requests by integrating with various systems.
- Provide real-time, contextual insights to assist colleagues in making informed decisions faster.
- Leverage predictive analytics to assess the risk level of proposed changes, flagging high-risk scenarios before approval.

This solution will streamline processes, empower employees with actionable intelligence, and significantly reduce the operational risks associated with change management.

## Project Structure
```
app.py
embed_data_from_pickle.py
embed_data.py
embed_jsonl_data.py
llama_inference.py
main.py
pinecone_setup.py
query_bot.py
readme.md
static/
    css/
        style.css
    js/
        script.js
    index.html
    logo.png
user_interface.py
Sample Test Data/
    change_impact.xlsx
    processes.xlsx
    reports.xlsx
    requirements.xlsx
    stakeholder.xlsx
```


## How to Run the Project

### Prerequisites

- Python 3.x
- Flask
- Requests
- Pinecone
- Joblib
- Pandas
- Scikit-learn

### Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/Harshal662/ReimaginedAI---KODERS.git
    cd ReimaginedAI---KODERS
    ```

2. Install the required Python packages:
    ```sh
    pip install -r requirements.txt
    ```

3. Set up the Pinecone index:
    ```python
    from pinecone_setup import initialize_pinecone
    initialize_pinecone()
    ```

4. Run the Flask server:
    ```sh
    python app.py
    ```

5. Open *localhost* in a web browser to interact with the RiskIQ.AI model.

### Usage

- **Chatbot Interface**: Interact with the RiskIQ.AI model through the web interface. Type/upload a business requirement and fill other fields to receive response from the model.
- **Embedding Data**: Use the scripts `embed_data_from_pickle.py`, `embed_data.py`, and `embed_jsonl_data.py` to generate embeddings and store them in Pinecone.


### For More Detail about Project Achitecture [click here](project.md)
