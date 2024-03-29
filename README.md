# RAG App using LangChain

![](https://github.com/ChloeHeekSuh/finetune-langchain/blob/main/Streamlit-finetune_app_2.gif)

### Configuration Setup:
Utilized the LangChain library for language model interaction.
Configured the project using environment variables loaded from a .env file(It has an OpenAI API key like 'OPENAI_API = YOUR API KEY').

### Data Integration:
Established a connection to a MySQL database using SQL database from LangChain.
Incorporated a few-shot dataset (few_shots) containing examples of SQL queries and their corresponding results.

### Embeddings and Vectorization:
Employed Hugging Face's sentence-transformers model for generating embeddings.
Created a vector store using Chroma from langchain for efficient storage and retrieval of vectorized examples.

### Semantic Similarity:
Implemented a SemanticSimilarityExampleSelector to identify the most relevant few-shot examples based on semantic similarity.

### Prompt Templates:
Defined a FewShotPrompt template for constructing prompts with few-shot examples.
Specified input variables for questions, SQL queries, SQL results, and answers.

### Execution and Output:
Created an SQL Database Chain to interact with the language model, the database, and the few-shot examples.
Executed the project by running a sample question through the database chain.

### Result:
Printed the output of the query to demonstrate successful integration and execution.
