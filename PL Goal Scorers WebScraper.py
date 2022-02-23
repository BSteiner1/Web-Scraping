#import libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs4
import requests
import pandas as pd

#define url
url = "https://www.bbc.co.uk/sport/football/premier-league/top-scorers"
#use requests to find the page
r = requests.get(url)

#use bs4 to scrape relevant column data 
soup = bs4(r.content, 'html.parser')
columns = soup.find("thead").find_all("th")

#define table columns
column_names = [c.string for c in columns]
print(column_names)

#add column headers not scraped from previous section
new_columns = soup.find("thead").find_all("span", class_ = 'gs-u-vh gs-u-display-inherit@m')
add_columns = [c.string for c in new_columns]

column_names[0] = "Player Rank"
for x in range(2,5):
    column_names[x] = add_columns[x-2]
print(add_columns)
column_names[6] = "Mins per Goal"

print(column_names)
    
#use bs4 to scrape relevant row data 
#create our list 'l' of rows
l = []
table_rows = soup.find("tbody").find_all("tr")
for tr in table_rows:
    td = tr.find_all("td")
    row = [str(tr.get_text()).strip() for tr in td]
    l.append(row)

df = pd.DataFrame(l, columns=column_names)
df.to_csv(r'C:\Users\bbste\Documents\Coding\Python\Gol.csv')

print(df.head())

