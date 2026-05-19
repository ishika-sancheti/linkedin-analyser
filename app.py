from flask import Flask, render_template, request, redirect, jsonify, Response, make_response
from flask_cors import CORS
from collections import Counter, defaultdict
from scraper import scrape_all_jobs
from analyzer import analyser_function
import scraper
import io
import csv

app=Flask(__name__)
CORS(app)

@app.route("/analyze", methods=['POST'])
def analyser():
    consolidated=defaultdict(Counter)
    smth=request.get_json()
    keyword=smth["keyword"]
    scraper_result, companies=scrape_all_jobs(keyword)
    for desc in scraper_result:
        analyser_result=analyser_function(desc)
        for category, skill in analyser_result.items():
            consolidated[category].update(skill)
    company_counts=Counter(companies)
    consolidated=dict(consolidated)
    csv_data = generate_csv(consolidated, company_counts)
    return csv_data
    #return jsonify({"skills": consolidated, "companies": dict(company_counts)})

def generate_csv(consolidated, company_counts):
    consolidated=dict(consolidated)
    company_counts=dict(company_counts)

    si=io.StringIO()
    write=csv.writer(si, delimiter=",")
    
    for category in consolidated:
        for skill, count in consolidated[category].items():
            write.writerow([category, skill, count])

    for company, count in company_counts.items():
        write.writerow([company, count])
    your_csv_string = make_response(si.getvalue())
    #your_csv_string=si.getvalue()
    your_csv_string.headers["Content-Disposition"] = "attachment; filename=export.csv"
    your_csv_string.headers["Content-type"] = "text/csv"
    return your_csv_string

    

if __name__=='__main__':
    app.run(debug=True, use_reloader=False)
