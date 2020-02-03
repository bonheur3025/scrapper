import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f'https://www.indeed.com/jobs?q=python&limit={LIMIT}'


def get_last_page():
    result = requests.get(URL)

    soup = BeautifulSoup(result.text, 'html.parser')

    pagination = soup.find('div', {'class': 'pagination'})

    links = pagination.find_all('a')
    pages = []

    for link in links[:-1]:
        pages.append(int(link.string))

    max_page = pages[-1]
    max_page = 3
    return max_page


def extract_job(html):
    title = html.find('div', {'class': 'title'}).find('a')['title']

    company = html.find('span', {'class': 'company'})
    company_anchor = company.find('a')
    if company_anchor is not None:
        company = company_anchor.string.strip()
    else:
        company = company.string.strip()

    location = html.find('div', {'class': 'recJobLoc'})['data-rc-loc']

    job_id = html['data-jk']

    return {'title': title, 'company': company, 'location': location, 'link': f'https://www.indeed.com/viewjob?jk={job_id}'}


def extract_html(last_page):

    jobs = []
    for page in range(last_page):
        print(f'Scrapping Indeed Page {page}')
        result = requests.get(f'{URL}&start={page*LIMIT}')
        soup = BeautifulSoup(result.text, 'html.parser')

        results = soup.find_all('div', {'class': 'jobsearch-SerpJobCard'})
        for result in results:
            jobs.append(extract_job(result))

    return jobs


def get_jobs():
    last_page = get_last_page()
    jobs = extract_html(last_page)
    return jobs