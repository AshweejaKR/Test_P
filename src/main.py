import json as js
import pandas as pd
import logging as log
import datetime as dt
import time as tm
import logging
from alice_blue import *
from openpyxl import Workbook
from openpyxl.styles import Alignment
import math
import statistics
from statistics import mean

# =============================================================================
# ========================== GLOBAL VARIABLES =================================
global APP_ID
global API_SECRET
global LTP
global SOCKET_OPENED
global USERNAME
global PASSWORD
global TWOFA
global RMPT
global RMTC
global LIST
global DEBUG
global OBJ
global EMA_CROSS_SCRIP
global BALANCE

# =============================================================================
# =============================================================================
def Init_config():
    global APP_ID
    global API_SECRET
    global USERNAME
    global PASSWORD
    global TWOFA
    global EMA_CROSS_SCRIP
    
    # Config
    USERNAME = 'username'
    PASSWORD = 'password'
    
    API_SECRET = 'api secret'
    APP_ID = 'app id'
    TWOFA = '1994'
    
    EMA_CROSS_SCRIP = 'SBIN'
   # logging.basicConfig(level=logging.DEBUG)        # Optional for getting debug messages.
    # Config

# =============================================================================
# =============================================================================
LIST = []
DEBUG = 0
BALANCE = 0.0
LTP = 0.0

#Add Yours Stock Name here
EMA_CROSS_SCRIP = 'INFY'

# =============================================================================
# =============================================================================

# =============================================================================
# ======================== Reading From JSON ==================================
def load_excel():
    global RMPT
    global RMTC
    global LIST
    
    print('load_excel() ....')
    
    xlfile = '../equity-spot.xlsx'
    df = pd.read_excel(xlfile, index_col=0, nrows=25)

    '''
    print(df['scrip'])

    for i in df['scrip']:
        print(i)  
    ''
    #temporarily commented
    xl_file = "..\Test_data.xlsx"
    excel_data = pd.read_excel(xl_file , index_col=None, header=None)
    #print(excel_data)
    
    RMPT = excel_data[7][2]
    RMTC = excel_data[7][3]
    
    print('R1: ', RMPT * 100, '%')
    print('R2: ', RMTC * 100, '%')

    for i in range(3, len(excel_data[1])):
        if(excel_data[3][i] == 1):
            print(i, ": ", excel_data[1][i])
            LIST.append(excel_data[1][i])
   '''
# =============================================================================
# ======================== Reading From JSON ==================================
def load_api():
    global APP_ID
    global API_SECRET
    global USERNAME
    global PASSWORD
    global TWOFA
    
    print('load_api() ....')
    with open("api_data.json") as f:
        j = js.load(f)
        f.close()
        APP_ID = j["APP_ID"]
        API_SECRET = j["API_SECRET"]
        USERNAME = j["USERNAME"]
        PASSWORD = j["PASSWORD"]
        TWOFA = j["TWOFA"]
        #print("APP_ID: ", APP_ID)
        #print("API_SECRET: ", API_SECRET)
        #print("USERNAME: ", USERNAME)
        #print("PASSWORD: ", PASSWORD)
        #print("TWOFA: ", TWOFA)
    
    
# =============================================================================
# =============================================================================
def login(_app_id, _api_secret, _username, _password, _twofa):
    print("login() ...")
    print("loging in ...")
    obj = "NA"
    #print('APP_ID: ', _app_id, '\nAPI_SECRET: ', _api_secret, '\nUSERNAME: ', _username, '\nPASSWORD: ', _password, '\nTWOFA: ', _twofa, '\n')
    try: 
        access_token =  AliceBlue.login_and_get_access_token(username = _username, password = _password, twoFA = _twofa,  api_secret = _api_secret, app_id = APP_ID)
        print('access_token: ', access_token, '\n\n\n')
        obj = AliceBlue(username = _username, password = _password, access_token = access_token, master_contracts_to_download = ['NSE'])    
        print("Login Successfull ...")
    except Exception as err:
        if(DEBUG):
            print(err)
        print("Login Failed ...")
        print("Check API SECRET or PASSWORD")
    
    #print(obj.get_profile()) # get profile
    #print("##Bal: ", obj.get_balance())
    #print("\n\nlogin done ...") 
    #print("Login Successfull ...")
    return obj
        
# =============================================================================
# =============================================================================     
def logout(obj):
    print("logout() ...")
    
# =============================================================================
# =============================================================================
def place_buy_order(ins_scrip, qty = 1):
    print("place_buy_order() ...")
    global OBJ
    global LTP
    sl = LTP - 2.5
    tls = 1
    bal = OBJ.get_balance()
    #print("Before Buy Bal: ", bal)
    OBJ.place_order(transaction_type = TransactionType.Buy,
                         instrument = ins_scrip,
                         quantity = qty,
                         order_type = OrderType.Market,
                         product_type = ProductType.Intraday,
                         price = 0.0,
                         trigger_price = None,
                         stop_loss = None,
                         square_off = None,
                         trailing_sl = None,
                         is_amo = False)
    bal = OBJ.get_balance()
    #print("After Buy Bal: ", bal)
# =============================================================================
# =============================================================================     
def place_sell_order(ins_scrip, qty = 1):
    print("place_sell_order() ...")
    global OBJ
    global LTP
    sl = LTP + 2.5
    tsl = 1
    bal = OBJ.get_balance()
    #print("Before Sell Bal: ", bal)
    OBJ.place_order(transaction_type = TransactionType.Sell,
                         instrument = ins_scrip,
                         quantity = qty,
                         order_type = OrderType.Market,
                         product_type = ProductType.Intraday,
                         price = 0.0,
                         trigger_price = None,
                         stop_loss = None,
                         square_off = None,
                         trailing_sl = None,
                         is_amo = False)
    bal = OBJ.get_balance()
    #print("After Sell Bal: ", bal)
                         
# =============================================================================
# =============================================================================  
def gen_report():
    print("gen_report() ...")
    

# =============================================================================
# =============================================================================
def event_handler_quote_update(tick):
    #print('event_handler_quote_update() ....')
    global LTP
    LTP = tick['ltp']
    #print("LTP: ", LTP, "\n")
    
# =============================================================================
# =============================================================================
def open_callback():
    print('open_callback() ....')
    global SOCKET_OPENED
    SOCKET_OPENED = True
    
# =============================================================================
# =============================== MAIN ========================================
def main():
    global APP_ID
    global API_SECRET
    global LTP
    global SOCKET_OPENED
    global USERNAME
    global PASSWORD
    global TWOFA
    global RMPT
    global RMTC
    global LIST
    global OBJ
    global DEBUG
    global EMA_CROSS_SCRIP
    global BALANCE

    DEBUG = 0
    LTP = 1565.00
    print("main() ....")
    
    if(DEBUG):
        Init_config() #for debug & test taking login credentials
    else:
        load_api()
        load_excel()
        
    OBJ = login(APP_ID, API_SECRET, USERNAME, PASSWORD, TWOFA)

    if(OBJ == "NA"):
        print("ERROR")
        exit(-1)
        
    data = OBJ.get_balance()
    bal = data['data']['cash_positions'][0]['net']
    BALANCE = float(bal)
    mis_multiplier = 4.5

    print('My Balance: ',  BALANCE)
    Qty = math.floor((BALANCE / LTP) * mis_multiplier)
    print("INFY QTY: ", Qty)
    
    ins_scrip = OBJ.get_instrument_by_symbol('NSE', EMA_CROSS_SCRIP)
    
    SOCKET_OPENED = False
    OBJ.start_websocket(subscribe_callback = event_handler_quote_update,
                        socket_open_callback = open_callback,   
                        run_in_background = True)
                          
    OBJ.subscribe(ins_scrip, LiveFeedType.MARKET_DATA)
    
    #place_buy_order(ins_scrip)
    #place_sell_order(ins_scrip)
# =============================================================================
# =============================================================================
# =============================================================================    
# --------------------- Test Strategy MA Crossover 15 & 9 SMA -----------------
    current_signal = ''
    #Just Debug
    #LTP = 5555555.555555
    #print("LTP: ", LTP)
    minute_close = []
    print("Start of Strategy ...")
    while True:
        if(dt.datetime.now().second == 0):
            minute_close.append(LTP)
            print("Min Close: ", minute_close)
            print('Balance: ',  BALANCE, "\n")
            
            data = OBJ.get_balance()
            bal = data['data']['cash_positions'][0]['net']
            BALANCE = float(bal)

            if(len(minute_close) > 16):
                sma_s = statistics.mean(minute_close[-9:])
                sma_l = statistics.mean(minute_close[-15:])
                #square_off buy order
                if(current_signal == 'buy'):
                    if(sma_s < sma_l):
                        place_sell_order(ins_scrip, Qty)
                        tm.sleep(0.2)
                        current_signal = '' 

                #square_off sell order 
                if(current_signal == 'sell'):
                    if(sma_s > sma_l):
                        place_buy_order(ins_scrip, Qty)
                        current_signal = ''
                        tm.sleep(0.2)

                if(current_signal != 'buy'):
                    if(sma_s > sma_l):
                        Qty = math.floor((BALANCE / LTP) * mis_multiplier)
                        print(Qty)
                        if(Qty >= 1):
                            place_buy_order(ins_scrip, Qty)
                            current_signal = 'buy'
                            tm.sleep(0.2)
                        else:
                            print("Insufficient Fund")
                
                if(current_signal != 'sell'):
                    if(sma_s < sma_l):
                        Qty = math.floor((BALANCE / LTP) * mis_multiplier)
                        print(Qty)
                        if(Qty >= 1):
                            place_sell_order(ins_scrip, Qty)
                            current_signal = 'sell'
                            tm.sleep(0.2)
                        else:
                            print("Insufficient Fund")      
            tm.sleep(1)
        tm.sleep(0.2)  # sleep for 200ms
# =============================================================================
# =============================================================================
# =============================================================================
    #place_buy_order(ins_scrip)
    #place_sell_order(ins_scrip)
    logout(OBJ)
    gen_report()
    print('LIST: ',  LIST)

# =============================================================================
# =============================== START =======================================
if __name__ == "__main__":
    print("starting ....")
    main()   
    print("Done ... ")
