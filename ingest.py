import os
from dotenv import load_dotenv
import google.generativeai as genai
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS

# Load the secret API keys from the .env file
load_dotenv()
print("API keys loaded.")

# Configure the Google AI client
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
print("Google AI client configured.")

# Define the path to your documents and where to save the index
DATA_PATH = "docs/"
DB_FAISS_PATH = "faiss_index"

def create_vector_db():
    # Step 1: Load all text documents from the 'docs' folder
    loader = DirectoryLoader(DATA_PATH, glob='*.txt', loader_cls=TextLoader)
    documents = loader.load()
    print(f"Loaded {len(documents)} documents.")

    # Step 2: Split the documents into smaller, manageable chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = text_splitter.split_documents(documents)
    print(f"Split documents into {len(chunks)} chunks.")

    # Step 3: Convert the text chunks into numerical vectors (embeddings) using Google AI
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

    # Step 4: Create the FAISS vector store and save it locally
    db = FAISS.from_documents(chunks, embeddings)
    db.save_local(DB_FAISS_PATH)
    print(f"Vector database has been created and saved locally at: {DB_FAISS_PATH}")

# This part ensures the function runs when you execute the script
if __name__ == "__main__":
    create_vector_db()