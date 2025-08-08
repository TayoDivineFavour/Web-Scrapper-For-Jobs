import requests
from bs4 import BeautifulSoup


job = input('Your job: ')
job_search = job.replace(' ' , '+')



url = f'https://www.capitalonecareers.com/search-jobs?l=&k={job_search}&p=1'
html = requests.get(url).text


doc = BeautifulSoup(html , 'html.parser')


pages_search = doc.find(class_="pagination-total-pages").text
pages = int(str(pages_search).split(' ')[-1])


for page in range(1 , pages + 1):

    url = f'https://www.capitalonecareers.com/search-jobs?l=&k={job_search}&p={page}'
    html = requests.get(url).text
    doc = BeautifulSoup(html , 'html.parser')

    section = doc.find('section' , id="search-results-list")

    ul = section.ul
    
    lis = ul.find_all('li')

    for li in lis:

        a = li.a
        herf = a['href']
        date = a.find('span' , class_="job-date-posted").text
        name = a.h2.text
        location = a.find(class_="job-location").text




