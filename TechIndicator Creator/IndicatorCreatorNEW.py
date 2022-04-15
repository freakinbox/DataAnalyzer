#DataBaseFiles TIMESERIES
#%%

#System and time
import os
import sys
import time
from datetime import datetime
import numpy as np

#Data handling
import json
import pandas as pd
import pandas_ta as ta
from pandas_ta import volume


#%%

ProgramDirectory = os.path.dirname(os.path.abspath(__file__)) #Activte for testing and hash out for exe
#ProgramDirectory = os.getcwd()
# FilesDirectory = (ProgramDirectory+"\\bin")
# os.makedirs(FilesDirectory, exist_ok=True)

# MainDataDir = (ProgramDirectory+"\\data")
# os.makedirs(MainDataDir, exist_ok=True)

# StocksDirectory = (MainDataDir+"\\stocks")
# os.makedirs(StocksDirectory, exist_ok=True)

# CryptoDirectory = (MainDataDir+"\\Crypto")
# os.makedirs(CryptoDirectory, exist_ok=True)

# FundamentalsDirectory = (MainDataDir+"\\Fundamentals") #TODO Started adding
# os.makedirs(FundamentalsDirectory, exist_ok=True)

# ForexDirectory = (MainDataDir+"\\Forex")
# os.makedirs(ForexDirectory, exist_ok=True)


#Goes to program directory
os.chdir(ProgramDirectory)

#Reads the pickles dataframe
df = pd.read_pickle('.//GME//dailyadjusted.pkl')

# df = df.astype({'open': float})
# df = df.astype({'low': float})
# df = df.astype({'high': float})
# df = df.astype({'close': float})
# df = df.astype({'adjusted close': float})
# df = df.astype({'volume': float})
# df = df.astype({'dividend amount': float})
# df = df.astype({'split coefficient': float})

df = df.astype(float)
#df = df.convert_objects(convert_numeric=True)


#df.ta.strategy(timed=True)
#%%

def sma(df):

    df = df.sort_index()
    df = df.astype({'close': float})
    df['sma'] = df.rolling(window=14)['close'].mean()

    df = df.sort_index(ascending=False)
    df = df.drop(df.columns.difference(['sma']), axis=1)

    return df


def ema(df):
    df = df.sort_index()
    df['ema'] = df['close'].ewm(span=14, adjust=False).mean()
    
    df = df.sort_index(ascending=False)
    df = df.drop(df.columns.difference(['ema']), axis=1)
    
    return df


#MacD will need variables added in as by default it runs on constants not directly based on
#Time 

def macd(df):
    df = df.sort_index()
    df = df.astype({'close': float})

    df['ema12'] = df['close'].ewm(span=12, adjust=False).mean()
    df['ema26'] = df['close'].ewm(span=26, adjust=False).mean()
    
    df['macd'] = df['ema12'] - df['ema26']
    df['macd9'] = df['macd'].ewm(span=9, adjust=False).mean()

    df['signalline'] = df['macd'].ewm(span=9, adjust=False).mean()
    df['macd_histo'] = df['macd'] - df['signalline']
    
    df = df.sort_index(ascending=False)
    df = df[['macd_histo','signalline','macd']]
    df = df.drop(df.columns.difference(['macd_histo', 'signalline', 'macd']), axis=1)
    
    return df


def stoch(df):
    df = df.sort_index()
    df = df.astype({'close': float})

    df['max'] = df.rolling(window=5, min_periods=0)['high'].max()
    df['min'] = df.rolling(window=5, min_periods=0)['low'].min()


    df['fast%K'] = ((df['close']-df['min'])/(df['max']-df['min']))*100
    df['slow%K'] = df.rolling(window=3,min_periods=0)['fast%K'].mean()
    df['slow%D'] = df.rolling(window=3,min_periods=0)['slow%K'].mean()

    df = df.sort_index(ascending=False)
    df = df[['fast%K','slow%D','slow%K']] #TODO choose method
    df = df.drop(df.columns.difference(['fast%K','slow%D','slow%K']), axis=1)

    return df


def rsi(df):
    df = df.sort_index()
    df = df.astype({'close': float})

    df['prevclose'] = df['close'].shift(1)
    df['up'] = np.where(df['close']>df['prevclose'], df['close']-df['prevclose'], 0)
    df['dn'] = np.where(df['prevclose']>df['close'], df['prevclose']-df['close'], 0)


    df['avup'] = df['up'].ewm(alpha=1/14, adjust=False).mean() #14 is the period to change
    df['avdn'] = df['dn'].ewm(alpha=1/14, adjust=False).mean()

    df['rs'] = df['avup']/df['avdn']

    df['rsi'] = 100-100/(1+df['rs'])

    df = df.sort_index(ascending=False)
    df = df.drop(df.columns.difference(['up','dn','avup','avdn','upper','dnper','rs',
    'rsi', 'nup', 'ndn']), axis=1)
    return df



def adx(df): #TODO works but should seperate to be able to chart out each of the various other idicators inside of this
    df = df.sort_index()
    df = df.astype({'low': float})
    df = df.astype({'high': float})
    df = df.astype({'close': float})

    #ATR should be good
    df['h-l'] = df['high'] - df['low']
    df['h-pc'] = np.abs(df['high'] - df['close'].shift(1))
    df['l-pc'] = np.abs(df['low'] - df['close'].shift(1))
    
    #ATR works properly 
    df['tr'] = df[['h-l','h-pc','l-pc']].max(axis=1)
    df['atr'] = df['tr'].ewm(alpha=1/14, adjust=False).mean()
    del df['h-l'], df['h-pc'], df['l-pc']

    
    df['1dm'] = df['high'] - df['high'].shift(1)
    df['2dm'] = df['low'].shift(1) - df['low']
    df['+dx'] = np.where((df['1dm'] > df['2dm']) & (df['1dm']>0), df['1dm'],0)
    df['-dx'] = np.where((df['1dm'] < df['2dm']) & (df['2dm']>0), df['2dm'],0)
    del df['1dm'], df['2dm']

    df['S+DM'] = df['+dx'].ewm(alpha=1/14, adjust=False).mean()
    df['S-DM'] = df['-dx'].ewm(alpha=1/14, adjust=False).mean()
    df['+dm'] = (df['S+DM']/df['atr'])*100
    df['-dm'] = (df['S-DM']/df['atr'])*100
    del df['S+DM'], df['S-DM']
    

    #df['adx'] = df['dmi'].ewm(span=14, adjust=False).mean()
    
    df['dx'] = (np.abs(df['+dm'] - df['-dm'])/(df['+dm'] + df['-dm']))*100
    df['adx'] = df['dx'].ewm(alpha=1/14, adjust=False).mean()

    df = df.sort_index(ascending=False)
    df = df.drop(df.columns.difference(['tr','atr','+dx','-dx','adx','+dm','-dm',]), axis=1)

    return df


def cci(df): #TODO works but doesn't match Alpha Vantage, It does match tradingview though. I think it's because I'm using the standard of 20 periods and might have used 14 when downloading from alphavantage
    df = df.sort_index()
    df = df.astype({'low': float})
    df = df.astype({'high': float})
    df = df.astype({'close': float})

    df['tp'] = (df['high'] + df['low'] + df['close'])/3
    df['tpsma20'] = df['tp'].rolling(window=20).mean()

    tosum = (np.abs(df['tp'] - df['tpsma20']), np.abs(df['tp'].shift(2) - df['tpsma20']), np.abs(df['tp'].shift(3) - df['tpsma20']), np.abs(df['tp'].shift(4) - df['tpsma20']), np.abs(df['tp'].shift(5) - df['tpsma20']), np.abs(df['tp'].shift(6) - df['tpsma20']), np.abs(df['tp'].shift(7) - df['tpsma20']), np.abs(df['tp'].shift(8) - df['tpsma20']), np.abs(df['tp'].shift(9) - df['tpsma20']), np.abs(df['tp'].shift(10) - df['tpsma20']), np.abs(df['tp'].shift(11) - df['tpsma20']), np.abs(df['tp'].shift(12) - df['tpsma20']), np.abs(df['tp'].shift(13) - df['tpsma20']), np.abs(df['tp'].shift(14) - df['tpsma20']), np.abs(df['tp'].shift(15) - df['tpsma20']), np.abs(df['tp'].shift(16) - df['tpsma20']), np.abs(df['tp'].shift(17) - df['tpsma20']), np.abs(df['tp'].shift(18) - df['tpsma20']), np.abs(df['tp'].shift(19) - df['tpsma20']), np.abs(df['tp'].shift(20) - df['tpsma20']))
    df['md'] = sum(np.abs(tosum))/20

    df['cci'] = (df['tp'] - df['tpsma20']) / (0.015 * df['md'])

    df = df.sort_index(ascending=False)
    df = df.drop(df.columns.difference(['tp','tpsma20','md','cci','adx','+dm','-dm',]), axis=1)

    return df


def aroon(df):
    df = df.sort_index()
    df = df.astype({'high': float})
    df = df.astype({'low': float})

    df['up'] = 100 * df['high'].rolling(14 + 1).apply(lambda x: x.argmax()) / 14
    df['dn'] = 100 * df['low'].rolling(14 + 1).apply(lambda x: x.argmin()) / 14

    df = df.sort_index(ascending=False)
    df = df.drop(df.columns.difference(['up','dn']), axis=1)

    return df


def bbands(df): #It's close but not exact but not sure that matters TODO
    df = df.sort_index()
    df = df.astype({'high': float})
    df = df.astype({'low': float})
    df = df.astype({'close': float})

    df['sd'] = df['close'].rolling(20).std()
    df['mid'] = df['close'].rolling(20).mean()
        
    df['upper'] = df['mid'] + (df['sd'] * 2)
    df['lower'] = df['mid'] - (df['sd'] * 2)

    df = df.sort_index(ascending=False)
    df = df.drop(df.columns.difference(['upper','lower']), axis=1)

    return df

def ad(df): #matches tradingview
    df = df.sort_index()
    df = df.astype({'high': float})
    df = df.astype({'low': float})
    df = df.astype({'close': float})
    df = df.astype({'volume': float})

    #using pandas_ta instead
    df['ad'] = ta.ad(df['high'], df['low'], df['close'], df['volume'])

    df['ad'] = df['ad'].round(1)


    df['ad3'] = (df['ad'].ewm(span=3, adjust=False).mean()).round(1)
    df['ad10'] = (df['ad'].ewm(span=10, adjust=False).mean()).round(1)

    df['cad'] = df['ad3'] - df['ad10']

    df = df.sort_index(ascending=False)

    #my code works but is very slow in comparison
    # df['mfm'] = ((df['close'] - df['low']) - (df['high'] - df['close']))/(df['high']-df['low'])
    # df['mfm'] = df['mfm'].round(4)

    # df['mfv'] = df['mfm'] * df['volume']
    # df['mfv'] = df['mfv'].round(3)

    # df['ad'] = np.nan
    # df.iloc[0, df.columns.get_loc('ad')] = df.iloc[0, df.columns.get_loc('mfv')]

    # df.reset_index(inplace= True)

    # for i in range(1, len(df)): #VERY slow
    #     df.loc[i, 'ad'] = (df.loc[i - 1, 'ad'] + df.loc[i, 'mfv']).round(1)
    
    # df['ad3'] = (df['ad'].ewm(span=3, adjust=False).mean()).round(1)
    # df['ad10'] = (df['ad'].ewm(span=10, adjust=False).mean()).round(1)

    # df['cad'] = df['ad3'] - df['ad10']

    # df.set_index('index', drop=True, inplace=True)
    # df.index.name = None

    df = df.sort_index(ascending=False)
    df = df.drop(df.columns.difference(['ad','cad']), axis=1)

    return df


def obv(df): #matches tradingview
    df = df.sort_index()
    df = df.astype({'close': float})
    df = df.astype({'volume': float})
    
    df['obv'] = ta.obv(df['close'], df['volume'])
    df['obv'] = df['obv'].astype(int)


    #My code works but is slow with a loop
    # pd.set_option('display.float_format', lambda x: '%.3f' % x)

    # df.reset_index(inplace= True)

    # df['obv'] = np.nan
    # df.iloc[0, df.columns.get_loc('obv')] = 0

    # for i in range(1, len(df)): #VERY slow


    #     if df.loc[i - 1, 'close'] < df.loc[i, 'close']:
    #         df.loc[i, 'obv'] = df.loc[i - 1, 'obv'] + df.loc[i, 'volume']

    #     if df.loc[i - 1, 'close'] > df.loc[i, 'close']:
    #         df.loc[i, 'obv'] = df.loc[i - 1, 'obv'] - df.loc[i, 'volume']

    #     if df.loc[i - 1, 'close'] == df.loc[i, 'close']:
    #         df.loc[i, 'obv'] = df.loc[i - 1, 'obv']
    
    # df['obv'] = df['obv'].round(2)
    
    # df.set_index('index', drop=True, inplace=True)
    # df.index.name = None

    df = df.sort_index(ascending=False)
    df = df.drop(df.columns.difference(['obv']), axis=1)
    
    return df









##################################################################

def wma(df):
    weights = np.arange(1,11)
    df = df.sort_index()
    df['wma'] = df['close'].rolling(10).apply(lambda prices: np.dot(prices, weights)/weights.sum(), raw=True)
    
    df = df.sort_index(ascending=False)
    df2 = df.drop(df.columns.difference(['wma']), axis=1)

    return df2




def dema(df):
    df = df.sort_index()
    df['ema'] = df['close'].ewm(span=14, adjust=False).mean()
    df['dema'] = 2*df['ema'] - df['ema'].ewm(span=14, adjust=False).mean()
    
    df = df.sort_index(ascending=False)
    df = df.drop(df.columns.difference(['dema']), axis=1)

    return df



def tema(df): #Not exact to Alpha Vantage numbers and will need to check
    df = df.sort_index()
    df['ema'] = df['close'].ewm(span=14, min_periods=14, adjust=False).mean()
    df['ema2'] = df['ema'].ewm(span=14, min_periods=14, adjust=False).mean()
    df['ema3'] = df['ema2'].ewm(span=14, min_periods=14, adjust=False).mean()

    df['tema'] = (3*df['ema']) - (3*df['ema2'])+df['ema3'].ewm(span=14, adjust=False).mean()

    df = df.sort_index(ascending=False)
    df = df.drop(df.columns.difference(['tema']), axis=1)

    return df

def trima(df):
    df = df.sort_index()
    df['trima'] = ta.trima(df['close'])

    df = df.drop(df.columns.difference(['trima']), axis=1)
    df = df.sort_index(ascending=False)

    return df


def kama(df):
    df = df.sort_index()
    df['kama'] = ta.kama(df['close'])

    df = df.drop(df.columns.difference(['kama']), axis=1)
    df = df.sort_index(ascending=False)

    return df

def t3(df):
    df = df.sort_index()
    df['t3'] = ta.t3(df['close'])

    df = df.drop(df.columns.difference(['t3']), axis=1)
    df = df.sort_index(ascending=False)

    return df


def willr(df):
    df = df.sort_index()
    df = df.astype({'high': float})
    df = df.astype({'low': float})
    df = df.astype({'close': float})

    df['willr'] = ta.willr(df.high, df.low, df.close)

    df = df.drop(df.columns.difference(['willr']), axis=1)
    df = df.sort_index(ascending=False)

    return df

def apo(df):
    df = df.sort_index()
    df = df.astype({'close': float})

    df['apo'] = ta.apo(df.close)

    df = df.drop(df.columns.difference(['apo']), axis=1)
    df = df.sort_index(ascending=False)

    return df

def mom(df):
    df = df.sort_index()
    df = df.astype({'close': float})

    df['mom'] = ta.mom(df.close)

    df = df.drop(df.columns.difference(['mom']), axis=1)
    df = df.sort_index(ascending=False)

    return df

def bop(df):
    df = df.sort_index()
    df = df.astype({'open': float})
    df = df.astype({'high': float})
    df = df.astype({'low': float})
    df = df.astype({'close': float})

    df['bop'] = ta.bop(df.open, df.high, df.low, df.close)
    df['bop'] =df['bop'].round(4)
    df = df.drop(df.columns.difference(['bop']), axis=1)
    df = df.sort_index(ascending=False)

    return df

def cmo(df):
    df = df.sort_index()
    df = df.astype({'close': float})

    df['cmo'] = ta.cmo(df.close)
    df = df.drop(df.columns.difference(['cmo']), axis=1)
    df = df.sort_index(ascending=False)

    return df

def roc(df):
    df = df.sort_index()
    df = df.astype({'close': float})

    df['roc'] = ta.roc(df.close)
    df = df.drop(df.columns.difference(['roc']), axis=1)
    df = df.sort_index(ascending=False)

    return df

def mfi(df):
    df = df.sort_index()
    df = df.astype({'high': float})
    df = df.astype({'low': float})
    df = df.astype({'close': float})
    df = df.astype({'volume': float})

    df['mfi'] = ta.mfi(df.high, df.low, df.close, df.volume)
    df = df.drop(df.columns.difference(['mfi']), axis=1)
    df = df.sort_index(ascending=False)

    return df

def trix(df):
    df = df.sort_index()
    df = df.astype({'high': float})
    df = df.astype({'low': float})
    df = df.astype({'close': float})
    df = df.astype({'volume': float})

    df['trix'] = ta.trix(df.close)
    df = df.drop(df.columns.difference(['trix']), axis=1)
    df = df.sort_index(ascending=False)

    return df


def midpoint(df):
    df = df.sort_index()
    df = df.astype({'close': float})

    df['midpoint'] = ta.midpoint(df.close)
    df = df.drop(df.columns.difference(['midpoint']), axis=1)
    df = df.sort_index(ascending=False)

    return df


def midprice(df):
    df = df.sort_index()
    df = df.astype({'high': float})
    df = df.astype({'low': float})
    df = df.astype({'close': float})

    df['midprice'] = ta.midprice(df.high, df.low)
    df = df.drop(df.columns.difference(['midprice']), axis=1)
    df = df.sort_index(ascending=False)

    return df


def atr(df):
    df = df.sort_index()
    df = df.astype({'high': float})
    df = df.astype({'low': float})
    df = df.astype({'close': float})

    df['atr'] = ta.atr(df.high, df.low, df.close)
    df = df.drop(df.columns.difference(['atr']), axis=1)
    df = df.sort_index(ascending=False)

    return df

def natr(df):
    df = df.sort_index()
    df = df.astype({'high': float})
    df = df.astype({'low': float})
    df = df.astype({'close': float})

    df['natr'] = ta.natr(df.high, df.low, df.close)
    df = df.drop(df.columns.difference(['natr']), axis=1)
    df = df.sort_index(ascending=False)

    return df

def adosc(df):
    df = df.sort_index()
    df = df.astype({'high': float})
    df = df.astype({'low': float})
    df = df.astype({'close': float})
    df = df.astype({'volume': float})

    df['adosc'] = ta.adosc(df.high, df.low, df.close, df.volume)
    df['adosc'] =df['adosc'].round(3)
    df = df.drop(df.columns.difference(['adosc']), axis=1)
    df = df.sort_index(ascending=False)

    return df

def dailytoweekly(df):
    agg_dict = {'open': 'first',
            'high': 'max',
            'low': 'min',
            'close': 'last',
            'adjusted close': 'last',
            'volume': 'sum'}

    df.index = pd.to_datetime(df.index)
    df = df.resample('W-FRI').agg(agg_dict)
    df = df.sort_index(ascending=False)

    return df

def dailytomonthly(df):
    agg_dict = {'open': 'first',
                'high': 'max',
                'low': 'min',
                'close': 'last',
                'adjusted close': 'last',
                'volume': 'sum'}

    df.index = pd.to_datetime(df.index)
    df = df.resample('M').agg(agg_dict)
    df = df.sort_index(ascending=False)

    return df

def dailytoyearly(df):
    agg_dict = {'open': 'first',
                'high': 'max',
                'low': 'min',
                'close': 'last',
                'adjusted close': 'last',
                'volume': 'sum'}

    df.index = pd.to_datetime(df.index)
    df = df.resample('Y').agg(agg_dict)
    df = df.sort_index(ascending=False)

    return df

df2 = dailytoyearly(df)

df2


#%%





# df = df.sort_index()
# df['trima'] = ta.trima(df['close'])
# df = df.sort_index(ascending=False)
# df

#%%