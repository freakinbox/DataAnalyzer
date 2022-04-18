#Data and URL handling
import pandas as pd
import urllib.request, urllib.error

#pd.set_option('display.max_columns', None) #Will display entire dataframe in console if activated
#%%
####### general functions ########

tick = 'GME'
p1 = 959385600
p2 = 1650153600
int = '1d'

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

df = yfprice(tick, p1, p2, int)

#%%

