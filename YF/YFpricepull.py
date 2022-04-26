#Data and URL handling
from locale import currency
#from msilib.schema import Error, tables #Disable for Linux runs
import time
from numpy import append
import requests
from bs4 import BeautifulSoup

import pycountry

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


canada = ['https://ca.finance.yahoo.com/screener/unsaved/c473eb82-e20c-4e8f-968e-7c4a65d1075f', 'canada']

us1 = ['https://ca.finance.yahoo.com/screener/unsaved/f6b0f0b2-a8d2-4e94-9c95-821fa20c05a3', 'us1']
us2 = ['https://ca.finance.yahoo.com/screener/unsaved/365ee524-a031-46b7-b110-145ce3709182', 'us2']

germany1 = ['https://ca.finance.yahoo.com/screener/unsaved/f1c84d3d-f478-4928-8a26-1d885fbe3cfd', 'germany1']
germany2 = ['https://ca.finance.yahoo.com/screener/unsaved/c410f6e1-6bc1-4b99-bfb3-c9151647812e', 'germany2']
germany3 = ['https://ca.finance.yahoo.com/screener/unsaved/72d5cdec-4170-4bbb-803f-5a9b7f9a01b6', 'germany3']
germany4 = ['https://ca.finance.yahoo.com/screener/unsaved/ac3103bd-a865-4e63-b2b3-8f640a071a9e', 'germany4']
germany5 = ['https://ca.finance.yahoo.com/screener/unsaved/d4a05e6b-adb8-4257-9cb0-b2ba8511adb7', 'germany5']

france = ['https://ca.finance.yahoo.com/screener/unsaved/fdb685da-94b8-4d46-836b-86b339ff762d', 'france']

argentina = ['https://ca.finance.yahoo.com/screener/unsaved/c5a9e651-9df4-4ac4-95dc-61792b1a385f', 'argentina']
austria = ['https://ca.finance.yahoo.com/screener/unsaved/1742767c-401e-4ed3-a97c-a143547480ad', 'austria']
australia = ['https://ca.finance.yahoo.com/screener/unsaved/f2660fe0-0c39-4e19-bcb1-cd15d3b73314', 'australia']
belgium = ['https://ca.finance.yahoo.com/screener/unsaved/6818b2ef-7824-478e-a32b-cbcc78d8f9e5', 'belgium']
brazil = ['https://ca.finance.yahoo.com/screener/unsaved/362c7e95-a9ad-4aa2-ac95-76ab21a5ae5d', 'brazil']
switzerland = ['https://ca.finance.yahoo.com/screener/unsaved/4dec4d3e-14ce-4b4c-a4cf-40ede608f829', 'switzerland']
chile = ['https://ca.finance.yahoo.com/screener/unsaved/9e0e6414-675a-4a00-9b6c-b7b91dac3d9b', 'chile']
china = ['https://ca.finance.yahoo.com/screener/unsaved/03c23650-91c0-4d9e-80e5-3d58fc193f79', 'china']
czech_republic = ['https://ca.finance.yahoo.com/screener/unsaved/029555b5-e2ca-4cd4-89de-6089fc4056e1', 'czech_republic']







denmark = ['https://ca.finance.yahoo.com/screener/unsaved/6cd61e78-adcf-4b6c-9dcb-7173bd048c62', 'denmark']
estonia = ['https://ca.finance.yahoo.com/screener/unsaved/fb82ae62-dc37-4772-98d9-6b08aad4ba62', 'estonia']
egypt = ['https://ca.finance.yahoo.com/screener/unsaved/e5bbc488-5aef-49d6-a028-6b5047352b56', 'egypt']
spain = ['https://ca.finance.yahoo.com/screener/unsaved/42ade32c-bbd4-43dc-908d-0feb6bd4092c', 'spain']
finland = ['https://ca.finance.yahoo.com/screener/unsaved/658cc07a-e205-41db-9a92-dbb6d6a82bf7', 'finland']

uk = ['https://ca.finance.yahoo.com/screener/unsaved/3226a9aa-bf2f-4b68-8440-52f3d45be317', 'uk']
greece =['https://ca.finance.yahoo.com/screener/unsaved/16ad731c-bfee-4538-8c5c-d71a5ebc3cf5', 'greece']
hong_kong = ['https://ca.finance.yahoo.com/screener/unsaved/b2abcf5d-2e49-4aed-b24d-63019574986d', 'hong_kong']
hungary = ['https://ca.finance.yahoo.com/screener/unsaved/007abcb6-6918-49eb-9eae-66b2d1cc1655', 'hungary']
indonesia = ['https://ca.finance.yahoo.com/screener/unsaved/b643cd97-007c-4a9c-9d95-62739239d421', 'indonesia']
ireland = ['https://ca.finance.yahoo.com/screener/unsaved/6b3b4537-249f-44ce-b101-a515ce9306b5', 'ireland']
israel = ['https://ca.finance.yahoo.com/screener/unsaved/6ba57da3-6b98-45a1-9450-7042255071b2', 'israel']
india = ['https://ca.finance.yahoo.com/screener/unsaved/ef7110fc-b879-45ea-92aa-25a4351bae51', 'india']
iceland = ['https://ca.finance.yahoo.com/screener/unsaved/30c97040-db89-4274-bbb7-2e1c4caf1390', 'iceland']
italy = ['https://ca.finance.yahoo.com/screener/unsaved/ecfe3584-9309-4d96-b57d-d99805f3e21f', 'italy']
japan = ['https://ca.finance.yahoo.com/screener/unsaved/f1eec316-622c-4063-bb51-d7db5cef27e7', 'japan']
south_korea = ['https://ca.finance.yahoo.com/screener/unsaved/64697652-3249-4332-9026-335d3a0fe570', 'south_korea']
lithuania = ['https://ca.finance.yahoo.com/screener/unsaved/409fb920-b3f3-4436-a50b-64ba98d4ab08', 'lithuania']
latvia = ['https://ca.finance.yahoo.com/screener/unsaved/466f07cb-45c6-48df-a778-bd6ecb51764a', 'latvia']
mexico = ['https://ca.finance.yahoo.com/screener/unsaved/c5b345d8-7fc9-4854-948b-b64da9c0e079', 'mexico']
malaysia = ['https://ca.finance.yahoo.com/screener/unsaved/eef6b36a-2e7f-434f-bbb9-647e8082d86b', 'malaysia']
netherlands = ['https://ca.finance.yahoo.com/screener/unsaved/7b89c306-0f7f-453d-8630-9aaa0b37d9c4', 'netherlands']
norway = ['https://ca.finance.yahoo.com/screener/unsaved/0b028bd8-d241-428c-ac6c-41c7426b40b8', 'norway']
new_zealand = ['https://ca.finance.yahoo.com/screener/unsaved/695d9078-5ce1-4ef1-9bb5-98b94450006d', 'new_zealand']
poland = ['https://ca.finance.yahoo.com/screener/unsaved/29f9277b-9f54-40e5-b333-9af8aa6c67d8', 'poland']
portugal = ['https://ca.finance.yahoo.com/screener/unsaved/0c97bf78-1a05-4665-baef-66ff6bb00153', 'portugal']
qatar = ['https://ca.finance.yahoo.com/screener/unsaved/1e1d3306-3061-464c-8ca1-2c80b3749fb6', 'qatar']
russia = ['https://ca.finance.yahoo.com/screener/unsaved/1e1d3306-3061-464c-8ca1-2c80b3749fb6', 'russia']
saudi_arabia = ['https://ca.finance.yahoo.com/screener/unsaved/8b08a708-81a2-4a5d-8049-5c341ba3356d', 'saudi_arabia']
sweden = ['https://ca.finance.yahoo.com/screener/unsaved/9fc549b4-3f52-4326-8968-db5288e3a82f', 'sweden']
singapore = ['https://ca.finance.yahoo.com/screener/unsaved/fa08bcbc-5456-4b19-b723-7bf0b327e5ae', 'singapore']
thailand = ['https://ca.finance.yahoo.com/screener/unsaved/86d7f6c8-52a5-407f-9a57-86eaf879cd00', 'thailand']
turkey = ['https://ca.finance.yahoo.com/screener/unsaved/082a18bc-4a3c-46b3-9cde-35a773875e3a', 'turkey']
taiwan = ['https://ca.finance.yahoo.com/screener/unsaved/fa4ee96d-58bf-492a-af80-ac1141d9053b', 'taiwan']
venezuela = ['https://ca.finance.yahoo.com/screener/unsaved/6ed6d5ac-f228-4daa-af36-5fae98d2c876', 'venezuela']
south_africa = ['https://ca.finance.yahoo.com/screener/unsaved/785834c2-65d3-407c-b12d-0868938280fc', 'south_africa']


rest_of_link = '?count=100&dependentField=sector&dependentValues=&offset={0}'
combine = [us1, us2, germany1, germany2, germany3, germany4, germany5, france]

done = [canada, argentina, austria, australia, belgium, brazil, switzerland, chile, china, czech_republic, denmark, estonia, egypt, spain, finland, uk, greece, hong_kong, hungary, indonesia, ireland, israel, india, iceland, italy, japan, south_korea, lithuania, latvia, mexico, malaysia, netherlands, norway, new_zealand, poland, portugal, qatar, russia, saudi_arabia, sweden, singapore, thailand, turkey, venezuela, south_africa, taiwan]

not_done = [taiwan]

tables=[]

country = ''
url= ''

#country = turkey
#url = f'{country[0]}?count=250&dependentField=sector&dependentValues=&offset='

def first_5000():
    for i in range(0, 51):
        page = '{0}'.format(i*250)
        url1 = url+page
        print (f'Processing Index {country[1]} {page}')
        try:
            
            try:
                dfs = requests.get(url1, headers=headers).content
                df = pd.read_html(dfs)[0]
            except Exception as v:
                dfs = requests.get(url1, headers=headers).content
                df = pd.read_html(dfs)[0]
                print(v,' retrying')
            if df.empty:
                print(f'{country[1]} loop ended at {page}')
                break
            else:
                tables.append(df)
                time.sleep(2)
        except Exception as e:
            print(e)
            continue
            
        results = pd.concat(tables, axis=0)
        result = results['Symbol']
        results = results.reset_index(drop=True)
        result.to_csv(f'{country[1]}1.csv', index=False)
    print('complete!!!')

def second_5000():
    for i in range(51, 101):
        page = '{0}'.format(i*100)
        url1 = url+page
        print (f'Processing Index {country[1]} {page}')
        try:
            
            try:
                dfs = requests.get(url1, headers=headers).content
                df = pd.read_html(dfs)[0]
            except Exception as v:
                dfs = requests.get(url1, headers=headers).content
                df = pd.read_html(dfs)[0]
                print(v,' retrying')
            if df.empty:
                print(f'{country[1]} loop ended at {page}')
                break
            else:
                tables.append(df)
                time.sleep(2)
        except Exception as e:
            print(e)
            continue
            
        results = pd.concat(tables, axis=0)
        result = results['Symbol']
        results = results.reset_index(drop=True)
        result.to_csv(f'{country[1]}2.csv', index=False)
    print('complete!!!')

def third_5000():
    for i in range(101, 151):
        page = '{0}'.format(i*100)
        url1 = url+page
        print (f'Processing Index {country[1]} {page}')
        try:
            
            try:
                dfs = requests.get(url1, headers=headers).content
                df = pd.read_html(dfs)[0]
            except Exception as v:
                dfs = requests.get(url1, headers=headers).content
                df = pd.read_html(dfs)[0]
                print(v,' retrying')
            if df.empty:
                print(f'{country[1]} loop ended at {page}')
                break
            else:
                tables.append(df)
                time.sleep(2)
        except Exception as e:
            print(e)
            continue
            
        results = pd.concat(tables, axis=0)
        result = results['Symbol']
        results = results.reset_index(drop=True)
        result.to_csv(f'{country[1]}3.csv', index=False)
    print('complete!!!')



#%%

'''
code to combine multifile CSV

'''
# country = south_africa
# url = f'{country[0]}?count=250&dependentField=sector&dependentValues=&offset='
# #first_5000()

# #%%

# combine = [us1, us2, germany1, germany2, germany3, germany4, germany5]

# name = 'germany'

# df1 = pd.read_csv(name+'11.csv')
# df2 = pd.read_csv(name+'21.csv')
# df3 = pd.read_csv(name+'31.csv')
# df4 = pd.read_csv(name+'41.csv')
# df5 = pd.read_csv(name+'51.csv')

# df3 = pd.concat([df1,df2,df3,df4,df5]).drop_duplicates().reset_index(drop=True)
# df3.to_csv(f'germany.csv', index=False)







#%%


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








#%%

done = [canada, argentina, austria, belgium, chile,australia,brazil,switzerland, china,czech_republic,denmark,estonia, egypt, spain, finland, uk, greece, hong_kong, hungary, indonesia, ireland, israel, india, france, iceland, japan, south_korea, lithuania, mexico, malaysia, netherlands, norway, new_zealand, poland, portugal, qatar, russia, saudi_arabia, sweden, singapore, thailand, venezuela, south_africa,]

notdone = []


appended_data = []

countryname = 'germany'
print(countryname)


filename = countryname+'1.csv'
df = pd.read_csv(filename)

for index, row in df.iterrows():
    tick = row.Symbol
    page = requests.get(f"https://ca.finance.yahoo.com/quote/{tick}/profile?p={tick}", headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    try:
        exchange = soup.select_one('#quote-header-info > div.Mt\(15px\).D\(f\).Jc\(sb\) > div.D\(ib\).Mt\(-5px\).Maw\(38\%\)--tab768.Maw\(38\%\).Mend\(10px\).Ov\(h\).smartphone_Maw\(85\%\).smartphone_Mend\(0px\) > div.C\(\$tertiaryColor\).Fz\(12px\) > span').text
        #exchange = exchange.split()[0]
        #currency1 = exchange.resplit()[0]
        first, *middle, last = exchange.split()

        exchange = first
        currency1 = last
    except AttributeError as e:
        print('exchange blank')
        sector = ''
    try:
        sector = soup.select_one('#Col1-0-Profile-Proxy > section > div.asset-profile-container > div > div > p.D\(ib\).Va\(t\) > span:nth-child(2)').text
    except AttributeError as e:
        print('sector blank')
        sector = ''

    try:
        industry = soup.select_one('#Col1-0-Profile-Proxy > section > div.asset-profile-container > div > div > p.D\(ib\).Va\(t\) > span:nth-child(5)').text
    except AttributeError as e:
        print('industry blank')
        industry = ''

    try:
        employees = soup.select_one('#Col1-0-Profile-Proxy > section > div.asset-profile-container > div > div > p.D\(ib\).Va\(t\) > span:nth-child(8)').text

    except AttributeError as e:
        print('employees blank')
        employees = ''

    try:
        location = soup.select_one('#Col1-0-Profile-Proxy > section > div.asset-profile-container > div > div > p.D\(ib\).W\(47\.727\%\).Pend\(40px\)')
        location = location.get_text(separator=", ")
    except AttributeError as e:
        print('location blank')
        location = ''

    for c in pycountry.countries:
        if c.name in location:
            #Country's name
            country_name = (c.name)
            #Country's code
            country_code = (c.alpha_2)
            # Country's official name
            try:
                country_official_name = (c.official_name)
            except AttributeError as e:
                continue

    data = [[tick, exchange, country_name, currency1, sector, industry, employees]]

    df = pd.DataFrame(data, columns = ['tick', 'exchange', 'country_name', 'currency', 'sector', 'industry', 'fulltime_employees'])

    appended_data.append(df)
    
    results = pd.concat(appended_data, axis=0)
    results = results.reset_index(drop=True)
    print(results.tail(1))
    results.to_csv(countryname+'.csv')

#%%
