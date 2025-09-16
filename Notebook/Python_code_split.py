from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter,Language

text = """from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence

OPENAI_API_KEY = "Paste your_api_key here"

llm = ChatOpenAI(model="gpt-3.5-turbo", api_key=OPENAI_API_KEY)
parser = StrOutputParser()

# Prompt 1 → summary
prompt1 = PromptTemplate(
    template="Summarize this text in one line:\n{text}",
    input_variables=["text"]
)

# Prompt 2 → translate
prompt2 = PromptTemplate(
    template="Translate this into Marathi:\n{summary}",
    input_variables=["summary"]
)

# Chain step by step
summary_chain = prompt1 | llm | parser
translate_chain = prompt2 | llm | parser

chain = RunnableSequence(
    first=summary_chain,
    last=translate_chain
)

result = chain.invoke({
    "text": "Artificial Intelligence helps machines think and learn like humans."
})

print(result)
"""
# splitter making

splitter = RecursiveCharacterTextSplitter.from_language(
    language = Language.PYTHON,
    chunk_size = 100,
    chunk_overlap = 0
)

result = splitter.split_text(text)

print(result)


# In this code we can split the "python" code as per the chunks size

# Using the directly py_code in the code 