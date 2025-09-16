from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import CharacterTextSplitter

loader = PyMuPDFLoader('Interview_ques.pdf')

docs = loader.load()

splitter = CharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap =0,
    separator = ''
)

result = splitter.split_documents(docs)

print(result[1].page_content)

print(result[1].metadata)

print(type(result))

print(len(result))

# by using the 'CharacterTextSplitter' we can extract the pdf and split into the small chunk as per the required character

# In this code we used 'pypdf loader' to extract the pdf , after that we use 'CharacterTextSplitter' to split the text .

# we can set character size for splitting text.