from binance.client import Client
from binanceAPI.position_utilities import enter_long, enter_short
from config import api_key, secret_key
from indicators.price import fetch_price
from indicators.rsi import fetch_RSI
from data.io_utilities import print_with_color, calculateWR, get_current_date_string
from time import sleep
from data.data_functions import save_result
import copy

# Binance API initialization
client = Client(api_key, secret_key)

# Global Variable Declarations
price = 0
state = 0
on_long = False
on_short = False
tp_price = 0
sl_price = 0
tp_count = 0
sl_count = 0
csv_path_result = "./data/pacebot_result.csv"
date = ""

# Global Functions
def close_position(isTP):
    global on_long
    global on_short
    global tp_count
    global sl_count 
    global csv_path_result
    global date

    position = ""

    if (on_long and isTP) or (on_short and (not isTP)): 
        position = "LONG"
    elif (on_long and (not isTP)) or (on_short and isTP):
        position = "SHORT"

    save_result(csv_path_result, date, position, "LONG" if on_long else "SHORT")

    if on_long and isTP:
        state = state + 1 if (state != 3) else 3
    elif on_long and (not isTP):
        state = state - 1
    elif on_short and isTP:
        state = state - 1 if (state != 0) else 0
    elif on_short and (not isTP):
        state = state + 1

    on_long = False
    on_short = False

    if isTP:
        tp_count = tp_count + 1
        print_with_color("green", "Position closed with TP")
        print_with_color("yellow", "TP: " + str(tp_count) + " SL: " + 
              str(sl_count) + " Win-Rate: " + calculateWR(tp_count, sl_count))
    else:
        sl_count = sl_count + 1
        print_with_color("red", "Position closed with SL")
        print_with_color("yellow", "TP: " + str(tp_count) + " SL: " + 
            str(sl_count) + " Win-Rate: " + calculateWR(tp_count, sl_count))

print_with_color("cyan", "PaceBot is running...")

# Initialization
rsi = fetch_RSI(client, "ETHUSDT", 6, "15m")
if (rsi > 50):
    state = 2
else:
    state = 1

while True:
    try:
        sleep(10)
        price = fetch_price(client, "ETHUSDT")

        if not (on_long or on_short):
            print()
            date = get_current_date_string()
            if state == 2 or state == 3:
                tp_price, sl_price = enter_long(client)
                on_long = True
                print_with_color("yellow", "Entered LONG Current: " + 
                    str(round(price, 2)) + " TP_PRICE: " + str(round(tp_price, 2)) + 
                    " SL_PRICE: " + str(round(sl_price, 2)))
            elif state == 0 or state == 1:
                tp_price, sl_price = enter_short(client)
                on_short = True
                print_with_color("yellow", "Entered SHORT Current: " + 
                    str(round(price, 2)) + " TP_PRICE: " + str(round(tp_price, 2)) + 
                    " SL_PRICE: " + str(round(sl_price, 2)))

        else:
            if (on_long and price > tp_price) or \
                (on_short and price < tp_price):
                close_position(True)
            elif (on_long and price < sl_price) or \
                (on_short and price > sl_price):
                close_position(False)

    except Exception as e:
        error_message = str(e)
        print_with_color("yellow", error_message)