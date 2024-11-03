from langchain.vectorstores import FAISS
from langchain.embeddings import SentenceTransformerEmbeddings
import faiss

# Sample documents to add to the vector store
documents = [
    {"id": "1", "text": "How to create an item in the system."},
    {"id": "2", "text": "Instructions for updating an item in the database."},
    {"id": "3", "text": "Deleting data from the system."}
]

# Convert documents into embeddings
embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
texts = [doc["text"] for doc in documents]
metadata = [{"id": doc["id"]} for doc in documents]

# Create FAISS vector store
vector_store = FAISS.from_texts(texts=texts, embedding=embeddings, metadatas=metadata)
