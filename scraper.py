import requests
from bs4 import BeautifulSoup
import re
import time

def get_job_id(keyword):
    details=[]
    for i in range(0, 50, 10):
        r=requests.get(f"https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords={keyword}&start={i}")
        soup=BeautifulSoup(r.text, 'html.parser')
        inputTag=soup.find_all(attrs={"data-entity-urn": True})
        for element in inputTag:
            if re.match(r"urn:li:jobPosting:\d+", element['data-entity-urn']):
                listing_job_id=element['data-entity-urn']
                job_id_indv=listing_job_id.split(":")[-1]    
                getting_company_class=element.find("h4", class_="base-search-card__subtitle")       #to make it search within the element - whcih is an indv job card
                company_text=getting_company_class.get_text(strip=True)
                details.append((job_id_indv, company_text))
    return details

# result = get_job_id(inputTag)
# print(result)


def get_job_desc(job_id):
    r2=requests.get(f"https://www.linkedin.com/jobs-guest/jobs/api/jobPosting/{job_id}")
    soup=BeautifulSoup(r2.text, 'html.parser')
    job_desc=soup.find("div", class_="description__text")
    if job_desc is None:
        return " "
    job_desc_text=job_desc.get_text()
    return job_desc_text
    
# result2=get_job_desc("4408775608")
# print(result2)

def scrape_all_jobs(keyword):
    list_co_ids=get_job_id(keyword)
    #print(f"Found {len(list_ids)} job IDs: {list_ids}")
    job_desc_list=[]
    company_name_list=[]
    for job_id, co_name in list_co_ids:
        job_desc_indv=get_job_desc(job_id)
        job_desc_list.append(job_desc_indv)
        company_name_list.append(co_name)
        time.sleep(0.5)
    return job_desc_list, company_name_list

# res=scrape_all_jobs("SDE")
# print(f"Total descriptions fetched: {len(res)}")        #just to check if all 50 are being printed
# print(res)