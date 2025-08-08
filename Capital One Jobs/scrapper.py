import requests
from bs4 import BeautifulSoup


job = input('Your job: ')
job_search = job.replace(' ' , '+')



url = f'https://www.capitalonecareers.com/search-jobs?l=&k={job_search}&p=1'

html = requests.get(url).text
print(html)