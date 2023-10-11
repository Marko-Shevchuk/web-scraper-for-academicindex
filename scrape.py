import csv
import requests
from bs4 import BeautifulSoup
 
def scrape_website(url, writer):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    elements = soup.select('.container-fluid .row .card .card-body .row .col-6 a')
    for element in elements:
        writer.writerow([element.contents[2].strip()])
with open('doi.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for i in range(0,116): # from page 1 to 117
        scrape_website('https://academicindex.org.ua/publications?page='+str(i), writer)
    