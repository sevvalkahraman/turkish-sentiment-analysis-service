#!flask/bin/python
import json
from flask import Flask, Response, request, jsonify
import requests
from flaskrun import flaskrun
from config import SlackConfig 
from nlp import findSentiment

application = Flask(__name__)


@application.route('/', methods=['POST'])
def post():
    data = ''
    try:
        userText = request.form['text'] 
        if not userText :
            data = "Please enter text."        
        else :
            result  = findSentiment(userText)
            if result < 0 :
                data = "Negative sentence."
            elif (result >= 0) and (result <= 0.5) :
                data = "It looks like neutral."
            else :
                data = "Positive sentence."
    except Exception as error:
        data =  {"text" : "Something went wrong when operating 'post' process. -> " + str(error)}
    return jsonify(data)

if __name__ == '__main__':
    flaskrun(application)