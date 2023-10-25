from bs4 import BeautifulSoup
import requests

filename = "https://www.moneycontrol.com/stocks/marketstats/nsegainer/index.php?index=FNO"
def scrape(filename):
    web = requests.get(filename).text
    soup = BeautifulSoup(web,'lxml')
    stocks = soup.find('div',class_="bsr_table hist_tbl_hm")
    
    row=[]
    
    rows = stocks.find_all('tr')
    for idx in range(8,len(rows)):
        #pass
        row.append(rows[idx].find('tr'))
    print(row)


scrape(filename)