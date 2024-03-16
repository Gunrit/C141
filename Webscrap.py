from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd
import requests

START_URL = "https://en.wikipedia.org/wiki/Lists_of_stars"
#browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
page = requests.get(START_URL)
soup = BeautifulSoup(page.text,"html.parser")

starTable = soup.find('table')
templist = []
tablerows = starTable.find_all('tr')
for tr in tablerows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    templist.append(row)
star_names = []
distance = []
mass = []
radius = []
for i in range(1,len(templist)):
    star_names.append(templist[i][2])
    distance.append(templist[i][4])
    mass.append(templist[i][3])
    radius.append(templist[i][5])
df = pd.DataFrame(list(zip(star_names,distance,mass,radius)),columns = ['Star Names','distance','Mass','Radius'])
print(df)