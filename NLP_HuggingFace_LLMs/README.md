# LearningAI - NLP, Hugging Face and LLMs models

In this section, you'll discover projects that leverage a variety of techniques in Natural Language Processing (NLP) and Generative AI.

### Projects:

1. **[Text Classification Using Transformers](https://nbviewer.org/github/sharmapratik88/LearningAI/blob/main/NLP_HuggingFace_LLMs/HF_Text_Classification.ipynb)**

This project features a Python script for training a text classification model to categorize resumes into various job categories using the Hugging Face Transformers library and PyTorch. It utilizes the comprehensive Resume Dataset from Kaggle, making it a valuable tool for automating the resume sorting process in recruitment.

Key Features:

* Leverages the Hugging Face Transformers library for model training and evaluation.
* Uses the Resume Dataset, containing over 2400 categorized resumes, for training.
* Employs distilbert-base-uncased, a pre-trained DistilBert model, for fine-tuning.
* Implements data preprocessing steps, including dataset splitting and tokenization.
* Fine-tunes the model with custom training arguments to optimize performance for resume classification.
* Saves the trained model and tokenizer for future use or deployment.
* Evaluates the model's performance (accuracy and F1-score) and demonstrates classification of new resumes from test dataset.

This script is ideal for developers and researchers interested in applying text classification to real-world recruitment processes, offering a practical example of using state-of-the-art NLP tools for automating tasks.

2. **[Text Summarization Using Transformers](https://nbviewer.org/github/sharmapratik88/LearningAI/blob/main/NLP_HuggingFace_LLMs/HF_Text_Summarizer.ipynb)**

This project features a Jupyter notebook that fine-tunes the Pegasus model for text summarization tasks using the SAMSum dataset. The script includes comprehensive steps for setting up the environment, preprocessing data, training the model, and evaluating its performance with ROUGE metrics. 

Key Features:

* Utilizes the Hugging Face Transformers library for model training and evaluation. 
* Employs the SAMSum dataset, which consists of dialogues and their corresponding summaries. 
* Implements a tokenizer to convert text data into a format suitable for the model. 
* Fine-tunes the Pegasus model with custom training arguments. 
* Saves the trained model and tokenizer for future use. 
* Provides a summarization pipeline to generate summaries from dialogues. 
* Evaluates the model's performance using ROUGE scores and displays the results.

This is ideal for those looking to understand and implement text summarization models using the HuggingFace transformers.

3. **[Machine Learning Using Transformers](https://nbviewer.org/github/sharmapratik88/LearningAI/blob/main/NLP_HuggingFace_LLMs/HF_Machine_Translation.ipynb)**

This project includes a Jupyter notebook that leverages the Hugging Face Transformers library to perform machine translation from English to Hindi. The script uses the Helsinki-NLP Opus-MT model and the IIT Bombay English-Hindi dataset for training and evaluation.

Key Features:

* Implements TensorFlow for model training and inference.
* Utilizes a pre-trained Helsinki-NLP Opus-MT model for English-to-Hindi translation.
* Processes and tokenizes the IIT Bombay English-Hindi dataset for machine translation tasks.
* Defines training parameters and compiles the model with an Adam optimizer and weight decay.
* Trains the model with specified batch size, learning rate, and epochs.
* Saves the trained model for future use or deployment.
* Provides a sample inference to demonstrate translation of English text to Hindi.

This is suitable for developers and researchers interested in machine translation and natural language processing, providing a practical example of training and using a translation model with HuggingFace transformers.