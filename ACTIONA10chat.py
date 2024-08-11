# https://www.youtube.com/watch?v=QmTtU-qbjUA&t=623s
# 1. Run Ollama pull llama3 
# 2. Run streamlit run ACTIONA10chat.py

from pandasai.llm.local_llm import LocalLLM
import streamlit as st
import pandas as pd
from pandasai import SmartDataframe

def chat_with_csv(df,query):
    llm=LocalLLM(api_base='http://localhost:11434/v1',
                model='llama3')
    pandas_ai=SmartDataframe(df,config={'llm':llm})
    result=pandas_ai.chat(query)
    return result

st.set_page_config(page_title="OnePlus Business Performance", page_icon=":moneybag:", layout="wide")
st.title("OnePlus Business Performance")

# Load the data
input_csvs = st.sidebar.file_uploader("Upload your CSV files", type=["csv"], accept_multiple_files=True)
if input_csvs:
    # Create a list of file names
    file_names = [file.name for file in input_csvs]
    # Display the selectbox with file names
    selected_file = st.sidebar.selectbox("Select a file", file_names)
    # Find the index of the selected file name
    selected_index = file_names.index(selected_file)
    st.info(f"File loaded successfully: {selected_file}")
    data = pd.read_csv(input_csvs[selected_index])
    st.dataframe(data.head(3),use_container_width=True)
    st.info("Chat Below")
    input_text = st.text_area("Enter your query")

    if input_text:
        if st.button("Chat"):
            st.info("Processing..."+input_text)
            result=chat_with_csv(data,input_text)
            st.success(result)
