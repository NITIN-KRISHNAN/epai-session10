import Stock
from collections import namedtuple

def test_weights_add_to_one():
    assert round(sum(Stock.get_random_weights(Stock.NUM_COMPANIES))) == 1

def test_random_stock():
    stock = Stock.get_random_stock()
    assert stock.open >= 100 and stock.open < 10000
    assert stock.high >= stock.low
    assert stock.close >= stock.low and stock.close <= stock.high


def test_index():
    stock = Stock.calculate_index(Stock.create_stock_market())
    assert stock.high >= stock.low
    assert stock.close >= stock.low and stock.close <= stock.high


def test_index_calculation():
    StockMarketExt = namedtuple("StockMarket", list(range(2)), rename=True)
    stock_market = StockMarketExt(*(Stock.StockExt('Rodriguez','Rod2' , 1372,1418,  1248, 1257, 0.36),
                                       Stock.StockExt('Freeman', 'Fre41', 7391, 8694, 7213, 7293, 0.64)))
    index = Stock.calculate_index(stock_market)
    assert index.high == (1418*.36 + 8694*.64) and index.open == (1372*.36 + 7391*.64) and index.low == (1248*.36 + 7213*.64) and index.close == (1257*.36 + 7293*.64)

