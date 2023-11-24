from langchain.llms import OpenAI
from langchain.prompts.prompt import PromptTemplate
# from langchain.chains import LLMChain
from dotenv import dotenv_values
from langchain.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.prompts import SemanticSimilarityExampleSelector
from langchain.chains.sql_database.prompt import PROMPT_SUFFIX, _mysql_prompt
from langchain.prompts import FewShotPromptTemplate
from few_shots import few_shots



config = dotenv_values("C:/lets_play/finetune-langchain/.env")
llm = OpenAI(openai_api_key= config["OPEN_API_KEY"])


def get_few_shots_db_chain():
    db_user = "root"
    db_password = "pass"
    db_host = "localhost"
    db_name = "atliq_tshirts"
    
    db= SQLDatabase.from_uri(f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}", sample_rows_in_table_info=3)
    
    embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
    to_vectorize = [" ".join(example.values())for example in few_shots]
    vectorstore = Chroma.from_texts(to_vectorize, embedding=embeddings, metadatas=few_shots)
    example_selector = SemanticSimilarityExampleSelector(
      vectorstore=vectorstore,
      k=2,
    )

    example_prompt = PromptTemplate(
    input_variables=["Question", "SQLQuery", "SQLResult","Answer",],
    template="\nQuestion: {Question}\nSQLQuery: {SQLQuery}\nSQLResult: {SQLResult}\nAnswer: {Answer}",
    )

    few_shots_prompt = FewShotPromptTemplate(
      example_selector=example_selector,
      example_prompt=example_prompt,
      prefix=_mysql_prompt,
      suffix=PROMPT_SUFFIX,
      input_variables=["input", "table_info", "top_k"],
    )

    db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True, prompt=few_shots_prompt)
    return db_chain


if __name__ == "__main__":
    db_chain = get_few_shots_db_chain()
    print(db_chain.run("How much is the price of all blue nike t-shirts?"))