#Data and URL handling
from locale import currency
from msilib.schema import Error, tables #Disable for Linux runs

from random import randint
from time import sleep

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

def yfprice(ticker, period1, period2, interval): #historical price puller, need to adapt for both single ticker and trying to use it on entire lists.
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


screener_new = 'https://ca.finance.yahoo.com/screener/new'





canada = ['ed305f75-c040-495b-844d-fde9fdd5ba1a', 'canada1']
us1 = ['f6b0f0b2-a8d2-4e94-9c95-821fa20c05a3', 'us1']
us2 = ['365ee524-a031-46b7-b110-145ce3709182', 'us2']
germany1 = ['f1c84d3d-f478-4928-8a26-1d885fbe3cfd', 'germany1']
germany2 = ['c410f6e1-6bc1-4b99-bfb3-c9151647812e', 'germany2']
germany3 = ['72d5cdec-4170-4bbb-803f-5a9b7f9a01b6', 'germany3']
germany4 = ['ac3103bd-a865-4e63-b2b3-8f640a071a9e', 'germany4']
germany5 = ['d4a05e6b-adb8-4257-9cb0-b2ba8511adb7', 'germany5']
france = ['fdb685da-94b8-4d46-836b-86b339ff762d', 'france1']
argentina = ['c5a9e651-9df4-4ac4-95dc-61792b1a385f', 'argentina1']
austria = ['1742767c-401e-4ed3-a97c-a143547480ad', 'austria1']
australia = ['f2660fe0-0c39-4e19-bcb1-cd15d3b73314', 'australia1']
belgium = ['6818b2ef-7824-478e-a32b-cbcc78d8f9e5', 'belgium1']
brazil = ['362c7e95-a9ad-4aa2-ac95-76ab21a5ae5d', 'brazil1']
switzerland = ['4dec4d3e-14ce-4b4c-a4cf-40ede608f829', 'switzerland1']
chile = ['9e0e6414-675a-4a00-9b6c-b7b91dac3d9b', 'chile1']
china = ['03c23650-91c0-4d9e-80e5-3d58fc193f79', 'china1']
czech_republic = ['029555b5-e2ca-4cd4-89de-6089fc4056e1', 'czech_republic1']
denmark = ['6cd61e78-adcf-4b6c-9dcb-7173bd048c62', 'denmark1']
estonia = ['fb82ae62-dc37-4772-98d9-6b08aad4ba62', 'estonia1']
egypt = ['e5bbc488-5aef-49d6-a028-6b5047352b56', 'egypt1']
spain = ['42ade32c-bbd4-43dc-908d-0feb6bd4092c', 'spain1']
finland = ['658cc07a-e205-41db-9a92-dbb6d6a82bf7', 'finland1']
uk = ['3226a9aa-bf2f-4b68-8440-52f3d45be317', 'uk1']
greece =['16ad731c-bfee-4538-8c5c-d71a5ebc3cf5', 'greece1']
hong_kong = ['b2abcf5d-2e49-4aed-b24d-63019574986d', 'hong_kong1']
hungary = ['007abcb6-6918-49eb-9eae-66b2d1cc1655', 'hungary1']
indonesia = ['b643cd97-007c-4a9c-9d95-62739239d421', 'indonesia1']
ireland = ['6b3b4537-249f-44ce-b101-a515ce9306b5', 'ireland1']
israel = ['6ba57da3-6b98-45a1-9450-7042255071b2', 'israel1']
india = ['ef7110fc-b879-45ea-92aa-25a4351bae51', 'india1']
iceland = ['30c97040-db89-4274-bbb7-2e1c4caf1390', 'iceland1']
italy = ['ecfe3584-9309-4d96-b57d-d99805f3e21f', 'italy1']
japan = ['f1eec316-622c-4063-bb51-d7db5cef27e7', 'japan1']
south_korea = ['64697652-3249-4332-9026-335d3a0fe570', 'south_korea1']
lithuania = ['409fb920-b3f3-4436-a50b-64ba98d4ab08', 'lithuania1']
latvia = ['466f07cb-45c6-48df-a778-bd6ecb51764a', 'latvia1']
mexico = ['c5b345d8-7fc9-4854-948b-b64da9c0e079', 'mexico1']
malaysia = ['eef6b36a-2e7f-434f-bbb9-647e8082d86b', 'malaysia1']
netherlands = ['7b89c306-0f7f-453d-8630-9aaa0b37d9c4', 'netherlands1']
norway = ['0b028bd8-d241-428c-ac6c-41c7426b40b8', 'norway1']
new_zealand = ['695d9078-5ce1-4ef1-9bb5-98b94450006d', 'new_zealand1']
poland = ['29f9277b-9f54-40e5-b333-9af8aa6c67d8', 'poland1']
portugal = ['0c97bf78-1a05-4665-baef-66ff6bb00153', 'portugal1']
qatar = ['1e1d3306-3061-464c-8ca1-2c80b3749fb6', 'qatar1']
russia = ['1e1d3306-3061-464c-8ca1-2c80b3749fb6', 'russia1']
saudi_arabia = ['8b08a708-81a2-4a5d-8049-5c341ba3356d', 'saudi_arabia1']
sweden = ['9fc549b4-3f52-4326-8968-db5288e3a82f', 'sweden1']
singapore = ['fa08bcbc-5456-4b19-b723-7bf0b327e5ae', 'singapore1']
thailand = ['86d7f6c8-52a5-407f-9a57-86eaf879cd00', 'thailand1']
turkey = ['082a18bc-4a3c-46b3-9cde-35a773875e3a', 'turkey1']
taiwan = ['fa4ee96d-58bf-492a-af80-ac1141d9053b', 'taiwan1']
venezuela = ['6ed6d5ac-f228-4daa-af36-5fae98d2c876', 'venezuela1']
south_africa = ['785834c2-65d3-407c-b12d-0868938280fc', 'south_africa1']


list1 = [canada, us1, us2, germany1, germany2, germany3, germany4, germany5, france, argentina, austria, australia, belgium, brazil, switzerland, chile, china, czech_republic, denmark, estonia, egypt, spain, finland, uk, greece, hong_kong, hungary, indonesia, ireland, india, iceland, italy, japan, south_korea, lithuania, latvia, mexico, malaysia, netherlands, norway, new_zealand, poland, portugal, qatar, russia, saudi_arabia, sweden, singapore, thailand, turkey, taiwan, venezuela, south_africa]


combine = [us1, us2, germany1, germany2, germany3, germany4, germany5, france]


country = ''

country = us1


def yf_screener_scraper(): #Need to test
    ''' 10k is the limit on the screener on Yahoo Finance'''
    url = f'https://ca.finance.yahoo.com/screener/unsaved/{country[0]}?count=250&dependentField=sector&dependentValues=&offset='
    tables=[]


    print('1')
    for i in range(0, 201):
    
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
                print(v,'retrying')
            if df.empty:
                print(f'{country[1]} loop ended at {page}')
                break
            else:
                tables.append(df)
                sleep(randint(1,3))
        except Exception as e:
            print(e)
            break
            
        results = pd.concat(tables, axis=0)

        trigger = trigger+1

        if trigger[1] == 20:
            pause1 = randint(45,60)
            count = count+6
            print(f'{count} done, sleeping for {pause1}')
            sleep(pause1)
            trigger[1] = 0
            

    results.drop_duplicates()
    result = results['Symbol']
    result.to_csv(f'{country[1]}.csv', index=False)
    print('Done!')



germanylist = [germany1, germany2, germany3, germany4, germany5]


list2 = [canada, us1, us2, germany1, germany2, germany3, germany4, germany5, france, argentina, austria, australia, belgium, brazil, switzerland, chile, china, czech_republic, denmark, estonia, egypt, spain, finland, uk, greece, hong_kong, hungary, indonesia, ireland, india, iceland, italy, japan, south_korea, lithuania, latvia, mexico, malaysia, netherlands, norway, new_zealand, poland, portugal, qatar, russia, saudi_arabia, sweden, singapore, thailand, turkey, taiwan, venezuela, south_africa]



for l in germanylist:
    country = l
    yf_screener_scraper()
    print ('finished, you can restart')

#%%

'''
code to combine multifile CSV

'''
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



appended_data = []
countryname = 'germany'
print(countryname)



for i in list1:
    #filename = i+'.csv'
    #df = pd.read_csv(filename)

    df = pd.read_csv(i+'.csv')

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
