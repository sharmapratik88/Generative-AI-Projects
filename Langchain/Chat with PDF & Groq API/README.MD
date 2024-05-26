# PDF Question Answering with LangChain & GROQ

This project is designed to create a Question-Answering (QA) system using a PDF document as the knowledge base. The code processes the PDF, splits it into manageable chunks, embeds these chunks into a vector database, and uses a language model to retrieve answers to user queries based on the content of the PDF.

## Features

- Loads and splits a PDF document into manageable chunks.
- Creates embeddings for the document chunks using the OllamaEmbeddings model.
- Stores the document embeddings in a Chroma vector database.
- Initializes the ChatGroq language model from Groq.
- Sets up a RetrievalQA chain to answer queries based on the document embeddings and the language model.

## Setting up the virtual environment
1. Create virtual environment: ```python -m venv venv```
2. Activate the virtual environment: ```venv\Scripts\activate``` on Windows or ```source venv/bin/activate``` on MacOS.
3. Install the dependencies: ```pip install -r requirements.txt```
4. Create a .env file and add ```GROQ_API_KEY="your GROQ API key"```
5. Place your PDF file in the pdfs directory and update the pdf_file variable in the script with the correct file path.
6. Adjust the configuration constants as needed, such as chunk_size, chunk_overlap, return_k, model_name, and embedding_model.
7. Run the script: ```chatwithPDF_groq.py```

## Logging
The code logs key steps and outputs to a file named logger.txt, which can be used for monitoring the processing steps and debugging if necessary.