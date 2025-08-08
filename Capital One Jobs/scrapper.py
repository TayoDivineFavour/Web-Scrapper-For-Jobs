import requests
from bs4 import BeautifulSoup
import pandas as pd


job = input('Your job: ')
job_search = job.replace(' ' , '+')
job_save = job.replace(' ' , '_')


url = f'https://www.capitalonecareers.com/search-jobs?l=&k={job_search}&p=1'
html = requests.get(url).text


doc = BeautifulSoup(html , 'html.parser')
pages_search = doc.find(class_="pagination-total-pages").text
pages = int(str(pages_search).split(' ')[-1])


Names = []
Date = []
Location = []
Link = []





for page in range(1 , pages + 1):

    url = f'https://www.capitalonecareers.com/search-jobs?l=&k={job_search}&p={page}'
    html = requests.get(url).text
    doc = BeautifulSoup(html , 'html.parser')

    section = doc.find('section' , id="search-results-list")

    ul = section.ul
    
    lis = ul.find_all('li')

    for li in lis:

        a = li.a


        Link.append(a['href'])
        Date.append(a.find('span' , class_="job-date-posted").text)
        Names.append(a.h2.text)
        Location.append(a.find(class_="job-location").text)





All_jobs = {
    "Name": Names ,
    "Date": Date ,
    "Location": Location, 
    "link": Link
}



df = pd.DataFrame(All_jobs)

df.to_excel(f'Capital_One_job( {job_save} ).xlsx' , index=False)