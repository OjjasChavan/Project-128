from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

START_URL = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'
browser = webdriver.Chrome('D:/Ojjas/Ojjas-Whjr/Project-127/chromedriver')
browser.ger(START_URL)
time.sleep(10)

def scrape():
    header = ['Confirmed brown dwarfs orbiting primary stars', 'Unconfirmed brown dwarfs', 'Field brown dwarfs', 'Former brown dwarfs']
    empty_list = []
    for i in range(0, 428):
        soup = BeautifulSoup(browser.page_source, 'html.parser')
        for tr_tag in soup.find_all('tr', attrs = {'class', 'brightest_stars'}):
            th_tag = tr_tag.find_all('th')
            temp_list = []
            for index, th_tag in enumerate(th_tag):
                if index == 0:
                    temp_list.append(th_tag.find_all('a')[0].contents[0])
                else:
                    try:
                        temp_list.append(th_tag.contents[0])
                    except:
                        temp_list.append('')
            empty_list.append(temp_list)
        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    with open('scrapper_2.csv', 'w') as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(header)
        csvwriter.writerows(empty_list)

scrape()

new_planets_data = []
hyperlink = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'

def scrape_more_data(hyperlink):
    try:
        page = requests.get(hyperlink)
      
        soup = BeautifulSoup(page.content, "html.parser")

        temp_list = []

        for tr_tag in soup.find_all("tr", attrs={"class": "fact_row"}):
            td_tags = tr_tag.find_all("td")
          
            for td_tag in td_tags:
                try: 
                    temp_list.append(td_tag.find_all("div", attrs={"class": "value"})[0].contents[0])
                except:
                    temp_list.append("")
                    
        new_planets_data.append(temp_list)

    except:
        time.sleep(1)
        scrape_more_data(hyperlink)

for index, data in enumerate(planets_data):
    scrape_more_data(data[5])
    print(f"scraping at hyperlink {index+1} is completed.")

print(new_planets_data[0:10])

final_planet_data = []

for index, data in enumerate(planets_data):
    new_planet_data_element = new_planets_data[index]
    new_planet_data_element = [elem.replace("\n", "") for elem in new_planet_data_element]
    new_planet_data_element = new_planet_data_element[:7]
    final_planet_data.append(data + new_planet_data_element)

with open("final.csv", "w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(final_planet_data)