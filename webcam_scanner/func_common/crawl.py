from bs4 import BeautifulSoup
import requests

def crawl(keyword):
    cve_result = []
    target = f"https://cve.mitre.org/cgi-bin/cvekey.cgi?keyword={keyword}"
    req = requests.get(target)
    html = req.text
    bf = BeautifulSoup(html,features="xml")
    texts = bf.find_all('div',id="TableWithRules")
    a_bf = BeautifulSoup(str(texts[0]),features="xml")
    a = a_bf.find_all("a")
    for each in a:
        if each.string != "":
            cve_result.append(each.string)
    return cve_result