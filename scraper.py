import requests
from bs4 import BeautifulSoup
import re

r=requests.get("https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=SDE&start=0")
soup=BeautifulSoup(r.text, 'html.parser')
inputTag=soup.find_all(attrs={"data-entity-urn": True})
def get_job_id(inputTag):
    job_id=[]
    for element in inputTag:
        if re.match(r"urn:li:jobPosting:\d+", element['data-entity-urn']):
            listing=element['data-entity-urn']
            job_id_indv=listing.split(":")[-1]
            job_id.append(job_id_indv)
    return job_id

result = get_job_id(inputTag)
print(result)


def get_job_desc(job_id):
    r2=requests.get(f"https://www.linkedin.com/jobs-guest/jobs/api/jobPosting/{job_id}")
    soup=BeautifulSoup(r2.text, 'html.parser')
    job_desc=soup.find("div", class_="description__text")
    job_desc_text=job_desc.get_text()
    return job_desc_text
    
result2=get_job_desc("4408775608")
print(result2)