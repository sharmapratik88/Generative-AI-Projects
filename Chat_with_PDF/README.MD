# Chat with PDF
Two projects described aim to create a Question-Answering (QA) system using PDF documents as the knowledge base.
Both projects involve processing PDF documents, embedding their content into a vector database, and utilizing language models for retrieval-based question answering. 
Here is a summary of each project:

## Project 1: PDF Q&A Retrieval with AWQ Quantization, Mistral Instruct v0.2, and vLLM
### Overview
This project demonstrates a comprehensive pipeline for processing PDF documents, embedding their content into a vector database, and utilizing a quantized language model for retrieval-based question answering.

#### Key Components
- **PDF Data Loading and Splitting**: Uses PyPDFLoader and RecursiveCharacterTextSplitter to load and split PDF documents into manageable chunks.
- **Vector Database Embedding**: Utilizes SentenceTransformerEmbeddings to embed text chunks and stores them in a Chroma vector database.
- **Model Quantization**: Implements AWQ quantization on the Mistral Instruct v0.2 model using AutoAWQForCausalLM and AutoTokenizer.
- **Retrieval-Based QA System**: Sets up a retrieval-based QA system using vLLM and Langchain's RetrievalQA.

- #### [Notebook Link](https://nbviewer.org/github/sharmapratik88/Generative-AI-Projects/blob/main/Chat_with_PDF/AWQ_Quantization/Chat_with_PDF_AWQ_Quantization.ipynb)

## Project 2: PDF Q&A Retrieval with LangChain & GROQ API
### Overview
This project is designed to create a QA system using a PDF document as the knowledge base, leveraging the GROQ API for language model operations.

##### Key Components
- **PDF Data Loading and Splitting**: Loads and splits PDF documents into manageable chunks.
- **Vector Database Embedding**: Creates embeddings for the document chunks using the OllamaEmbeddings model.
- **Language Model Initialization**: Initializes the ChatGroq language model from Groq.
- **Retrieval-Based QA System**: Sets up a RetrievalQA chain to answer queries based on the document embeddings and the language model.

- #### [Script Link](https://github.com/sharmapratik88/Generative-AI-Projects/blob/main/Chat_with_PDF/GROQ_API/chat_with_pdf_groq.py)
