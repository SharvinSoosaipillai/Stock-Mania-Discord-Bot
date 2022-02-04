from aiohttp import request
import yfinance as yf
import datetime
from datetime import datetime
from pytz import timezone
import pytz


def yfinanceinfoo (tickersymbol):
    tickerdata = yf.Ticker(tickersymbol)
    tickerinfo = tickerdata.info
    return (tickerinfo)

def pacific():

    date_format='%m/%d/%Y %H:%M:%S %Z'
    date = datetime.now(tz=pytz.utc)

    date = date.astimezone(timezone('US/Pacific'))
    time = ('Current date & time is: '+ date.strftime(date_format))
    return time


def eastern():
    datec = datetime.now()
    time = ('Current date & time is: '+ datec)
    return time

def London():
    date_format='%m/%d/%Y %H:%M:%S %Z'
    date = datetime.now(tz=pytz.utc)
    date = date.astimezone(timezone('Europe/London'))

    time = ('Current date & time is: '+ date.strftime(date_format))
    print (pytz.all_timezones)
    return time

def japan():
    date_format='%m/%d/%Y %H:%M:%S %Z'
    date = datetime.now(tz=pytz.utc)
    date = date.astimezone(timezone('Japan'))

    time = ('Current date & time is: '+ date.strftime(date_format))
    return time


def australia():
    date_format='%m/%d/%Y %H:%M:%S %Z'
    date = datetime.now(tz=pytz.utc)
    date = date.astimezone(timezone('Australia/Sydney'))

    time = ('Current date & time is: '+ date.strftime(date_format))
    print (pytz.all_timezones)
    return time


def central():
    date_format='%m/%d/%Y %H:%M:%S %Z'
    date = datetime.now(tz=pytz.utc)
    date = date.astimezone(timezone('Canada/Central'))

    time = ('Current date & time is: '+ date.strftime(date_format))
    print (pytz.all_timezones)
    return time
