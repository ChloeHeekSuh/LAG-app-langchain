from tuned_langchain import get_few_shots_db_chain
import streamlit as st

st.title("T-Shirts Stocks: Q & A")

question = st.text_input("Question: ")
if question:
  chain = get_few_shots_db_chain()
  response = chain.run(question)

  st.header("Answer")
  st.write(response)