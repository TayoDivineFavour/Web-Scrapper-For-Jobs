import requests
from bs4 import BeautifulSoup


job = input('Your job: ')
job_search = job.replace(' ' , '+')



url = f'https://www.capitalonecareers.com/search-jobs?l=&k={job_search}&p=1'

html = requests.get(url).text

doc = BeautifulSoup(html , 'html.parser')

pages_search = doc.find(class_="pagination-total-pages").text
pages = int(str(pages_search).split(' ')[-1])
print(pages)
