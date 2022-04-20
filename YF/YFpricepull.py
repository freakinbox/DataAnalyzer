#Data and URL handling
from msilib.schema import tables
import time
import requests
from bs4 import BeautifulSoup

import pandas as pd
import urllib.request, urllib.error



#pd.set_option('display.max_columns', None) #Will display entire dataframe in console if activated
#%%
####### general functions ########

#tick = 'GME'
#p1 = 959385600
#p2 = 1650153600
#int = '1d'

def yfprice(ticker, period1, period2, interval):
    url = f'https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={period1}&period2={period2}&interval={interval}&events=history&includeAdjustedClose=true'

    '''periods must be in unicode for now 1 is start and 2 is end
        TODO add converter for normal dates so others can plug what they want into this
           - To this or the normal program? Not sure.
       Interval options are 1d , 1wk, 1mo   
    '''
    #URL status checker
    try:
        conn = urllib.request.urlopen(url)
    except urllib.error.HTTPError as e:
        # Return code error (e.g. 404, 501, ...)
        # ...
        print('HTTPError: {}'.format(e.code))
        df = '404'
        return df
    except urllib.error.URLError as e:
        # Not an HTTP-specific error (e.g. connection refused)
        # ...
        print('URLError: {}'.format(e.reason))
        df='error'
        return df
    else:
        # 200
        # ...
        print('good')
        df = pd.read_csv(url)
        df['Date'] = pd.to_datetime(df['Date'])
        #df = df.sort_index(ascending=False)

    return df

#df = yfprice(tick, p1, p2, int) #Testcode
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}



#Canada Stock Market list
def UpdateCan(): #this could be run as a daily update from Yahoo for all Canadian stocks and then just concat onto old file on server
    tables=[]
    for i in range(0, 30000):
        url = 'https://ca.finance.yahoo.com/screener/unsaved/c473eb82-e20c-4e8f-968e-7c4a65d1075f?count=100&dependentField=sector&dependentValues=&offset={0}'.format(i*100)
        
        print ('Processing Index {0}'.format(i*100))

        try:
            dfs = requests.get(url, headers=headers).content
            df = pd.read_html(dfs)[0]
            if df.empty:
                print('loop ended')
                break
            else:
                tables.append(df)
                #time.sleep(1)
        except Exception as e:
            print(e)
            continue
        
    results = pd.concat(tables, axis=0)

    result = results['Symbol']
    result.to_csv('Canada.csv', index=False)


    print('Update Can finished')

def UpdateNasdaqGS():
    tables=[]
    for i in range(0, 30000):
        url = 'https://ca.finance.yahoo.com/screener/unsaved/217a7f7b-a655-4af3-9fd9-5a9872379cbc?count=100&offset={0}'.format(i*100)
        
        print ('Processing Index {0}'.format(i*100))

        try:
            dfs = requests.get(url, headers=headers).content
            df = pd.read_html(dfs)[0]
            if df.empty:
                print('loop ended')
                break
            else:
                tables.append(df)
                #time.sleep(1)
        except Exception as e:
            print(e)
            continue
        
    results = pd.concat(tables, axis=0)

    result = results['Symbol']
    result.to_csv('NasdaqGS.csv', index=False)


    print('Update Nasdaq GS finished')

def UpdateNasdaqCM():
    tables=[]
    for i in range(0, 30000):
        url = 'https://ca.finance.yahoo.com/screener/unsaved/dd9b9cb4-5b41-4548-b64c-507a4dc196a7?count=100&offset={0}'.format(i*100)
        
        print ('Processing Index {0}'.format(i*100))

        try:
            dfs = requests.get(url, headers=headers).content
            df = pd.read_html(dfs)[0]
            if df.empty:
                print('loop ended')
                break
            else:
                tables.append(df)
                #time.sleep(1)
        except Exception as e:
            print(e)
            continue
        
    results = pd.concat(tables, axis=0)

    result = results['Symbol']
    result.to_csv('NasdaqCM.csv', index=False)


    print('Update Nasdaq CM finished')

def UpdateNasdaqGM():
    tables=[]
    for i in range(0, 30000):
        url = 'https://ca.finance.yahoo.com/screener/unsaved/b03ec675-feae-4645-8ebd-6cd3fd20fa39?count=100&offset={0}'.format(i*100)
        
        print ('Processing Index {0}'.format(i*100))

        try:
            dfs = requests.get(url, headers=headers).content
            df = pd.read_html(dfs)[0]
            if df.empty:
                print('loop ended')
                break
            else:
                tables.append(df)
                #time.sleep(1)
        except Exception as e:
            print(e)
            continue
        
    results = pd.concat(tables, axis=0)

    result = results['Symbol']
    result.to_csv('NasdaqGM.csv', index=False)


    print('Update Nasdaq GM finished')

def UpdateBAS():
    tables=[]
    for i in range(0, 30000):
        url = 'https://ca.finance.yahoo.com/screener/unsaved/ddf09ad9-6856-4b01-a837-69b3dea3cd55?count=100&offset={0}'.format(i*100)
        
        print ('Processing Index {0}'.format(i*100))

        try:
            dfs = requests.get(url, headers=headers).content
            df = pd.read_html(dfs)[0]
            if df.empty:
                print('loop ended')
                break
            else:
                tables.append(df)
                #time.sleep(1)
        except Exception as e:
            print(e)
            continue
        
    results = pd.concat(tables, axis=0)

    result = results['Symbol']
    result.to_csv('BAS.csv', index=False)


    print('Update BAS finished')

def UpdateNYSE():
    tables=[]
    for i in range(0, 30000):
        url = 'https://ca.finance.yahoo.com/screener/unsaved/c13355aa-b574-48b1-b472-be353c61e5e7?count=100&offset={0}'.format(i*100)
        
        print ('Processing Index {0}'.format(i*100))

        try:
            dfs = requests.get(url, headers=headers).content
            df = pd.read_html(dfs)[0]
            if df.empty:
                print('loop ended')
                break
            else:
                tables.append(df)
                #time.sleep(1)
        except Exception as e:
            print(e)
            continue
        
    results = pd.concat(tables, axis=0)

    result = results['Symbol']
    result.to_csv('NYSE.csv', index=False)


    print('Update NYSE finished')


url = 'https://ca.finance.yahoo.com/quote/GME/profile?p=GME'
        
dfs = requests.get(url, headers=headers).content
df = pd.read_html(dfs)
            
#%%               

# page = requests.get("https://ca.finance.yahoo.com/quote/GME/profile?p=GME", headers=headers)
# soup = BeautifulSoup(page.content, 'html.parser')





#  # Extract first <h1>(...)</h1> text
# first_h1 = soup.select('body')[0]

print(first_h1)



#%%

UpdateCan()
UpdateNasdaqCM()
UpdateNasdaqGM()
UpdateNasdaqGS()
UpdateNYSE()
UpdateBAS()

#%%
