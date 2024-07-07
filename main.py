from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import re

# Initialize the WebDriver (using Chrome in this example)
service = Service(executable_path=r"C:\Users\igoro\Documents\Python projects 2024\Web scraping football data from Futbalnet\chromedriver.exe")
driver = webdriver.Chrome(service=service)


# Open the webpage
driver.get('https://sportnet.sme.sk/futbalnet/z/sfz/s/4408/vyhodnotenie/?part=8115&tableView=')

# Give the page time to load
time.sleep(2)

# Function to click the "Zobraziť viac" button until it's no longer available
def click_show_more():
    while True:
        try:
            # Find the "Zobraziť viac" button
            show_more_button = driver.find_element(By.CSS_SELECTOR, 'button.sc-cVksOY.bAQjtc.sc-cuaByG.cmsiVT')
            # Click the button
            show_more_button.click()
            # Wait for the content to load
            time.sleep(1)
        except Exception as e:
            # Break the loop if the button is not found
            print("No more 'Zobraziť viac' button found or an error occurred:", e)
            break

# Click the "Zobraziť viac" button until all data is loaded
click_show_more()

page_source = driver.page_source
headers = {'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'} # in web search type: "what is my user agent"

soup = BeautifulSoup(page_source, 'html.parser')

datas = soup.find_all('div', class_='sc-LUDBL klGdHG') #sc-LUDBL klGdHG

M_LINK = []

for data in datas:
    match_link = data.find_all('a', class_='sc-heOvnj jzBGuQ')[0]['href'] #['href']
    M_LINK.append(f"https://sportnet.sme.sk{match_link}#zostavy")


PLAYERS = []
BENCH_PLAYERS= []

for match in M_LINK:
    matchTree = requests.get(match, headers=headers)
    matchSoup = BeautifulSoup(matchTree.content, 'html.parser')
    div_elements = matchSoup.find_all('div', class_='sc-jXwHBv hoYKTq') # matchSoup.find_all('div', class_='sc-biqTHF gvuawW')


    for divs in div_elements:
        a_element = divs.find_all('a', class_='sc-ieyQOK jdnLFK')
        lineups = a_element[:11]  # starting lineup

        for lineup in lineups:
            PLAYERS.append(lineup.get_text().replace("\xa0(C)", ""))

        substitutes = a_element[11:]  # bench substitutions

        classes = ['sc-biqTHF kwJtxc', 'sc-biqTHF gvuawW']

        for sub in substitutes:
            name_pattern = re.compile(rf'{sub.get_text().strip()}', re.IGNORECASE)

            for c in classes:
                DIVS_ = divs.find_all('div', class_=f'{c}')
                filtered_divs = [div1 for div1 in DIVS_ if div1.find('svg', id='Layer_1')]
                for div in filtered_divs:
                    subs_final = div.get_text().strip()

                    match = name_pattern.search(subs_final)

                    if match:
                        name = match.group()
                        BENCH_PLAYERS.append(name)
                    else:
                        print("Name not found")


PLAYERS.extend(BENCH_PLAYERS)

enter_name = input("Enter name of player from 3. liga Východ: ")
print(PLAYERS.count(enter_name))