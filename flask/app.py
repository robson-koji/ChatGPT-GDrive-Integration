from flask import Flask, request, jsonify
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA 
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.memory import ConversationBufferMemory


app = Flask(__name__)
DB_DIR = "../db"

@app.route('/qa', methods=['GET'])
def question_answering():
    query = request.args.get('query')
    if not query:
        return jsonify({'error': 'No query provided'})
    
    if len(query) > 150:
        return jsonify({'error': 'Query too long'})

    embeddings = OpenAIEmbeddings()
    db = Chroma(
        persist_directory=DB_DIR, 
        embedding_function=embeddings
    )
    retriever = db.as_retriever()

    # Language model initialization
    llm = ChatOpenAI(
        temperature=0,
        model_name="gpt-3.5-turbo",
        request_timeout=120,
        max_tokens=1500
    )

    # Question-answering setup
    qa = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="map_reduce",
        retriever=retriever,
        memory=ConversationBufferMemory()
    )

    # Perform question-answering
    answer = qa.run(query)

    return jsonify({'answer': answer})


if __name__ == '__main__':
    app.run()