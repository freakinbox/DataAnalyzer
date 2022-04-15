#DataBaseFiles TIMESERIES Testing
#%%



from tkinter import *
from tkinter.ttk import *
import pandas as pd
import os
import sys
import time
from datetime import datetime
import requests
#import AlphaAPI

'''
notes

meta = ['Note']
df = {'Note': 'Thank you for using Alpha Vantage! Our standard API call frequency is 5 calls per minute and 500 calls per day. Please visit https://www.alphavantage.co/premium/ if you would like to target a higher API call frequency.'}





'''





'''

alphaAPI test code

#TODO TESTCODE
import os
ProgramDirectory = os.path.dirname(os.path.abspath(__file__))
FilesDirectory = (ProgramDirectory+"\\bin")
ticker = "AC.TO"
if 'apikey.txt' in os.listdir(FilesDirectory):
        with open(FilesDirectory+'\\apikey.txt', 'r') as file:
            apikey = file.read().replace('\n', '')
            file.close
            if apikey == "":
                print('no api key')
                AskAPI()               
            else:
                apikey= apikey
                print('API key read successful')

rsiAV(ticker, apikey)
#%%

'''




ProgramDirectory = os.path.dirname(os.path.abspath(__file__)) #Activte for testing and hash out for exe
#ProgramDirectory = os.getcwd()
MainDataDir = (ProgramDirectory+"\\data")
os.makedirs(MainDataDir, exist_ok=True)
StocksDirectory = (MainDataDir+"\\stocks")
os.makedirs(StocksDirectory, exist_ok=True)
FilesDirectory = (ProgramDirectory+"\\bin")
os.makedirs(FilesDirectory, exist_ok=True)


tick = 'GME'
tick2 = 'GME'
times2 = times2Json = None
tech = None
day = None
apikey = None
FiletypeChoice = None
csvF = jsonF = htmlF = pickledF = None

    
#%%

with open(FilesDirectory+'\\apikey.txt', 'r') as file:
    apikey = file.read().replace('\n', '')
    file.close
    #IntraTimes = TimeSeries(apikey, output_format=c)
    print('API key read successful')

#%%
os.makedirs(f'{StocksDirectory}\\{tick2}',exist_ok=True)
os.makedirs(f'{StocksDirectory}\\{tick2}\\csv',exist_ok=True)
os.makedirs(f'{StocksDirectory}\\{tick2}\\json',exist_ok=True)
os.makedirs(f'{StocksDirectory}\\{tick2}\\pickled',exist_ok=True)






#UI Settings
class UIsettings:
    '''UI sizes
    
    -Listboxsize

    -entryboxsize
    
    '''
    freaklogo = 'FreakLogoIcon.ico'

    class Listboxsize:
        '''Choice listbox variables'''
        #Main window size and center position
        x1 = 350
        y1 = 550
        xx = x1/2
        yy = y1/2
        
        #Element positions
        totaldayX = xx+135
        totaldayY = yy-253
        textX = xx
        textY = yy-225
        listboxX = xx
        listboxY = yy-20
        listboxH = 15
        listboxW = 18
        SelectallbX = xx
        SelectallbY = yy+165
        SelectbX = xx
        SelectbY = yy+195
        CancelbX = xx+130
        CancelbY = yy+255
        #Horizontal adjustements for dual list windows
        listbox1X=xx-60
        listbox2X=xx+60
        listbox2textY=yy-255
        listbox2selectallY= yy+195
        listbox2selectbY=yy+225

    class entryboxsize:
        Width = 400
        Height = 300
        #Midpoint
        xx = Width/2
        yy = Height/2
        textX = xx
        textY = yy-70
        msgX = xx
        msgY = yy+50
        entryX = xx
        entryY = yy-10
        totaldayX = xx+160
        totaldayY = yy-110
        selectbuttonX = xx+75
        selectbuttonY = yy+130
        cancebuttonX = xx+155
        cancelbuttonY = yy+130

#selections from listboxes
class choicestime():
    tick=None
    tick2=None
    crypto=None
    forex=None
    economic=None
    secondary=None

    modeselection=50, 'none'

    choicetime=50, 'none'
    choiceintradayext1=50, 'none'
    choiceintradayext2=50, 'none'
    FiletypeChoice=50, 'none'
    
    class mode():
        mode=None
        Stocks = None
        Crypto = None
        Fundamental = None
        Forex = None
        Economic = None

    
    class filetypes():
        csvF = None
        jsonF = None
        htmlF = None
        pickledF = None
    class timechoices():
        Intraday = None
        IntradayExtHistory = None
        DailyAdjusted = None
        WeeklyAdjusted = None
        MonthlyAdjusted = None
    
    class intraext1():    
        Year1Month1 = None
        Year1Month2 = None
        Year1Month3 = None
        Year1Month4 = None
        Year1Month5 = None
        Year1Month6 = None
        Year1Month7 = None
        Year1Month8 = None
        Year1Month9 = None
        Year1Month10 = None
        Year1Month11 = None
        Year1Month12 = None
    
    class intraext2():    
        Year2Month1 = None
        Year2Month2 = None
        Year2Month3 = None
        Year2Month4 = None
        Year2Month5 = None
        Year2Month6 = None
        Year2Month7 = None
        Year2Month8 = None
        Year2Month9 = None
        Year2Month10 = None
        Year2Month11 = None
        Year2Month12 = None

    class Stockindicators():
        choicehuindicator=50,'none'
        choiceoindicator1=50,'none'
        choiceoindicator2=50,'none'
        class HighUsage():
            sma=None
            ema=None
            vwap=None
            macd=None
            stoch=None
            rsi=None
            adx=None
            cci=None
            aroon=None
            bbands=None
            ad=None
            obv=None
    
        class otherindicators():
            wma=None
            dema=None
            tema=None
            trima=None
            kama=None
            mama=None
            t3=None
            macdext=None
            stochf=None
            stochrsi=None
            willr=None
            adxr=None
            apo=None
            ppo=None
            mom=None
            bop=None
            cmo=None
            roc=None
            rocr=None
            aroonosc=None
            mfi=None
            trix=None
            ulrosc=None
            dx=None
            minus_di=None
            plus_di=None
            minus_dm=None
            plus_dm=None
            midpoint=None
            midprice=None
            sar=None
            trange=None
            atr=None
            natr=None
            adosc=None
            ht_trendline=None
            ht_sine=None
            ht_trendmode=None
            ht_dcperiod=None
            ht_dcphase=None
            ht_phasor=None

class Selections():
    choicecrypto=50
    class crypto():
        firstcurrency=None
        secondcurrency=None

        exchangerate=None
        rating=None
        intraday=None
        daily=None
        weekly=None
        monthly=None

    choiceforex=50
    class forex():
        firstcurrency=None
        secondcurrency=None

        exchangerate=None
        intraday=None
        daily=None
        weekly=None
        monthly=None

    filetypechoice=None
    class filetypes():
        csvF = None
        jsonF = None
        htmlF = None
        pickledF = None


    class timechoices():
        Intraday = None
        IntradayExtHistory = None
        DailyAdjusted = None
        WeeklyAdjusted = None
        MonthlyAdjusted = None

class choicescrypto():
    choicecrypto=50
    class crypto():
        secondcurrency=None

        exchangerate=None
        rating=None
        intraday=None
        daily=None
        weekly=None
        monthly=None

#Other Settings and variabless
class other():
    total=0
    count=0
    timer=0
    mode=None


#timer= 0
#count=0
#timer=0




def EntryboxBasic(mode):
    '''
    explanation is for Message in window

    mode = 'stocks', 'cyrpto', 'forex', and 'secondarycrypto','secondaryforex' (for a second currency)
    '''
    root = Tk()
    root.title("FB's Financial Data Downloader")
    root.iconbitmap(UIsettings.freaklogo)

    Height = UIsettings.entryboxsize.Height
    Width = UIsettings.entryboxsize.Width
    
    maincanvas = Canvas(root, width=Width, height=Height)
    maincanvas.pack()

    entry = Entry(root)

    
    if mode=='stocks':
        explanation = 'Please enter Symbol below'
    elif mode=='crypto':
        explanation = 'Please enter supported Crypto currency below'
    elif mode=='forex':
        explanation = 'Please enter Forex currency below'
    elif mode=='secondarycrypto':
        explanation='Please enter second currency below'
    elif mode=='secondaryforex':
        explanation='Please enter second currency below*'
    else:
        explanation='there has been an error'



    def getAnswer():
        if entry.get() == '' :
            maincanvas.create_window(UI.msgX, UI.msgY, window=msg)

        elif mode=='stocks':
            tick = entry.get()
            choicestime.tick = tick
            print('tick =',choicestime.tick)
            choicestime.tick2 = (tick.replace('.',''))
            print('tick2 =',choicestime.tick2)
            root.destroy()
        elif mode=='crypto':
            Selections.crypto.firstcurrency = entry.get()
            print(Selections.crypto.firstcurrency)
            root.destroy()
        elif mode=='forex':
            Selections.forex.firstcurrency = entry.get()
            print(Selections.forex.firstcurrency)
            root.destroy()
        elif mode=='secondarycrypto':
            Selections.crypto.secondcurrency = entry.get()
            print(Selections.crypto.secondcurrency)
            root.destroy()
        elif mode=='secondaryforex':
            Selections.forex.secondcurrency = entry.get()
            print('Second forex is ' ,Selections.forex.secondcurrency)
            root.destroy()
        else:
            print ('stuck')

    #Elements
    total = other.total
    totalday = Message(root, text=(str(total)+'/500 for the day'))
    text1 = Message(root,justify=CENTER, width=150, text=str(explanation))
    msg = Message(root,justify=CENTER, width=150, text=str('**please enter something**'))
    Selectbutton = Button(root, text='Accept',command=getAnswer)
    Cancelbutton = Button(root, text='Cancel', command=sys.exit)
    
    #Positioning, can be changed in UI settings
    UI = UIsettings.entryboxsize()
    
    maincanvas.create_window(UI.textX, UI.textY, window=text1)
    maincanvas.create_window(UI.entryX, UI.entryY, window=entry)
    maincanvas.create_window(UI.totaldayX, UI.totaldayY, window=totalday)
    maincanvas.create_window(UI.selectbuttonX, UI.selectbuttonY, window=Selectbutton)
    maincanvas.create_window(UI.cancebuttonX, UI.cancelbuttonY, window=Cancelbutton)
    
    root.protocol("WM_DELETE_WINDOW", sys.exit)
    root.mainloop()





EntryboxBasic('crypto')
#%%


def pause():
    root = Tk()
    root.title("FB's Financial Data Downloader")
    root.iconbitmap(UIsettings.freaklogo)

    Height = UIsettings.entryboxsize.Height
    Width = UIsettings.entryboxsize.Width
    
    maincanvas = Canvas(root, width=Width, height=Height)
    
    timer= other.timer

    def update():
        timer = other.timer
        if timer >= 60:
            other.timer = 0
            progress['value'] = timer
            root.update_idletasks()
            time.sleep(2)
            root.destroy()
            
        else:
            other.timer = timer + 1
            progress['value'] = timer
            root.update_idletasks()
            timelabel.after(1000, update)
            timelabel.config(text=str(timer))

    def exit1():
        sys.exit()

    total = other.total

    #Elements
    totalday = Message(root, text=(str(total)+'/500 for the day'))
    progress = Progressbar(root, orient = HORIZONTAL,length = 300, maximum=60 , mode = 'determinate')
    text = Label(root, text='Please Wait')
    text1 = Message(root,justify=CENTER, width=150, text=('Hit the 5 calls per 60 seconds for free alphavantage api keys'))
    progress = Progressbar(root, orient = HORIZONTAL,length = 300, maximum=60 , mode = 'determinate')
    timelabel = Label(root, text=str(timer))
    timelabel.lift(progress)
    exitb = Button(root, text='Cancel & Exit)',command=exit1)

    UI = UIsettings.entryboxsize()
    
    maincanvas.create_window(370, 20, window=totalday)
    maincanvas.create_window(200, 60, window=text)
    maincanvas.create_window(UI.textX, UI.textY, window=text1)
    maincanvas.create_window(UI.xx, UI.yy, window=progress)
    maincanvas.create_window(UI.cancebuttonX, UI.cancelbuttonY, window=exitb)
    maincanvas.create_window(UI.xx, UI.yy, window=timelabel)
    

    timelabel.after(1000, update())
    maincanvas.pack()
    root.mainloop()

    
    
    


    
    
    
    #Positioning, can be changed in UI settings
    
    



def tickselection():
    root = Tk()
    root.title("FB's Financial Data Downloader")
    root.iconbitmap(UIsettings.freaklogo)

    Height = UIsettings.entryboxsize.Height
    Width = UIsettings.entryboxsize.Width
    
    maincanvas = Canvas(root, width=Width, height=Height)
    maincanvas.pack()
    
    
    global total
    

    entry = Entry(root)
    
    def getAnswer():
        tick = entry.get()
        choices.tick = tick
        print('tick =',tick)
        tick2 = (tick.replace('.',''))
        choices.tick2 = tick2
        print('tick2 =',tick2)
        root.destroy()

    #Elements
    totalday = Message(root, text=(str(total)+'/500 for the day'))
    text1 = Message(root,justify=CENTER, width=150, text=('Please enter ticker below'))
    Selectbutton = Button(root, text='Accept',command=getAnswer)
    Cancelbutton = Button(root, text='Cancel', command=sys.exit)
    
    #Positioning, can be changed in UI settings
    UI = UIsettings.entryboxsize()
    
    maincanvas.create_window(UI.textX, UI.textY, window=text1)
    maincanvas.create_window(UI.entryX, UI.entryY, window=entry)
    maincanvas.create_window(UI.totaldayX, UI.totaldayY, window=totalday)
    maincanvas.create_window(UI.selectbuttonX, UI.selectbuttonY, window=Selectbutton)
    maincanvas.create_window(UI.cancebuttonX, UI.cancelbuttonY, window=Cancelbutton)

    root.mainloop()

tickselection()
#%%



def ChoiceHighUsageIndicators():


    root=Tk()
    lbs=UIsettings().Listboxsize()
    root.title("FB's Financial Data Downloader")
    root.iconbitmap(UIsettings.freaklogo)
    maincanvas = Canvas(root, width=lbs.x1, height=lbs.y1)
    maincanvas.pack()

    listbox=Listbox(root,height=lbs.listboxH,width=lbs.listboxW,bg="grey",activestyle='dotbox',font="Helvetica",fg="yellow",selectmode=MULTIPLE)

    listbox.insert(0,"SMA")
    listbox.insert(1,"EMA")
    listbox.insert(2,"VWAP")
    listbox.insert(3,"MACD")
    listbox.insert(4,"STOCH")
    listbox.insert(5,"RSI")
    listbox.insert(6,"ADX")
    listbox.insert(7,"CCI")
    listbox.insert(8,"AROON")
    listbox.insert(9,"BBANDS")
    listbox.insert(10,"AD")
    listbox.insert(11,"OBV")
    
    checkboxmore = Checkbutton(root, text = "Display 40 more Indicators")
    def selected_item():
        choices.Stockindicators.choicehuindicator = listbox.curselection()
        if 'selected' in checkboxmore.state():

            print(checkboxmore.state(), 'is true, selected')
            root.destroy()
            ChoiceOtherIndicators()
            
        else:
            print(checkboxmore.state(), 'is false selected')
            root.destroy()

    def selectall():
        choices.Stockindicators.choicehuindicator = 0,1,2,3,4,5,6,7,8,9,10,11
        if  'selected' in checkboxmore.state():
            print(checkboxmore.state(), 'is true selected all')
            root.destroy()
            ChoiceOtherIndicators()
        else:                
            print(checkboxmore.state(), 'is false selected all')
            root.destroy()

    totalday = Message(root, text=(str(total)+'/500 for the day'))      
    


    Selectb=Button(root,text='Accept Selection',command=selected_item)
    Cancelb=Button(root,text='Cancel',command=root.destroy)
    Selectallb=Button(root,text='SELECT ALL',command=selectall)
    
    text1 = Message(root,justify=CENTER, width=150, text=('Select From the High Usage Indicator List'))
    
    maincanvas.create_window(lbs.totaldayX, lbs.totaldayY, window=totalday)
    maincanvas.create_window(lbs.textX,lbs.textY,anchor=N, window=text1)
    maincanvas.create_window(lbs.xx, lbs.yy+140, window=checkboxmore)
    maincanvas.create_window(lbs.listboxX,lbs.listboxY, window=listbox)
    maincanvas.create_window(lbs.SelectallbX,lbs.SelectallbY,window=Selectallb)
    maincanvas.create_window(lbs.SelectbX,lbs.SelectbY,window=Selectb)
    maincanvas.create_window(lbs.CancelbX,lbs.CancelbY,window=Cancelb)

    root.mainloop()

def ChoiceOtherIndicators():


    root=Tk()
    lbs=UIsettings().Listboxsize()
    root.title("FB's Financial Data Downloader")
    root.iconbitmap(UIsettings.freaklogo)
    maincanvas = Canvas(root, width=lbs.x1, height=lbs.y1)
    maincanvas.pack()

    listbox1=Listbox(root,height=20,width=12,bg="grey",activestyle='dotbox',font="Helvetica",fg="yellow",selectmode=MULTIPLE,exportselection=0)

    listbox1.insert(0,"WMA")
    listbox1.insert(1,"DEMA")
    listbox1.insert(2,"TEMA")
    listbox1.insert(3,"KAMA")
    listbox1.insert(4,"MAMA")
    listbox1.insert(5,"T3")
    listbox1.insert(6,"MACDEXT")
    listbox1.insert(7,"STOCHF")
    listbox1.insert(8,"STOCHRSI")
    listbox1.insert(9,"WILLR")
    listbox1.insert(10,"ADXR")
    listbox1.insert(11,"APO")
    listbox1.insert(12,"PPO")
    listbox1.insert(13,"MOM")
    listbox1.insert(14,"BOP")
    listbox1.insert(15,"CMO")
    listbox1.insert(16,"ROC")
    listbox1.insert(17,"ROCR")
    listbox1.insert(18,"AROONOSC")
    listbox1.insert(19,"MFI")
    

    listbox2=Listbox(root,height=20,width=12,bg="grey",activestyle='dotbox',font="Helvetica",fg="yellow",selectmode=MULTIPLE,exportselection=0)

    listbox2.insert(0,"TRIX")
    listbox2.insert(1,"ULTOSC")
    listbox2.insert(2,"DX")
    listbox2.insert(3,"MINUS_DI")
    listbox2.insert(4,"PLUS_DI")
    listbox2.insert(5,"MINUS_DM")
    listbox2.insert(6,"PLUS_DM")
    listbox2.insert(7,"MIDPOINT")
    listbox2.insert(8,"MIDPRICE")
    listbox2.insert(9,"SAR")
    listbox2.insert(10,"TRANGE")
    listbox2.insert(11,"ATR")
    listbox2.insert(12,"NATR")
    listbox2.insert(13,"ADOSC")
    listbox2.insert(14,"HT_TRENDLINE")
    listbox2.insert(15,"HT_SINE")
    listbox2.insert(16,"HT_TRENDMODE")
    listbox2.insert(17,"HT_DCPERIOD")
    listbox2.insert(18,"HT_DCPHASE")
    listbox2.insert(19,"HT_PHASOR")

    def selected_item():
        choices.Stockindicators.choiceoindicator1 = listbox1.curselection()
        choices.Stockindicators.choiceoindicator2 = listbox2.curselection()
        root.destroy()

    def selectall():
        choices.Stockindicators.choiceoindicator1 = 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19
        choices.Stockindicators.choiceoindicator2 = 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19
        root.destroy()

    totalday = Message(root, text=(str(total)+'/500 for the day'))      

    Selectb=Button(root,text='Accept Selection',command=selected_item)
    Cancelb=Button(root,text='Cancel',command=root.destroy)
    Selectallb=Button(root,text='SELECT ALL',command=selectall)
    
    text1 = Message(root,justify=CENTER, width=150, text=('Select From the Other Indicators List'))
    
    maincanvas.create_window(lbs.totaldayX, lbs.totaldayY, window=totalday)
    maincanvas.create_window(lbs.textX,lbs.listbox2textY,anchor=N, window=text1)
    maincanvas.create_window(lbs.listbox1X,lbs.listboxY, window=listbox1)
    maincanvas.create_window(lbs.listbox2X,lbs.listboxY, window=listbox2)
    maincanvas.create_window(lbs.SelectallbX,lbs.listbox2selectallY,window=Selectallb)
    maincanvas.create_window(lbs.SelectbX,lbs.listbox2selectbY,window=Selectb)
    #maincanvas.create_window(lbs.CancelbX,lbs.CancelbY,window=Cancelb)

    root.mainloop()


ChoiceHighUsageIndicators()
#%%
def ChoiceTime():
    root=Tk()
    lbs=UIsettings().Listboxsize()
    root.title("FB's Financial Data Downloader")
    root.iconbitmap(UIsettings.freaklogo)
    maincanvas = Canvas(root, width=lbs.x1, height=lbs.y1)
    maincanvas.pack()

    listbox=Listbox(root,height=lbs.listboxH,width=lbs.listboxW,bg="grey",activestyle='dotbox',font="Helvetica",fg="yellow",selectmode=MULTIPLE)

    listbox.insert(0,"Intraday")
    listbox.insert(1,"Intraday Ext. History")
    listbox.insert(2,"Daily Adjusted")
    listbox.insert(3,"Weekly Adjusted")
    listbox.insert(4,"Monthly Adjusted")

    def selected_item():
        choices.choicetime = listbox.curselection()
        root.destroy()

    def selectall():
        choices.choicetime = 0,1,2,3,4
        root.destroy()

    totalday = Message(root, text=(str(total)+'/500 for the day'))      

    Selectb=Button(root,text='Accept Selection',command=selected_item)
    Cancelb=Button(root,text='Cancel',command=root.destroy)
    Selectallb=Button(root,text='SELECT ALL',command=selectall)
    
    text1 = Message(root,justify=CENTER, width=150, text=('Select Time periods'))

    maincanvas.create_window(lbs.totaldayX, lbs.totaldayY, window=totalday)
    maincanvas.create_window(lbs.textX,lbs.textY,anchor=N, window=text1)
    maincanvas.create_window(lbs.listboxX,lbs.listboxY, window=listbox)
    maincanvas.create_window(lbs.SelectallbX,lbs.SelectallbY,window=Selectallb)
    maincanvas.create_window(lbs.SelectbX,lbs.SelectbY,window=Selectb)
    maincanvas.create_window(lbs.CancelbX,lbs.CancelbY,window=Cancelb)

    root.mainloop()




    

#%%



#print(choices().choice)
ChoiceOtherIndicators()
print (choices.Stockindicators.choiceoindicator)

#%%
def IntradayTimeYear1():
    root=Tk()
    root.iconbitmap(UIsettings.freaklogo)
    lbs=UIsettings().Listboxsize()
    root.title("FB's Financial Data Downloader")
    
    maincanvas = Canvas(root, width=lbs.x1, height=lbs.y1)
    maincanvas.pack()

    listbox=Listbox(root,height=lbs.listboxH,width=lbs.listboxW,bg="grey",activestyle='dotbox',font="Helvetica",fg="yellow",selectmode=MULTIPLE)

    listbox.insert(0,"Year 1 Month 1")
    listbox.insert(1,"Year 1 Month 2")
    listbox.insert(2,"Year 1 Month 3")
    listbox.insert(3,"Year 1 Month 4")
    listbox.insert(4,"Year 1 Month 5")
    listbox.insert(5,"Year 1 Month 6")
    listbox.insert(6,"Year 1 Month 7")
    listbox.insert(7,"Year 1 Month 8")
    listbox.insert(8,"Year 1 Month 9")
    listbox.insert(9,"Year 1 Month 10")
    listbox.insert(10,"Year 1 Month 11")
    listbox.insert(11,"Year 1 Month 12")

    def selected_item():
        choices.choiceintradayext1 = listbox.curselection()
        root.destroy()

    def selectall():
        choices.choiceintradayext2 = 0,1,2,3,4,5,6,7,8,9,10,11
        root.destroy()
        

    totalday = Message(root, text=(str(total)+'/500 for the day')) 

    Selectb=Button(root,text='Accept Selection',command=selected_item)
    Cancelb=Button(root,text='Cancel',command=root.destroy)
    Selectallb=Button(root,text='SELECT ALL',command=selectall)

    maincanvas.create_window(lbs.totaldayX,lbs.totaldayY, window=totalday)
    maincanvas.create_text(lbs.textX,lbs.textY, text='Select Time periods')
    maincanvas.create_window(lbs.listboxX,lbs.listboxY, window=listbox)
    maincanvas.create_window(lbs.SelectallbX,lbs.SelectallbY,window=Selectallb)
    maincanvas.create_window(lbs.SelectbX,lbs.SelectbY,window=Selectb)
    maincanvas.create_window(lbs.CancelbX,lbs.CancelbY,window=Cancelb)
    
    root.mainloop()

def IntradayTimeYear2():
    root=Tk()
    root.iconbitmap(UIsettings.freaklogo)
    lbs=UIsettings().Listboxsize()
    root.title("FB's Financial Data Downloader")
    
    maincanvas = Canvas(root, width=lbs.x1, height=lbs.y1)
    maincanvas.pack()

    listbox=Listbox(root,height=lbs.listboxH,width=lbs.listboxW,bg="grey",activestyle='dotbox',font="Helvetica",fg="yellow",selectmode=MULTIPLE)

    listbox.insert(0,"Year 2 Month 1")
    listbox.insert(1,"Year 2 Month 2")
    listbox.insert(2,"Year 2 Month 3")
    listbox.insert(3,"Year 2 Month 4")
    listbox.insert(4,"Year 2 Month 5")
    listbox.insert(5,"Year 2 Month 6")
    listbox.insert(6,"Year 2 Month 7")
    listbox.insert(7,"Year 2 Month 8")
    listbox.insert(8,"Year 2 Month 9")
    listbox.insert(9,"Year 2 Month 10")
    listbox.insert(10,"Year 2 Month 11")
    listbox.insert(11,"Year 2 Month 12")   

    def selected_item():
        choices.choiceintradayext1 = listbox.curselection()
        root.destroy()

    def selectall():
        choices.choiceintradayext1 = 0,1,2,3,4,5,6,7,8,9,10,11
        root.destroy()

    totalday = Message(root, text=(str(total)+'/500 for the day'))       

    Selectb=Button(root,text='Accept Selection',command=selected_item)
    Cancelb=Button(root,text='Cancel',command=root.destroy)
    Selectallb=Button(root,text='SELECT ALL',command=selectall)
    
    maincanvas.create_window(lbs.totaldayX,lbs.totaldayY, window=totalday)
    maincanvas.create_text(lbs.textX,lbs.textY, text='Select Time periods')
    maincanvas.create_window(lbs.listboxX,lbs.listboxY, window=listbox)
    maincanvas.create_window(lbs.SelectallbX,lbs.SelectallbY,window=Selectallb)
    maincanvas.create_window(lbs.SelectbX,lbs.SelectbY,window=Selectb)
    maincanvas.create_window(lbs.CancelbX,lbs.CancelbY,window=Cancelb)

    root.mainloop()




IntradayTimeYear1()
print (choice2)
IntradayTimeYear2()
#IntradayTimeYear2()
#%%

##--------------------------   The Code Above is default API and directory test code for all testing
#meta, df = AlphaAPI.mamaAV(tick,'5min','close',apikey)

#%%
#       ***** This makes request and converts json into a Dataframe

currentDIR = os.getcwd()

#df.groupby("date")  ####Needed for Tech indicators I believe
#df.columns = df.columns.astype(str).str[3:]# Removes the number and space before the column titles

#name = 'Daily'
#df.to_csv(f'{currentDIR}\\csv\\{name}.csv')
#meta.to_csv(f'{currentDIR}\\csv\\{name}meta.csv')
#df.to_json(f'{currentDIR}\\json\\{name}.json')
#meta.to_json(f'{currentDIR}\\json\\{name}meta.json')

# %%

# %%
