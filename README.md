# Project idea
As big fan of football (soccer) and its statistics too, I decided to create Python script that counts player appearances in the Slovak 3. liga East (Východ) for 2023-24, because I did not find them among statistics (https://sportnet.sme.sk/futbalnet/k/stara-lubovna-redfox-football-club/tim/58861/hraci/?partId=&sutaz=6477ac257b634444d118634a) for 3rd tier of Slovak football. The script can be applied for any team, league or season that come from the same website. Currently, it operates only with player data of STARÁ ĽUBOVŇA REDFOX FOOTBALL CLUB, but I am planning to include all teams and also enhance logic/ funcionality of the script, and later make it in OOP style...

# Script logic/ timeline/ steps
```
1. I scraped squad data for each team (https://github.com/kixelo/PlayerAppearancesCounter/blob/master/3_liga_east_2023_24_squad_RawFile.csv), with Name, goals, yellow cards and red cards columns (saved in CSV format).
2. Next step was to scrape all 3. liga results for 2023-24 season from https://sportnet.sme.sk/futbalnet/z/sfz/s/4408/vyhodnotenie/?part=647a3f3b76d0d348cd095fa9&tableView= .
3. Then I had to gather, filter and clean all results to get only player names which participated in game, simply it means, scrape all starting match lineups, it was quite easy.
4. The most challenging thing for me was to come up with "logic" that counts only bench players that participated in game = substitutions. https://en.wikipedia.org/wiki/Substitute_(association_football). It took me a few days to find solution.
5. Finally, all scraped data of starting lineup players, + substitutions have been stored in Python list []. Then I used Python List count() method to return the number of "appearances" for each player. To see the output see "CSV" file below: 
```

# Output of the script
```
CSV file with all data that I wanted to have -->>> https://github.com/kixelo/PlayerAppearancesCounter/blob/master/3_liga_east_2023_24_squad_v2.csv <<<--
To verify my results, I attached an article from Futbalnet, where the statistics are mentioned for one player from my "CSV file" (Filip Serečin). (1st picture below)
https://sportnet.sme.sk/spravy/futbal-rozhovor-filip-serecin-redfox-football-club-stara-lubovna-najlepsi-strelec-iii-liga-vychod/
The 2nd one (below) is picture from my "CSV file".
```
<img src="https://github.com/kixelo/PlayerAppearancesCounter/blob/master/Screenshot%202024-07-09%20175424.png" />
<img src="https://github.com/kixelo/PlayerAppearancesCounter/blob/master/Screenshot%202024-07-09%20175732.png" />


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
