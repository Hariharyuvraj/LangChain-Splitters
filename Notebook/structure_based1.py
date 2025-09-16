from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

loader = PyPDFLoader('Interview_ques.pdf')

docs = loader.load()

# splitter making

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 50,
    chunk_overlap = 0
)

result = splitter.split_documents(docs)

print(result)

print(len(result))

print(type(result))

# On the basis of structure_splitter basis we have split the documents 
# In this splitter it keeps the meaning of the words/ sentence
# with the help of "PyPDFLoader" we load a pdf and then used" "RecursiveCharacterTextSplitter"