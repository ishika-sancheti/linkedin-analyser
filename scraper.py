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
            job_id=listing.split(":")[-1]
        job_id.append(job_id)
    return job_id


# r2=requests.get("https://www.linkedin.com/jobs-guest/jobs/api/jobPosting/4408775608")
# print(r2.text)