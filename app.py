from flask import Flask, render_template, request, redirect, jsonify
from flask_cors import CORS

from analyzer import analyser_function
import scraper

app=Flask(__name__)
CORS(app)

@app.route("/analyze", methods=['POST'])
def analyser():
    smth=request.get_json()
    res=analyser_function(smth["text"])
    return jsonify(res)

if __name__=='__main__':
    app.run(debug=True, use_reloader=False)
