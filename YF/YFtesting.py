

from msilib.schema import Error, tables #Disable for Linux runs

from random import randint
from time import sleep

from numpy import append
import requests
import json
from bs4 import BeautifulSoup


import pandas as pd
import urllib.request, urllib.error



#%%


#headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
def newpuller():
    appended_data=[]
    total = 0

    for i in range(0,41):

    

        page = i*250

        if page > (total+250):
            print('ending')
            break

        print (f'Processing Index {page} / {total}')

        cookies = {
            'B': '7b0s3s5h5qof2&b=3&s=05',
            'PRF': 't%3D2330.TW%252BSCM1R.RG%252BAMC%252BDAC.V%252BGME',
            'A1': 'd=AQABBOJhXWICEJDDoC-1ue9fht2Ig-GDg3UFEgEBBgFvaWJSYyUHb2UB_eMBAAcI4mFdYuGDg3U&S=AQAAAusHy4pL3cCa8tWvsZ7MOEc',
            'A3': 'd=AQABBOJhXWICEJDDoC-1ue9fht2Ig-GDg3UFEgEBBgFvaWJSYyUHb2UB_eMBAAcI4mFdYuGDg3U&S=AQAAAusHy4pL3cCa8tWvsZ7MOEc',
            'A1S': 'd=AQABBOJhXWICEJDDoC-1ue9fht2Ig-GDg3UFEgEBBgFvaWJSYyUHb2UB_eMBAAcI4mFdYuGDg3U&S=AQAAAusHy4pL3cCa8tWvsZ7MOEc&j=WORLD',
            'GUC': 'AQEBBgFiaW9jUkIcXAQt',
            'ucs': 'lbit=1',
            'cmp': 't=1651145165&j=0&u=1---',
        }

        headers = {
            'authority': 'query2.finance.yahoo.com',
            'accept': '*/*',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'cache-control': 'no-cache',
            # Already added when you pass json=
            # 'content-type': 'application/json',
            # Requests sorts cookies= alphabetically
            # 'cookie': 'B=7b0s3s5h5qof2&b=3&s=05; PRF=t%3D2330.TW%252BSCM1R.RG%252BAMC%252BDAC.V%252BGME; A1=d=AQABBOJhXWICEJDDoC-1ue9fht2Ig-GDg3UFEgEBBgFvaWJSYyUHb2UB_eMBAAcI4mFdYuGDg3U&S=AQAAAusHy4pL3cCa8tWvsZ7MOEc; A3=d=AQABBOJhXWICEJDDoC-1ue9fht2Ig-GDg3UFEgEBBgFvaWJSYyUHb2UB_eMBAAcI4mFdYuGDg3U&S=AQAAAusHy4pL3cCa8tWvsZ7MOEc; A1S=d=AQABBOJhXWICEJDDoC-1ue9fht2Ig-GDg3UFEgEBBgFvaWJSYyUHb2UB_eMBAAcI4mFdYuGDg3U&S=AQAAAusHy4pL3cCa8tWvsZ7MOEc&j=WORLD; GUC=AQEBBgFiaW9jUkIcXAQt; ucs=lbit=1; cmp=t=1651145165&j=0&u=1---',
            'origin': 'https://ca.finance.yahoo.com',
            'pragma': 'no-cache',
            'referer': 'https://ca.finance.yahoo.com/screener/new',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
        }

        params = {
            'crumb': 'qaFzythCc3q',
            'lang': 'en-CA',
            'region': 'CA',
            'formatted': 'true',
            'corsDomain': 'ca.finance.yahoo.com',
        }

        json_data = {
            'size': 250,
            'offset': page,
            'sortField': 'intradaymarketcap',
            'sortType': 'DESC',
            'quoteType': 'EQUITY',
            'topOperator': 'AND',
            'query': {
                'operator': 'AND',
                'operands': [
                    {
                        'operator': 'or',
                        'operands': [
                            {
                                'operator': 'EQ',
                                'operands': [
                                    'region',
                                    'ca',
                                ],
                            },
                        ],
                    },
                ],
            },
            'userId': '',
            'userIdType': 'guid',
        }

        response = requests.post('https://query2.finance.yahoo.com/v1/finance/screener', params=params, cookies=cookies, headers=headers, json=json_data)

        x = json.loads(response.text)
        
        if i==0:
            total = int(x['finance']['result'][0]['total'])
        
        
        df = pd.json_normalize(x['finance']['result'][0]['quotes'])

        appended_data.append(df)
        results = pd.concat(appended_data, axis=0)
        results = results.reset_index(drop=True)
        #results.to_csv('canada_test.csv')
        
        
        sleep(randint(1,3))
    results.drop_duplicates()
    results.to_csv(f'canada_test.csv', index=False)
    print('Done!')


#%%


## Germany between then end of day price (EOD)
import requests




argentina = ['ar', 'argentina']
austria = ['at', 'austria']
australia = ['au', 'australia']
belgium = ['be', 'belgium']
brazil = ['br', 'brazil']
canada = ['ca', 'canada']
switzerland = ['ch', 'switzerland']
chile = ['cl','chile']
china = ['cn', 'china']
czech_republic = ['cz', 'czech_republic']
germany = ['de', 'germany']
denmark = ['dk', 'denmark']
estonia = ['ee', 'estonia']
egypt = ['eg', 'egypt']
spain = ['es', 'spain']
finland = ['fi', 'finland']
france = ['fr', 'france']
united_kingdom = ['gb', 'united_kingdom']
greece = ['gr', 'greece']
hong_kong = ['hk', 'hong_kong']
hungary = ['hu', 'hungary']
indonesia = ['id', 'indonesia']
ireland = ['ie', 'ireland']
israel = ['il', 'israel']
india = ['in', 'india']
iceland = ['is', 'iceland']
italy = ['it', 'italy']
japan = ['jp', 'japan']
south_korea = ['kr', 'south_korea']
sri_lanka = ['lk', 'sri_lanka']
lithuania = ['lt', 'lithuania']
latvia = ['lv', 'latvia']
mexico = ['mx', 'mexico']
malaysia = ['my', 'malaysia']
netherlands = ['nl', 'netherlands']
norway = ['no', 'norway']
new_zealand = ['nz', 'new_zealand']
poland = ['pl', 'poland']
portugal = ['pt', 'portugal']
qatar = ['qa', 'qatar']
russia = ['ru', 'russia']
saudi_arabia = ['sa', 'saudi_arabia']
sweden = ['se', 'sweden']
singapore = ['sg', 'singapore']
thailand = ['th', 'thailand']
turkey = ['tr', 'turkey']
taiwan = ['tw', 'taiwan']
united_states = ['us', 'united_states']
venezuela = ['ve', 'venezuela']
south_africa = ['za', 'south_africa']


Countries = [argentina, austria , australia, belgium, brazil,canada, switzerland, chile, china, czech_republic, germany, denmark, estonia, egypt, spain, finland, france, united_kingdom, greece, hong_kong, hungary, indonesia, ireland, israel, india, iceland, italy, japan, south_korea, sri_lanka, lithuania, latvia, mexico, malaysia, netherlands, norway, new_zealand, poland, portugal, qatar, russia, saudi_arabia, sweden, singapore, thailand, turkey, taiwan, united_states, venezuela, south_africa]









country_code = germany
print ('Country code = ', country_code[0])
print ('Country name = ', country_code[1])






appended_data=[]



cookies = {
    'B': '7b0s3s5h5qof2&b=3&s=05',
    'PRF': 't%3D2330.TW%252BSCM1R.RG%252BAMC%252BDAC.V%252BGME',
    'A1': 'd=AQABBOJhXWICEJDDoC-1ue9fht2Ig-GDg3UFEgEBBgFvaWJSYyUHb2UB_eMBAAcI4mFdYuGDg3U&S=AQAAAusHy4pL3cCa8tWvsZ7MOEc',
    'A3': 'd=AQABBOJhXWICEJDDoC-1ue9fht2Ig-GDg3UFEgEBBgFvaWJSYyUHb2UB_eMBAAcI4mFdYuGDg3U&S=AQAAAusHy4pL3cCa8tWvsZ7MOEc',
    'A1S': 'd=AQABBOJhXWICEJDDoC-1ue9fht2Ig-GDg3UFEgEBBgFvaWJSYyUHb2UB_eMBAAcI4mFdYuGDg3U&S=AQAAAusHy4pL3cCa8tWvsZ7MOEc&j=WORLD',
    'GUC': 'AQEBBgFiaW9jUkIcXAQt',
    'ucs': 'lbit=1',
    'cmp': 't=1651145165&j=0&u=1---',
}

headers = {
    'authority': 'query2.finance.yahoo.com',
    'accept': '*/*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cache-control': 'no-cache',
    # Already added when you pass json=
    # 'content-type': 'application/json',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'B=7b0s3s5h5qof2&b=3&s=05; PRF=t%3D2330.TW%252BSCM1R.RG%252BAMC%252BDAC.V%252BGME; A1=d=AQABBOJhXWICEJDDoC-1ue9fht2Ig-GDg3UFEgEBBgFvaWJSYyUHb2UB_eMBAAcI4mFdYuGDg3U&S=AQAAAusHy4pL3cCa8tWvsZ7MOEc; A3=d=AQABBOJhXWICEJDDoC-1ue9fht2Ig-GDg3UFEgEBBgFvaWJSYyUHb2UB_eMBAAcI4mFdYuGDg3U&S=AQAAAusHy4pL3cCa8tWvsZ7MOEc; A1S=d=AQABBOJhXWICEJDDoC-1ue9fht2Ig-GDg3UFEgEBBgFvaWJSYyUHb2UB_eMBAAcI4mFdYuGDg3U&S=AQAAAusHy4pL3cCa8tWvsZ7MOEc&j=WORLD; GUC=AQEBBgFiaW9jUkIcXAQt; ucs=lbit=1; cmp=t=1651145165&j=0&u=1---',
    'origin': 'https://ca.finance.yahoo.com',
    'pragma': 'no-cache',
    'referer': 'https://ca.finance.yahoo.com/screener/new',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
}

params = {
    'crumb': 'qaFzythCc3q',
    'lang': 'en-CA',
    'region': 'CA',
    'formatted': 'true',
    'corsDomain': 'ca.finance.yahoo.com',
}

json_data = {
    'size': 25,
    'offset': 0,
    'sortField': 'intradaymarketcap',
    'sortType': 'DESC',
    'quoteType': 'EQUITY',
    'topOperator': 'AND',
    'query': {
        'operator': 'AND',
        'operands': [
            {
                'operator': 'or',
                'operands': [
                    {
                        'operator': 'EQ',
                        'operands': [
                            'region',
                            country_code[0],
                        ],
                    },
                ],
            },
        ],
    },
    'userId': '',
    'userIdType': 'guid',
}

print ('checking upper limit')
response = requests.post('https://query2.finance.yahoo.com/v1/finance/screener', params=params, cookies=cookies, headers=headers, json=json_data)

x = json.loads(response.text)

total = int(x['finance']['result'][0]['total'])

#delete later
print('delete later')

def eodprice_range(min, max):
    json_data = {
            'size': 25,
            'offset': 0,
            'sortField': 'intradaymarketcap',
            'sortType': 'DESC',
            'quoteType': 'EQUITY',
            'topOperator': 'AND',
            'query': {
                'operator': 'AND',
                'operands': [
                    {
                        'operator': 'or',
                        'operands': [
                            {
                                'operator': 'EQ',
                                'operands': [
                                    'region',
                                    country_code[0],
                                ],
                            },
                        ],
                    },
                    {
                        'operator': 'btwn',
                        'operands': [
                            'eodprice',
                            min,
                            max,
                        ],
                    },
                ],
            },
            'userId': '',
            'userIdType': 'guid',
        }

    response = requests.post('https://query1.finance.yahoo.com/v1/finance/screener', params=params, cookies=cookies, headers=headers, json=json_data)

    x = json.loads(response.text)
    total = int(x['finance']['result'][0]['total'])
    return total



limits = []
if total <= 9000:
    print ('Upper limit is UNDER 9000 entries')
    appended_data=[]
    up_limit = (int(total))/250
    up_limit = round(up_limit)+1
    print('upper limit = ', up_limit)

    for i in range(0,up_limit):
        
        page = i*250
        page2 = page+250
        print (f'Processing Index {page2} / {total}')
        

        json_data = {
            'size': 250,
            'offset': page,
            'sortField': 'intradaymarketcap',
            'sortType': 'DESC',
            'quoteType': 'EQUITY',
            'topOperator': 'AND',
            'query': {
                'operator': 'AND',
                'operands': [
                    {
                        'operator': 'or',
                        'operands': [
                            {
                                'operator': 'EQ',
                                'operands': [
                                    'region',
                                    country_code[0],
                                ],
                            },
                        ],
                    },
                ],
            },
            'userId': '',
            'userIdType': 'guid',
        }

        response = requests.post('https://query2.finance.yahoo.com/v1/finance/screener', params=params, cookies=cookies, headers=headers, json=json_data)

        x = json.loads(response.text)
        
        if i==0:
            total = int(x['finance']['result'][0]['total'])
        
        
        df = pd.json_normalize(x['finance']['result'][0]['quotes'])

        appended_data.append(df)
        results = pd.concat(appended_data, axis=0)
        results = results.reset_index(drop=True)
        #results.to_csv('canada_test.csv')
        
        
        
        sleep(randint(1,3))
    results.drop_duplicates()
    results.to_csv(f'canada_test.csv', index=False)
    print('Done!')    

#Sets the scanner ranges
if total > 9000:
    print ('Upper limit is OVER 9000 entries')
    #sets the very first price range
    increment = 1
    result = 0
    x = 0
    while x < 6000:
        result = round(result + increment, 1)
        sleep(1)
        x = eodprice_range(0, result)
        print(result, x)
    
    if x > 7500:
        print ('lowering')
    while x > 7500:
        result = round(result-0.1, 1)
        sleep(1)
        x = eodprice_range(0, result)
        print(result, x)
        
    remaining = x
    print('Remaining = ', (total - remaining))

    limits.append([0, result])
    print(limits)
#%%

    #Run until there's less than 6000 remaining for greater than EOD price
    print ('total = ', total, 'remaining = ', remaining)
    while remaining < (total - 6000):
        
        result = round(limits[-1][1], 1)
        x=0
        increment = 3
        prev = 0
        
        while x < 4000 or remaining < total - 6000:
            
            result = result + increment
            print ('result = ',result)

            #result = round(result, 1)
            sleep(1)
            x = eodprice_range(limits[-1][1], result)
            
            prev = x - prev
            change = x - prev
            


            if change < 1000:
                print ('Adding 10. Total change = ', prev)
                increment = increment + 10
            prev = x
            print('result =',result, 'total on page =', x )
            print('change =',change, 'remaining =', remaining)


        if x > 5000:
            print ('lowering')
        while x > 5000:
            print('increment = ',increment)
            result = round(result-1, 1)
            sleep(1)
            x = eodprice_range(limits[-1][1], result)
            print(result, x)
        remaining = remaining + x
        print('Remaining = ', (total - remaining))
        limits.append([limits[-1][1], result])
    print(limits)
    
    print('Remaining = ',(total - remaining))

#%%


#%%







## Germany great then end of day price (EOD)
import requests

cookies = {
    'B': '7b0s3s5h5qof2&b=3&s=05',
    'PRF': 't%3D2330.TW%252BSCM1R.RG%252BAMC%252BDAC.V%252BGME',
    'A1': 'd=AQABBOJhXWICEJDDoC-1ue9fht2Ig-GDg3UFEgEBBgFvaWJSYyUHb2UB_eMBAAcI4mFdYuGDg3U&S=AQAAAusHy4pL3cCa8tWvsZ7MOEc',
    'A3': 'd=AQABBOJhXWICEJDDoC-1ue9fht2Ig-GDg3UFEgEBBgFvaWJSYyUHb2UB_eMBAAcI4mFdYuGDg3U&S=AQAAAusHy4pL3cCa8tWvsZ7MOEc',
    'A1S': 'd=AQABBOJhXWICEJDDoC-1ue9fht2Ig-GDg3UFEgEBBgFvaWJSYyUHb2UB_eMBAAcI4mFdYuGDg3U&S=AQAAAusHy4pL3cCa8tWvsZ7MOEc&j=WORLD',
    'GUC': 'AQEBBgFiaW9jUkIcXAQt',
    'ucs': 'lbit=1',
    'cmp': 't=1651166765&j=0&u=1---',
}

json_data = {
    'size': 25,
    'offset': 0,
    'sortField': 'intradaymarketcap',
    'sortType': 'DESC',
    'quoteType': 'EQUITY',
    'topOperator': 'AND',
    'query': {
        'operator': 'AND',
        'operands': [
            {
                'operator': 'or',
                'operands': [
                    {
                        'operator': 'EQ',
                        'operands': [
                            'region',
                            'de',
                        ],
                    },
                ],
            },
            {
                'operator': 'gt',
                'operands': [
                    'eodprice',
                    100,
                ],
            },
        ],
    },
    'userId': '',
    'userIdType': 'guid',
}

response = requests.post('https://query1.finance.yahoo.com/v1/finance/screener', params=params, cookies=cookies, headers=headers, json=json_data)