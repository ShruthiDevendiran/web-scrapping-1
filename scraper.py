from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from bs4 import BeautifulSoup
import time

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

browser = webdriver.Chrome('/chromedriver.exe')
browser.get(START_URL)

scraped_data = []
time.sleep(10)

def scrape():
    soup = BeautifulSoup(browser.page_source,"html.parser")
    bright_star_table = soup.find("table",attrs = {"class","wikitable"})
    table_body = bright_star_table.find('tbody')
    stars_data = table_body.find_all('tr')

    for stars in stars_data:
        titles = stars.find_all('td')
        print(titles)

        temp_list = []

        for title in titles:
            title_text = title.text.strip()
            print(title_text)

            temp_list.append(title_text)
        
        scraped_data.append(temp_list)

stars_data = []

for i in range(0,len(scraped_data)):
    Star_name = scraped_data[i][1]
    Distance = scraped_data[i][3]
    Mass = scraped_data[i][5]
    Radius = scraped_data[i][6]
    Lumonisity = scraped_data[i][7]

    required_data = [Star_name,Distance,Mass,Radius,Lumonisity]

    stars_data.append(required_data)
    
scrape()

headers = ['Star_name','Distance','Mass','Radius','Lumonisity']

stars_1 = pd.DataFrame(stars_data, columns = headers)

stars_1.to_csv('stars_data.csv',index = True,index_label = "id")


        

