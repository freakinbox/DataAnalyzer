#DataBaseFiles TIMESERIES
#%%

import AlphaAPI2 as av #My own module

from tkinter import *  #Gui, need to reduce how much it imports
from tkinter.ttk import * #Same as above

#System and time
import os
import sys
import time
from datetime import datetime

#Data handling
import json
import pandas as pd


#TODO UI
#-attempt to make the UI a module with it's own seperate config files
#-make UI more fluid through changes (if window size is the same just reuse the old window instead of creating a new one)


#TODO better class variable organization, that I don't need to think about to read or adjust

###### CURRENTLY ADDING IN FUNDAMENTALS

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

        msgX = xx
        msgY = yy+140

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
    usmarket=True

    modeselection=50, 'none'

    choicetime=50, 'none'
    choiceintradayext1=50, 'none'
    choiceintradayext2=50, 'none'
    FiletypeChoice=50, 'none'
    
    class mode():
        mode=None
        Stocks = None
        Crypto = None
        Fundamentals = None
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

    choicetime=None
    class timechoices():
        Intraday = None
        IntradayExtHistory = None
        DailyAdjusted = None
        WeeklyAdjusted = None
        MonthlyAdjusted = None

    choicefundamentals=None
    class Fundamentals():
        Overview = None
        Earnings = None
        IncomeStatement = None
        BalanceSheet = None
        CashFlow = None

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
    Cont=False
    DateLastAccessed = None
    DailyLimitDate = None
    apikey = ''




#ProgramDirectory = os.path.dirname(os.path.abspath(__file__)) #Activte for partial testing and hash out for exe
MainDirectory = os.getcwd()

ProgramDirectory = (MainDirectory+"\\DataCollection")

FilesDirectory = (ProgramDirectory+"\\bin")
os.makedirs(FilesDirectory, exist_ok=True)

MainDataDir = (MainDirectory+"\\data")
os.makedirs(MainDataDir, exist_ok=True)

StocksDirectory = (MainDataDir+"\\stocks")
os.makedirs(StocksDirectory, exist_ok=True)

CryptoDirectory = (MainDataDir+"\\Crypto")
os.makedirs(CryptoDirectory, exist_ok=True)

FundamentalsDirectory = (MainDataDir+"\\Fundamentals") #TODO Started adding
os.makedirs(FundamentalsDirectory, exist_ok=True)

ForexDirectory = (MainDataDir+"\\Forex")
os.makedirs(ForexDirectory, exist_ok=True)

#EconomicDirectory = (MainDataDir+"\\Economic")  #TODO add
#os.makedirs(EconomicDirectory, exist_ok=True)

other.apikey=None #Why is this here?

#External Vars
with open((FilesDirectory+'\\VAR.json'), 'r') as externalVAR:
    VAR = json.load(externalVAR)
    if VAR['datelastaccessed'] == "":
        other.DateLastAccessed = ""
    else:
        other.DateLastAccessed = datetime.fromisoformat((VAR['datelastaccessed']))

    if VAR['dailylimitdate'] == "":
        other.DailyLimitDate = ""
    else:
        other.DailyLimitDate = datetime.date(datetime.fromisoformat((VAR['dailylimitdate'])))
    
    theCURtime = datetime.now()
    if other.DateLastAccessed =="" or other.DailyLimitDate == "":
        isgodays = 2
        isgoseconds = 90
    else:
        isgodays = ((datetime.date(theCURtime))-other.DailyLimitDate).days
        isgoseconds = (theCURtime-other.DateLastAccessed).seconds

#TODO make sure this is working properly
def JsonUpdateTOTAL(**DayLimit):
    
    with open ((FilesDirectory+'\\VAR.json'), 'r+') as externalVAR:
        VAR = json.load(externalVAR)
        if DayLimit and other.total == 0:
            VAR['dailylimitdate']=datetime.isoformat(datetime.now())
        else:
            VAR['total']=other.total
            VAR['count']=other.count
            VAR['datelastaccessed']=datetime.isoformat(datetime.now())
        
        externalVAR.seek(0)
        json.dump(VAR, externalVAR, indent=4)
        externalVAR.truncate()





def pause():
    root = Tk()
    root.title("FB's Financial Data Downloader")
    root.iconbitmap(UIsettings.freaklogo)

    Height = UIsettings.entryboxsize.Height
    Width = UIsettings.entryboxsize.Width
    
    maincanvas = Canvas(root, width=Width, height=Height)

    def update():
        if other.timer >= 60:
            other.timer = 0
            progress['value'] = other.timer
            root.update_idletasks()
            time.sleep(2)
            root.destroy()
            
        else:
            other.timer = other.timer + 1
            progress['value'] = other.timer
            root.update_idletasks()
            timelabel.after(1000, update)
            timelabel.config(text=str(other.timer))

    def exit1():
        sys.exit()

    total = other.total

    #Elements
    totalday = Message(root, text=(str(total)+'/500 for the day'))
    progress = Progressbar(root, orient = HORIZONTAL,length = 300, maximum=60 , mode = 'determinate')
    text = Label(root, text='Please Wait')
    text1 = Message(root,justify=CENTER, width=150, text=('Hit the 5 calls per 60 seconds for free alphavantage api keys'))
    progress = Progressbar(root, orient = HORIZONTAL,length = 300, maximum=60 , mode = 'determinate')
    timelabel = Label(root, text=str(other.timer))
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

def timerS():
    time.sleep(1)
    other.DateLastAccessed = datetime.now()
    other.total = other.total+1
    other.count = other.count+1
    print(r'{}/5 & {}/500'.format(other.count, other.total))

    if other.count <5:
        print('under 5')
        JsonUpdateTOTAL()
        
    elif other.count == 5:
        other.count=0
        JsonUpdateTOTAL()
        print('at 5, will pause now')
        pause()

#Select mode program will run in
#TODO I should be able to write a generalized selection script to replace all of these with a function or module instead
def ChoiceMode():
    root=Tk()
    lbs=UIsettings().Listboxsize()
    root.title("FB's Financial Data Downloader")
    root.iconbitmap(UIsettings.freaklogo)
    maincanvas = Canvas(root, width=lbs.x1, height=lbs.y1)
    maincanvas.pack()

    listbox=Listbox(root,height=lbs.listboxH,width=lbs.listboxW,bg="grey",activestyle='dotbox',font="Helvetica",fg="yellow")

    listbox.insert(0,"Stocks")
    listbox.insert(1,"Crypto")
    listbox.insert(2,"Forex")
    listbox.insert(3,"Fundamentals")
    #listbox.insert(4,"Economic")
 

    def selected_item():
        other.mode = listbox.curselection()
        print(listbox.curselection())
        if listbox.curselection() == ():
            maincanvas.create_window(UI.msgX, UI.msgY, window=msg)
        else:
            root.destroy()


    UI = UIsettings.Listboxsize()
    msg = Message(root,justify=CENTER, width=150, text=str('**please select something**'))

    total = other.total
    totalday = Message(root, text=(str(total)+'/500 for the day'))
    text1 = Message(root,justify=CENTER, width=150, text=('Select desired mode'))
    Selectb=Button(root,text='Accept',command=selected_item)
    Cancelb=Button(root,text='Cancel',command=sys.exit)

    
    
    maincanvas.create_window(lbs.totaldayX, lbs.totaldayY, window=totalday)
    maincanvas.create_window(lbs.textX,lbs.textY,anchor=N, window=text1)
    maincanvas.create_window(lbs.listboxX,lbs.listboxY, window=listbox)
    maincanvas.create_window(lbs.SelectbX,lbs.SelectbY,window=Selectb)
    maincanvas.create_window(lbs.CancelbX,lbs.CancelbY,window=Cancelb)
    

    
    root.mainloop()

def SelectionMode():
    

    def ifin(index, name2):
        
        if index in other.mode:
            print(name2)
            return True            
        elif index not in other.mode:
            print(name2, 'not')
            return None
    
    
    choicestime.mode.Stocks=ifin(0,"Stocks")
    choicestime.mode.Crypto=ifin(1,"Crypto")
    choicestime.mode.Forex=ifin(2,"Forex")
    choicestime.mode.Fundamentals=ifin(3,"Fundamentals")
    #choicestime.mode.Economic=ifin(4,"Economic")

    #if no selection it shuts program down #TODO change to prompt requesting input with continue and exit buttons
    if choicestime.mode.Stocks and choicestime.mode.Crypto and choicestime.mode.Fundamentals and choicestime.mode.Forex and choicestime.mode.Economic  == False or None:
        exit()

#Select filetypes data will be saved in
def ChoiceFileTypes():
    root=Tk()
    lbs=UIsettings().Listboxsize()
    root.title("FB's Financial Data Downloader")
    root.iconbitmap(UIsettings.freaklogo)
    maincanvas = Canvas(root, width=lbs.x1, height=lbs.y1)
    maincanvas.pack()

    listbox=Listbox(root,height=lbs.listboxH,width=lbs.listboxW,bg="grey",activestyle='dotbox',font="Helvetica",fg="yellow",selectmode=MULTIPLE)

    listbox.insert(0,"csv")
    listbox.insert(1,"json")
    listbox.insert(2,"html")
    listbox.insert(3,"'Pickled' DataFrame")
 

    def selected_item():
        Selections.filetypechoice=listbox.curselection()
        if listbox.curselection() == ():
            maincanvas.create_window(UI.msgX, UI.msgY, window=msg)
        else:
            root.destroy()
    

    def selectall():
        Selections.filetypechoice=0,1,2,3
        root.destroy()
        
    UI = UIsettings.Listboxsize()
    msg = Message(root,justify=CENTER, width=150, text=str('**please select something**'))

    total = other.total
    totalday = Message(root, text=(str(total)+'/500 for the day'))
    text1 = Message(root,justify=CENTER, width=150, text=('Select desired filetypes'))
    Selectb=Button(root,text='Accept',command=selected_item)
    Cancelb=Button(root,text='Cancel',command=sys.exit)
    Selectallb=Button(root,text='SELECT ALL',command=selectall)
    
    maincanvas.create_window(lbs.totaldayX, lbs.totaldayY, window=totalday)
    maincanvas.create_window(lbs.textX,lbs.textY,anchor=N, window=text1)
    maincanvas.create_window(lbs.listboxX,lbs.listboxY, window=listbox)
    maincanvas.create_window(lbs.SelectallbX,lbs.SelectallbY,window=Selectallb)
    maincanvas.create_window(lbs.SelectbX,lbs.SelectbY,window=Selectb)
    maincanvas.create_window(lbs.CancelbX,lbs.CancelbY,window=Cancelb)

    
    root.mainloop()

def SelectionFiletype():
    
    csvF = Selections.filetypes.csvF
    jsonF = Selections.filetypes.jsonF
    htmlF = Selections.filetypes.htmlF
    pickledF = Selections.filetypes.pickledF

    


    def ifin(index,name2):
        
        if index in Selections.filetypechoice:
            print(name2)
            return True            
        elif index not in Selections.filetypechoice:
            print(name2, 'not')
            return None

    
    
    Selections.filetypes.csvF=ifin(0,'csv')
    Selections.filetypes.jsonF=ifin(1,'json')
    Selections.filetypes.htmlF=ifin(2,'html')
    Selections.filetypes.pickledF=ifin(3,"'Pickled' DataFrame")

    #if no selection it defaults to csv
    if csvF and jsonF and htmlF and pickledF == False or None:
        csvF = True

#Default single entrybox window with modes
def EntryboxBasic(mode):
    '''
    explanation is for Message in window

    mode = 'stocks', 'cyrpto', 'forex', 'fundamentals', and 'secondarycrypto','secondaryforex' (for a second currency)
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
    elif mode=='fundamentals':
        explanation='Please enter Symbol below'
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
            if "." in tick:
                choicestime.usmarket=False
            else:
                choicestime.usmarket=True
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
        elif mode=='fundamentals':
            tick = entry.get()
            choicestime.tick = tick
            print('tick =',choicestime.tick)
            choicestime.tick2 = (tick.replace('.',''))
            print('tick2 =',choicestime.tick2)
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

def APIkey():
    #TODO change to new config file and have placeholder text there always. New one is a python config file in the /bin directory that will not be synched to 
    def AskAPI():
        root = Tk()
        root.title("Freakinbox's Ticker Entry")

        maincanvas = Canvas(root, width=400, height=300)
        maincanvas.pack()

        text = Label(root, text='Please enter Alphavantage API key below to continue')
        maincanvas.create_window(200, 50, window=text)
        
        entry = Entry(root, width=30)
        maincanvas.create_window(200, 140, window=entry)

        def getAnswer():
            output = entry.get()
            root.destroy()
            if output == '':
                print("You didn't enter a key")
                sys.exit()
            else:
                f= open(FilesDirectory+"\\apikey.txt","w+")
                f.write(output)
                f.close()
                print('apikey entered')

            other.apikey = output
            print('successful')

        Selectbutton = Button(root, text='Accept Selection',command=getAnswer)
        Cancelbutton = Button(root, text='Cancel', command=sys.exit)

        text.pack
        entry.pack
        Selectbutton.pack(side=RIGHT, padx=5, pady=5)
        Cancelbutton.pack(side=RIGHT)

        root.protocol("WM_DELETE_WINDOW", sys.exit)
        root.mainloop()
    
    
    if 'apikey.json' in os.listdir(FilesDirectory):
        with open ((FilesDirectory+'\\apikey.json'), 'r') as file:
            VAR = json.load(file)
            print(VAR['apikey'])
            if VAR['apikey'] == "" or None:
                print('no api key')
                AskAPI()
            else:
                other.apikey == VAR['apikey']
                print('API key read successful')
                
    if 'apikey.json' not in os.listdir(FilesDirectory):
        AskAPI()


#Creates ticker named folder
def DirectoryCreator(modex):
    '''
    modes = 'stocks', 'crypto', 'fundamentals', 'forex', 'economic'
    '''

    csvF = Selections.filetypes.csvF
    jsonF = Selections.filetypes.jsonF
    htmlF = Selections.filetypes.htmlF
    pickledF = Selections.filetypes.pickledF
    
    if modex == 'stocks':
        os.makedirs(f'{StocksDirectory}\\{choicestime.tick2}',exist_ok=True)
        os.chdir(f'{StocksDirectory}\\{choicestime.tick2}')
        print(os.getcwd())

        if csvF:
            os.makedirs('csv',exist_ok=True)
        if jsonF:
            os.makedirs('json',exist_ok=True)
        if htmlF:
            os.makedirs('html',exist_ok=True)
        if pickledF:
            os.makedirs('pickled',exist_ok=True)
        os.chdir(ProgramDirectory)

    if modex == 'crypto':
        
        os.makedirs('{}\\{}'.format(CryptoDirectory,Selections.crypto.firstcurrency),exist_ok=True)
        os.chdir('{}\\{}'.format(CryptoDirectory,Selections.crypto.firstcurrency))
        
        if csvF:
            os.makedirs('csv',exist_ok=True)
        if jsonF:
            os.makedirs('json',exist_ok=True)
        if htmlF:
            os.makedirs('html',exist_ok=True)
        if pickledF:
            os.makedirs('pickled',exist_ok=True)
        os.chdir(ProgramDirectory)

    if modex == 'forex':
        #TODO add in folders for each secondary currency
        os.makedirs('{}\\{}'.format(ForexDirectory,Selections.forex.firstcurrency),exist_ok=True)
        os.chdir('{}\\{}'.format(ForexDirectory,Selections.forex.firstcurrency))
        
        if csvF:
            os.makedirs('csv',exist_ok=True)
        if jsonF:
            os.makedirs('json',exist_ok=True)
        if htmlF:
            os.makedirs('html',exist_ok=True)
        if pickledF:
            os.makedirs('pickled',exist_ok=True)
        os.chdir(ProgramDirectory)
    
    
    if modex == 'fundamentals':
        os.makedirs(f'{FundamentalsDirectory}\\{choicestime.tick2}',exist_ok=True)
        os.chdir(f'{FundamentalsDirectory}\\{choicestime.tick2}')

        if csvF:
            os.makedirs(f'csv',exist_ok=True)
        if jsonF:
            os.makedirs(f'json',exist_ok=True)
        if htmlF:
            os.makedirs(f'html',exist_ok=True)
        if pickledF:
            os.makedirs(f'pickled',exist_ok=True)
        os.chdir(ProgramDirectory)
    
    # if mode1 == 'economic':
    #     os.makedirs(f'{EconomicDirectory}',exist_ok=True)
    #     if csvF:
    #         os.makedirs(f'{EconomicDirectory}\\csv',exist_ok=True)
    #     if jsonF:
    #         os.makedirs(f'{EconomicDirectory}\\json',exist_ok=True)
    #     if htmlF:
    #         os.makedirs(f'{EconomicDirectory}\\html',exist_ok=True)
    #     if pickledF:
    #         os.makedirs(f'{EconomicDirectory}\\pickled',exist_ok=True)

    #else:
    #    print("whoops")

#GUI to select time periods
def ChoiceTimeUS():
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
        choicestime.choicetime = listbox.curselection()
        root.destroy()
        

    def selectall():
        choicestime.choicetime = 0,1,2,3,4
        root.destroy()

    
    total = other.total
    totalday = Message(root, text=(str(total)+'/500 for the day'))      

    Selectb=Button(root,text='Accept Selection',command=selected_item)
    Cancelb=Button(root,text='Cancel',command=sys.exit)
    Selectallb=Button(root,text='SELECT ALL',command=selectall)
    
    text1 = Message(root,justify=CENTER, width=150, text=('Select Time periods'))

    maincanvas.create_window(lbs.totaldayX, lbs.totaldayY, window=totalday)
    maincanvas.create_window(lbs.textX,lbs.textY,anchor=N, window=text1)
    maincanvas.create_window(lbs.listboxX,lbs.listboxY, window=listbox)
    maincanvas.create_window(lbs.SelectallbX,lbs.SelectallbY,window=Selectallb)
    maincanvas.create_window(lbs.SelectbX,lbs.SelectbY,window=Selectb)
    maincanvas.create_window(lbs.CancelbX,lbs.CancelbY,window=Cancelb)

    root.protocol("WM_DELETE_WINDOW", sys.exit)
    root.mainloop()

#reads time period selections for API call
def SelectionTimeUS():

    def ifin(index,name2):
        
        if index in choicestime.choicetime:
            print(name2)
            return True         
        elif index not in choicestime.choicetime:
            print(name2,'not')
            return False
            

    choicestime.timechoices.Intraday=ifin(0,'Intraday')
    choicestime.timechoices.IntradayExtHistory=ifin(1,'Intraday Ext. History')
    choicestime.timechoices.DailyAdjusted=ifin(2,'Daily Adjusted')
    choicestime.timechoices.WeeklyAdjusted=ifin(3,'Weekly Adjusted')
    choicestime.timechoices.MonthlyAdjusted=ifin(4,'Monthly Adjusted')

def ChoiceTime():

    #TODO add message that states Intraday options removed for non US markets
    root=Tk()
    lbs=UIsettings().Listboxsize()
    root.title("FB's Financial Data Downloader")
    root.iconbitmap(UIsettings.freaklogo)
    maincanvas = Canvas(root, width=lbs.x1, height=lbs.y1)
    maincanvas.pack()

    listbox=Listbox(root,height=lbs.listboxH,width=lbs.listboxW,bg="grey",activestyle='dotbox',font="Helvetica",fg="yellow",selectmode=MULTIPLE)

    listbox.insert(0,"Daily Adjusted")
    listbox.insert(1,"Weekly Adjusted")
    listbox.insert(2,"Monthly Adjusted")

    def selected_item():
        choicestime.choicetime = listbox.curselection()
        root.destroy()
        

    def selectall():
        choicestime.choicetime = 0,1,2
        root.destroy()

    
    total = other.total
    totalday = Message(root, text=(str(total)+'/500 for the day'))      

    Selectb=Button(root,text='Accept Selection',command=selected_item)
    Cancelb=Button(root,text='Cancel',command=sys.exit)
    Selectallb=Button(root,text='SELECT ALL',command=selectall)
    
    text1 = Message(root,justify=CENTER, width=150, text=('Select Time periods'))

    maincanvas.create_window(lbs.totaldayX, lbs.totaldayY, window=totalday)
    maincanvas.create_window(lbs.textX,lbs.textY,anchor=N, window=text1)
    maincanvas.create_window(lbs.listboxX,lbs.listboxY, window=listbox)
    maincanvas.create_window(lbs.SelectallbX,lbs.SelectallbY,window=Selectallb)
    maincanvas.create_window(lbs.SelectbX,lbs.SelectbY,window=Selectb)
    maincanvas.create_window(lbs.CancelbX,lbs.CancelbY,window=Cancelb)

    root.protocol("WM_DELETE_WINDOW", sys.exit)
    root.mainloop()

#reads time period selections for API call
def SelectionTime():

    def ifin(index,name2):
        
        if index in choicestime.choicetime:
            print(name2)
            return True         
        elif index not in choicestime.choicetime:
            print(name2,'not')
            return False
            

    choicestime.timechoices.Intraday=False
    choicestime.timechoices.IntradayExtHistory=False
    choicestime.timechoices.DailyAdjusted=ifin(0,'Daily Adjusted')
    choicestime.timechoices.WeeklyAdjusted=ifin(1,'Weekly Adjusted')
    choicestime.timechoices.MonthlyAdjusted=ifin(2,'Monthly Adjusted')


#Select Intraday first year
def ChoiceIntradayExt1():
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
        choicestime.choiceintradayext1 = listbox.curselection()
        root.destroy()

    def selectall():
        choicestime.choiceintradayext1 = 0,1,2,3,4,5,6,7,8,9,10,11
        root.destroy()

    total = other.total
    totalday = Message(root, text=(str(total)+'/500 for the day')) 

    Selectb=Button(root,text='Accept Selection',command=selected_item)
    Cancelb=Button(root,text='Cancel',command=sys.exit)
    Selectallb=Button(root,text='SELECT ALL',command=selectall)

    text1 = Message(root,justify=CENTER, width=150, text=('Select Intraday Time periods from the previous year'))

    maincanvas.create_window(lbs.totaldayX,lbs.totaldayY, window=totalday)
    maincanvas.create_window(lbs.textX,lbs.textY,anchor=N, window=text1)
    maincanvas.create_window(lbs.listboxX,lbs.listboxY, window=listbox)
    maincanvas.create_window(lbs.SelectallbX,lbs.SelectallbY,window=Selectallb)
    maincanvas.create_window(lbs.SelectbX,lbs.SelectbY,window=Selectb)
    maincanvas.create_window(lbs.CancelbX,lbs.CancelbY,window=Cancelb)
    
    root.protocol("WM_DELETE_WINDOW", sys.exit)
    root.mainloop()

def SelectionIntradayExt1():


    def ifin(index,name2):
        
        if index in choicestime.choiceintradayext1:
            print(name2)
            return True         
        elif index not in choicestime.choiceintradayext1:
            print(name2,'not')
            return False
            

    choicestime.intraext1.Year1Month1 = ifin(0,"Year 1 Month 1")
    choicestime.intraext1.Year1Month2 = ifin(1,"Year 1 Month 2")
    choicestime.intraext1.Year1Month3 = ifin(2,"Year 1 Month 3")
    choicestime.intraext1.Year1Month4 = ifin(3,"Year 1 Month 4")
    choicestime.intraext1.Year1Month5 = ifin(4,"Year 1 Month 5")
    choicestime.intraext1.Year1Month6 = ifin(5,"Year 1 Month 6")
    choicestime.intraext1.Year1Month7 = ifin(6,"Year 1 Month 7")
    choicestime.intraext1.Year1Month8 = ifin(7,"Year 1 Month 8")
    choicestime.intraext1.Year1Month9 = ifin(8,"Year 1 Month 9")
    choicestime.intraext1.Year1Month10 = ifin(9,"Year 1 Month 10")
    choicestime.intraext1.Year1Month11 = ifin(10,"Year 1 Month 11")
    choicestime.intraext1.Year1Month12 = ifin(11,"Year 1 Month 12")

#Select Intraday Second year
def ChoiceIntradayExt2():
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
        choicestime.choiceintradayext2 = listbox.curselection()
        root.destroy()

    def selectall():
        choicestime.choiceintradayext2 = 0,1,2,3,4,5,6,7,8,9,10,11
        root.destroy()

    total = other.total
    totalday = Message(root, text=(str(total)+'/500 for the day'))       

    Selectb=Button(root,text='Accept Selection',command=selected_item)
    Cancelb=Button(root,text='Cancel',command=sys.exit)
    Selectallb=Button(root,text='SELECT ALL',command=selectall)
    
    text1 = Message(root,justify=CENTER, width=150, text=('Select Intraday Time periods from 1 - 2 years ago'))

    maincanvas.create_window(lbs.totaldayX,lbs.totaldayY, window=totalday)
    maincanvas.create_window(lbs.textX,lbs.textY,anchor=N, window=text1)
    maincanvas.create_window(lbs.listboxX,lbs.listboxY, window=listbox)
    maincanvas.create_window(lbs.SelectallbX,lbs.SelectallbY,window=Selectallb)
    maincanvas.create_window(lbs.SelectbX,lbs.SelectbY,window=Selectb)
    maincanvas.create_window(lbs.CancelbX,lbs.CancelbY,window=Cancelb)

    root.protocol("WM_DELETE_WINDOW", sys.exit)
    root.mainloop()

def SelectionIntradayExt2():


    def ifin(index,name2):
        
        if index in choicestime.choiceintradayext2:
            print(name2)
            return True         
        elif index not in choicestime.choiceintradayext2:
            print(name2,'not')
            return False


    choicestime.intraext2.Year2Month1 = ifin(0,"Year 2 Month 1")
    choicestime.intraext2.Year2Month2 = ifin(1,"Year 2 Month 2")
    choicestime.intraext2.Year2Month3 = ifin(2,"Year 2 Month 3")
    choicestime.intraext2.Year2Month4 = ifin(3,"Year 2 Month 4")
    choicestime.intraext2.Year2Month5 = ifin(4,"Year 2 Month 5")
    choicestime.intraext2.Year2Month6 = ifin(5,"Year 2 Month 6")
    choicestime.intraext2.Year2Month7 = ifin(6,"Year 2 Month 7")
    choicestime.intraext2.Year2Month8 = ifin(7,"Year 2 Month 8")
    choicestime.intraext2.Year2Month9 = ifin(8,"Year 2 Month 9")
    choicestime.intraext2.Year2Month10 = ifin(9,"Year 2 Month 10")
    choicestime.intraext2.Year2Month11 = ifin(10,"Year 2 Month 11")
    choicestime.intraext2.Year2Month12 = ifin(11,"Year 2 Month 12")

#Select Indicators US market
def ChoiceHighUsageIndicatorsUS():
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
        choicestime.Stockindicators.choicehuindicator = listbox.curselection()
        if 'selected' in checkboxmore.state():

            print(checkboxmore.state(), 'is true, selected')
            root.destroy()
            ChoiceOtherIndicators()
            
        else:
            print(checkboxmore.state(), 'is false selected')
            root.destroy()

    def selectall():
        choicestime.Stockindicators.choicehuindicator = 0,1,2,3,4,5,6,7,8,9,10,11
        if  'selected' in checkboxmore.state():
            print(checkboxmore.state(), 'is true selected all')
            root.destroy()
            SelectionHighUsageIndicators()
            ChoiceOtherIndicators()
        else:                
            print(checkboxmore.state(), 'is false selected all')
            root.destroy()

    total = other.total
    totalday = Message(root, text=(str(total)+'/500 for the day'))      
    


    Selectb=Button(root,text='Accept Selection',command=selected_item)
    Cancelb=Button(root,text='Cancel',command=sys.exit)
    Selectallb=Button(root,text='SELECT ALL',command=selectall)
    
    text1 = Message(root,justify=CENTER, width=150, text=('Select From the High Usage Indicator List'))
    
    maincanvas.create_window(lbs.totaldayX, lbs.totaldayY, window=totalday)
    maincanvas.create_window(lbs.textX,lbs.textY,anchor=N, window=text1)
    maincanvas.create_window(lbs.xx, lbs.yy+140, window=checkboxmore)
    maincanvas.create_window(lbs.listboxX,lbs.listboxY, window=listbox)
    maincanvas.create_window(lbs.SelectallbX,lbs.SelectallbY,window=Selectallb)
    maincanvas.create_window(lbs.SelectbX,lbs.SelectbY,window=Selectb)
    maincanvas.create_window(lbs.CancelbX,lbs.CancelbY,window=Cancelb)

    root.protocol("WM_DELETE_WINDOW", sys.exit)
    root.mainloop()

def ChoiceOtherIndicatorsUS():
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
        choicestime.Stockindicators.choiceoindicator1 = listbox1.curselection()
        choicestime.Stockindicators.choiceoindicator2 = listbox2.curselection()
        root.destroy()

    def selectall():
        choicestime.Stockindicators.choiceoindicator1 = 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19
        choicestime.Stockindicators.choiceoindicator2 = 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19
        root.destroy()

    
    total = other.total
    totalday = Message(root, text=(str(total)+'/500 for the day'))      

    Selectb=Button(root,text='Accept Selection',command=selected_item)
    Cancelb=Button(root,text='Cancel',command=sys.exit)
    Selectallb=Button(root,text='SELECT ALL',command=selectall)
    
    text1 = Message(root,justify=CENTER, width=150, text=('Select From the Other Indicators List'))
    
    maincanvas.create_window(lbs.totaldayX, lbs.totaldayY, window=totalday)
    maincanvas.create_window(lbs.textX,lbs.listbox2textY,anchor=N, window=text1)
    maincanvas.create_window(lbs.listbox1X,lbs.listboxY, window=listbox1)
    maincanvas.create_window(lbs.listbox2X,lbs.listboxY, window=listbox2)
    maincanvas.create_window(lbs.SelectallbX,lbs.listbox2selectallY,window=Selectallb)
    maincanvas.create_window(lbs.SelectbX,lbs.listbox2selectbY,window=Selectb)
    maincanvas.create_window(lbs.CancelbX,lbs.CancelbY,window=Cancelb) #TODO MAY NEED TO HASH THIS OUT AGAIN, REMOVED IT FOR NOW AS I CAN'T SEE WHY IT WOULD BE

    root.protocol("WM_DELETE_WINDOW", sys.exit)
    root.mainloop()

def SelectionHighUsageIndicatorsUS():


    def ifin(index,name2):
        
        if index in choicestime.Stockindicators.choicehuindicator:
            print(name2)
            return True         
        elif index not in choicestime.Stockindicators.choicehuindicator:
            print(name2,'not')
            return False
            
    choicestime.Stockindicators.HighUsage.sma = ifin(0,"SMA")
    choicestime.Stockindicators.HighUsage.ema = ifin(1,"EMA")
    choicestime.Stockindicators.HighUsage.vwap = ifin(2,"VWAP")
    choicestime.Stockindicators.HighUsage.macd = ifin(3,"MACD")
    choicestime.Stockindicators.HighUsage.stoch = ifin(4,"STOCH")
    choicestime.Stockindicators.HighUsage.rsi = ifin(5,"RSI")
    choicestime.Stockindicators.HighUsage.adx = ifin(6,"ADX")
    choicestime.Stockindicators.HighUsage.cci = ifin(7,"CCI")
    choicestime.Stockindicators.HighUsage.aroon = ifin(8,"AROON")
    choicestime.Stockindicators.HighUsage.bbands = ifin(9,"BBANDS")
    choicestime.Stockindicators.HighUsage.ad = ifin(10,"AD")
    choicestime.Stockindicators.HighUsage.obv = ifin(11,"OBV")

def SelectionOtherIndicatorsUS():


    def ifin1(index,name2):
        
        if index in choicestime.Stockindicators.choiceoindicator1:
            print(name2)
            return True         
        elif index not in choicestime.Stockindicators.choiceoindicator1:
            print(name2,'not')
            return False
    
    def ifin2(index,name2):
        
        if index in choicestime.Stockindicators.choiceoindicator2:
            print(name2)
            return True         
        elif index not in choicestime.Stockindicators.choiceoindicator2:
            print(name2,'not')
            return False


            
            
    choicestime.Stockindicators.otherindicators.wma= ifin1(0,"WMA")
    choicestime.Stockindicators.otherindicators.dema= ifin1(1,"DEMA")
    choicestime.Stockindicators.otherindicators.tema= ifin1(2,"TEMA")
    choicestime.Stockindicators.otherindicators.kama= ifin1(3,"KAMA")
    choicestime.Stockindicators.otherindicators.mama= ifin1(4,"MAMA")
    choicestime.Stockindicators.otherindicators.t3= ifin1(5,"T3")
    choicestime.Stockindicators.otherindicators.macdext= ifin1(6,"MACDEXT")
    choicestime.Stockindicators.otherindicators.stochf= ifin1(7,"STOCHF")
    choicestime.Stockindicators.otherindicators.stochrsi= ifin1(8,"STOCHRSI")
    choicestime.Stockindicators.otherindicators.willr= ifin1(9,"WILLR")
    choicestime.Stockindicators.otherindicators.adxr= ifin1(10,"ADXR")
    choicestime.Stockindicators.otherindicators.apo= ifin1(11,"APO")
    choicestime.Stockindicators.otherindicators.ppo= ifin1(12,"PPO")
    choicestime.Stockindicators.otherindicators.mom= ifin1(13,"MOM")
    choicestime.Stockindicators.otherindicators.bop= ifin1(14,"BOP")
    choicestime.Stockindicators.otherindicators.cmo= ifin1(15,"CMO")
    choicestime.Stockindicators.otherindicators.roc= ifin1(16,"ROC")
    choicestime.Stockindicators.otherindicators.rocr= ifin1(17,"ROCR")
    choicestime.Stockindicators.otherindicators.aroonosc= ifin1(18,"AROONOSC")
    choicestime.Stockindicators.otherindicators.mfi= ifin1(19,"MFI")



    choicestime.Stockindicators.otherindicators.trix= ifin2(0,"TRIX")
    choicestime.Stockindicators.otherindicators.ulrosc= ifin2(1,"ULTOSC")
    choicestime.Stockindicators.otherindicators.dx= ifin2(2,"DX")
    choicestime.Stockindicators.otherindicators.minus_di= ifin2(3,"MINUS_DI")
    choicestime.Stockindicators.otherindicators.plus_di= ifin2(4,"PLUS_DI")
    choicestime.Stockindicators.otherindicators.minus_dm= ifin2(5,"MINUS_DM")
    choicestime.Stockindicators.otherindicators.plus_dm= ifin2(6,"PLUS_DM")
    choicestime.Stockindicators.otherindicators.midpoint= ifin2(7,"MIDPOINT")
    choicestime.Stockindicators.otherindicators.midprice= ifin2(8,"MIDPRICE")
    choicestime.Stockindicators.otherindicators.sar= ifin2(9,"SAR")
    choicestime.Stockindicators.otherindicators.trange= ifin2(10,"TRANGE")
    choicestime.Stockindicators.otherindicators.atr= ifin2(11,"ATR")
    choicestime.Stockindicators.otherindicators.natr= ifin2(12,"NATR")
    choicestime.Stockindicators.otherindicators.adosc= ifin2(13,"ADOSC")
    choicestime.Stockindicators.otherindicators.ht_trendline= ifin2(14,"HT_TRENDLINE")
    choicestime.Stockindicators.otherindicators.ht_sine= ifin2(15,"HT_SINE")
    choicestime.Stockindicators.otherindicators.ht_trendmode= ifin2(16,"HT_TRENDMODE")
    choicestime.Stockindicators.otherindicators.ht_dcperiod= ifin2(17,"HT_DCPERIOD")
    choicestime.Stockindicators.otherindicators.ht_dcphase= ifin2(18,"HT_DCPHASE")
    choicestime.Stockindicators.otherindicators.ht_phasor= ifin2(19,"HT_PHASOR")


#Select Indicators all other markets
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
    listbox.insert(2,"MACD")
    listbox.insert(3,"STOCH")
    listbox.insert(4,"RSI")
    listbox.insert(5,"ADX")
    listbox.insert(6,"CCI")
    listbox.insert(7,"AROON")
    listbox.insert(8,"BBANDS")
    listbox.insert(9,"AD")
    listbox.insert(10,"OBV")
    
    checkboxmore = Checkbutton(root, text = "Display 40 more Indicators")
    def selected_item():
        choicestime.Stockindicators.choicehuindicator = listbox.curselection()
        if 'selected' in checkboxmore.state():

            print(checkboxmore.state(), 'is true, selected')
            root.destroy()
            ChoiceOtherIndicators()
            
        else:
            print(checkboxmore.state(), 'is false selected')
            root.destroy()

    def selectall():
        choicestime.Stockindicators.choicehuindicator = 0,1,2,3,4,5,6,7,8,9,10
        if  'selected' in checkboxmore.state():
            print(checkboxmore.state(), 'is true selected all')
            root.destroy()
            SelectionHighUsageIndicators()
            ChoiceOtherIndicators()
        else:                
            print(checkboxmore.state(), 'is false selected all')
            root.destroy()

    total = other.total
    totalday = Message(root, text=(str(total)+'/500 for the day'))      
    


    Selectb=Button(root,text='Accept Selection',command=selected_item)
    Cancelb=Button(root,text='Cancel',command=sys.exit)
    Selectallb=Button(root,text='SELECT ALL',command=selectall)
    
    text1 = Message(root,justify=CENTER, width=150, text=('Select From the High Usage Indicator List'))
    
    maincanvas.create_window(lbs.totaldayX, lbs.totaldayY, window=totalday)
    maincanvas.create_window(lbs.textX,lbs.textY,anchor=N, window=text1)
    maincanvas.create_window(lbs.xx, lbs.yy+140, window=checkboxmore)
    maincanvas.create_window(lbs.listboxX,lbs.listboxY, window=listbox)
    maincanvas.create_window(lbs.SelectallbX,lbs.SelectallbY,window=Selectallb)
    maincanvas.create_window(lbs.SelectbX,lbs.SelectbY,window=Selectb)
    maincanvas.create_window(lbs.CancelbX,lbs.CancelbY,window=Cancelb)

    root.protocol("WM_DELETE_WINDOW", sys.exit)
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
        choicestime.Stockindicators.choiceoindicator1 = listbox1.curselection()
        choicestime.Stockindicators.choiceoindicator2 = listbox2.curselection()
        root.destroy()

    def selectall():
        choicestime.Stockindicators.choiceoindicator1 = 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19
        choicestime.Stockindicators.choiceoindicator2 = 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19
        root.destroy()

    
    total = other.total
    totalday = Message(root, text=(str(total)+'/500 for the day'))      

    Selectb=Button(root,text='Accept Selection',command=selected_item)
    Cancelb=Button(root,text='Cancel',command=sys.exit)
    Selectallb=Button(root,text='SELECT ALL',command=selectall)
    
    text1 = Message(root,justify=CENTER, width=150, text=('Select From the Other Indicators List'))
    
    maincanvas.create_window(lbs.totaldayX, lbs.totaldayY, window=totalday)
    maincanvas.create_window(lbs.textX,lbs.listbox2textY,anchor=N, window=text1)
    maincanvas.create_window(lbs.listbox1X,lbs.listboxY, window=listbox1)
    maincanvas.create_window(lbs.listbox2X,lbs.listboxY, window=listbox2)
    maincanvas.create_window(lbs.SelectallbX,lbs.listbox2selectallY,window=Selectallb)
    maincanvas.create_window(lbs.SelectbX,lbs.listbox2selectbY,window=Selectb)
    maincanvas.create_window(lbs.CancelbX,lbs.CancelbY,window=Cancelb) #TODO MAY NEED TO HASH THIS OUT AGAIN, REMOVED IT FOR NOW AS I CAN'T SEE WHY IT WOULD BE

    root.protocol("WM_DELETE_WINDOW", sys.exit)
    root.mainloop()

def SelectionHighUsageIndicators():


    def ifin(index,name2):
        
        if index in choicestime.Stockindicators.choicehuindicator:
            print(name2)
            return True         
        elif index not in choicestime.Stockindicators.choicehuindicator:
            print(name2,'not')
            return False
            
    choicestime.Stockindicators.HighUsage.sma = ifin(0,"SMA")
    choicestime.Stockindicators.HighUsage.ema = ifin(1,"EMA")
    choicestime.Stockindicators.HighUsage.vwap = False
    choicestime.Stockindicators.HighUsage.macd = ifin(2,"MACD")
    choicestime.Stockindicators.HighUsage.stoch = ifin(3,"STOCH")
    choicestime.Stockindicators.HighUsage.rsi = ifin(4,"RSI")
    choicestime.Stockindicators.HighUsage.adx = ifin(5,"ADX")
    choicestime.Stockindicators.HighUsage.cci = ifin(6,"CCI")
    choicestime.Stockindicators.HighUsage.aroon = ifin(7,"AROON")
    choicestime.Stockindicators.HighUsage.bbands = ifin(8,"BBANDS")
    choicestime.Stockindicators.HighUsage.ad = ifin(9,"AD")
    choicestime.Stockindicators.HighUsage.obv = ifin(10,"OBV")

def SelectionOtherIndicators():


    def ifin1(index,name2):
        
        if index in choicestime.Stockindicators.choiceoindicator1:
            print(name2)
            return True         
        elif index not in choicestime.Stockindicators.choiceoindicator1:
            print(name2,'not')
            return False
    
    def ifin2(index,name2):
        
        if index in choicestime.Stockindicators.choiceoindicator2:
            print(name2)
            return True         
        elif index not in choicestime.Stockindicators.choiceoindicator2:
            print(name2,'not')
            return False


            
            
    choicestime.Stockindicators.otherindicators.wma= ifin1(0,"WMA")
    choicestime.Stockindicators.otherindicators.dema= ifin1(1,"DEMA")
    choicestime.Stockindicators.otherindicators.tema= ifin1(2,"TEMA")
    choicestime.Stockindicators.otherindicators.kama= ifin1(3,"KAMA")
    choicestime.Stockindicators.otherindicators.mama= ifin1(4,"MAMA")
    choicestime.Stockindicators.otherindicators.t3= ifin1(5,"T3")
    choicestime.Stockindicators.otherindicators.macdext= ifin1(6,"MACDEXT")
    choicestime.Stockindicators.otherindicators.stochf= ifin1(7,"STOCHF")
    choicestime.Stockindicators.otherindicators.stochrsi= ifin1(8,"STOCHRSI")
    choicestime.Stockindicators.otherindicators.willr= ifin1(9,"WILLR")
    choicestime.Stockindicators.otherindicators.adxr= ifin1(10,"ADXR")
    choicestime.Stockindicators.otherindicators.apo= ifin1(11,"APO")
    choicestime.Stockindicators.otherindicators.ppo= ifin1(12,"PPO")
    choicestime.Stockindicators.otherindicators.mom= ifin1(13,"MOM")
    choicestime.Stockindicators.otherindicators.bop= ifin1(14,"BOP")
    choicestime.Stockindicators.otherindicators.cmo= ifin1(15,"CMO")
    choicestime.Stockindicators.otherindicators.roc= ifin1(16,"ROC")
    choicestime.Stockindicators.otherindicators.rocr= ifin1(17,"ROCR")
    choicestime.Stockindicators.otherindicators.aroonosc= ifin1(18,"AROONOSC")
    choicestime.Stockindicators.otherindicators.mfi= ifin1(19,"MFI")



    choicestime.Stockindicators.otherindicators.trix= ifin2(0,"TRIX")
    choicestime.Stockindicators.otherindicators.ulrosc= ifin2(1,"ULTOSC")
    choicestime.Stockindicators.otherindicators.dx= ifin2(2,"DX")
    choicestime.Stockindicators.otherindicators.minus_di= ifin2(3,"MINUS_DI")
    choicestime.Stockindicators.otherindicators.plus_di= ifin2(4,"PLUS_DI")
    choicestime.Stockindicators.otherindicators.minus_dm= ifin2(5,"MINUS_DM")
    choicestime.Stockindicators.otherindicators.plus_dm= ifin2(6,"PLUS_DM")
    choicestime.Stockindicators.otherindicators.midpoint= ifin2(7,"MIDPOINT")
    choicestime.Stockindicators.otherindicators.midprice= ifin2(8,"MIDPRICE")
    choicestime.Stockindicators.otherindicators.sar= ifin2(9,"SAR")
    choicestime.Stockindicators.otherindicators.trange= ifin2(10,"TRANGE")
    choicestime.Stockindicators.otherindicators.atr= ifin2(11,"ATR")
    choicestime.Stockindicators.otherindicators.natr= ifin2(12,"NATR")
    choicestime.Stockindicators.otherindicators.adosc= ifin2(13,"ADOSC")
    choicestime.Stockindicators.otherindicators.ht_trendline= ifin2(14,"HT_TRENDLINE")
    choicestime.Stockindicators.otherindicators.ht_sine= ifin2(15,"HT_SINE")
    choicestime.Stockindicators.otherindicators.ht_trendmode= ifin2(16,"HT_TRENDMODE")
    choicestime.Stockindicators.otherindicators.ht_dcperiod= ifin2(17,"HT_DCPERIOD")
    choicestime.Stockindicators.otherindicators.ht_dcphase= ifin2(18,"HT_DCPHASE")
    choicestime.Stockindicators.otherindicators.ht_phasor= ifin2(19,"HT_PHASOR")


'''

CRYPTO & FOREX

'''

#GUI to select time periods
def ChoiceCrypto():
    root=Tk()
    lbs=UIsettings().Listboxsize()
    root.title("FB's Financial Data Downloader")
    root.iconbitmap(UIsettings.freaklogo)
    maincanvas = Canvas(root, width=lbs.x1, height=lbs.y1)
    maincanvas.pack()

    listbox=Listbox(root,height=lbs.listboxH,width=lbs.listboxW,bg="grey",activestyle='dotbox',font="Helvetica",fg="yellow",selectmode=MULTIPLE)

    listbox.insert(0,"Exchange Rate")
    listbox.insert(1,"Intraday")
    listbox.insert(2,"Daily")
    listbox.insert(3,"Weekly")
    listbox.insert(4,"Monthly")

    def selected_item():
        Selections.choicecrypto = listbox.curselection()
        root.destroy()
        

    def selectall():
        Selections.choicecrypto = 0,1,2,3,4
        root.destroy()

    
    total = other.total
    totalday = Message(root, text=(str(total)+'/500 for the day'))      

    Selectb=Button(root,text='Accept Selection',command=selected_item)
    Cancelb=Button(root,text='Cancel',command=sys.exit)
    Selectallb=Button(root,text='SELECT ALL',command=selectall)
    
    text1 = Message(root,justify=CENTER, width=150, text=('Select Time periods'))

    maincanvas.create_window(lbs.totaldayX, lbs.totaldayY, window=totalday)
    maincanvas.create_window(lbs.textX,lbs.textY,anchor=N, window=text1)
    maincanvas.create_window(lbs.listboxX,lbs.listboxY, window=listbox)
    maincanvas.create_window(lbs.SelectallbX,lbs.SelectallbY,window=Selectallb)
    maincanvas.create_window(lbs.SelectbX,lbs.SelectbY,window=Selectb)
    maincanvas.create_window(lbs.CancelbX,lbs.CancelbY,window=Cancelb)

    root.protocol("WM_DELETE_WINDOW", sys.exit)
    root.mainloop()

#reads time period selections for API call
def SelectionCrypto():

    def ifin(index,name2):
        
        if index in Selections.choicecrypto:
            print(name2)
            return True         
        elif index not in Selections.choicecrypto:
            print(name2,'not')
            return False
            

    Selections.crypto.exchangerate=ifin(0,'Exchange Rate')
    Selections.crypto.intraday=ifin(1,'Intraday')
    Selections.crypto.daily=ifin(2,'Daily')
    Selections.crypto.weekly=ifin(3,'Weekly')
    Selections.crypto.monthly=ifin(4,'Monthly')


def ChoiceForex():
    root=Tk()
    lbs=UIsettings().Listboxsize()
    root.title("FB's Financial Data Downloader")
    root.iconbitmap(UIsettings.freaklogo)
    maincanvas = Canvas(root, width=lbs.x1, height=lbs.y1)
    maincanvas.pack()

    listbox=Listbox(root,height=lbs.listboxH,width=lbs.listboxW,bg="grey",activestyle='dotbox',font="Helvetica",fg="yellow",selectmode=MULTIPLE)

    listbox.insert(0,"Exchange Rate")
    listbox.insert(1,"Intraday")
    listbox.insert(2,"Daily")
    listbox.insert(3,"Weekly")
    listbox.insert(4,"Monthly")

    def selected_item():
        Selections.choiceforex = listbox.curselection()
        print(Selections.choiceforex)
        root.destroy()
        

    def selectall():
        Selections.choiceforex = 0,1,2,3,4
        root.destroy()

    
    total = other.total
    totalday = Message(root, text=(str(total)+'/500 for the day'))      

    Selectb=Button(root,text='Accept Selection',command=selected_item)
    Cancelb=Button(root,text='Cancel',command=sys.exit)
    Selectallb=Button(root,text='SELECT ALL',command=selectall)
    
    text1 = Message(root,justify=CENTER, width=150, text=('Select Time periods'))

    maincanvas.create_window(lbs.totaldayX, lbs.totaldayY, window=totalday)
    maincanvas.create_window(lbs.textX,lbs.textY,anchor=N, window=text1)
    maincanvas.create_window(lbs.listboxX,lbs.listboxY, window=listbox)
    maincanvas.create_window(lbs.SelectallbX,lbs.SelectallbY,window=Selectallb)
    maincanvas.create_window(lbs.SelectbX,lbs.SelectbY,window=Selectb)
    maincanvas.create_window(lbs.CancelbX,lbs.CancelbY,window=Cancelb)
    root.protocol("WM_DELETE_WINDOW", sys.exit)

    root.mainloop()

#reads time period selections for API call
def SelectionForex():

    def ifin(index,name2):
        
        if index in Selections.choiceforex:
            print(name2)
            return True         
        elif index not in Selections.choiceforex:
            print(name2,'not')
            return False
            

    Selections.forex.exchangerate=ifin(0,'Exchange Rate')
    Selections.forex.intraday=ifin(1,'Intraday')
    Selections.forex.daily=ifin(2,'Daily')
    Selections.forex.weekly=ifin(3,'Weekly')
    Selections.forex.monthly=ifin(4,'Monthly')

#Fundamental functions
def ChoiceFundamentals():
    root=Tk()
    lbs=UIsettings().Listboxsize()
    root.title("FB's Financial Data Downloader")
    root.iconbitmap(UIsettings.freaklogo)
    maincanvas = Canvas(root, width=lbs.x1, height=lbs.y1)
    maincanvas.pack()

    listbox=Listbox(root,height=lbs.listboxH,width=lbs.listboxW,bg="grey",activestyle='dotbox',font="Helvetica",fg="yellow",selectmode=MULTIPLE)

    listbox.insert(0,"Overview")
    listbox.insert(1,"Earnings")
    listbox.insert(2,"Income Statement")
    listbox.insert(3,"Balance Sheet")
    listbox.insert(4,"Cash Flow")

    def selected_item():
        Selections.choicefundamentals=listbox.curselection()
        root.destroy()
        

    def selectall():
        Selections.choicefundamentals=0,1,2,3,4
        root.destroy()

    
    total = other.total
    totalday = Message(root,text=(str(total)+'/500 for the day'))      

    Selectb=Button(root,text='Accept Selection',command=selected_item)
    Cancelb=Button(root,text='Cancel',command=sys.exit)
    Selectallb=Button(root,text='SELECT ALL',command=selectall)
    
    text1 = Message(root,justify=CENTER, width=150, text=('Select Fundamentals to download'))

    maincanvas.create_window(lbs.totaldayX, lbs.totaldayY, window=totalday)
    maincanvas.create_window(lbs.textX,lbs.textY,anchor=N, window=text1)
    maincanvas.create_window(lbs.listboxX,lbs.listboxY, window=listbox)
    maincanvas.create_window(lbs.SelectallbX,lbs.SelectallbY,window=Selectallb)
    maincanvas.create_window(lbs.SelectbX,lbs.SelectbY,window=Selectb)
    maincanvas.create_window(lbs.CancelbX,lbs.CancelbY,window=Cancelb)

    root.protocol("WM_DELETE_WINDOW", sys.exit)
    root.mainloop()

def SelectionFundamentals():

    def ifin(index,name2):
        
        if index in Selections.choicefundamentals:
            print(name2)
            return True         
        elif index not in Selections.choicefundamentals:
            print(name2,'not')
            return False
            

    Selections.Fundamentals.Overview=ifin(0,'Overview')
    Selections.Fundamentals.Earnings=ifin(1,'Earnings')
    Selections.Fundamentals.IncomeStatement=ifin(2,'Income Statement')
    Selections.Fundamentals.BalanceSheet=ifin(3,'Balance Sheet')
    Selections.Fundamentals.CashFlow=ifin(4,'Cash Flow')





#GUI to continue, ask for ticker, if they quit it will update a directory list csv file and exit the program
def continue2(mode):
    #TODO clean up and remove timer text background over progress bar
    '''
    explanation is for Message in window

    mode = 'stocks', 'cyrpto', 'forex', 'fundamentals'
    '''
    
    root = Tk()
    root.title("FB's Financial Data Downloader")
    root.iconbitmap(UIsettings.freaklogo)

    Height = UIsettings.entryboxsize.Height
    Width = UIsettings.entryboxsize.Width
    
    maincanvas = Canvas(root, width=Width, height=Height)
    maincanvas.pack()

    
    total = other.total
    totalday = Message(root, text=(str(total)+'/500 for the day'))
    maincanvas.create_window(370, 20, window=totalday)
    totalday.pack  

    entry = Entry(root)
    maincanvas.create_window(200, 140, window=entry)

    def Continue():
        
        curdir = os.getcwd()
        if mode == 'stocks':
            os.chdir(StocksDirectory)
        elif mode == 'crypto':
            os.chdir(CryptoDirectory)
        elif mode == 'forex':
            os.chdir(ForexDirectory)
        elif mode == 'fundamentals':
            os.chdir(FundamentalsDirectory)
        DirectoryUpdate()
        os.chdir(curdir)

        
        if mode == 'stocks':
            choicestime.tick = entry.get()
            choicestime.tick2 = (choicestime.tick.replace('.',''))
            print('tick2 =',choicestime.tick2)
            other.Cont = True
            if "." in choicestime.tick:
                choicestime.usmarket=False
            else:
                choicestime.usmarket=True

            print (choicestime.tick)
        elif mode == 'crypto':
            Selections.crypto.firstcurrency = entry.get()
            print(Selections.crypto.firstcurrency)
            other.Cont = True
        elif mode == 'forex':
            Selections.forex.firstcurrency = entry.get()
            print(Selections.forex.firstcurrency)
            other.Cont = True
        if mode == 'fundamentals':
            choicestime.tick = entry.get()
            choicestime.tick2 = (choicestime.tick.replace('.',''))
            print('tick2 =',choicestime.tick2)
            other.Cont = True
            print (choicestime.tick)
        

        #TODO add in adjustable timer variable to remove the amount of seconds caculated from the timer (So if you wait 30 seconds it will only be a 30 second wait)
        if (datetime.now()-other.DateLastAccessed).seconds >= 60:
            print((datetime.now()-other.DateLastAccessed).seconds)
            print("you paused long enough on your own")
            other.count=0
            root.destroy()
            Sequence()
        else:
            root.destroy()
            Sequence()

    def exit1():
        print('Goodbye')
        if mode == 'stocks':
            os.chdir(StocksDirectory)
        elif mode == 'crypto':
            os.chdir(CryptoDirectory)
        elif mode == 'forex':
            os.chdir(ForexDirectory)
        elif mode == 'fundamentals':
            os.chdir(FundamentalsDirectory)
        DirectoryUpdate()
        root.destroy()
        sys.exit
        

    #Elements
    #Positioning, can be changed in UI settings
    text1 = Message(root,justify=CENTER, width=150, text=('Do you have more tickers to enter?'))
    maincanvas.create_window(200, 50, window=text1)

    continueb = Button(root, text='Yes',command=Continue)
    exitb = Button(root, text='No (Exit)',command=exit1)

    UI = UIsettings.entryboxsize()
    maincanvas.create_window(UI.textX, UI.textY, window=text1)
    maincanvas.create_window(UI.entryX, UI.entryY, window=entry)
    maincanvas.create_window(UI.totaldayX, UI.totaldayY, window=totalday)
    maincanvas.create_window(UI.selectbuttonX, UI.selectbuttonY, window=continueb)
    maincanvas.create_window(UI.cancebuttonX, UI.cancelbuttonY, window=exitb)

    root.mainloop()
   
#Run in continue2 or when csv list of current folders in directory required
def DirectoryUpdate():
    dir_list = next(os.walk('.'))[1]
    print(dir_list)
    list1 = (dir_list)

    df = pd.DataFrame(list(zip(*[list1]))).add_prefix('ticker')
    df.to_csv('list.csv', index=False)

#API callers
def stocksAPI():

    csvF = Selections.filetypes.csvF
    jsonF = Selections.filetypes.jsonF
    htmlF = Selections.filetypes.htmlF
    pickledF = Selections.filetypes.pickledF
    tick= choicestime.tick
    tick2 = choicestime.tick2

    if choicestime.choicetime and choicestime.Stockindicators.choiceoindicator1 and choicestime.Stockindicators.choiceoindicator2 and choicestime.Stockindicators.choicehuindicator == None:
        print('you need to enter something')
        sys.exit()


    def pandastofile(cmd,name):
        meta, df = cmd

        if 'Invalid API call' in str(df):
            print('American stocks only for Intraday stats on Alpha vantage')
        elif 'Error Message' in meta:
            print('whoops there was an error in the api call')
        
        
        else:
            tick2 = choicestime.tick2
            if csvF:
                df.to_csv(f'{StocksDirectory}\\{tick2}\\csv\\{name}.csv')
            if jsonF:
                df.to_json(f'{StocksDirectory}\\{tick2}\\json\\{name}.json')
            if htmlF:
                df.to_html(f'{StocksDirectory}\\{tick2}\\html\\{name}.html')
            if pickledF:
                df.to_pickle(f'{StocksDirectory}\\{tick2}\\pickled\\{name}.pkl')
            
            print('')
            print(name,'Download complete')

    


    Item = choicestime.timechoices.Intraday
    ItemName = 'intraday'
    if Item:
        timerS()
        var3 = av.IntradayAV(tick, other.apikey)#TODO add interval and add error handler
        pandastofile(var3, ItemName)

    Item = choicestime.timechoices.DailyAdjusted
    ItemName = 'dailyadjusted'
    if Item:
        timerS()
        var3 = av.DailyAdjustedAV(tick, other.apikey)
        pandastofile(var3, ItemName)
    
    Item = choicestime.timechoices.WeeklyAdjusted
    ItemName = 'weeklyadjusted'
    if Item:
        timerS()
        var3 = av.WeeklyAdjustedAV(tick, other.apikey)
        pandastofile(var3, ItemName)

    Item = choicestime.timechoices.MonthlyAdjusted
    ItemName = 'monthlyadjusted'
    if Item:
        timerS()
        var3 = av.MonthlyAdjustedAV(tick, other.apikey)
        pandastofile(var3, ItemName)

    def techAPIAV(var,cmd,name):
        if var:
            meta, df = cmd
            tick2 = choicestime.tick2

            if 'Invalid API call' in str(df):
                print('American stocks only for Intraday stats (such as VWAP) on Alpha vantage')
            elif 'Error Message' in meta:
                print('whoops there was an error in the api call')
            else:
                df = df.sort_index(ascending=False)
                if csvF:
                    df.to_csv(f'{StocksDirectory}\\{tick2}\\csv\\{name}.csv')
                if jsonF:
                    df.to_json(f'{StocksDirectory}\\{tick2}\\json\\{name}.json')
                if htmlF:
                    df.to_html(f'{StocksDirectory}\\{tick2}\\html\\{name}.html')
                if pickledF:
                    df.to_pickle(f'{StocksDirectory}\\{tick2}\\pickled\\{name}.pkl')

                print('')
                print(name,'Download complete')
        else:
            var=var


    #Intraday Extended

    Item = choicestime.intraext1.Year1Month1
    ItemName = 'year1month1'
    if Item:
        timerS()
        var3 = av.IntradayExtendedAV(tick,other.apikey, slice=ItemName) #add settings
        techAPIAV(Item, var3, ItemName)

    Item = choicestime.intraext1.Year1Month2
    ItemName = 'year1month2'
    if Item:
        timerS()
        var3 = av.IntradayExtendedAV(tick,other.apikey, slice=ItemName) #add settings
        techAPIAV(Item, var3, ItemName)

    Item = choicestime.intraext1.Year1Month3
    ItemName = 'year1month3'
    if Item:
        timerS()
        var3 = av.IntradayExtendedAV(tick,other.apikey, slice=ItemName) #add settings
        techAPIAV(Item, var3, ItemName)

    Item = choicestime.intraext1.Year1Month4
    ItemName = 'year1month4'
    if Item:
        timerS()
        var3 = av.IntradayExtendedAV(tick,other.apikey, slice=ItemName) #add settings
        techAPIAV(Item, var3, ItemName)

    Item = choicestime.intraext1.Year1Month5
    ItemName = 'year1month5'
    if Item:
        timerS()
        var3 = av.IntradayExtendedAV(tick,other.apikey, slice=ItemName) #add settings
        techAPIAV(Item, var3, ItemName)

    Item = choicestime.intraext1.Year1Month6
    ItemName = 'year1month6'
    if Item:
        timerS()
        var3 = av.IntradayExtendedAV(tick,other.apikey, slice=ItemName) #add settings
        techAPIAV(Item, var3, ItemName)

    Item = choicestime.intraext1.Year1Month7
    ItemName = 'year1month7'
    if Item:
        timerS()
        var3 = av.IntradayExtendedAV(tick,other.apikey, slice=ItemName) #add settings
        techAPIAV(Item, var3, ItemName)

    Item = choicestime.intraext1.Year1Month8
    ItemName = 'year1month8'
    if Item:
        timerS()
        var3 = av.IntradayExtendedAV(tick,other.apikey, slice=ItemName) #add settings
        techAPIAV(Item, var3, ItemName)

    Item = choicestime.intraext1.Year1Month9
    ItemName = 'year1month9'
    if Item:
        timerS()
        var3 = av.IntradayExtendedAV(tick,other.apikey, slice=ItemName) #add settings
        techAPIAV(Item, var3, ItemName)

    Item = choicestime.intraext1.Year1Month10
    ItemName = 'year1month10'
    if Item:
        timerS()
        var3 = av.IntradayExtendedAV(tick,other.apikey, slice=ItemName) #add settings
        techAPIAV(Item, var3, ItemName)

    Item = choicestime.intraext1.Year1Month11
    ItemName = 'year1month11'
    if Item:
        timerS()
        var3 = av.IntradayExtendedAV(tick,other.apikey, slice=ItemName) #add settings
        techAPIAV(Item, var3, ItemName)

    Item = choicestime.intraext1.Year1Month12
    ItemName = 'year1month12'
    if Item:
        timerS()
        var3 = av.IntradayExtendedAV(tick,other.apikey, slice=ItemName) #add settings
        techAPIAV(Item, var3, ItemName)

    Item = choicestime.intraext2.Year2Month1
    ItemName = 'year2month1'
    if Item:
        timerS()
        var3 = av.IntradayExtendedAV(tick,other.apikey, slice=ItemName) #add settings
        techAPIAV(Item, var3, ItemName)

    Item = choicestime.intraext2.Year2Month2
    ItemName = 'year2month2'
    if Item:
        timerS()
        var3 = av.IntradayExtendedAV(tick,other.apikey, slice=ItemName) #add settings
        techAPIAV(Item, var3, ItemName)

    Item = choicestime.intraext2.Year2Month3
    ItemName = 'year2month3'
    if Item:
        timerS()
        var3 = av.IntradayExtendedAV(tick,other.apikey, slice=ItemName) #add settings
        techAPIAV(Item, var3, ItemName)

    Item = choicestime.intraext2.Year2Month4
    ItemName = 'year2month4'
    if Item:
        timerS()
        var3 = av.IntradayExtendedAV(tick,other.apikey, slice=ItemName) #add settings
        techAPIAV(Item, var3, ItemName)

    Item = choicestime.intraext2.Year2Month5
    ItemName = 'year2month5'
    if Item:
        timerS()
        var3 = av.IntradayExtendedAV(tick,other.apikey, slice=ItemName) #add settings
        techAPIAV(Item, var3, ItemName)

    Item = choicestime.intraext2.Year2Month6
    ItemName = 'year2month6'
    if Item:
        timerS()
        var3 = av.IntradayExtendedAV(tick,other.apikey, slice=ItemName) #add settings
        techAPIAV(Item, var3, ItemName)

    Item = choicestime.intraext2.Year2Month7
    ItemName = 'year2month7'
    if Item:
        timerS()
        var3 = av.IntradayExtendedAV(tick,other.apikey, slice=ItemName) #add settings
        techAPIAV(Item, var3, ItemName)

    Item = choicestime.intraext2.Year2Month8
    ItemName = 'year2month8'
    if Item:
        timerS()
        var3 = av.IntradayExtendedAV(tick,other.apikey, slice=ItemName) #add settings
        techAPIAV(Item, var3, ItemName)

    Item = choicestime.intraext2.Year2Month9
    ItemName = 'year2month9'
    if Item:
        timerS()
        var3 = av.IntradayExtendedAV(tick,other.apikey, slice=ItemName) #add settings
        techAPIAV(Item, var3, ItemName)

    Item = choicestime.intraext2.Year2Month10
    ItemName = 'year2month10'
    if Item:
        timerS()
        var3 = av.IntradayExtendedAV(tick,other.apikey, slice=ItemName) #add settings
        techAPIAV(Item, var3, ItemName)

    Item = choicestime.intraext2.Year2Month11
    ItemName = 'year2month11'
    if Item:
        timerS()
        var3 = av.IntradayExtendedAV(tick,other.apikey, slice=ItemName) #add settings
        techAPIAV(Item, var3, ItemName)

    Item = choicestime.intraext2.Year2Month12
    ItemName = 'year2month12'
    if Item:
        timerS()
        var3 = av.IntradayExtendedAV(tick,other.apikey, slice=ItemName) #add settings
        techAPIAV(Item, var3, ItemName)


    #HighUsage First

    Item = choicestime.Stockindicators.HighUsage.sma
    ItemName = 'sma'
    if Item:
        timerS()
        var3 = av.smaAV(tick,other.apikey) #add settings
        techAPIAV(Item, var3, ItemName)

    Item = choicestime.Stockindicators.HighUsage.ema
    ItemName = 'ema'
    if Item:
        timerS()
        var3 = av.emaAV(tick,other.apikey) #add settings
        techAPIAV(Item, var3, ItemName)

    Item = choicestime.Stockindicators.HighUsage.vwap
    ItemName = 'vwap'
    if Item:
        timerS()
        var3 = av.vwapAV(tick, other.apikey) #add settings
        techAPIAV(Item, var3, ItemName)

    Item = choicestime.Stockindicators.HighUsage.macd
    ItemName = 'macd'
    if Item:
        timerS()
        var3 = av.macdAV(tick, other.apikey) #add settings
        techAPIAV(Item, var3, ItemName)
    
    Item = choicestime.Stockindicators.HighUsage.stoch
    ItemName = 'stoch'
    if Item:
        timerS()
        var3 = av.stochAV(tick, other.apikey) #add settings
        techAPIAV(Item, var3, ItemName)

    Item = choicestime.Stockindicators.HighUsage.rsi
    ItemName = 'rsi'
    if Item:
        timerS()
        var3 = av.rsiAV(tick, other.apikey) #add settings
        techAPIAV(Item, var3, ItemName)


    Item = choicestime.Stockindicators.HighUsage.adx
    ItemName = 'adx'
    if Item:
        timerS()
        var3 = av.adxAV(tick, other.apikey) #add settings
        techAPIAV(Item, var3, ItemName)

    Item = choicestime.Stockindicators.HighUsage.cci
    ItemName = 'cci'
    if Item:
        timerS()
        var3 = av.cciAV(tick, other.apikey) #add settings
        techAPIAV(Item, var3, ItemName)

    Item = choicestime.Stockindicators.HighUsage.aroon
    ItemName = 'aroon'
    if Item:
        timerS()
        var3 = av.aroonAV(tick, other.apikey) #add settings
        techAPIAV(Item, var3, ItemName)

    Item = choicestime.Stockindicators.HighUsage.bbands
    ItemName = 'bbands'
    if Item:
        timerS()
        var3 = av.bbandsAV(tick, other.apikey) #add settings
        techAPIAV(Item, var3, ItemName)

    Item = choicestime.Stockindicators.HighUsage.ad
    ItemName = 'ad'
    if Item:
        timerS()
        var3 = av.adAV(tick, other.apikey) #add settings
        techAPIAV(Item, var3, ItemName)

    Item = choicestime.Stockindicators.HighUsage.obv
    ItemName = 'obv'
    if Item:
        timerS()
        var3 = av.obvAV(tick, other.apikey) #add settings
        techAPIAV(Item, var3, ItemName)


    # OTHER INDICATORS


    Item = choicestime.Stockindicators.otherindicators.wma
    ItemName = 'wma'
    if Item:
        timerS()
        var3 = av.wmaAV(tick, other.apikey) #add settings
        techAPIAV(Item, var3, ItemName)

    Item = choicestime.Stockindicators.otherindicators.dema
    ItemName = 'dema'
    if Item:
        timerS()
        var3 = av.demaAV(tick, other.apikey) #add settings
        techAPIAV(Item, var3, ItemName)

    Item = choicestime.Stockindicators.otherindicators.tema
    ItemName = 'tema'
    if Item:
        timerS()
        var3 = av.temaAV(tick, other.apikey) #add settings
        techAPIAV(Item, var3, ItemName)

    Item = choicestime.Stockindicators.otherindicators.trima
    ItemName = 'trima'
    if Item:
        timerS()
        var3 = av.trimaAV(tick, other.apikey) #add settings
        techAPIAV(Item, var3, ItemName)

    Item = choicestime.Stockindicators.otherindicators.kama
    ItemName = 'kama'
    if Item:
        timerS()
        var3 = av.kamaAV(tick, other.apikey) #add settings
        techAPIAV(Item, var3, ItemName)

    Item = choicestime.Stockindicators.otherindicators.mama
    ItemName = 'mama'
    if Item:
        timerS()
        var3 = av.mamaAV(tick, other.apikey) #add settings
        techAPIAV(Item, var3, ItemName)

    Item = choicestime.Stockindicators.otherindicators.t3
    ItemName = 't3'
    if Item:
        timerS()
        var3 = av.t3AV(tick, other.apikey) #add settings
        techAPIAV(Item, var3, ItemName)

    Item = choicestime.Stockindicators.otherindicators.macdext
    ItemName = 'macdext'
    if Item:
        timerS()
        var3 = av.macdextAV(tick, other.apikey) #add settings
        techAPIAV(Item, var3, ItemName)

    Item = choicestime.Stockindicators.otherindicators.stochf
    ItemName = 'stochf'
    if Item:
        timerS()
        var3 = av.stochFAV(tick, other.apikey) #add settings
        techAPIAV(Item, var3, ItemName)

    Item = choicestime.Stockindicators.otherindicators.stochrsi
    ItemName = 'stochrsi'
    if Item:
        timerS()
        var3 = av.stochrsiAV(tick, other.apikey) #add settings
        techAPIAV(Item, var3, ItemName)

    Item = choicestime.Stockindicators.otherindicators.willr
    ItemName = 'willr'
    if Item:
        timerS()
        var3 = av.willrAV(tick, other.apikey) #add settings
        techAPIAV(Item, var3, ItemName)

    Item = choicestime.Stockindicators.otherindicators.adxr
    ItemName = 'adxr'
    if Item:
        timerS()
        var3 = av.adxrAV(tick, other.apikey) #add settings
        techAPIAV(Item, var3, ItemName)

    Item = choicestime.Stockindicators.otherindicators.apo
    ItemName = 'apo'
    if Item:
        timerS()
        var3 = av.apoAV(tick, other.apikey) #add settings
        techAPIAV(Item, var3, ItemName)

    Item = choicestime.Stockindicators.otherindicators.ppo
    ItemName = 'ppo'
    if Item:
        timerS()
        var3 = av.ppoAV(tick, other.apikey) #add settings
        techAPIAV(Item, var3, ItemName)

    Item = choicestime.Stockindicators.otherindicators.mom
    ItemName = 'mom'
    if Item:
        timerS()
        var3 = av.momAV(tick, other.apikey) #add settings
        techAPIAV(Item, var3, ItemName)

    Item = choicestime.Stockindicators.otherindicators.bop
    ItemName = 'bop'
    if Item:
        timerS()
        var3 = av.bopAV(tick, other.apikey) #add settings
        techAPIAV(Item, var3, ItemName)

    Item = choicestime.Stockindicators.otherindicators.cmo
    ItemName = 'cmo'
    if Item:
        timerS()
        var3 = av.cmoAV(tick, other.apikey) #add settings
        techAPIAV(Item, var3, ItemName)

    Item = choicestime.Stockindicators.otherindicators.roc
    ItemName = 'roc'
    if Item:
        timerS()
        var3 = av.rocAV(tick, other.apikey) #add settings
        techAPIAV(Item, var3, ItemName)

    Item = choicestime.Stockindicators.otherindicators.rocr
    ItemName = 'rocr'
    if Item:
        timerS()
        var3 = av.rocrAV(tick, other.apikey) #add settings
        techAPIAV(Item, var3, ItemName)

    Item = choicestime.Stockindicators.otherindicators.aroonosc
    ItemName = 'aroonosc'
    if Item:
        timerS()
        var3 = av.aroonoscAV(tick, other.apikey) #add settings
        techAPIAV(Item, var3, ItemName)

    Item = choicestime.Stockindicators.otherindicators.mfi
    ItemName = 'mfi'
    if Item:
        timerS()
        var3 = av.mfiAV(tick, other.apikey) #add settings
        techAPIAV(Item, var3, ItemName)

    Item = choicestime.Stockindicators.otherindicators.trix
    ItemName = 'trix'
    if Item:
        timerS()
        var3 = av.trixAV(tick, other.apikey) #add settings
        techAPIAV(Item, var3, ItemName)

    Item = choicestime.Stockindicators.otherindicators.ulrosc
    ItemName = 'ulrosc'
    if Item:
        timerS()
        var3 = av.ultoscAV(tick, other.apikey) #add settings
        techAPIAV(Item, var3, ItemName)

    Item = choicestime.Stockindicators.otherindicators.dx
    ItemName = 'dx'
    if Item:
        timerS()
        var3 = av.dxAV(tick, other.apikey) #add settings
        techAPIAV(Item, var3, ItemName)

    Item = choicestime.Stockindicators.otherindicators.minus_di
    ItemName = 'minus_di'
    if Item:
        timerS()
        var3 = av.minus_diAV(tick, other.apikey) #add settings
        techAPIAV(Item, var3, ItemName)

    Item = choicestime.Stockindicators.otherindicators.plus_di
    ItemName = 'plus_di'
    if Item:
        timerS()
        var3 = av.plus_diAV(tick, other.apikey) #add settings
        techAPIAV(Item, var3, ItemName)

    Item = choicestime.Stockindicators.otherindicators.minus_dm
    ItemName = 'minus_dm'
    if Item:
        timerS()
        var3 = av.dxAV(tick, other.apikey) #add settings
        techAPIAV(Item, var3, ItemName)

    Item = choicestime.Stockindicators.otherindicators.plus_dm
    ItemName = 'plus_dm'
    if Item:
        timerS()
        var3 = av.plus_dmAV(tick, other.apikey) #add settings
        techAPIAV(Item, var3, ItemName)

    Item = choicestime.Stockindicators.otherindicators.midpoint
    ItemName = 'midpoint'
    if Item:
        timerS()
        var3 = av.midpointAV(tick, other.apikey) #add settings
        techAPIAV(Item, var3, ItemName)

    Item = choicestime.Stockindicators.otherindicators.midprice
    ItemName = 'midprice'
    if Item:
        timerS()
        var3 = av.midpriceAV(tick, other.apikey) #add settings
        techAPIAV(Item, var3, ItemName)

    Item = choicestime.Stockindicators.otherindicators.sar
    ItemName = 'sar'
    if Item:
        timerS()
        var3 = av.sarAV(tick, other.apikey) #add settings
        techAPIAV(Item, var3, ItemName)

    Item = choicestime.Stockindicators.otherindicators.trange
    ItemName = 'trange'
    if Item:
        timerS()
        var3 = av.trangeAV(tick, other.apikey) #add settings
        techAPIAV(Item, var3, ItemName)

    Item = choicestime.Stockindicators.otherindicators.atr
    ItemName = 'atr'
    if Item:
        timerS()
        var3 = av.atrAV(tick, other.apikey) #add settings
        techAPIAV(Item, var3, ItemName)

    Item = choicestime.Stockindicators.otherindicators.natr
    ItemName = 'natr'
    if Item:
        timerS()
        var3 = av.natrAV(tick, other.apikey) #add settings
        techAPIAV(Item, var3, ItemName)

    Item = choicestime.Stockindicators.otherindicators.adosc
    ItemName = 'adosc'
    if Item:
        timerS()
        var3 = av.adoscAV(tick, other.apikey) #add settings
        techAPIAV(Item, var3, ItemName)

    Item = choicestime.Stockindicators.otherindicators.ht_trendline
    ItemName = 'ht_trendline'
    if Item:
        timerS()
        var3 = av.ht_trendlineAV(tick, other.apikey) #add settings
        techAPIAV(Item, var3, ItemName)

    Item = choicestime.Stockindicators.otherindicators.ht_sine
    ItemName = 'ht_sine'
    if Item:
        timerS()
        var3 = av.ht_sineAV(tick, other.apikey) #add settings
        techAPIAV(Item, var3, ItemName)

    Item = choicestime.Stockindicators.otherindicators.ht_trendmode
    ItemName = 'ht_trendmode'
    if Item:
        timerS()
        var3 = av.ht_trendmodeAV(tick, other.apikey) #add settings
        techAPIAV(Item, var3, ItemName)

    Item = choicestime.Stockindicators.otherindicators.ht_dcperiod
    ItemName = 'ht_dcperiod'
    if Item:
        timerS()
        var3 = av.ht_dcperiodAV(tick, other.apikey) #add settings
        techAPIAV(Item, var3, ItemName)

    Item = choicestime.Stockindicators.otherindicators.ht_dcphase
    ItemName = 'ht_dcphase'
    if Item:
        timerS()
        var3 = av.ht_dcphaseAV(tick, other.apikey) #add settings
        techAPIAV(Item, var3, ItemName)

    Item = choicestime.Stockindicators.otherindicators.ht_phasor
    ItemName = 'ht_phasor'
    if Item:
        timerS()
        var3 = av.ht_phasorAV(tick, other.apikey) #add settings
        techAPIAV(Item, var3, ItemName)


    print(f'Stock Data download for {tick} complete')

def cryptocurrencyAPI():
    csvF = Selections.filetypes.csvF
    jsonF = Selections.filetypes.jsonF
    htmlF = Selections.filetypes.htmlF
    pickledF = Selections.filetypes.pickledF
    tick= Selections.choicecrypto
    tick2 = Selections.crypto.secondcurrency


    if Selections.crypto.firstcurrency== None: #TODO get this value reset with continue()
        print('you need to enter something')
        sys.exit()

    def pandastofile(cmd,name):
        meta, df = cmd

        symbol = Selections.crypto.firstcurrency
        second = Selections.crypto.secondcurrency
        
        if 'Error Message' in df:
            print('whoops there was an error in the api call')
        else:
            if csvF:
                df.to_csv(f'{CryptoDirectory}\\{symbol}\\csv\\{second}_{name}.csv')
            if jsonF:
                df.to_json(f'{CryptoDirectory}\\{symbol}\\json\\{second}_{name}.json')
            if htmlF:
                df.to_html(f'{CryptoDirectory}\\{symbol}\\html\\{second}_{name}.html')
            if pickledF:
                df.to_pickle(f'{CryptoDirectory}\\{symbol}\\pickled\\{second}_{name}.pkl')
            
        print('')
        print(name,'Download complete')


    Item = Selections.crypto.exchangerate
    if Item:
        timerS()
        ItemName = 'exchange'
        var3 = av.currency_exchange_rateAV(Selections.crypto.firstcurrency,Selections.crypto.secondcurrency,other.apikey)#TODO add interval
        pandastofile(var3, ItemName)
    
    Item = Selections.crypto.intraday
    if Item:
        timerS()
        ItemName = 'intraday'
        var3 = av.crypto_intradayAV(Selections.crypto.firstcurrency,Selections.crypto.secondcurrency, other.apikey)
        pandastofile(var3, ItemName)

    Item = Selections.crypto.daily
    if Item:
        timerS()
        ItemName = 'daily'
        var3 = av.digital_currency_dailyAV(Selections.crypto.firstcurrency,Selections.crypto.secondcurrency, other.apikey)
        pandastofile(var3, ItemName)
    
    Item = Selections.crypto.weekly
    if Item:
        timerS()
        ItemName = 'weekly'
        var3 = av.digital_currency_weeklyAV(Selections.crypto.firstcurrency,Selections.crypto.secondcurrency, other.apikey)
        pandastofile(var3, ItemName)

    Item = Selections.crypto.monthly
    if Item:
        timerS()
        ItemName = 'monthly'
        var3 = av.digital_currency_monthlyAV(Selections.crypto.firstcurrency,Selections.crypto.secondcurrency, other.apikey)
        pandastofile(var3, ItemName)

def forexcurrencyAPI():
    csvF = Selections.filetypes.csvF
    jsonF = Selections.filetypes.jsonF
    htmlF = Selections.filetypes.htmlF
    pickledF = Selections.filetypes.pickledF
    tick= Selections.choiceforex
    tick2 = Selections.forex.secondcurrency


    if Selections.forex.firstcurrency== None:
        print('you need to enter something')
        sys.exit()

    def pandastofile(cmd,name):
        meta, df = cmd

        symbol = Selections.forex.firstcurrency
        second = Selections.forex.secondcurrency
        
        if 'Error Message' in df:
            print('whoops there was an error in the api call')
        else:
            if csvF:
                df.to_csv(f'{ForexDirectory}\\{symbol}\\csv\\{second}_{name}.csv')
            if jsonF:
                df.to_json(f'{ForexDirectory}\\{symbol}\\json\\{second}_{name}.json')
            if htmlF:
                df.to_html(f'{ForexDirectory}\\{symbol}\\html\\{second}_{name}.html')
            if pickledF:
                df.to_pickle(f'{ForexDirectory}\\{symbol}\\pickled\\{second}_{name}.pkl')
            
        print('')
        print(name,'Download complete')


    Item = Selections.forex.exchangerate
    if Item:
        timerS()
        ItemName = 'exchange'
        var3 = av.currency_exchange_rateAV(Selections.forex.firstcurrency,Selections.forex.secondcurrency,other.apikey)#TODO add interval
        pandastofile(var3, ItemName)

    Item = Selections.forex.intraday
    if Item:
        timerS()
        ItemName = 'intraday'
        var3 = av.fx_intradayAV(Selections.forex.firstcurrency,Selections.forex.secondcurrency, other.apikey)
        pandastofile(var3, ItemName)

    Item = Selections.forex.daily
    if Item:
        timerS()
        ItemName = 'daily'
        var3 = av.fx_dailyAV(Selections.forex.firstcurrency,Selections.forex.secondcurrency, other.apikey)
        pandastofile(var3, ItemName)
    
    Item = Selections.forex.weekly
    if Item:
        timerS()
        ItemName = 'weekly'
        var3 = av.fx_weeklyAV(Selections.forex.firstcurrency,Selections.forex.secondcurrency, other.apikey)
        pandastofile(var3, ItemName)

    Item = Selections.forex.monthly
    if Item:
        timerS()
        ItemName = 'monthly'
        var3 = av.fx_monthlyAV(Selections.forex.firstcurrency,Selections.forex.secondcurrency, other.apikey)
        pandastofile(var3, ItemName)

def fundamentalsAPI():
    csvF=Selections.filetypes.csvF
    jsonF=Selections.filetypes.jsonF
    htmlF=Selections.filetypes.htmlF
    pickledF=Selections.filetypes.pickledF


    if choicestime.tick== None:
        print('you need to enter something')
        sys.exit()

    def pandastofile(cmd,name):
        ae, qe = cmd

        symbol=choicestime.tick2
        
        if 'Error Message' in qe:
            print('whoops there was an error in the api call')
        elif qe == {}:
            print("This company likely doesn't exist through Alpha Vantage, sorry")
        else:
            if csvF:
                ae.to_csv(f'{FundamentalsDirectory}\\{symbol}\\csv\\annual_{name}.csv')
            if jsonF:
                ae.to_json(f'{FundamentalsDirectory}\\{symbol}\\json\\annual_{name}.json')
            if htmlF:
                ae.to_html(f'{FundamentalsDirectory}\\{symbol}\\html\\annual_{name}.html')
            if pickledF:
                ae.to_pickle(f'{FundamentalsDirectory}\\{symbol}\\pickled\\annual_{name}.pkl')
            if csvF:
                qe.to_csv(f'{FundamentalsDirectory}\\{symbol}\\csv\\quarterly_{name}.csv')
            if jsonF:
                qe.to_json(f'{FundamentalsDirectory}\\{symbol}\\json\\quarterly_{name}.json')
            if htmlF:
                qe.to_html(f'{FundamentalsDirectory}\\{symbol}\\html\\quarterly_{name}.html')
            if pickledF:
                qe.to_pickle(f'{FundamentalsDirectory}\\{symbol}\\pickled\\quarterly_{name}.pkl')
            
            print('')
            print(name,'Download complete')

    def pandastofileSINGLE(cmd,name):
        meta, df = cmd

        if 'Error Message' in meta:
            print('whoops there was an error in the api call')
        elif df == {}:
            print("This company likely doesn't exist through Alpha Vantage, sorry")
        else:
            symbol=choicestime.tick2
            if csvF:
                df.to_csv(f'{FundamentalsDirectory}\\{symbol}\\csv\\{name}.csv')
            if jsonF:
                df.to_json(f'{FundamentalsDirectory}\\{symbol}\\json\\{name}.json')
            if htmlF:
                df.to_html(f'{FundamentalsDirectory}\\{symbol}\\html\\{name}.html')
            if pickledF:
                df.to_pickle(f'{FundamentalsDirectory}\\{symbol}\\pickled\\{name}.pkl')

            print('')
            print(name,'Download complete')
            print(r'{}/5 & {}/500'.format(other.count,other.total))

    


    Item = Selections.Fundamentals.Overview
    if Item:
        timerS()
        ItemName = 'overview'
        var3 = av.overviewAV(choicestime.tick,other.apikey)#TODO add interval
        pandastofileSINGLE(var3, ItemName)

    Item = Selections.Fundamentals.Earnings
    if Item:
        timerS()
        ItemName = 'earnings'
        var3 = av.earningsAV(choicestime.tick,other.apikey)
        pandastofile(var3, ItemName)

    Item = Selections.Fundamentals.IncomeStatement
    if Item:
        timerS()
        ItemName = 'incomestatement'
        var3 = av.income_statementAV(choicestime.tick,other.apikey)
        pandastofile(var3, ItemName)

    Item = Selections.Fundamentals.BalanceSheet
    if Item:
        timerS()
        ItemName = 'balancesheet'
        var3 = av.balance_sheetAV(choicestime.tick,other.apikey)
        pandastofile(var3, ItemName)

    Item = Selections.Fundamentals.CashFlow
    if Item:
        timerS()
        ItemName = 'cashflow'
        var3 = av.cash_flowAV(choicestime.tick,other.apikey)
        pandastofile(var3, ItemName)

if isgodays >=1 :
    other.total = 0
    other.count = 0
elif isgodays<1 and isgoseconds>=60:
    other.total = (VAR['total']) 
    other.count = 0
elif isgodays<1 and isgoseconds<60:
    other.total = (VAR['total']) 
    other.count = (VAR['count'])

JsonUpdateTOTAL(DayLimit=True)

if other.total>=500:
    print('500/500 you are out of API calls for today please come back tomorrow')
    sys.exit()
if other.count>=5:
    print('it has been less than 60 seconds since you last made 5 API calls')
    pause()

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)


APIkey()
ChoiceMode()
SelectionMode()

ChoiceFileTypes()
SelectionFiletype()


# else:
#     print('not implemented')#TODO add in economic option which requires dropdown list instead of entry





def Sequence():
    #STOCKS
    if choicestime.mode.Stocks is True and other.Cont is False:
        EntryboxBasic('stocks')
        print('stocks selected')
        DirectoryCreator('stocks')    
        

        if choicestime.usmarket:
            #Select timeframes
            ChoiceTimeUS() 
            SelectionTimeUS()

            #If intraday EXT is selected give choicestime
            if choicestime.timechoices.IntradayExtHistory:
                ChoiceIntradayExt1()
                SelectionIntradayExt1()
                ChoiceIntradayExt2()
                SelectionIntradayExt2()
            
            #Selectindicators
            ChoiceHighUsageIndicatorsUS()
            SelectionHighUsageIndicatorsUS()
            SelectionOtherIndicatorsUS()
        
        elif choicestime.usmarket == False:
            #Select timeframes
            ChoiceTime() 
            SelectionTime()

            #If intraday EXT is selected give choicestime
            if choicestime.timechoices.IntradayExtHistory:
                ChoiceIntradayExt1()
                SelectionIntradayExt1()
                ChoiceIntradayExt2()
                SelectionIntradayExt2()
            
            #Selectindicators
            ChoiceHighUsageIndicators()
            SelectionHighUsageIndicators()
            SelectionOtherIndicators()
        
        #API calls
        stocksAPI()
        continue2('stocks')

    elif choicestime.mode.Stocks and other.Cont:
        other.Cont = False
        print('stocks still selected')
        DirectoryCreator('stocks')
        
        if choicestime.usmarket:
            #Select timeframes
            ChoiceTimeUS() 
            SelectionTimeUS()

            #If intraday EXT is selected give choicestime
            if choicestime.timechoices.IntradayExtHistory:
                ChoiceIntradayExt1()
                SelectionIntradayExt1()
                ChoiceIntradayExt2()
                SelectionIntradayExt2()
        
            #Selectindicators
            ChoiceHighUsageIndicatorsUS()
            SelectionHighUsageIndicatorsUS()
            SelectionOtherIndicatorsUS()
        
        elif choicestime.usmarket == False:
            #Select timeframes
            ChoiceTime()
            SelectionTime()

            #If intraday EXT is selected give choicestime
            if choicestime.timechoices.IntradayExtHistory:
                ChoiceIntradayExt1()
                SelectionIntradayExt1()
                ChoiceIntradayExt2()
                SelectionIntradayExt2()
        
            #Selectindicators
            ChoiceHighUsageIndicators()
            SelectionHighUsageIndicators()
            SelectionOtherIndicators()



        #API calls
        stocksAPI()
        continue2('stocks')
    
    
    
    #CRYPTO
    if choicestime.mode.Crypto is True and other.Cont is False:
        EntryboxBasic('crypto')
        print('crypto selected')
        DirectoryCreator('crypto')
        #Select Crypto and timeframes
        ChoiceCrypto()
        SelectionCrypto()
        if Selections.crypto.exchangerate or Selections.crypto.intraday or Selections.crypto.daily or Selections.crypto.weekly or Selections.crypto.monthly:
            EntryboxBasic('secondarycrypto')
        cryptocurrencyAPI()
        continue2('crypto') #TODO add in auto clearing of secondary currency value in Continue2 crypto exit
    
    elif choicestime.mode.Crypto and other.Cont:
        print('Crypto still selected')
        DirectoryCreator('crypto')
        ChoiceCrypto()
        SelectionCrypto()
        if Selections.crypto.exchangerate or Selections.crypto.intraday or Selections.crypto.daily or Selections.crypto.weekly or Selections.crypto.monthly:
            EntryboxBasic('secondarycrypto')
        cryptocurrencyAPI()
        continue2('crypto')
    
    
    #FOREX
    if choicestime.mode.Forex is True and other.Cont is False:
        EntryboxBasic('forex')
        print('forex selected')
        DirectoryCreator('forex')
        #TODO add continue
        #Select Crypto and timeframes
        ChoiceForex()
        SelectionForex()
        EntryboxBasic('secondaryforex')
        forexcurrencyAPI()
        continue2('forex')

    elif choicestime.mode.Forex and other.Cont:
        print('Forex still selected')
        DirectoryCreator('forex')
        ChoiceForex()
        SelectionForex()
        EntryboxBasic('secondaryforex')
        forexcurrencyAPI()
        continue2('forex')


    #FUNDAMENTALS
    if choicestime.mode.Fundamentals is True and other.Cont is False:
        EntryboxBasic('fundamentals')
        print('fundamentals selected')
        DirectoryCreator('fundamentals')
        ChoiceFundamentals()
        SelectionFundamentals()
        fundamentalsAPI()
        continue2('fundamentals')

    elif choicestime.mode.Fundamentals and other.Cont:
        print('Fundamentals still selected')
        DirectoryCreator('fundamentals')
        ChoiceFundamentals()
        SelectionFundamentals()
        fundamentalsAPI()
        continue2('fundamentals')

#TODO test crypto and Forex to make sure they function properly and then add Fundamentals and Economic options

Sequence()
# %%
