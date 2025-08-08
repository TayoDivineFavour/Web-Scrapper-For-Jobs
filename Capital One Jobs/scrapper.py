import requests
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm


job = input('Your job: ')
job_search = job.replace(' ' , '+')
job_save = job.replace(' ' , '_')


try:

    url = f'https://www.capitalonecareers.com/search-jobs?l=&k={job_search}&p=1'
    html = requests.get(url).text
    print(f'{job_save} search in progress please wait.....')


except Exception as e:

    print(f'An error occured {e}')





doc = BeautifulSoup(html , 'html.parser')

try:

    pages_search = doc.find(class_="pagination-total-pages").text
    pages = int(str(pages_search).split(' ')[-1])

except Exception as e:
        print(f'An error occured {e}')



Names = []
Date = []
Location = []
Link = []




for page in tqdm(range(1 , pages + 1) , desc='scraping pages'):

    try:
        headers = {'User-Agent' : 'Mozilla/5.0'}
        url = f'https://www.capitalonecareers.com/search-jobs?l=&k={job_search}&p={page}'
        html = requests.get(url, headers=headers).text

    except Exception as e:

        print(f'An error occured {e}')




    doc = BeautifulSoup(html , 'html.parser')
    section = doc.find('section' , id="search-results-list")
    ul = section.ul
    lis = ul.find_all('li')
    


    for li in lis:

        a = li.a
        extracted_link = a['href']
        added_link = f'https://www.capitalonecareers.com{extracted_link}'

    
        Link.append(added_link)
        Date.append(a.find('span' , class_="job-date-posted").text)
        Names.append(a.h2.text)
        Location.append(a.find(class_="job-location").text)




All_jobs = {
    "Name": Names ,
    "Date": Date ,
    "Location": Location, 
    "link": Link
}



def save_to_excel(data):
     
    df = pd.DataFrame(data)

    df.to_excel(f'Capital_One_job( {job_save} ).xlsx' , index=False)

    print(f'{job_save} search file ready please check directory')

save_to_excel(All_jobs)