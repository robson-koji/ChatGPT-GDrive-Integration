import os
from langchain.document_loaders import GoogleDriveLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma


DB_DIR = "../db"

# Google Drive content retrieval
if 'GDRIVE_FOLDER_ID' not in os.environ:
    raise Exception(f"Environment variable GDRIVE_FOLDER_ID is not set.")

folder_id = os.getenv('GDRIVE_FOLDER_ID')

loader = GoogleDriveLoader(folder_id=folder_id, recursive=False)
docs = loader.load()

# Document splitting
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=4000, chunk_overlap=0, separators=[" ", ",", "\n"]
)
texts = text_splitter.split_documents(docs)

# Chroma database creation
embeddings = OpenAIEmbeddings()
db = Chroma.from_documents(
        texts,
        embeddings,
        persist_directory=DB_DIR
    )
db.persist()


