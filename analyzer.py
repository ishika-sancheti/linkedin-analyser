import re
from keywords import keywords_list

def analyser_function(text):
    text=text.lower()
    res={}
    for category, skills in keywords_list.items():
        res[category]=[]
        for keyword in skills:
            add=re.findall(r'\b' + keyword + r'\b', text)
            res[category].extend(set(add))  
    return res


# sample = "looking for a python developer with aws and docker experience, must have a b.tech degree"
# print(analyser_function(sample))