from faker import Faker
from collections import namedtuple
import random

NUM_COMPANIES = 100
Stock = namedtuple("Stock", "name, symbol, open, high, close")
StockExt = namedtuple("StockExt", Stock._fields + ("weight"))

def create_stock_market():
    weights = get_random_weights(NUM_COMPANIES)
    for weight in weights:
        pass

def get_random_weights(num):
    random_list = [random.random() for i in range(num)]
    sum_random_list = sum(random_list)
    random_list = [num / sum_random_list for num in random_list]
    return random_list