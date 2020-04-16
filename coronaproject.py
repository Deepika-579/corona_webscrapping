import requests
from bs4 import BeautifulSoup
import pandas
url="https://www.worldometers.info/coronavirus/"
r=requests.get(url)
print(r.text)
html=r.text
soup=BeautifulSoup(html,'html.parser')
print(soup.title.text)
print()
print()
live_data=soup.find_all('div',id='maincounter-wrap')
for i in live_data:
    print(i.text)
table_body=soup.find('tbody')
table_rows=table_body.find_all('tr')
countries=[]
totalcases=[]
newcases=[]
totaldeath=[]
todaysdeath=[]
totalrecoveries=[]
for tr in table_rows:
    td=tr.find_all('td')
    countries.append(td[0].text)
    totalcases.append(td[1].text)
    newcases.append(td[2].text)
    totaldeath.append(td[3].text)
    todaysdeath.append(td[4].text)
    totalrecoveries.append(td[5].text)
headers=['countries','totalcases','new cases','totaldeath','todays death','totalrecoveries']
df=pandas.DataFrame(list(zip(countries,totalcases,newcases,totaldeath,todaysdeath,totalrecoveries)),columns=headers)
print(df)
        
    


