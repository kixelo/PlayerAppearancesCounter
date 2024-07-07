from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re

classes = ['sc-biqTHF kwJtxc', 'sc-biqTHF gvuawW']
for c in classes:
            DIVS_ = divs.find_all('div', class_=f'{c}')
            filtered_divs = [div1 for div1 in DIVS_ if div1.find('svg', id='Layer_1')]
            for div in filtered_divs:
                subs_final = div.get_text().strip()

                name_pattern = re.compile(rf'{substitutes[i]}', re.IGNORECASE)

                # print(name_pattern)
                #match = name_pattern.search(subs_final)


                if match:
                    name = match.group()
                    print(name)

                    # else:
                    # print("Name not found")
