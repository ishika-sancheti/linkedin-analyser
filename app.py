from flask import Flask, render_template, request, redirect, jsonify
from flask_cors import CORS
from collections import Counter, defaultdict
from scraper import scrape_all_jobs
from analyzer import analyser_function
import scraper

app=Flask(__name__)
CORS(app)

@app.route("/analyze", methods=['POST'])
def analyser():
    consolidated=defaultdict(Counter)
    smth=request.get_json()
    keyword=smth["keyword"]
    scraper_result=scrape_all_jobs(keyword)
    for desc in scraper_result:
        analyser_result=analyser_function(desc)
        for category, skill in analyser_result.items():
            consolidated[category].update(skill)
    consolidated=dict(consolidated)
    return jsonify(consolidated)

if __name__=='__main__':
    app.run(debug=True, use_reloader=False)
