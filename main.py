from binance.client import Client
from binanceAPI.position_utilities import enter_long, enter_short
from config import api_key, secret_key
from data.io_utilities import print_with_color, calculateWR, print_position_message
from time import sleep
from data.data_functions import save_position, save_result
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
# Global Functions

print_with_color("cyan", "PaceBot is running...")

while True:
    try:
        sleep(10)
        price = fetch_price(client)

        if not (on_long or on_short):
            if state == 0 or state == 1:
                tp_price, sl_price = enter_long(client)
                on_long = True
                print_with_color("yellow", "Entered LONG Current: " + 
                    str(round(price, 2)) + " TP_PRICE: " + str(round(tp_price, 2)) + 
                    " SL_PRICE: " + str(round(sl_price, 2)))
            elif state == 2 or state == 3:
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