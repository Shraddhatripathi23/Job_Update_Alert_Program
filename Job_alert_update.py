#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup

def search_jobs(keyword, location):
    url = f"https://www.google.com/search?q={keyword}+jobs+in+{location}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, "html.parser")
    job_results = soup.find_all("div", class_="tF2Cxc")

    for result in job_results:
        title_element = result.find("h2")
        company_element = result.find("div", class_="yuRUbf").find("span")
        description_element = result.find("span", class_="aCOpRe")
        link_element = result.a

        title = title_element.text if title_element else "N/A"
        company = company_element.text if company_element else "N/A"
        description = description_element.text if description_element else "N/A"
        link = link_element["href"] if link_element else "N/A"

        print("Title:", title)
        print("Company:", company)
        print("Description:", description)
        print("Link:", link)
        print()

# Example usage
search_jobs("python developer ,fullstack developer", "india")


# In[ ]:




