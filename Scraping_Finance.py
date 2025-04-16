import requests
from bs4 import BeautifulSoup
import pandas as pd 


# This is a logic that allows us to navigate through all the website pages
pages = [1 + i*20 for i in range(0, (9981-21)//20 + 1)]

# Empty lists
No = []
Company = []
Sector = []
Industry = []
Country = []
PE = []
PEG = []
PB = []
Dividend = []
EPS = []
ROA = []
ROE = []
DE = []
ProfitM = []
Beta = []
Earnings = []
Volume = []
Price = []
Change = []
Ticker = []

for i in pages:
    main_url = 'https://****.com/screener.****='+str(i)
    headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"}
    main_response = requests.get(main_url, headers=headers)
    main_soup = BeautifulSoup(main_response.text,'html.parser')

table = main_soup.find('table',class_='styled-table-new is-rounded is-tabular-nums w-full screener_table')
header = table.find('tr',align='center')
header2 = header.find_all('th',class_='table-header cursor-pointer')
cols = []

for i in header2:
    col = i.text
    cols.append(col)

rows = table.find_all('tr',valign='top')
rows1 = []
for i in rows:
    test = i.find_all('td',height='10')
    temp = []
    for j in test:
        temp.append(j.text)
    rows1.append(temp)

for i in rows1:
    No.append(i[0])
    Ticker.append(i[1])
    Company.append(i[2])
    Sector.append(i[3])
    Industry.append(i[4])
    Country.append(i[5])
    PE.append(i[7])
    PEG.append(i[8])
    PB.append(i[9])
    Dividend.append(i[10])
    EPS.append(i[11])
    ROA.append(i[12])
    ROE.append(i[13])
    DE.append(i[14])
    ProfitM.append(i[15])
    Beta.append(i[16])
    Earnings.append(i[17])
    Volume.append(i[18])
    Price.append(i[19])
    Change.append(i[20])

df = pd.DataFrame({'Symbol':Ticker,
    'Company':Company,
    'Sector':Sector,
    'Industry':Industry,
    'Country':Country,
    'Price':Price,
    'ROA':ROA,
    'ROE':ROE,       
    'Beta':Beta,       
    'Debt_Equity':DE,                   
    'Price_Earning':PE,
    'EPS':EPS,                
    'PEG':PEG,
    'Change':Change,                   
    'Price_Book':PB,
    'Payment_Date':Earnings,                   
    'Dividend':Dividend,
    'Profit_Margin':ProfitM,
    'Volume':Volume
    })

df = df.applymap(lambda x: 'null' if x == '-' else x)

cols_to_modify = ['Price', 'ROA', 'ROE', 'Profit_Margin', 'Change',
                'Price_Earning', 'PEG', 'Price_Book', 'EPS',
                'Debt_Equity', 'Beta', 'Dividend']

for col in cols_to_modify:
    df[col] = df[col].astype(str)
    df[col] = df[col].str.replace('%', '')
    df[col] = df[col].str.replace('.', ',')

df = df.applymap(lambda x: 'null' if x == '-' else x)

cols_to_modify = ['Price', 'ROA', 'ROE', 'Profit_Margin', 'Change',
                'Price_Earning', 'PEG', 'Price_Book', 'EPS',
                'Debt_Equity', 'Beta', 'Dividend']

for col in cols_to_modify:
    df[col] = df[col].astype(str)
    df[col] = df[col].str.replace('%', '')
    df[col] = df[col].str.replace('.', ',')
