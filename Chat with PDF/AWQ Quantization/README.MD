# PDF Q&A Retrieval with AWQ Quantization, Mistral Instruct v0.2 and vLLM
This project demonstrates a comprehensive pipeline for processing PDF documents, embedding their content into a vector database, and utilizing a quantized language model for retrieval-based question answering. The key components include loading and splitting PDF documents, embedding the text into a vector database, quantizing a language model, and setting up a retrieval-based QA system.

## Important Libraries
- **PyPDFLoader**: For loading PDF documents.
- **RecursiveCharacterTextSplitter**: For splitting text into manageable chunks.
- **AutoAWQForCausalLM**: For quantizing language models.
- **AutoTokenizer**: For tokenizing text.
- **SentenceTransformerEmbeddings**: For embedding text using pre-trained models.
- **Chroma**: For creating and managing a vector database.
- **vLLM**: For loading and using quantized language models.
- **Langchain's RetrievalQA**: For setting up a retrieval-based question answering system.

## Features
- **PDF Data Ingestion**: Efficiently load and process PDF documents, splitting them into manageable chunks.
- **Vector Database Embedding**: Utilize SentenceTransformer embeddings to create a searchable vector database.
- **AWQ Model Quantization**: Implement AWQ quantization on the Mistral Instruct v0.2 model for optimized performance.
- **Query Handling**: Use vLLM to generate accurate responses to queries from the processed PDF documents.
- **Logging**: Comprehensive logging of the entire process for better traceability and debugging.

## Steps to get started
### Clone the repository
```bash
git clone https://github.com/sharmapratik88/Learning-Generative-AI.git
cd 'Learning-Generative-AI/Chat with PDF/AWQ Quantization'
```

### Setting up the virtual environment
1. Create the virtual environment: ```python -m venv venv```.
2. Activate the virtual environment: ```venv\Scripts\activate``` on Windows and ```source venv/bin/activate``` on MacOS.
3. Install dependencies: ```pip install -r requirements.txt```.
4. Create a .env file in the project root and add your HuggingFace token ```HF_TOKEN="your HF token"```.
5. Install the Jupyter kernel: ```python -m ipykernel install --user --name venv --display-name "ChatWithPDF"```.

## Logging
The code logs key steps and outputs to a file named logger.txt, which can be used for monitoring the processing steps and debugging if necessary.