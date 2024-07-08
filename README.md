# Project idea
As big fan of football (soccer) and its statistics too, I decided to create Python script that counts player appearances in the Slovak 3. liga East (Východ) for 2023-24, because I did not find them among statistics (https://sportnet.sme.sk/futbalnet/k/stara-lubovna-redfox-football-club/tim/58861/hraci/?partId=&sutaz=6477ac257b634444d118634a) for 3rd tier of Slovak football. The script can be applied for any team, league or season that come from the same website. Currently, it operates only with player data of STARÁ ĽUBOVŇA REDFOX FOOTBALL CLUB, but I am planning to include all teams and also enhance logic/ funcionality of the script, and later make it in OOP style...

# Output of the script
CSV file with all data that I wanted to have -->>> https://github.com/kixelo/PlayerAppearancesCounter/blob/master/3_liga_east_2023_24_squad_v2.csv <<<--

## Desktop application that I used for coding part
```
PyCharm
```

## Stuff that helped me to meet my desired results
```
Jupyter Notebook (for data analysis)
ChatGPT (gave me some useful hints)
```

## Build Setup, required to install dependencies for the project
pip install selenium
pip install requests
pip install pandas
pip install beautifulsoup4

## Used libraries and modules
```
import re
import time
import pandas
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
```

## App Images:
<img src="https://github.com/kixelo/PlayerAppearancesCounter/blob/master/output.png" />
