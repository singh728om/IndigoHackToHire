# IndigoHackToHire
Hack to Hire Hackathon @Indigo

>> unizp indigo.zip file to start (uploaded zip file due to large file error from github side) either you can unzip Indigo.zip(all files in one place) OR work induvidually with notebook and app.py.
>> 
```sh
>> Open (IndigoHackToHire.pptx)for detailed presentation.
presented by: pixom.ai@gmail.com
```

# Question Answering System Using BERT

This project demonstrates the development of a state-of-the-art question-answering model leveraging the Quora Question Answer Dataset. The objective is to create an AI system capable of understanding and generating accurate responses to a variety of user queries, mimicking human-like interaction.

## Table of Contents
- [Introduction](#introduction)
- [Dataset](#dataset)
- [Model](#model)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Results](#results)
- [Visualization](#visualization)
- [Insights and Recommendations](#insights-and-recommendations)
- [Contributing](#contributing)
- [License](#license)

## Introduction
The goal of this project is to build a question-answering system using the BERT model. The system processes input text (context) and questions, then generates accurate answers based on the context.

## Dataset
We use the Quora Question Answer Dataset available on Hugging Face Datasets.
Data set: https://huggingface.co/datasets/toughdata/quora-question-answer-
dataset

## Model
We utilize the `bert-base-uncased` model from the Hugging Face Transformers library. The model is fine-tuned on the dataset to improve its question-answering capabilities.

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Steps
1. Clone the repository:
    ```sh
    git clone https://github.com/singh728om/IndigoHackToHire.git
    cd IndigoHackToHire
    ```
    or
   ```sh
    git clone https://github.com/your-username/question-answering-system.git
    cd question-answering-system
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

### Training the Model
To train the model, run the Jupyter notebook provided in the repository. The notebook contains steps for data exploration, preprocessing, model training, and evaluation.

### Running the Flask App
1. Start the Flask application:
    ```sh
    python app.py
    ```

2. Open your browser and navigate to `http://localhost:5000`.

### API Endpoints
- `POST /predict`: Takes a JSON payload with `context` and `question` fields, and returns the answer.

#### Example Request
```json
{
    "context": "Quora is a question-and-answer website where questions are asked, answered, and edited by Internet users.",
    "question": "What is Quora?"
}


