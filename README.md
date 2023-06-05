# About

Vectorize a Google Drive folder content to a vector database to query and obtain answers using ChatGPT.

## Technology Stack
- Google Drive
- LangChain
  - Chroma DB
- ChatGPT
- Flask


# Project Structure
A very simple and straightforward personal chatbot API project written in Python, using ChatGPT, LangChain, and Flask, to answer questions about your files in Google Drive.


```
+-- db --+
|        |
|        +-- ChromaDB files
|
+-- flask --+
|           |
|           +-- app.py
|
+-- gdrive_copy --+
                  |
                  +-- copy_gdrive.py
```


# Requirements
## Google Drive API enabled
You need a Google Account to log into the Google Cloud Console and enable the Google Drive API. This is the most tedious part.

## ChatGPT API
You need an OpenAI Account and enable the ChatGPT API.

## Set Environment Variables
Set the following environment variables to use the system:

- OPENAI_API_KEY
  (e.g., export OPENAI_API_KEY=<YOUR OPENAI API KEY> in Unix-based systems)

- GDRIVE_FOLDER_ID
  (e.g., export GDRIVE_FOLDER_ID=<YOUR GDRIVE_FOLDER_ID> in Unix-based systems)

## Install Python Requirements
You may need to install the necessary dependencies (Flask, OpenAI, etc.) using pip or any package manager you prefer before running the code.



# Procedure
Considering that all the requirements are met, there are only two steps to follow:

1. Run the script below. It will download data from your Google Drive folder and load it into your local Chroma DB:

    ```
    python gdrive_copy/copy_gdrive.py
    ```

2. Run the Flask application and turn on the endpoint to start querying your data. 

    ```
    python app.py or flask run
    ```


## Flask Application
I've created a Flask application and defined a GET endpoint `/api/chat`. The endpoint expects a query parameter called `query` to be passed with the GET request. It then runs the `qa.run()` function to obtain an answer based on the provided query and returns the answer as the API response.

The API will be accessible at `http://localhost:5000/api/chat`. 

## Using Examples
You can ask anything that is contained in the documents from your Google Drive folder. If everything is set correctly, ChatGPT will answer as expected.

Start making a GET requests to this endpoint by appending the query parameter like `http://localhost:5000/api/chat?query="hi"`.