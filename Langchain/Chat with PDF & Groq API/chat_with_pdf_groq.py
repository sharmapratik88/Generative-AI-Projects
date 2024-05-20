# Import necessary libraries for PDF loading, text splitting, embeddings, vector database, and environment variables
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA
from dotenv import load_dotenv
import os
import logging

# Load environment variables from a .env file
_ = load_dotenv()

# Configure logging to output to a file with a specific format and date format
logging.basicConfig(filename='logger.txt',
                    format='%(asctime)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S',
                    level=logging.INFO)

############################
# DEFINE CONSTANTS
############################
# Constants for the PDF file, text splitting, and model configurations
pdf_file = './pdfs/2404.07220v1.pdf'  # Path to the PDF file to be processed
chunk_size = 2500  # Size of text chunks for splitting the document
chunk_overlap = 100  # Number of characters to overlap between chunks
return_k = 3  # Number of top results to return from searches
model_name = 'mixtral-8x7b-32768'  # Name of the model for Groq LLM
embedding_model = 'mxbai-embed-large'  # Name of the embedding model for Groq LLM

############################
# READ DATA FROM PDF FILE
############################
# Log the start of reading the PDF file and load the content
logging.info('--------------------------------')
logging.info('Reading the PDF data!')
loader = PyPDFLoader(pdf_file)  # Initialize the PDF loader with the file path
docs = loader.load_and_split()  # Load and split the PDF into manageable chunks
logging.info(f'The total pages loaded as content: {str(len(docs))}')

############################
# Embeddings
############################
# Initialize the embeddings using the specified model
embeddings = OllamaEmbeddings(model=embedding_model)  # Ollama embeddings for document vectorization

############################
# Vector DB
############################
# Log the initialization of the Chroma vector database
logging.info('Initiating the Chroma DB vectorization step')
vectordb = Chroma.from_documents(documents=docs, embedding=embeddings)  # Create a Chroma vector database from documents
retriever = vectordb.as_retriever(search_kwargs={'k': return_k})  # Set up the Chroma DB as a retriever

############################
# GROQ LLM
############################
# Log the initialization of the GROQ LLM with the specified model
logging.info(f'Initiating the GROQ LLM with {model_name}')
# Initialize GROQ LLM with API key and model
llm = ChatGroq(groq_api_key=os.environ['GROQ_API_KEY'], model_name=model_name, temperature=0.6)
# Set up RetrievalQA with LLM and retriever
qa_with_sources = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever)

# Define the query to be asked to the LLM
query = 'What is Hybrid Search?'  # The question to be answered by the LLM
logging.info(f'Question to the LLM: {query}')
response = qa_with_sources(query)['result']  # Get the response from the retrieval QA chain
logging.info(f'Answer from the LLM: {response}')  # Log the answer received from the LLM
