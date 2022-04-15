###### DataGathering Module


import pandas as pd
import requests

#       ***** This makes request and converts json into a Dataframe and then sends them back to the main program making the call
   

####### general functions ########

def theget(url):
    try: #TODO Add this exception handling to all other api calls, Maybe make it it's own function
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print('**AlphaAPI warning** - HTTP error')
        meta='**AlphaAPI warning**  HTTP Error'
        return meta, err
    except requests.exceptions.RequestException as err:
        print('**AlphaAPI warning** - there was a call exception')
        meta='**AlphaAPI warning**   requests exception'
        return meta, err
    else:
        meta = 'ok'
        return meta,response

def thecheck(meta,response,url):
    #Error handling
    if meta == 'ok':
        data=response.json()
        keys=list(data)
        if 'Error Message' in keys:
            #print('whoops there was an error in the api call')
            status='err'
            return keys, data, status
        elif data == {}:
            print('retrying...')
            meta, response = theget(url)
            data = response.json()
            if 'Error Message' in keys:
                print('whoops there was an error in the api call')
                status = 'err'
                return keys, data, status

            elif data == {} or data == "" or data == [] or None:
                print('data is blank')
                keys = '**AlphaAPI error**'
                err = 'Download has failed'
                status = 'err'
                return keys, err, status

            else:
                status = 'ok'
                return meta, response, status
        


        else:
            status = 'ok'
            return meta, response, status
    
    
    else:
        print('err')
        status = 'err'
        return meta, response, status

##################################



#%%
def IntradayAV(ticker, apikey, interval='5min'):
    '''
    Always Adjusted close values

    interval 1min, 5min, 15min, 30min, 60min (Default = 5min)
    '''

    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={ticker}&interval={interval}&outputsize=full&apikey={apikey}'
    meta,response = theget(url)
    meta,data,status=thecheck(meta,response,url)
    
    if status == 'ok':
        data=response.json()
        MetaData = data['Meta Data']
        #Selects the data that isn't Meta Data and seperates it on it's own
        key = list(data)
        key = key.pop(1)
        dailyChart = data[str(key)]
        meta = pd.DataFrame.from_dict(MetaData, orient='index')
        df = pd.DataFrame.from_dict(dailyChart, orient='index')
        return meta, df

    else:
        return meta, data

def IntradayExtendedAV(ticker, apikey, slice, interval='5min'):

    '''
    Always Adjusted close value

    interval 1min, 5min, 15min, 30min, 60min (Default = 5min)
    
    slice - year1month1, year1month2 -, year2month12
    '''
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={ticker}&interval={interval}&slice={slice}&outputsize=full&apikey={apikey}'
    meta,response = theget(url)
    meta,data,status=thecheck(meta,response,url)
    
    if status == 'ok':
        data=response.json()
        MetaData = data['Meta Data']
        #Selects the data that isn't Meta Data and seperates it on it's own
        key = list(data)
        key = key.pop(1)
        dailyChart = data[str(key)]
        meta = pd.DataFrame.from_dict(MetaData, orient='index')
        df = pd.DataFrame.from_dict(dailyChart, orient='index')
        return meta, df
    
    else:
        return meta, data

def DailyAdjustedAV(ticker, apikey):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={ticker}&outputsize=full&apikey={apikey}'
    meta,response = theget(url)
    meta,data,status=thecheck(meta,response,url)
    
    if status == 'ok':
        data=response.json()
        MetaData = data['Meta Data']
        #Selects the data that isn't Meta Data and seperates it on it's own
        key = list(data)
        key = key.pop(1)
        dailyChart = data[str(key)]
        meta = pd.DataFrame.from_dict(MetaData, orient='index')
        df = pd.DataFrame.from_dict(dailyChart, orient='index')
        #df.groupby("date")
        df.columns = df.columns.astype(str).str[3:]
        return meta, df

    else:
        return meta, data

def WeeklyAdjustedAV(ticker, apikey):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY_ADJUSTED&symbol={ticker}&outputsize=full&apikey={apikey}'
    meta,response = theget(url)
    meta,data,status=thecheck(meta,response,url)
    
    if status == 'ok':
        data=response.json()
        MetaData = data['Meta Data']
        #Selects the data that isn't Meta Data and seperates it on it's own
        key = list(data)
        key = key.pop(1)
        dailyChart = data[str(key)]
        meta = pd.DataFrame.from_dict(MetaData, orient='index')
        df = pd.DataFrame.from_dict(dailyChart, orient='index')
        return meta, df

    else:
        return meta, data

def MonthlyAdjustedAV(ticker, apikey):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY_ADJUSTED&symbol={ticker}&outputsize=full&apikey={apikey}'
    meta,response = theget(url)
    meta,data,status=thecheck(meta,response,url)
    
    if status == 'ok':
        data=response.json()
        MetaData = data['Meta Data']
        #Selects the data that isn't Meta Data and seperates it on it's own
        key = list(data)
        key = key.pop(1)
        dailyChart = data[str(key)]
        meta = pd.DataFrame.from_dict(MetaData, orient='index')
        df = pd.DataFrame.from_dict(dailyChart, orient='index')
        return meta, df

    else:
        meta, data



#### INDICATORS


def smaAV(ticker, apikey, interval='daily', time_period='14', series_type='close'):

    '''
    interval = 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly  (default = daily)

    time_period = Positive integers are accepted (e.g., time_period=60, time_period=200) (Default = 14)

    series_type = Four types are supported: close, open, high, low (default = close)
    '''

    url = f'https://www.alphavantage.co/query?function=SMA&symbol={ticker}&interval={interval}&time_period={time_period}&series_type={series_type}&apikey={apikey}'
    meta,response = theget(url)
    meta,data,status=thecheck(meta,response,url)
    
    if status == 'ok':
        data=response.json()
        MetaData = data['Meta Data']
        #Selects the data that isn't Meta Data and seperates it on it's own
        key = list(data)
        key = key.pop(1)
        dailyChart = data[str(key)]
        meta = pd.DataFrame.from_dict(MetaData, orient='index')
        df = pd.DataFrame.from_dict(dailyChart, orient='index')
        return meta, df
    
    else:
        return meta, data

def emaAV(ticker, apikey, interval='daily', time_period='14', series_type='close'):

    '''
    interval = 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly (default = daily)

    time_period = Positive integers are accepted (e.g., time_period=60, time_period=200) (Default = 14)

    series_type = Four types are supported: close, open, high, low (default = close)
    '''

    url = f'https://www.alphavantage.co/query?function=EMA&symbol={ticker}&interval={interval}&time_period={time_period}&series_type={series_type}&apikey={apikey}'
    meta,response = theget(url)
    meta,data,status=thecheck(meta,response,url)
    
    if status == 'ok':
        data=response.json()
        MetaData = data['Meta Data']
        #Selects the data that isn't Meta Data and seperates it on it's own
        key = list(data)
        key = key.pop(1)
        dailyChart = data[str(key)]
        meta = pd.DataFrame.from_dict(MetaData, orient='index')
        df = pd.DataFrame.from_dict(dailyChart, orient='index')
        return meta, df

    else:
        return meta, data

def wmaAV(ticker, apikey, interval='daily', time_period='14', series_type='close'):

    '''
    interval = 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly (default = daily)

    time_period = Positive integers are accepted (e.g., time_period=60, time_period=200) (default = 14)

    series_type = Four types are supported: close, open, high, low (default = close)
    '''

    url = f'https://www.alphavantage.co/query?function=WMA&symbol={ticker}&interval={interval}&time_period={time_period}&series_type={series_type}&apikey={apikey}'
    meta,response = theget(url)
    meta,data,status=thecheck(meta,response,url)
    
    if status == 'ok':
        data=response.json()
        MetaData = data['Meta Data']
        #Selects the data that isn't Meta Data and seperates it on it's own
        key = list(data)
        key = key.pop(1)
        dailyChart = data[str(key)]
        meta = pd.DataFrame.from_dict(MetaData, orient='index')
        df = pd.DataFrame.from_dict(dailyChart, orient='index')
        return meta, df

    else:
        return meta, data

def demaAV(ticker, apikey, interval='daily', time_period='14', series_type='close'):

    '''
    interval = 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly (default = daily)

    time_period = Positive integers are accepted (e.g., time_period=60, time_period=200) (default = 14)

    series_type = Four types are supported: close, open, high, low (default = close)
    '''

    url = f'https://www.alphavantage.co/query?function=DEMA&symbol={ticker}&interval={interval}&time_period={time_period}&series_type={series_type}&apikey={apikey}'
    meta,response = theget(url)
    meta,data,status=thecheck(meta,response,url)
    
    if status == 'ok':
        data=response.json()
        MetaData = data['Meta Data']
        #Selects the data that isn't Meta Data and seperates it on it's own
        key = list(data)
        key = key.pop(1)
        dailyChart = data[str(key)]
        meta = pd.DataFrame.from_dict(MetaData, orient='index')
        df = pd.DataFrame.from_dict(dailyChart, orient='index')
        return meta, df

    else:
        return meta, data

def temaAV(ticker, apikey, interval='daily', time_period='14', series_type='close'):

    '''
    interval = 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly (default = daily)

    time_period = Positive integers are accepted (e.g., time_period=60, time_period=200) (default = 14)

    series_type = Four types are supported: close, open, high, low (default = close)
    '''

    url = f'https://www.alphavantage.co/query?function=TEMA&symbol={ticker}&interval={interval}&time_period={time_period}&series_type={series_type}&apikey={apikey}'
    meta,response = theget(url)
    meta,data,status=thecheck(meta,response,url)
    
    if status == 'ok':
        data=response.json()
        MetaData = data['Meta Data']
        #Selects the data that isn't Meta Data and seperates it on it's own
        key = list(data)
        key = key.pop(1)
        dailyChart = data[str(key)]
        meta = pd.DataFrame.from_dict(MetaData, orient='index')
        df = pd.DataFrame.from_dict(dailyChart, orient='index')
        return meta, df

    else:
        return meta, data

def trimaAV(ticker, apikey, interval='daily', time_period='14', series_type='close'):

    '''
    interval = 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly (default = daily)

    time_period = Positive integers are accepted (e.g., time_period=60, time_period=200) (default = 14)

    series_type = Four types are supported: close, open, high, low (default = close)
    '''

    url = f'https://www.alphavantage.co/query?function=TRIMA&symbol={ticker}&interval={interval}&time_period={time_period}&series_type={series_type}&apikey={apikey}'
    meta,response = theget(url)
    meta,data,status=thecheck(meta,response,url)
    
    if status == 'ok':
        data=response.json()
        MetaData = data['Meta Data']
        #Selects the data that isn't Meta Data and seperates it on it's own
        key = list(data)
        key = key.pop(1)
        dailyChart = data[str(key)]
        meta = pd.DataFrame.from_dict(MetaData, orient='index')
        df = pd.DataFrame.from_dict(dailyChart, orient='index')
        return meta, df

    else:
        return meta, data

def kamaAV(ticker, apikey, interval='daily', time_period='14', series_type='close'):

    '''
    interval = 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly (Default = daily)

    time_period = Positive integers are accepted (e.g., time_period=60, time_period=200) (Default = 14)

    series_type = Four types are supported: close, open, high, low (Default = close)
    '''

    url = f'https://www.alphavantage.co/query?function=KAMA&symbol={ticker}&interval={interval}&time_period={time_period}&series_type={series_type}&apikey={apikey}'
    meta,response = theget(url)
    meta,data,status=thecheck(meta,response,url)
    
    if status == 'ok':
        data=response.json()
        MetaData = data['Meta Data']
        #Selects the data that isn't Meta Data and seperates it on it's own
        key = list(data)
        key = key.pop(1)
        dailyChart = data[str(key)]
        meta = pd.DataFrame.from_dict(MetaData, orient='index')
        df = pd.DataFrame.from_dict(dailyChart, orient='index')
        return meta, df

    else:
        return meta, data

def mamaAV(ticker, apikey, interval='daily', series_type='close', fastlimit='0.01',slowlimit='0.01'):

    '''
    interval = 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly (Default = daily)

    series_type = Four types are supported: close, open, high, low (Default = close)

    default = 'fastlimit=0.01' and 'slowlimit=0.01'
    '''

    url = f'https://www.alphavantage.co/query?function=MAMA&symbol={ticker}&interval={interval}&series_type={series_type}&fastlimit={fastlimit}&slowlimit={slowlimit}&apikey={apikey}'
    meta,response = theget(url)
    meta,data,status=thecheck(meta,response,url)
    
    if status == 'ok':
        data=response.json()
        MetaData = data['Meta Data']
        #Selects the data that isn't Meta Data and seperates it on it's own
        key = list(data)
        key = key.pop(1)
        dailyChart = data[str(key)]
        meta = pd.DataFrame.from_dict(MetaData, orient='index')
        df = pd.DataFrame.from_dict(dailyChart, orient='index')
        return meta, df
    
    else:
        return meta, data

def vwapAV(ticker, apikey, interval='5min'):

    '''
    interval = 1min, 5min, 15min, 30min, 60min (Default = 5min)
    
    '''

    url = f'https://www.alphavantage.co/query?function=VWAP&symbol={ticker}&interval={interval}&apikey={apikey}'
    meta,response = theget(url)
    meta,data,status=thecheck(meta,response,url)
    
    if status == 'ok':
        data=response.json()
        MetaData = data['Meta Data']
        #Selects the data that isn't Meta Data and seperates it on it's own
        key = list(data)
        key = key.pop(1)
        dailyChart = data[str(key)]
        meta = pd.DataFrame.from_dict(MetaData, orient='index')
        df = pd.DataFrame.from_dict(dailyChart, orient='index')
        return meta, df

    else:
        return meta, data

def t3AV(ticker, apikey, interval='daily', time_period='14', series_type='close'):

    '''
    interval = 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly (Default = daily)

    time_period = Positive integers are accepted (e.g., time_period=60, time_period=200) (Default = 14)

    series_type = Four types are supported: close, open, high, low (Default = close)
    
    '''

    url = f'https://www.alphavantage.co/query?function=T3&symbol={ticker}&interval={interval}&time_period={time_period}&series_type={series_type}&apikey={apikey}'
    meta,response = theget(url)
    meta,data,status=thecheck(meta,response,url)
    
    if status == 'ok':
        data=response.json()
        MetaData = data['Meta Data']
        #Selects the data that isn't Meta Data and seperates it on it's own
        key = list(data)
        key = key.pop(1)
        dailyChart = data[str(key)]
        meta = pd.DataFrame.from_dict(MetaData, orient='index')
        df = pd.DataFrame.from_dict(dailyChart, orient='index')
        return meta, df

    else:
        return meta, data

def macdAV(ticker, apikey, interval='daily', series_type='close', fastperiod='12', slowperiod='26',signalperiod='9'):

    '''
    interval = 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly (Default = daily)

    time_period = Positive integers are accepted (e.g., time_period=60, time_period=200) (Default = 14)

    series_type = Four types are supported: close, open, high, low (Default = close)

    fastperiod(Default = 12), slowperiod(Default = 26), and signal period(Default = 9) all accept positive integers 
    
    '''

    url = f'https://www.alphavantage.co/query?function=MACD&symbol={ticker}&interval={interval}&series_type={series_type}&fastperiod={fastperiod}&slowperiod={slowperiod}&signalperiod={signalperiod}&apikey={apikey}'
    meta,response = theget(url)
    meta,data,status=thecheck(meta,response,url)
    
    if status == 'ok':
        data=response.json()
        MetaData = data['Meta Data']
        #Selects the data that isn't Meta Data and seperates it on it's own
        key = list(data)
        key = key.pop(1)
        dailyChart = data[str(key)]
        meta = pd.DataFrame.from_dict(MetaData, orient='index')
        df = pd.DataFrame.from_dict(dailyChart, orient='index')
        return meta, df

    else:
        return meta, data

def macdextAV(ticker, apikey, interval='daily', series_type='close', fastperiod='12', slowperiod='26',signalperiod='9', fastmatype='0', slowmatype='0', signalmatype='0'):

    '''
    interval = 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly (Default = daily)

    time_period = Positive integers are accepted (e.g., time_period=60, time_period=200) (Default = 14)

    series_type = Four types are supported: close, open, high, low (Default = close)

    fastperiod (Default = 12), slowperiod (Default = 26), and signal period (Default = 9) all accept positive integers 

    fastmatype - slowmatype - signalmatype - (Default = 0)

    Integers 0 - 8 are accepted with the following mappings. 0 = Simple Moving Average (SMA), 1 = Exponential Moving Average (EMA), 2 = Weighted Moving Average (WMA), 
    3 = Double Exponential Moving Average (DEMA), 4 = Triple Exponential Moving Average (TEMA), 5 = Triangular Moving Average (TRIMA), 6 = T3 Moving Average, 
    7 = Kaufman Adaptive Moving Average (KAMA), 8 = MESA Adaptive Moving Average (MAMA). 
    '''

    url = f'https://www.alphavantage.co/query?function=MACDEXT&symbol={ticker}&interval={interval}&series_type={series_type}&fastperiod={fastperiod}&slowperiod={slowperiod}&signalperiod={signalperiod}&fastmatype={fastmatype}&slowmatype={slowmatype}&signalmatype={signalmatype}&apikey={apikey}'
    meta,response = theget(url)
    meta,data,status=thecheck(meta,response,url)
    
    if status == 'ok':
        data=response.json()
        MetaData = data['Meta Data']
        #Selects the data that isn't Meta Data and seperates it on it's own
        key = list(data)
        key = key.pop(1)
        dailyChart = data[str(key)]
        meta = pd.DataFrame.from_dict(MetaData, orient='index')
        df = pd.DataFrame.from_dict(dailyChart, orient='index')
        return meta, df

    else:
        return meta, data

def stochAV(ticker, apikey ,interval='daily', fastkperiod='5', slowkperiod='3',slowdperiod='3',slowkmatype='0', slowdmatype='0'):

    '''
    interval = 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly (Default = daily)

    fastkperiod (Default = 5), slowkperiod (Default = 3), and slowdperiod (Default = 3) all accept positive integers 

    slowkmatype - slowdmatype - (Default = 0)

    Integers 0 - 8 are accepted with the following mappings. 0 = Simple Moving Average (SMA), 1 = Exponential Moving Average (EMA), 2 = Weighted Moving Average (WMA), 
    3 = Double Exponential Moving Average (DEMA), 4 = Triple Exponential Moving Average (TEMA), 5 = Triangular Moving Average (TRIMA), 6 = T3 Moving Average, 
    7 = Kaufman Adaptive Moving Average (KAMA), 8 = MESA Adaptive Moving Average (MAMA). 
    '''

    url = f'https://www.alphavantage.co/query?function=STOCH&symbol={ticker}&interval={interval}&fastkperiod={fastkperiod}&slowkperiod={slowkperiod}&slowdperiod={slowdperiod}&slowkmatype={slowkmatype}&slowdmatype={slowdmatype}&apikey={apikey}'
    meta,response = theget(url)
    meta,data,status=thecheck(meta,response,url)
    
    if status == 'ok':
        data=response.json()
        MetaData = data['Meta Data']
        #Selects the data that isn't Meta Data and seperates it on it's own
        key = list(data)
        key = key.pop(1)
        dailyChart = data[str(key)]
        meta = pd.DataFrame.from_dict(MetaData, orient='index')
        df = pd.DataFrame.from_dict(dailyChart, orient='index')
        return meta, df

    else:
        return meta, data

def stochFAV(ticker, apikey, interval='daily', fastkperiod='5', fastdperiod='3', fastdmatype='0'):

    '''
    interval = 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly (Default = daily)

    fastkperiod (Default = 5) and fastdperiod (Default = 3) accept positive integers 

    fastdmatype - (Default = 0)
    
    Integers 0 - 8 are accepted with the following mappings. 0 = Simple Moving Average (SMA), 1 = Exponential Moving Average (EMA), 2 = Weighted Moving Average (WMA), 
    3 = Double Exponential Moving Average (DEMA), 4 = Triple Exponential Moving Average (TEMA), 5 = Triangular Moving Average (TRIMA), 6 = T3 Moving Average, 
    7 = Kaufman Adaptive Moving Average (KAMA), 8 = MESA Adaptive Moving Average (MAMA). 
    '''

    url = f'https://www.alphavantage.co/query?function=STOCHF&symbol={ticker}&interval={interval}&fastkperiod={fastkperiod}&fastdperiod={fastdperiod}&fastdmatype={fastdmatype}&apikey={apikey}'
    meta,response = theget(url)
    meta,data,status=thecheck(meta,response,url)
    
    if status == 'ok':
        data=response.json()
        MetaData = data['Meta Data']
        #Selects the data that isn't Meta Data and seperates it on it's own
        key = list(data)
        key = key.pop(1)
        dailyChart = data[str(key)]
        meta = pd.DataFrame.from_dict(MetaData, orient='index')
        df = pd.DataFrame.from_dict(dailyChart, orient='index')
        return meta, df

    else:
        return meta, data

def rsiAV(ticker, apikey, interval='daily', time_period='14', series_type='close'):

    '''
    interval = 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly (Default = daily)

    time_period = Positive integers are accepted (e.g., time_period=60, time_period=200) (Default = 14)

    series_type = Four types are supported: close, open, high, low (Default = close)
    '''

    url = f'https://www.alphavantage.co/query?function=RSI&symbol={ticker}&interval={interval}&time_period={time_period}&series_type={series_type}&apikey={apikey}'
    meta,response = theget(url)
    meta,data,status=thecheck(meta,response,url)
    
    if status == 'ok':
        data=response.json()
        MetaData = data['Meta Data']
        #Selects the data that isn't Meta Data and seperates it on it's own
        key = list(data)
        key = key.pop(1)
        dailyChart = data[str(key)]
        meta = pd.DataFrame.from_dict(MetaData, orient='index')
        df = pd.DataFrame.from_dict(dailyChart, orient='index')
        return meta, df

    else:
        return meta, data

def stochrsiAV(ticker, apikey, interval='daily', time_period='14', series_type='close', fastkperiod='5', fastdperiod='3', fastmatype='0'):

    '''
    interval = 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly (Default = daily)

    time_period = Positive integers are accepted (e.g., time_period=60, time_period=200) (Default = 14)

    series_type = Four types are supported: close, open, high, low (Default = close)

    fastperiod (Default = 5) and fastdperiod (Default = 3) accept positive integers 

    fastmatype - (Default = 0)
        
    Integers 0 - 8 are accepted with the following mappings. 0 = Simple Moving Average (SMA), 1 = Exponential Moving Average (EMA), 2 = Weighted Moving Average (WMA), 
    3 = Double Exponential Moving Average (DEMA), 4 = Triple Exponential Moving Average (TEMA), 5 = Triangular Moving Average (TRIMA), 6 = T3 Moving Average, 
    7 = Kaufman Adaptive Moving Average (KAMA), 8 = MESA Adaptive Moving Average (MAMA). 
    '''

    url = f'https://www.alphavantage.co/query?function=STOCHRSI&symbol={ticker}&interval={interval}&time_period={time_period}&series_type={series_type}&fastkperiod={fastkperiod}&fastdperiod={fastdperiod}&fastmatype={fastmatype}&apikey={apikey}'
    meta,response = theget(url)
    meta,data,status=thecheck(meta,response,url)
    
    if status == 'ok':
        data=response.json()
        MetaData = data['Meta Data']
        #Selects the data that isn't Meta Data and seperates it on it's own
        key = list(data)
        key = key.pop(1)
        dailyChart = data[str(key)]
        meta = pd.DataFrame.from_dict(MetaData, orient='index')
        df = pd.DataFrame.from_dict(dailyChart, orient='index')
        return meta, df

    return meta, data

def willrAV(ticker, apikey, interval='daily', time_period='14'):

    '''
    interval = 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly (Default = daily)

    time_period = Positive integers are accepted (e.g., time_period=60, time_period=200) (Default = 14)
    '''

    url = f'https://www.alphavantage.co/query?function=WILLR&symbol={ticker}&interval={interval}&time_period={time_period}&apikey={apikey}'
    meta,response = theget(url)
    meta,data,status=thecheck(meta,response,url)
    
    if status == 'ok':
        data=response.json()
        MetaData = data['Meta Data']
        #Selects the data that isn't Meta Data and seperates it on it's own
        key = list(data)
        key = key.pop(1)
        dailyChart = data[str(key)]
        meta = pd.DataFrame.from_dict(MetaData, orient='index')
        df = pd.DataFrame.from_dict(dailyChart, orient='index')
        return meta, df

    else:
        return meta, data

def adxAV(ticker, apikey, interval='daily', time_period='14'):

    '''
    interval = 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly (Default = daily)

    time_period = Positive integers are accepted (e.g., time_period=60, time_period=200) (Default = 14)    
    '''

    url = f'https://www.alphavantage.co/query?function=ADX&symbol={ticker}&interval={interval}&time_period={time_period}&apikey={apikey}'
    meta,response = theget(url)
    meta,data,status=thecheck(meta,response,url)
    
    if status == 'ok':
        data=response.json()
        MetaData = data['Meta Data']
        #Selects the data that isn't Meta Data and seperates it on it's own
        key = list(data)
        key = key.pop(1)
        dailyChart = data[str(key)]
        meta = pd.DataFrame.from_dict(MetaData, orient='index')
        df = pd.DataFrame.from_dict(dailyChart, orient='index')
        return meta, df

    else:
        return meta, data

def adxrAV(ticker, apikey, interval='daily', time_period='14'):

    '''
    interval = 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly (Default = daily)

    time_period = Positive integers are accepted (e.g., time_period=60, time_period=200) (Default = 14)
    '''

    url = f'https://www.alphavantage.co/query?function=ADXR&symbol={ticker}&interval={interval}&time_period={time_period}&apikey={apikey}'
    meta,response = theget(url)
    meta,data,status=thecheck(meta,response,url)
    
    if status == 'ok':
        data=response.json()
        MetaData = data['Meta Data']
        #Selects the data that isn't Meta Data and seperates it on it's own
        key = list(data)
        key = key.pop(1)
        dailyChart = data[str(key)]
        meta = pd.DataFrame.from_dict(MetaData, orient='index')
        df = pd.DataFrame.from_dict(dailyChart, orient='index')
        return meta, df

    else:
        return meta, data

def apoAV(ticker, apikey, interval='daily', series_type='close', fastperiod='12', slowperiod='26', matype='0'):

    '''
    interval = 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly (Default = daily)

    series_type = Four types are supported: close, open, high, low (Default = close)

    fastperiod (Default = 12) and slowperiod (Default = 26) accept positive integers 

    matype - (Default = 0)
        
    Integers 0 - 8 are accepted with the following mappings. 0 = Simple Moving Average (SMA), 1 = Exponential Moving Average (EMA), 2 = Weighted Moving Average (WMA), 
    3 = Double Exponential Moving Average (DEMA), 4 = Triple Exponential Moving Average (TEMA), 5 = Triangular Moving Average (TRIMA), 6 = T3 Moving Average, 
    7 = Kaufman Adaptive Moving Average (KAMA), 8 = MESA Adaptive Moving Average (MAMA). 
    '''

    url = f'https://www.alphavantage.co/query?function=APO&symbol={ticker}&interval={interval}&series_type={series_type}&fastperiod={fastperiod}&slowperiod={slowperiod}&matype={matype}&apikey={apikey}'
    meta,response = theget(url)
    meta,data,status=thecheck(meta,response,url)
    
    if status == 'ok':
        data=response.json()
        MetaData = data['Meta Data']
        #Selects the data that isn't Meta Data and seperates it on it's own
        key = list(data)
        key = key.pop(1)
        dailyChart = data[str(key)]
        meta = pd.DataFrame.from_dict(MetaData, orient='index')
        df = pd.DataFrame.from_dict(dailyChart, orient='index')
        return meta, df

    else:
        return meta, data

def ppoAV(ticker, apikey, interval='daily', series_type='close', fastperiod='12', slowperiod='26', matype='0'):

    '''
    interval = 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly (Default = daily)

    series_type = Four types are supported: close, open, high, low (Default = close)

    fastperiod (Default = 12) and slowperiod (Default = 26) accept positive integers 

    matype - (Default = 0)
        
    Integers 0 - 8 are accepted with the following mappings. 0 = Simple Moving Average (SMA), 1 = Exponential Moving Average (EMA), 2 = Weighted Moving Average (WMA), 
    3 = Double Exponential Moving Average (DEMA), 4 = Triple Exponential Moving Average (TEMA), 5 = Triangular Moving Average (TRIMA), 6 = T3 Moving Average, 
    7 = Kaufman Adaptive Moving Average (KAMA), 8 = MESA Adaptive Moving Average (MAMA). 
    '''

    url = f'https://www.alphavantage.co/query?function=PPO&symbol={ticker}&interval={interval}&series_type={series_type}&fastperiod={fastperiod}&slowperiod={slowperiod}&matype={matype}&apikey={apikey}'
    meta,response = theget(url)
    meta,data,status=thecheck(meta,response,url)
    
    if status == 'ok':
        data=response.json()
        MetaData = data['Meta Data']
        #Selects the data that isn't Meta Data and seperates it on it's own
        key = list(data)
        key = key.pop(1)
        dailyChart = data[str(key)]
        meta = pd.DataFrame.from_dict(MetaData, orient='index')
        df = pd.DataFrame.from_dict(dailyChart, orient='index')
        return meta, df

    else:
        return meta, data

def momAV(ticker, apikey, interval='daily', time_period='14', series_type='close'):

    '''
    interval = 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly (Default = daily)

    time_period = Positive integers are accepted (e.g., time_period=60, time_period=200) (Default = 14)

    series_type = Four types are supported: close, open, high, low (Default = close)
    '''

    url = f'https://www.alphavantage.co/query?function=MOM&symbol={ticker}&interval={interval}&time_period={time_period}&series_type={series_type}&apikey={apikey}'
    meta,response = theget(url)
    meta,data,status=thecheck(meta,response,url)
    
    if status == 'ok':
        data=response.json()
        MetaData = data['Meta Data']
        #Selects the data that isn't Meta Data and seperates it on it's own
        key = list(data)
        key = key.pop(1)
        dailyChart = data[str(key)]
        meta = pd.DataFrame.from_dict(MetaData, orient='index')
        df = pd.DataFrame.from_dict(dailyChart, orient='index')
        return meta, df

    else:
        return meta, data

def bopAV(ticker, apikey, interval='daily'):

    '''
    interval = 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly (Default = daily)
    '''

    url = f'https://www.alphavantage.co/query?function=BOP&symbol={ticker}&interval={interval}&apikey={apikey}'
    meta,response = theget(url)
    meta,data,status=thecheck(meta,response,url)
    
    if status == 'ok':
        data=response.json()
        MetaData = data['Meta Data']
        #Selects the data that isn't Meta Data and seperates it on it's own
        key = list(data)
        key = key.pop(1)
        dailyChart = data[str(key)]
        meta = pd.DataFrame.from_dict(MetaData, orient='index')
        df = pd.DataFrame.from_dict(dailyChart, orient='index')
        return meta, df

    else:
        return meta, data

def cciAV(ticker, apikey, interval='daily', time_period='14'):

    '''
    interval = 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly (Default = daily)

    time_period = Positive integers are accepted (e.g., time_period=60, time_period=200) (Default = 14)
    '''

    url = f'https://www.alphavantage.co/query?function=CCI&symbol={ticker}&interval={interval}&time_period={time_period}&apikey={apikey}'
    meta,response = theget(url)
    meta,data,status=thecheck(meta,response,url)
    
    if status == 'ok':
        data=response.json()
        MetaData = data['Meta Data']
        #Selects the data that isn't Meta Data and seperates it on it's own
        key = list(data)
        key = key.pop(1)
        dailyChart = data[str(key)]
        meta = pd.DataFrame.from_dict(MetaData, orient='index')
        df = pd.DataFrame.from_dict(dailyChart, orient='index')
        return meta, df

    else:
        return meta, data

def cmoAV(ticker, apikey, interval='daily', time_period='14', series_type='close'):

    '''
    interval = 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly (Default = daily)

    time_period = Positive integers are accepted (e.g., time_period=60, time_period=200) (Default = 14)

    series_type = Four types are supported: close, open, high, low (Default = close)
    '''

    url = f'https://www.alphavantage.co/query?function=CMO&symbol={ticker}&interval={interval}&time_period={time_period}&series_type={series_type}&apikey={apikey}'
    meta,response = theget(url)
    meta,data,status=thecheck(meta,response,url)
    
    if status == 'ok':
        data=response.json()
        MetaData = data['Meta Data']
        #Selects the data that isn't Meta Data and seperates it on it's own
        key = list(data)
        key = key.pop(1)
        dailyChart = data[str(key)]
        meta = pd.DataFrame.from_dict(MetaData, orient='index')
        df = pd.DataFrame.from_dict(dailyChart, orient='index')
        return meta, df

    else:
        return meta, data

def rocAV(ticker, apikey, interval='daily', time_period='14', series_type='close'):

    '''
    interval = 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly (Default = daily)

    time_period = Positive integers are accepted (e.g., time_period=60, time_period=200) (Default = 14)

    series_type = Four types are supported: close, open, high, low (Default = close)
    '''

    url = f'https://www.alphavantage.co/query?function=ROC&symbol={ticker}&interval={interval}&time_period={time_period}&series_type={series_type}&apikey={apikey}'
    meta,response = theget(url)
    meta,data,status=thecheck(meta,response,url)
    
    if status == 'ok':
        data=response.json()
        MetaData = data['Meta Data']
        #Selects the data that isn't Meta Data and seperates it on it's own
        key = list(data)
        key = key.pop(1)
        dailyChart = data[str(key)]
        meta = pd.DataFrame.from_dict(MetaData, orient='index')
        df = pd.DataFrame.from_dict(dailyChart, orient='index')
        return meta, df

    else:
        return meta, data

def rocrAV(ticker, apikey, interval='daily', time_period='14', series_type='close'):

    '''
    interval = 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly (Default = daily)

    time_period = Positive integers are accepted (e.g., time_period=60, time_period=200) (Default = 14)

    series_type = Four types are supported: close, open, high, low (Default = close)
    '''

    url = f'https://www.alphavantage.co/query?function=ROCR&symbol={ticker}&interval={interval}&time_period={time_period}&series_type={series_type}&apikey={apikey}'
    meta,response = theget(url)
    meta,data,status=thecheck(meta,response,url)
    
    if status == 'ok':
        data=response.json()
        MetaData = data['Meta Data']
        #Selects the data that isn't Meta Data and seperates it on it's own
        key = list(data)
        key = key.pop(1)
        dailyChart = data[str(key)]
        meta = pd.DataFrame.from_dict(MetaData, orient='index')
        df = pd.DataFrame.from_dict(dailyChart, orient='index')
        return meta, df

    else:
        return meta, data

def aroonAV(ticker, apikey, interval='daily', time_period='14'):

    '''
    interval = 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly (Default = daily)

    time_period = Positive integers are accepted (e.g., time_period=60, time_period=200) (Default = 14)
    '''

    url = f'https://www.alphavantage.co/query?function=AROON&symbol={ticker}&interval={interval}&time_period={time_period}&apikey={apikey}'
    meta,response = theget(url)
    meta,data,status=thecheck(meta,response,url)
    
    if status == 'ok':
        data=response.json()
        MetaData = data['Meta Data']
        #Selects the data that isn't Meta Data and seperates it on it's own
        key = list(data)
        key = key.pop(1)
        dailyChart = data[str(key)]
        meta = pd.DataFrame.from_dict(MetaData, orient='index')
        df = pd.DataFrame.from_dict(dailyChart, orient='index')
        return meta, df

    else:
        return meta, data

def aroonoscAV(ticker, apikey, interval='daily', time_period='14'):

    '''
    interval = 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly (Default = daily)

    time_period = Positive integers are accepted (e.g., time_period=60, time_period=200) (Default = 14)
    '''

    url = f'https://www.alphavantage.co/query?function=AROONOSC&symbol={ticker}&interval={interval}&time_period={time_period}&apikey={apikey}'
    meta,response = theget(url)
    meta,data,status=thecheck(meta,response,url)
    
    if status == 'ok':
        data=response.json()
        MetaData = data['Meta Data']
        #Selects the data that isn't Meta Data and seperates it on it's own
        key = list(data)
        key = key.pop(1)
        dailyChart = data[str(key)]
        meta = pd.DataFrame.from_dict(MetaData, orient='index')
        df = pd.DataFrame.from_dict(dailyChart, orient='index')
        return meta, df

    else:
        return meta, data

def mfiAV(ticker, apikey, interval='daily', time_period='14'):

    '''
    interval = 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly (Default = daily)

    time_period = Positive integers are accepted (e.g., time_period=60, time_period=200) (Default = 14)
    '''

    url = f'https://www.alphavantage.co/query?function=MFI&symbol={ticker}&interval={interval}&time_period={time_period}&apikey={apikey}'
    meta,response = theget(url)
    meta,data,status=thecheck(meta,response,url)
    
    if status == 'ok':
        data=response.json()
        MetaData = data['Meta Data']
        #Selects the data that isn't Meta Data and seperates it on it's own
        key = list(data)
        key = key.pop(1)
        dailyChart = data[str(key)]
        meta = pd.DataFrame.from_dict(MetaData, orient='index')
        df = pd.DataFrame.from_dict(dailyChart, orient='index')
        return meta, df

    else:
        return meta, data

def trixAV(ticker, apikey, interval='daily', time_period='14', series_type='close'):

    '''
    interval = 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly (Default = daily)

    time_period = Positive integers are accepted (e.g., time_period=60, time_period=200) (Default = 14)

    series_type = Four types are supported: close, open, high, low (Default = close)
    '''
    
    url = f'https://www.alphavantage.co/query?function=TRIX&symbol={ticker}&interval={interval}&time_period={time_period}&series_type={series_type}&apikey={apikey}'
    meta,response = theget(url)
    meta,data,status=thecheck(meta,response,url)
    
    if status == 'ok':
        data=response.json()
        MetaData = data['Meta Data']
        #Selects the data that isn't Meta Data and seperates it on it's own
        key = list(data)
        key = key.pop(1)
        dailyChart = data[str(key)]
        meta = pd.DataFrame.from_dict(MetaData, orient='index')
        df = pd.DataFrame.from_dict(dailyChart, orient='index')
        return meta, df

    else:
        return meta, data

def ultoscAV(ticker, apikey, interval='daily', timeperiod1='7', timeperiod2='14', timeperiod3='28'):

    '''
    interval = 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly (Default = daily)

    timeperiod1 = Positive integers are accepted (e.g., time_period=60, time_period=200) (Default = 7)

    timeperiod2 = Positive integers are accepted (e.g., time_period=60, time_period=200) (Default = 14)

    timeperiod3 = Positive integers are accepted (e.g., time_period=60, time_period=200) (Default = 28)
    '''

    url = f'https://www.alphavantage.co/query?function=ULTOSC&symbol={ticker}&interval={interval}&timeperiod1={timeperiod1}&timeperiod2={timeperiod2}&timeperiod3={timeperiod3}&apikey={apikey}'
    meta,response = theget(url)
    meta,data,status=thecheck(meta,response,url)
    
    if status == 'ok':
        data=response.json()
        MetaData = data['Meta Data']
        #Selects the data that isn't Meta Data and seperates it on it's own
        key = list(data)
        key = key.pop(1)
        dailyChart = data[str(key)]
        meta = pd.DataFrame.from_dict(MetaData, orient='index')
        df = pd.DataFrame.from_dict(dailyChart, orient='index')
        return meta, df

    else:
        return meta, data

def dxAV(ticker, apikey, interval='daily', time_period='14'):

    '''
    interval = 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly (Default = daily)

    time_period = Positive integers are accepted (e.g., time_period=60, time_period=200) (Default = 14)
    '''

    url = f'https://www.alphavantage.co/query?function=DX&symbol={ticker}&interval={interval}&time_period={time_period}&apikey={apikey}'
    meta,response = theget(url)
    meta,data,status=thecheck(meta,response,url)
    
    if status == 'ok':
        data=response.json()
        MetaData = data['Meta Data']
        #Selects the data that isn't Meta Data and seperates it on it's own
        key = list(data)
        key = key.pop(1)
        dailyChart = data[str(key)]
        meta = pd.DataFrame.from_dict(MetaData, orient='index')
        df = pd.DataFrame.from_dict(dailyChart, orient='index')
        return meta, df

    else:
        return meta, data

def minus_diAV(ticker, apikey, interval='daily', time_period='14'):

    '''
    interval = 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly (Default = daily)

    time_period = Positive integers are accepted (e.g., time_period=60, time_period=200) (Default = 14)
    '''

    url = f'https://www.alphavantage.co/query?function=MINUS_DI&symbol={ticker}&interval={interval}&time_period={time_period}&apikey={apikey}'
    meta,response = theget(url)
    meta,data,status=thecheck(meta,response,url)
    
    if status == 'ok':
        data=response.json()
        MetaData = data['Meta Data']
        #Selects the data that isn't Meta Data and seperates it on it's own
        key = list(data)
        key = key.pop(1)
        dailyChart = data[str(key)]
        meta = pd.DataFrame.from_dict(MetaData, orient='index')
        df = pd.DataFrame.from_dict(dailyChart, orient='index')
        return meta, df

    else:
        return meta, data

def plus_diAV(ticker, apikey, interval='daily', time_period='14'):

    '''
    interval = 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly (Default = daily)

    time_period = Positive integers are accepted (e.g., time_period=60, time_period=200) (Default = 14)
    '''

    url = f'https://www.alphavantage.co/query?function=PLUS_DI&symbol={ticker}&interval={interval}&time_period={time_period}&apikey={apikey}'
    meta,response = theget(url)
    meta,data,status=thecheck(meta,response,url)
    
    if status == 'ok':
        data=response.json()
        MetaData = data['Meta Data']
        #Selects the data that isn't Meta Data and seperates it on it's own
        key = list(data)
        key = key.pop(1)
        dailyChart = data[str(key)]
        meta = pd.DataFrame.from_dict(MetaData, orient='index')
        df = pd.DataFrame.from_dict(dailyChart, orient='index')
        return meta, df

    else:
        return meta, data

def minus_dmAV(ticker, apikey, interval='daily', time_period='14'):

    '''
    interval = 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly (Default = daily)

    time_period = Positive integers are accepted (e.g., time_period=60, time_period=200) (Default = 14)
    '''

    url = f'https://www.alphavantage.co/query?function=MINUS_DM&symbol={ticker}&interval={interval}&time_period={time_period}&apikey={apikey}'
    meta,response = theget(url)
    meta,data,status=thecheck(meta,response,url)
    
    if status == 'ok':
        data=response.json()
        MetaData = data['Meta Data']
        #Selects the data that isn't Meta Data and seperates it on it's own
        key = list(data)
        key = key.pop(1)
        dailyChart = data[str(key)]
        meta = pd.DataFrame.from_dict(MetaData, orient='index')
        df = pd.DataFrame.from_dict(dailyChart, orient='index')
        return meta, df

    else:
        return meta, data

def plus_dmAV(ticker, apikey, interval='daily', time_period='14'):

    '''
    interval = 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly (Default = daily)

    time_period = Positive integers are accepted (e.g., time_period=60, time_period=200) (Default = 14)
    '''

    url = f'https://www.alphavantage.co/query?function=PLUS_DM&symbol={ticker}&interval={interval}&time_period={time_period}&apikey={apikey}'
    meta,response = theget(url)
    meta,data,status=thecheck(meta,response,url)
    
    if status == 'ok':
        data=response.json()
        MetaData = data['Meta Data']
        #Selects the data that isn't Meta Data and seperates it on it's own
        key = list(data)
        key = key.pop(1)
        dailyChart = data[str(key)]
        meta = pd.DataFrame.from_dict(MetaData, orient='index')
        df = pd.DataFrame.from_dict(dailyChart, orient='index')
        return meta, df

    else:
        return meta, data

def bbandsAV(ticker, apikey, interval='daily', time_period='14', series_type='close', nbdevup='2', nbdevdn='2', matype='0'):

    '''
    interval = 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly (Default = daily)

    time_period = Positive integers are accepted (e.g., time_period=60, time_period=200) (Default = 14)

    series_type = Four types are supported: close, open, high, low (Default = close)

    nbdevup - The standard deviation multiplier of the upper band. Positive integers are accepted. (Default = 2)

    nbdevdn - The standard deviation multiplier of the lower band. Positive integers are accepted. By default, (Default = 2)

    matype - (Default = 0)
        
    Integers 0 - 8 are accepted with the following mappings. 0 = Simple Moving Average (SMA), 1 = Exponential Moving Average (EMA), 2 = Weighted Moving Average (WMA), 
    3 = Double Exponential Moving Average (DEMA), 4 = Triple Exponential Moving Average (TEMA), 5 = Triangular Moving Average (TRIMA), 6 = T3 Moving Average, 
    7 = Kaufman Adaptive Moving Average (KAMA), 8 = MESA Adaptive Moving Average (MAMA).  
    '''

    url = f'https://www.alphavantage.co/query?function=BBANDS&symbol={ticker}&interval={interval}&time_period={time_period}&series_type={series_type}&nbdevup={nbdevup}&nbdevdn={nbdevdn}&matype={matype}&apikey={apikey}'
    meta,response = theget(url)
    meta,data,status=thecheck(meta,response,url)
    
    if status == 'ok':
        data=response.json()
        MetaData = data['Meta Data']
        #Selects the data that isn't Meta Data and seperates it on it's own
        key = list(data)
        key = key.pop(1)
        dailyChart = data[str(key)]
        meta = pd.DataFrame.from_dict(MetaData, orient='index')
        df = pd.DataFrame.from_dict(dailyChart, orient='index')
        return meta, df

    else:
        return meta, data

def midpointAV(ticker, apikey, interval='daily', time_period='14', series_type='close'):

    '''
    interval = 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly (Default = daily)

    time_period = Positive integers are accepted (e.g., time_period=60, time_period=200) (Default = 14)

    series_type = Four types are supported: close, open, high, low (Default = close)
    '''

    url = f'https://www.alphavantage.co/query?function=MIDPOINT&symbol={ticker}&interval={interval}&time_period={time_period}&series_type={series_type}&apikey={apikey}'
    meta,response = theget(url)
    meta,data,status=thecheck(meta,response,url)
    
    if status == 'ok':
        data=response.json()
        MetaData = data['Meta Data']
        #Selects the data that isn't Meta Data and seperates it on it's own
        key = list(data)
        key = key.pop(1)
        dailyChart = data[str(key)]
        meta = pd.DataFrame.from_dict(MetaData, orient='index')
        df = pd.DataFrame.from_dict(dailyChart, orient='index')
        return meta, df

    else:
        return meta, data

def midpriceAV(ticker, apikey, interval='daily', time_period='14'):

    '''
    interval = 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly (Default = daily)

    time_period = Positive integers are accepted (e.g., time_period=60, time_period=200) (Default = daily)
    '''

    url = f'https://www.alphavantage.co/query?function=MIDPRICE&symbol={ticker}&interval={interval}&time_period={time_period}&apikey={apikey}'
    meta,response = theget(url)
    meta,data,status=thecheck(meta,response,url)
    
    if status == 'ok':
        data=response.json()
        MetaData = data['Meta Data']
        #Selects the data that isn't Meta Data and seperates it on it's own
        key = list(data)
        key = key.pop(1)
        dailyChart = data[str(key)]
        meta = pd.DataFrame.from_dict(MetaData, orient='index')
        df = pd.DataFrame.from_dict(dailyChart, orient='index')
        return meta, df

    else:
        return meta, data

def sarAV(ticker, apikey, interval='daily', acceleration='0.01', maximum='0.20'):

    '''
    interval = 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly (Default = daily)

    accleration - The acceleration factor. Positive floats are accepted (Default = 0.01)

    maximum - The acceleration factor maximum value. Positive floats are accepted (Default = 0.20)
    '''

    url = f'https://www.alphavantage.co/query?function=SAR&symbol={ticker}&interval={interval}&acceleration={acceleration}&maximum={maximum}&apikey={apikey}'
    meta,response = theget(url)
    meta,data,status=thecheck(meta,response,url)
    
    if status == 'ok':
        data=response.json()
        MetaData = data['Meta Data']
        #Selects the data that isn't Meta Data and seperates it on it's own
        key = list(data)
        key = key.pop(1)
        dailyChart = data[str(key)]
        meta = pd.DataFrame.from_dict(MetaData, orient='index')
        df = pd.DataFrame.from_dict(dailyChart, orient='index')
        return meta, df

    else:
        return meta, data

def trangeAV(ticker, apikey, interval='daily'):

    '''
    interval = 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly (Default = daily)
    '''

    url = f'https://www.alphavantage.co/query?function=TRANGE&symbol={ticker}&interval={interval}&apikey={apikey}'
    meta,response = theget(url)
    meta,data,status=thecheck(meta,response,url)
    
    if status == 'ok':
        data=response.json()
        MetaData = data['Meta Data']
        #Selects the data that isn't Meta Data and seperates it on it's own
        key = list(data)
        key = key.pop(1)
        dailyChart = data[str(key)]
        meta = pd.DataFrame.from_dict(MetaData, orient='index')
        df = pd.DataFrame.from_dict(dailyChart, orient='index')
        return meta, df

    else:
        return meta, data

def atrAV(ticker, apikey, interval='daily', time_period='14'):

    '''
    interval = 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly (Default = daily)

    time_period = Positive integers are accepted (e.g., time_period=60, time_period=200) (Default = 14)
    
    '''
    url = f'https://www.alphavantage.co/query?function=ATR&symbol={ticker}&interval={interval}&time_period={time_period}&apikey={apikey}'
    meta,response = theget(url)
    meta,data,status=thecheck(meta,response,url)
    
    if status == 'ok':
        data=response.json()
        MetaData = data['Meta Data']
        #Selects the data that isn't Meta Data and seperates it on it's own
        key = list(data)
        key = key.pop(1)
        dailyChart = data[str(key)]
        meta = pd.DataFrame.from_dict(MetaData, orient='index')
        df = pd.DataFrame.from_dict(dailyChart, orient='index')
        return meta, df

    else:
        return meta, data

def natrAV(ticker, apikey, interval='daily', time_period='14'):

    '''
    interval = 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly (Default = daily)

    time_period = Positive integers are accepted (e.g., time_period=60, time_period=200) (Default = 14)
    '''

    url = f'https://www.alphavantage.co/query?function=NATR&symbol={ticker}&interval={interval}&time_period={time_period}&apikey={apikey}'
    meta,response = theget(url)
    meta,data,status=thecheck(meta,response,url)
    
    if status == 'ok':
        data=response.json()
        MetaData = data['Meta Data']
        #Selects the data that isn't Meta Data and seperates it on it's own
        key = list(data)
        key = key.pop(1)
        dailyChart = data[str(key)]
        meta = pd.DataFrame.from_dict(MetaData, orient='index')
        df = pd.DataFrame.from_dict(dailyChart, orient='index')
        return meta, df

    else:
        return meta, data

def adAV(ticker, apikey, interval='daily'):

    '''
    interval = 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly (Default = daily)

    time_period = Positive integers are accepted (e.g., time_period=60, time_period=200) (Default = 14)

    '''
    url = f'https://www.alphavantage.co/query?function=AD&symbol={ticker}&interval={interval}&apikey={apikey}'
    meta,response = theget(url)
    meta,data,status=thecheck(meta,response,url)
    
    if status == 'ok':
        data=response.json()
        MetaData = data['Meta Data']
        #Selects the data that isn't Meta Data and seperates it on it's own
        key = list(data)
        key = key.pop(1)
        dailyChart = data[str(key)]
        meta = pd.DataFrame.from_dict(MetaData, orient='index')
        df = pd.DataFrame.from_dict(dailyChart, orient='index')
        return meta, df

    else:
        return meta, data

def adoscAV(ticker, apikey, interval='daily', fastperiod='3', slowperiod='10'):

    '''
    interval = 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly (Default = daily)

    fastperiod (Default = 3) and slowperiod (Default = 10) accept positive integers 
    '''

    url = f'https://www.alphavantage.co/query?function=ADOSC&symbol={ticker}&interval={interval}&fastperiod={fastperiod}&slowperiod={slowperiod}&apikey={apikey}'
    meta,response = theget(url)
    meta,data,status=thecheck(meta,response,url)
    
    if status == 'ok':
        data=response.json()
        MetaData = data['Meta Data']
        #Selects the data that isn't Meta Data and seperates it on it's own
        key = list(data)
        key = key.pop(1)
        dailyChart = data[str(key)]
        meta = pd.DataFrame.from_dict(MetaData, orient='index')
        df = pd.DataFrame.from_dict(dailyChart, orient='index')
        return meta, df

    else:
        return meta, data

def obvAV(ticker, apikey, interval='daily'):

    '''
    interval = 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly (Default = daily)
    '''

    url = f'https://www.alphavantage.co/query?function=OBV&symbol={ticker}&interval={interval}&apikey={apikey}'
    meta,response = theget(url)
    meta,data,status=thecheck(meta,response,url)
    
    if status == 'ok':
        data=response.json()
        MetaData = data['Meta Data']
        #Selects the data that isn't Meta Data and seperates it on it's own
        key = list(data)
        key = key.pop(1)
        dailyChart = data[str(key)]
        meta = pd.DataFrame.from_dict(MetaData, orient='index')
        df = pd.DataFrame.from_dict(dailyChart, orient='index')
        return meta, df

    else:
        return meta, data

def ht_trendlineAV(ticker, apikey, interval='daily', series_type='close'):

    '''
    interval = 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly (Default = daily)

    series_type = Four types are supported: close, open, high, low (Default = daily)
    '''

    url = f'https://www.alphavantage.co/query?function=HT_TRENDLINE&symbol={ticker}&interval={interval}&series_type={series_type}&apikey={apikey}'
    meta,response = theget(url)
    meta,data,status=thecheck(meta,response,url)
    
    if status == 'ok':
        data=response.json()
        MetaData = data['Meta Data']
        #Selects the data that isn't Meta Data and seperates it on it's own
        key = list(data)
        key = key.pop(1)
        dailyChart = data[str(key)]
        meta = pd.DataFrame.from_dict(MetaData, orient='index')
        df = pd.DataFrame.from_dict(dailyChart, orient='index')
        return meta, df

    else:
        return meta, data

def ht_sineAV(ticker, apikey, interval='daily', series_type='close'):

    '''
    interval = 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly (Default = daily)

    series_type = Four types are supported: close, open, high, low (Default = daily)
    '''

    url = f'https://www.alphavantage.co/query?function=HT_SINE&symbol={ticker}&interval={interval}&series_type={series_type}&apikey={apikey}'
    meta,response = theget(url)
    meta,data,status=thecheck(meta,response,url)
    
    if status == 'ok':
        data=response.json()
        MetaData = data['Meta Data']
        #Selects the data that isn't Meta Data and seperates it on it's own
        key = list(data)
        key = key.pop(1)
        dailyChart = data[str(key)]
        meta = pd.DataFrame.from_dict(MetaData, orient='index')
        df = pd.DataFrame.from_dict(dailyChart, orient='index')
        return meta, df

    else:
        return meta, data

def ht_trendmodeAV(ticker, apikey, interval='daily', series_type='close'):

    '''
    interval = 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly (Default = daily)

    series_type = Four types are supported: close, open, high, low (Default = close)
    '''

    url = f'https://www.alphavantage.co/query?function=HT_TRENDMODE&symbol={ticker}&interval={interval}&series_type={series_type}&apikey={apikey}'
    meta,response = theget(url)
    meta,data,status=thecheck(meta,response,url)
    
    if status == 'ok':
        data=response.json()
        MetaData = data['Meta Data']
        #Selects the data that isn't Meta Data and seperates it on it's own
        key = list(data)
        key = key.pop(1)
        dailyChart = data[str(key)]
        meta = pd.DataFrame.from_dict(MetaData, orient='index')
        df = pd.DataFrame.from_dict(dailyChart, orient='index')
        return meta, df

    else:
        return meta, data

def ht_dcperiodAV(ticker, apikey, interval='daily', series_type='close'):

    '''
    interval = 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly (Default = daily)

    series_type = Four types are supported: close, open, high, low (Default = daily)
    '''

    url = f'https://www.alphavantage.co/query?function=HT_DCPERIOD&symbol={ticker}&interval={interval}&series_type={series_type}&apikey={apikey}'
    meta,response = theget(url)
    meta,data,status=thecheck(meta,response,url)
    
    if status == 'ok':
        data=response.json()
        MetaData = data['Meta Data']
        #Selects the data that isn't Meta Data and seperates it on it's own
        key = list(data)
        key = key.pop(1)
        dailyChart = data[str(key)]
        meta = pd.DataFrame.from_dict(MetaData, orient='index')
        df = pd.DataFrame.from_dict(dailyChart, orient='index')
        return meta, df

    else:
        return meta, data

def ht_dcphaseAV(ticker, apikey, interval='daily', series_type='close'):

    '''
    interval = 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly (Default = daily)

    series_type = Four types are supported: close, open, high, low (Default = daily)
    '''

    url = f'https://www.alphavantage.co/query?function=HT_DCPHASE&symbol={ticker}&interval={interval}&series_type={series_type}&apikey={apikey}'
    meta,response = theget(url)
    meta,data,status=thecheck(meta,response,url)
    
    if status == 'ok':
        data=response.json()
        MetaData = data['Meta Data']
        #Selects the data that isn't Meta Data and seperates it on it's own
        key = list(data)
        key = key.pop(1)
        dailyChart = data[str(key)]
        meta = pd.DataFrame.from_dict(MetaData, orient='index')
        df = pd.DataFrame.from_dict(dailyChart, orient='index')
        return meta, df
    
    else:
        return meta, data

def ht_phasorAV(ticker, apikey, interval='daily', series_type='close'):

    '''
    interval = 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly (Default = daily)

    series_type = Four types are supported: close, open, high, low (Default = daily)
    '''

    url = f'https://www.alphavantage.co/query?function=HT_PHASOR&symbol={ticker}&interval={interval}&series_type={series_type}&apikey={apikey}'
    meta,response = theget(url)
    meta,data,status=thecheck(meta,response,url)
    
    if status == 'ok':
        data=response.json()
        MetaData = data['Meta Data']
        #Selects the data that isn't Meta Data and seperates it on it's own
        key = list(data)
        key = key.pop(1)
        dailyChart = data[str(key)]
        meta = pd.DataFrame.from_dict(MetaData, orient='index')
        df = pd.DataFrame.from_dict(dailyChart, orient='index')
        return meta, df

    else:
        return meta, data


##### ----- CYRPTO and FOREX##################################
'''


xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx















xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

'''


##### ----- CYRPTO and FOREX##################################

def currency_exchange_rateAV(from_currency, to_currency, apikey):
    '''
    '''
    url=f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={from_currency}&to_currency={to_currency}&apikey={apikey}'
    meta,response = theget(url)
    meta,data,status=thecheck(meta,response,url)
    
    if status == 'ok':
        data=response.json()
        Exchange=data
        df=pd.DataFrame.from_dict(Exchange, orient='index')
        meta=''
        return meta,df
    else:
        return meta,data

    

def fx_intradayAV(from_symbol,to_symbol, apikey, interval='5min'):

    '''
    interval = 1min, 5min, 15min, 30min, 60min (Default = 5min)
    
    '''
    url = f'https://www.alphavantage.co/query?function=FX_INTRADAY&from_symbol={from_symbol}&to_symbol={to_symbol}&interval={interval}&outputsize=full&apikey={apikey}'
    meta,response = theget(url)
    meta,data,status=thecheck(meta,response,url)
    
    if status == 'ok':
        data=response.json()
        MetaData = data['Meta Data']
        #Selects the data that isn't Meta Data and seperates it on it's own
        key = list(data)
        key = key.pop(1)
        dailyChart = data[str(key)]
        meta = pd.DataFrame.from_dict(MetaData, orient='index')
        df = pd.DataFrame.from_dict(dailyChart, orient='index')
        return meta, df
    else:
        return meta, data

def fx_dailyAV(from_symbol,to_symbol, apikey):

    '''
    '''
    url = f'https://www.alphavantage.co/query?function=FX_DAILY&from_symbol={from_symbol}&to_symbol={to_symbol}&outputsize=full&apikey={apikey}'
    meta,response = theget(url)
    meta,data,status=thecheck(meta,response,url)
    
    if status == 'ok':
        data=response.json()
        MetaData = data['Meta Data']
        #Selects the data that isn't Meta Data and seperates it on it's own
        key = list(data)
        key = key.pop(1)
        dailyChart = data[str(key)]
        meta = pd.DataFrame.from_dict(MetaData, orient='index')
        df = pd.DataFrame.from_dict(dailyChart, orient='index')
        return meta, df
    
    else:
        return meta, data

def fx_weeklyAV(from_symbol,to_symbol, apikey):

    '''
    '''
    url = f'https://www.alphavantage.co/query?function=FX_WEEKLY&from_symbol={from_symbol}&to_symbol={to_symbol}&outputsize=full&apikey={apikey}'
    meta,response = theget(url)
    meta,data,status=thecheck(meta,response,url)
    
    if status == 'ok':
        data=response.json()
        MetaData = data['Meta Data']
        #Selects the data that isn't Meta Data and seperates it on it's own
        key = list(data)
        key = key.pop(1)
        dailyChart = data[str(key)]
        meta = pd.DataFrame.from_dict(MetaData, orient='index')
        df = pd.DataFrame.from_dict(dailyChart, orient='index')
        return meta, df
    
    else:
        return meta, data

def fx_monthlyAV(from_symbol,to_symbol, apikey):

    '''
    '''
    url = f'https://www.alphavantage.co/query?function=FX_MONTHLY&from_symbol={from_symbol}&to_symbol={to_symbol}&apikey={apikey}'
    meta,response = theget(url)
    meta,data,status=thecheck(meta,response,url)
    
    if status == 'ok':
        data=response.json()
        MetaData = data['Meta Data']
        #Selects the data that isn't Meta Data and seperates it on it's own
        key = list(data)
        key = key.pop(1)
        dailyChart = data[str(key)]
        meta = pd.DataFrame.from_dict(MetaData, orient='index')
        df = pd.DataFrame.from_dict(dailyChart, orient='index')
        return meta, df

    else:
        return meta, data

'''
import os
ProgramDirectory = os.path.dirname(os.path.abspath(__file__))
FilesDirectory = (ProgramDirectory+"\\bin")
ticker = "BTC"
if 'apikey.txt' in os.listdir(FilesDirectory):
        with open(FilesDirectory+'\\apikey.txt', 'r') as file:
            apikey = file.read().replace('\n', '')
            file.close
            if apikey == "":
                print('no api key')         
            else:
                apikey= apikey
                print('API key read successful')
meta, df = crypto_ratingAV(ticker, apikey)
#%%
'''

def crypto_intradayAV(symbol, market, apikey, interval='5min'):

    '''
    market eg = USD, CAD (currency)

    interval = 1min, 5min, 15min, 30min, 60min (Default = 5min)
    '''
    url = f'https://www.alphavantage.co/query?function=CRYPTO_INTRADAY&symbol={symbol}&market={market}&interval={interval}&outputsize=full&apikey={apikey}'
    meta,response = theget(url)
    meta,data,status=thecheck(meta,response,url)
    
    if status == 'ok':
        data=response.json()
        MetaData = data['Meta Data']
        #Selects the data that isn't Meta Data and seperates it on it's own
        key = list(data)
        key = key.pop(1)
        dailyChart = data[str(key)]
        meta = pd.DataFrame.from_dict(MetaData, orient='index')
        df = pd.DataFrame.from_dict(dailyChart, orient='index')
        return meta, df
    else:
        return meta, data

def digital_currency_dailyAV(symbol, market, apikey):

    '''
    '''
    url = f'https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol={symbol}&market={market}&apikey={apikey}'
    meta,response = theget(url)
    meta,data,status=thecheck(meta,response,url)
    
    if status == 'ok':
        data=response.json()
        MetaData = data['Meta Data']
        #Selects the data that isn't Meta Data and seperates it on it's own
        key = list(data)
        key = key.pop(1)
        dailyChart = data[str(key)]
        meta = pd.DataFrame.from_dict(MetaData, orient='index')
        df = pd.DataFrame.from_dict(dailyChart, orient='index')
        return meta, df

    else:
        return meta,data

def digital_currency_weeklyAV(symbol, market, apikey):

    '''
    '''
    url = f'https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_WEEKLY&symbol={symbol}&market={market}&apikey={apikey}'
    meta,response = theget(url)
    meta,data,status=thecheck(meta,response,url)
    
    if status == 'ok':
        data=response.json()
        MetaData = data['Meta Data']
        #Selects the data that isn't Meta Data and seperates it on it's own
        key = list(data)
        key = key.pop(1)
        dailyChart = data[str(key)]
        meta = pd.DataFrame.from_dict(MetaData, orient='index')
        df = pd.DataFrame.from_dict(dailyChart, orient='index')
        return meta, df
    else:
        return meta, data

def digital_currency_monthlyAV(symbol, market, apikey):

    '''
    '''
    url = f'https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_MONTHLY&symbol={symbol}&market={market}&apikey={apikey}'
    meta,response = theget(url)
    meta,data,status=thecheck(meta,response,url)
    
    if status == 'ok':
        data=response.json()
        MetaData = data['Meta Data']
        #Selects the data that isn't Meta Data and seperates it on it's own
        key = list(data)
        key = key.pop(1)
        dailyChart = data[str(key)]
        meta = pd.DataFrame.from_dict(MetaData, orient='index')
        df = pd.DataFrame.from_dict(dailyChart, orient='index')
        return meta, df
    
    else:
        return meta, data



##### ----- Fundamentals ##################################
'''


xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx















xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


'''
##### ----- Fundamentals ##################################  left out Listing&delisting status, Earnings and IPO calendar  #TODO


def overviewAV(symbol, apikey):
    #TODO update so it has two outputs but will also need to change
    # avcaller1NEW as well
    '''
    No meta, just df
    '''
    url = f'https://www.alphavantage.co/query?function=OVERVIEW&symbol={symbol}&apikey={apikey}'
    meta,response = theget(url)
    meta,data,status=thecheck(meta,response,url)
    
    if status == 'ok':
        data=response.json()
        df = pd.DataFrame.from_dict(data)
        return meta, df

    else:
        return meta, data

def earningsAV(symbol, apikey):
    '''
    gives you annual and quartly earnings in that order
    '''
    url = f'https://www.alphavantage.co/query?function=EARNINGS&symbol={symbol}&apikey={apikey}'
    meta,response = theget(url)
    meta,data,status=thecheck(meta,response,url)
    
    if status == 'ok':
        ae1 = data['annualEarnings']
        #Selects the data that isn't Meta Data and seperates it on it's own
        qe1 = data['quarterlyEarnings']
        ae = pd.DataFrame.from_dict(ae1)
        qe = pd.DataFrame.from_dict(qe1)
        return ae, qe
    
    else:
        return meta, data

def income_statementAV(symbol, apikey):
    '''
    gives you annual and quartly earnings in that order
    '''
    url = f'https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol={symbol}&apikey={apikey}'
    meta,response = theget(url)
    meta,data,status=thecheck(meta,response,url)
    
    if status == 'ok':
        data=response.json()
        ar1 = data['annualReports']
        #Selects the data that isn't Meta Data and seperates it on it's own
        qr1 = data['quarterlyReports']
        ar = pd.DataFrame.from_dict(ar1)
        qr = pd.DataFrame.from_dict(qr1)
        return ar, qr
    
    else:
        return meta, data

def balance_sheetAV(symbol, apikey):
    '''
    gives you annual and quartly earnings in that order
    '''
    url = f'https://www.alphavantage.co/query?function=BALANCE_SHEET&symbol={symbol}&apikey={apikey}'
    meta,response = theget(url)
    meta,data,status=thecheck(meta,response,url)
    
    if status == 'ok':
        data=response.json()
        ar1 = data['annualReports']
        #Selects the data that isn't Meta Data and seperates it on it's own
        qr1 = data['quarterlyReports']
        ar = pd.DataFrame.from_dict(ar1)
        qr = pd.DataFrame.from_dict(qr1)
        return ar, qr

    else:
        return meta, data

def cash_flowAV(symbol, apikey):
    '''
    gives you annual and quartly earnings in that order
    '''
    url = f'https://www.alphavantage.co/query?function=CASH_FLOW&symbol={symbol}&apikey={apikey}'
    meta,response = theget(url)
    meta,data,status=thecheck(meta,response,url)
    
    if status == 'ok':
        data=response.json()
        ar1 = data['annualReports']
        #Selects the data that isn't Meta Data and seperates it on it's own
        qr1 = data['quarterlyReports']
        ar = pd.DataFrame.from_dict(ar1)
        qr = pd.DataFrame.from_dict(qr1)
        return ar, qr

    else:
        return meta, data

##### ----- Economic Indicators ##################################
'''


xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx















xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


'''
##### ----- Economic Indicators ##################################




def real_gdpAV(apikey, interval='annual'):

    '''
    --United States--
    By default, interval=annual. Strings quarterly and annual are accepted.
    '''
    url = f'https://www.alphavantage.co/query?function=REAL_GDP&interval={interval}&apikey={apikey}'
    meta,response = theget(url)
    meta,data,status=thecheck(meta,response,url)
    
    if status == 'ok':
        data=response.json()
        data1 = data['data']
        del data['data']
        meta1 = data
        #Selects the data that isn't Meta Data and seperates it on it's own
        
        meta = pd.DataFrame.from_dict(meta1, orient='index')
        data = pd.DataFrame.from_dict(data1)
        return meta, data

    else:
        return meta, data

def real_gdp_per_capitaAV(apikey):

    '''
    --United States--
    By default, interval=annual. Strings quarterly and annual are accepted.
    '''
    url = f'https://www.alphavantage.co/query?function=REAL_GDP_PER_CAPITA&apikey={apikey}'
    meta,response = theget(url)
    meta,data,status=thecheck(meta,response,url)
    
    if status == 'ok':
        data=response.json()
        data1 = data['data']
        del data['data']
        meta1 = data
        
        meta = pd.DataFrame.from_dict(meta1, orient='index')
        data = pd.DataFrame.from_dict(data1)
        return meta, data

    else:
        return meta, data

def treasury_yieldAV(apikey, interval='annual', maturity='10year'):

    '''
    --United States--
    By default, interval=annual. Strings quarterly and annual are accepted.

    By default, maturity=10year. Strings 3month, 5year, 10year, and 30year are accepted.
    '''
    url = f'https://www.alphavantage.co/query?function=TREASURY_YIELD&interval={interval}&maturity={maturity}&apikey={apikey}'
    meta,response = theget(url)
    meta,data,status=thecheck(meta,response,url)
    
    if status == 'ok':
        data=response.json()
        data1 = data['data']
        del data['data']
        meta1 = data
        
        meta = pd.DataFrame.from_dict(meta1, orient='index')
        data = pd.DataFrame.from_dict(data1)
        return meta, data

    else:
        return meta, data

def federal_funds_rateAV(apikey, interval='monthly'):

    '''
    --United States-- INTEREST RATE
    By default, interval=monthly. Strings daily, weekly, and monthly are accepted.
    '''
    url = f'https://www.alphavantage.co/query?function=FEDERAL_FUNDS_RATE&interval={interval}&apikey={apikey}'
    meta,response = theget(url)
    meta,data,status=thecheck(meta,response,url)
    
    if status == 'ok':
        data=response.json()
        data1 = data['data']
        del data['data']
        meta1 = data
        
        meta = pd.DataFrame.from_dict(meta1, orient='index')
        data = pd.DataFrame.from_dict(data1)
        return meta, data

    else:
        return meta, data

def cpiAV(apikey, interval='monthly'):

    '''
    --United States--
    By default, interval=monthly. Strings monthly and semiannual are accepted.
    '''
    url = f'https://www.alphavantage.co/query?function=CPI&interval={interval}&apikey={apikey}'
    meta,response = theget(url)
    meta,data,status=thecheck(meta,response,url)
    
    if status == 'ok':
        data=response.json()
        data1 = data['data']
        del data['data']
        meta1 = data
        
        meta = pd.DataFrame.from_dict(meta1, orient='index')
        data = pd.DataFrame.from_dict(data1)
        return meta, data

    else:
        return meta, data

def inflationAV(apikey):

    '''
    --United States--
    By default, interval=monthly. Strings monthly and semiannual are accepted.
    '''
    url = f'https://www.alphavantage.co/query?function=INFLATION&apikey={apikey}'
    meta,response = theget(url)
    meta,data,status=thecheck(meta,response,url)
    
    if status == 'ok':
        data=response.json()
        data1 = data['data']
        del data['data']
        meta1 = data
        
        meta = pd.DataFrame.from_dict(meta1, orient='index')
        data = pd.DataFrame.from_dict(data1)
        return meta, data

    else:
        return meta, data

def inflation_expectationAV(apikey):

    '''
    '''
    url = f'https://www.alphavantage.co/query?function=INFLATION_EXPECTATION&apikey={apikey}'
    meta,response = theget(url)
    meta,data,status=thecheck(meta,response,url)
    
    if status == 'ok':
        data=response.json()
        data1 = data['data']
        del data['data']
        meta1 = data
        
        meta = pd.DataFrame.from_dict(meta1, orient='index')
        data = pd.DataFrame.from_dict(data1)
        return meta, data

    else:
        return meta, data

def consumer_sentimentAV(apikey):

    '''
    '''
    url = f'https://www.alphavantage.co/query?function=CONSUMER_SENTIMENT&apikey={apikey}'
    meta,response = theget(url)
    meta,data,status=thecheck(meta,response,url)
    
    if status == 'ok':
        data=response.json()
        data1 = data['data']
        del data['data'] #Removes data and leaves you with Meta Data
        meta1 = data
        
        meta = pd.DataFrame.from_dict(meta1, orient='index')
        data = pd.DataFrame.from_dict(data1)
        return meta, data

    else:
        return meta, data

def retail_salesAV(apikey):

    '''
    '''
    url = f'https://www.alphavantage.co/query?function=RETAIL_SALES&apikey={apikey}'
    meta,response = theget(url)
    meta,data,status=thecheck(meta,response,url)
    
    if status == 'ok':
        data=response.json()
        data1 = data['data']
        del data['data'] #Removes data and leaves you with Meta Data
        meta1 = data
        
        meta = pd.DataFrame.from_dict(meta1, orient='index')
        data = pd.DataFrame.from_dict(data1)
        return meta, data

    else:
        return meta, data

def durablesAV(apikey):

    '''
    '''
    url = f'https://www.alphavantage.co/query?function=DURABLES&apikey={apikey}'
    meta,response = theget(url)
    meta,data,status=thecheck(meta,response,url)
    
    if status == 'ok':
        data=response.json()
        data1 = data['data']
        del data['data'] #Removes data and leaves you with Meta Data
        meta1 = data
        
        meta = pd.DataFrame.from_dict(meta1, orient='index')
        data = pd.DataFrame.from_dict(data1)
        return meta, data

    else:
        return meta, data

def unemploymentAV(apikey):

    '''
    '''
    url = f'https://www.alphavantage.co/query?function=UNEMPLOYMENT&apikey={apikey}'
    meta,response = theget(url)
    meta,data,status=thecheck(meta,response,url)
    
    if status == 'ok':
        data=response.json()
        data1 = data['data']
        del data['data'] #Removes data and leaves you with Meta Data
        meta1 = data
        
        meta = pd.DataFrame.from_dict(meta1, orient='index')
        data = pd.DataFrame.from_dict(data1)
        return meta, data
    
    else:
        return meta, data

def nonfarm_payrollAV(apikey):

    '''
    '''
    url = f'https://www.alphavantage.co/query?function=NONFARM_PAYROLL&apikey={apikey}'
    meta,response = theget(url)
    meta,data,status=thecheck(meta,response,url)
    
    if status == 'ok':
        data=response.json()
        data1 = data['data']
        del data['data'] #Removes data and leaves you with Meta Data
        meta1 = data
        
        meta = pd.DataFrame.from_dict(meta1, orient='index')
        data = pd.DataFrame.from_dict(data1)
        return meta, data

    else:
        return meta, data






'''
#TODO TESTING CODE
import os
ProgramDirectory = os.path.dirname(os.path.abspath(__file__))
FilesDirectory = (ProgramDirectory+"\\bin")
ticker = "DAC.V"
if 'apikey.txt' in os.listdir(FilesDirectory):
        with open(FilesDirectory+'\\apikey.txt', 'r') as file:
            apikey = file.read().replace('\n', '')
            file.close
            if apikey == "":
                print('no api key')         
            else:
                apikey= apikey
                print('API key read successful')

#meta, df = overviewAV(ticker, apikey)
meta, df = fx_intradayAV("CAD","JPY", apikey)
#%%
'''