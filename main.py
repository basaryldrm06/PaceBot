from binance.client import Client
from binanceAPI.position_utilities import enter_long, enter_short
from config import api_key, secret_key
from data.io_utilities import print_with_color, calculateWR, print_position_message
from time import sleep
from data.data_functions import save_position, save_result
import copy

# Binance API initialization
client = Client(api_key, secret_key)
