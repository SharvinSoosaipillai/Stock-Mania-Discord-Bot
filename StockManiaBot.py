#importing different modules 
import discord
from discord.ext import commands
from aiohttp import request 
from parttwo import *
import os
import datetime


    
#creating variable for the client
client = commands.Bot(command_prefix = '-')

#variables 
Token = os.getenv("Tokken")
api_key = os.getenv("API_KEY")
positive_increase = 'https://www.nicepng.com/png/detail/19-195680_graph-clipart-arrow-png-stocks-going-up-png.png'
negative_increase = 'https://www.pngimages.pics/images/quotes/english/general/trending-down-arrow-decrease-png-52650-222775.png'
no_change = 'https://marcellusdrilling.com/wp-content/uploads/2018/07/no-rate-increase.png'
notes = []


#Events
@client.event

async def on_ready():

    await client.change_presence(activity= discord.Game ("The Market"))



@client.command()

async def status(ctx):

    await ctx.send("Stock Mania is online and is playing the market")


@client.command()

async def yesterdaystockinfo(ctx, *, stock):

    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=' + stock +"&apikey="+ api_key

    async with request ("GET" , url) as response:
        api_page = await response.json()

        tod = datetime.datetime.now().date()
        d = datetime.timedelta(days = 0)
        a = str(tod - d)

        current_day = api_page['Time Series (Daily)']

        if a in current_day:
            
            currentt_day = (current_day[a])
            open = currentt_day['1. open']
            open_value = round(float(open),2)
            high = currentt_day['2. high']
            high_value = round(float(high),2)
            low = currentt_day['3. low']
            low_value = round(float(low),2)
            close = currentt_day['4. close']
            close_value = round(float(close),2)
            volume = currentt_day['5. volume']
            value_change = round((float(close) - float(open)), 2)
            percent_change = round(((value_change/float(open)) *100) , 2)
            real_percent_value_change = str(percent_change) + '%' 

        else:

            day = 1

            while True:
                
                tod1 = datetime.datetime.now().date()
                d1 = datetime.timedelta(days = day)
                a1 = str(tod1 - d1)
                
                if a1 in current_day:
                    currentt_day = (current_day[a1])
                    open = currentt_day['1. open']
                    open_value = round(float(open),2)
                    high = currentt_day['2. high']
                    high_value = round(float(high),2)
                    low = currentt_day['3. low']
                    low_value = round(float(low),2)
                    close = currentt_day['4. close']
                    close_value = round(float(close),2)
                    volume = currentt_day['5. volume']
                    value_change = round((float(close) - float(open)), 2)
                    percent_change = round(((value_change/float(open)) *100) , 2)
                    real_percent_value_change = str(percent_change) + '%' 
                
                    break
                
                else:
                
                    day += 1

    info = yfinanceinfoo(stock)

    business_summary = (info["longBusinessSummary"])
    logo = (info['logo_url'])
    real_summary = ""
    for i in range(4):
        period = business_summary.find(".")
        sentence = (business_summary[0:period + 1])
        real_summary += (sentence)
        business_summary = business_summary.replace(business_summary[0:period + 1], '')
    market_cap = (info["marketCap"])


    yeasterdaystock_embed = discord.Embed(title = stock +" Stock Info", description = real_summary, colour = discord.Colour.blue())
    yeasterdaystock_embed.add_field(name = "Open ($)", value = open_value, inline = True)
    yeasterdaystock_embed.add_field(name = "High ($)", value = high_value, inline = True)
    yeasterdaystock_embed.add_field(name = "Low ($)", value = low_value, inline = True)
    yeasterdaystock_embed.add_field(name = "Close ($)", value = close_value, inline = True)
    yeasterdaystock_embed.add_field(name = "Volume", value = volume, inline = True)
    yeasterdaystock_embed.add_field(name = "Market Cap ($)", value = market_cap, inline = True)
    yeasterdaystock_embed.add_field(name = "Value Change\n(From most Recent Close) ($)", value = value_change, inline = True)
    yeasterdaystock_embed.add_field(name = "Percent Change\n(From most Recent Close) (%)", value = real_percent_value_change , inline = True)
    yeasterdaystock_embed.set_thumbnail(url = logo)


    if float(close) > float(open):
        yeasterdaystock_embed.set_image(url = positive_increase)
    elif float(open) > float(close):
        yeasterdaystock_embed.set_image(url = negative_increase)
    elif float(open) == float(close):
        yeasterdaystock_embed.set_image(url = no_change)


    await ctx.send(embed = yeasterdaystock_embed)




@client.command()

async def weeklystockinfo(ctx, *, stock):

    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol=' + stock +"&apikey="+ api_key

    async with request ("GET" , url) as response:

        api_page = await response.json()

        tod = datetime.datetime.now().date()
        d = datetime.timedelta(days = 0)
        a = str(tod - d)

        current_day = api_page['Weekly Time Series']


        if a in current_day:

            currentt_day = (current_day[a])
            open = currentt_day['1. open']
            open_value = round(float(open),2)
            high = currentt_day['2. high']
            high_value = round(float(high),2)
            low = currentt_day['3. low']
            low_value = round(float(low),2)
            close = currentt_day['4. close']
            close_value = round(float(close),2)
            volume = currentt_day['5. volume']
            value_change = round((float(close) - float(open)), 2)
            percent_change = round(((value_change/float(open)) *100) , 2)
            real_percent_value_change = str(percent_change) + '%' 

        else:

            day = 1

            while True:

                tod1 = datetime.datetime.now().date()
                d1 = datetime.timedelta(days = day)
                a1 = str(tod1 - d1)

                if a1 in current_day:
                    currentt_day = (current_day[a1])
                    open = currentt_day['1. open']
                    open_value = round(float(open),2)
                    high = currentt_day['2. high']
                    high_value = round(float(high),2)
                    low = currentt_day['3. low']
                    low_value = round(float(low),2)
                    close = currentt_day['4. close']
                    close_value = round(float(close),2)
                    volume = currentt_day['5. volume']
                    value_change = round((float(close) - float(open)), 2)
                    percent_change = round(((value_change/float(open)) *100) , 2)
                    real_percent_value_change = str(percent_change) + '%' 
                    break

                else:

                    day += 1


    info = yfinanceinfoo(stock)

    business_summary = str(info["longBusinessSummary"])
    real_summary = ""

    for i in range(4):

        period = business_summary.find(".")
        sentence = (business_summary[0:period + 1])
        real_summary += (sentence)
        business_summary = business_summary.replace(business_summary[0:period + 1], '')


    logo = (info['logo_url'])
    market_cap = (info["marketCap"])

    Weeklystock_embed = discord.Embed(title = str(stock) +" Stock Info", description = real_summary, colour = discord.Colour.blue())
    Weeklystock_embed.add_field(name = "Open ($)", value = open_value, inline = True)
    Weeklystock_embed.add_field(name = "High ($)", value = high_value, inline = True)
    Weeklystock_embed.add_field(name = "Low ($)", value = low_value, inline = True)
    Weeklystock_embed.add_field(name = "Close ($)", value = close_value, inline = True)
    Weeklystock_embed.add_field(name = "Volume", value = volume, inline = True)
    Weeklystock_embed.add_field(name = "Market Cap ($)", value = market_cap, inline = True)    
    Weeklystock_embed.add_field(name = "Value Change \n(From most Recent Close) ($)", value = value_change, inline = True)
    Weeklystock_embed.add_field(name = "Percent Change \n(From most Recent Close) (%)", value = real_percent_value_change , inline = True)
    Weeklystock_embed.set_thumbnail(url = logo)

    if float(close) > float(open):
        Weeklystock_embed.set_image(url = positive_increase)
    
    elif float(open) > float(close):
        Weeklystock_embed.set_image(url = negative_increase)
    
    elif float(open) == float(close):
        Weeklystock_embed.set_image(url = no_change)


    await ctx.send(embed = Weeklystock_embed)




@client.command()

async def monthlystockinfo(ctx, *, stock):

    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=' + stock +"&apikey="+ api_key

    async with request ("GET" , url) as response:

        api_page = await response.json()

        tod = datetime.datetime.now().date()
        d = datetime.timedelta(days = 0)
        a = str(tod - d)

        current_day = api_page['Monthly Time Series']


        if a in current_day:

            currentt_day = (current_day[a])
            open = currentt_day['1. open']
            open_value = round(float(open),2)
            high = currentt_day['2. high']
            high_value = round(float(high),2)
            low = currentt_day['3. low']
            low_value = round(float(low),2)
            close = currentt_day['4. close']
            close_value = round(float(close),2)
            volume = currentt_day['5. volume']
            value_change = round((float(close) - float(open)), 2)
            percent_change = round(((value_change/float(open)) *100) , 2)
            real_percent_value_change = str(percent_change) + '%' 

        else:
            day = 1
    
            while True:
    
                tod1 = datetime.datetime.now().date()
                d1 = datetime.timedelta(days = day)
                a1 = str(tod1 - d1)

                if a1 in current_day:
                    currentt_day = (current_day[a1])
                    open = currentt_day['1. open']
                    open_value = round(float(open),2)
                    high = currentt_day['2. high']
                    high_value = round(float(high),2)
                    low = currentt_day['3. low']
                    low_value = round(float(low),2)
                    close = currentt_day['4. close']
                    close_value = round(float(close),2)
                    volume = currentt_day['5. volume']
                    value_change = round((float(close) - float(open)), 2)
                    percent_change = round(((value_change/float(open)) *100) , 2)
                    real_percent_value_change = str(percent_change) + '%' 
                    break
    
                else:
                    day += 1


    info = yfinanceinfoo(stock)

    business_summary = (info["longBusinessSummary"])
    logo = (info['logo_url'])
    real_summary = ""
    
    for i in range(4):
        period = business_summary.find(".")
        sentence = (business_summary[0:period + 1])
        real_summary += (sentence)
        business_summary = business_summary.replace(business_summary[0:period + 1], '')

    market_cap = (info["marketCap"])

    Monthlystock_embed = discord.Embed(title = stock +" Stock Info", description = real_summary, colour = discord.Colour.blue())
    Monthlystock_embed.add_field(name = "Open ($)", value = open_value, inline = True)
    Monthlystock_embed.add_field(name = "High ($)", value = high_value, inline = True)
    Monthlystock_embed.add_field(name = "Low ($)", value = low_value, inline = True)
    Monthlystock_embed.add_field(name = "Close ($)", value = close_value, inline = True)
    Monthlystock_embed.add_field(name = "Volume", value = volume, inline = True)
    Monthlystock_embed.add_field(name = "Market Cap ($)", value = market_cap, inline = True)
    Monthlystock_embed.add_field(name = "Value Change \n(From most Recent Close) ($)", value = value_change, inline = True)
    Monthlystock_embed.add_field(name = "Percent Change \n(From most Recent Close) (%)", value = real_percent_value_change , inline = True)
    Monthlystock_embed.set_thumbnail(url = logo)


    if float(close) > float(open):
        Monthlystock_embed.set_image(url = positive_increase)
    
    elif float(open) > float(close):
        Monthlystock_embed.set_image(url = negative_increase)
    
    elif float(open) == float(close):
        Monthlystock_embed.set_image(url = no_change)


    await ctx.send(embed = Monthlystock_embed)


@client.command()
async def yearlystockinfo(ctx, *, stock):
    
    info = yfinanceinfoo(stock)
    business_summary = (info["longBusinessSummary"])
    logo = (info['logo_url'])
    
    real_summary = ""

    for i in range(4):
        period = business_summary.find(".")
        sentence = (business_summary[0:period + 1])
        real_summary += (sentence)
        business_summary = business_summary.replace(business_summary[0:period + 1], '')

    current_price = (info["currentPrice"])
    previous_close = (info["previousClose"]) 
    yearhigh = (info["fiftyTwoWeekHigh"]) 
    yearlow = (info["fiftyTwoWeekLow"]) 
    averagevol = (info["regularMarketVolume"]) 
    twohundreddayavg = (info["twoHundredDayAverage"]) 
    value_change = round((float(previous_close) - float(current_price)), 2)
    percent_change = round(((value_change/float(current_price)) *100) , 2)
    real_percent_value_change = str(percent_change) + '%' 

    yearlystock_embed = discord.Embed(title = stock +" Stock Info", description = real_summary, colour = discord.Colour.blue())
    yearlystock_embed.add_field(name = "Current Price  ($)", value = current_price, inline = True)
    yearlystock_embed.add_field(name = "52 Week High ($)", value = yearhigh, inline = True)
    yearlystock_embed.add_field(name = "52 Week Low ($)", value = yearlow, inline = True)
    yearlystock_embed.add_field(name = "Previous Close", value = previous_close, inline = True)
    yearlystock_embed.add_field(name = "Average Volume", value = averagevol, inline = True)
    yearlystock_embed.add_field(name = "Two Hundred Day Average", value = twohundreddayavg, inline = True)
    yearlystock_embed.add_field(name = "Value Change \n(From most Recent Close)", value = value_change, inline = True)
    yearlystock_embed.add_field(name = "Percent Change \n(From most Recent Close)", value = real_percent_value_change , inline = True)
    yearlystock_embed.set_thumbnail(url = logo)


    if float(current_price) > float(previous_close):
        yearlystock_embed.set_image(url = positive_increase)
    
    elif float(previous_close) > float(current_price):
        yearlystock_embed.set_image(url = negative_increase)
    
    elif float(current_price) == float(previous_close):
        yearlystock_embed.set_image(url = no_change)

    await ctx.send(embed = yearlystock_embed)

@client.command()

async def stock(ctx, *, stock):
    
    info = yfinanceinfoo(stock)
    business_summary = (info["longBusinessSummary"])
    logo = (info['logo_url'])
    real_summary = ""

    for i in range(4):
        period = business_summary.find(".")
        sentence = (business_summary[0:period + 1])
        real_summary += (sentence)
        business_summary = business_summary.replace(business_summary[0:period + 1], '')

    current_price = (info["currentPrice"])
    day_high = (info["dayHigh"])
    day_low = (info["dayLow"])
    Volume = (info["volume"])
    previous_close = (info["previousClose"])
    market_cap = (info["marketCap"])

    value_change = round((float(current_price) - float(previous_close)), 2)
    percent_change = round(((value_change/float(current_price)) *100) , 2)
    real_percent_value_change = str(percent_change) + '%' 

    stock_embed = discord.Embed(title = stock, description = real_summary, colour = discord.Colour.blue())
    stock_embed.add_field(name = "Current Price", value = current_price, inline = True)
    stock_embed.add_field(name = "Day High", value = day_high, inline = True)
    stock_embed.add_field(name = "Day Low", value = day_low, inline = True)
    stock_embed.add_field(name = "Previous Close", value = previous_close, inline = True)
    stock_embed.add_field(name = "Volume", value = Volume, inline = True)
    stock_embed.add_field(name = "Market Cap", value = market_cap, inline = True)
    stock_embed.add_field(name = "Value Change ", value = value_change, inline = True)
    stock_embed.add_field(name = "Percent Change ", value = real_percent_value_change , inline = True)
    stock_embed.set_thumbnail(url = logo)

    if float(current_price) > float(previous_close):
        stock_embed.set_image(url = positive_increase)

    elif float(previous_close) > float(current_price):
        stock_embed.set_image(url = negative_increase)

    elif float(current_price) == float(previous_close):
        stock_embed.set_image(url = no_change)


    await ctx.send(embed = stock_embed)



@client.command()

async def timePST (ctx):

    psttime = pacific()
    await ctx.send(psttime)

@client.command()

async def timeEST (ctx):

    datec = datetime.now()
    time = ('Current date & time is: '+ datec)
    await ctx.send(time)

@client.command()

async def timeUK (ctx):

    uktime = London()
    await ctx.send(uktime)

@client.command()

async def timeJST (ctx):

    japan_time = japan()

    await ctx.send(japan_time)


@client.command()

async def timeAUST (ctx):

    australia_time = australia()
    await ctx.send(australia_time)

@client.command()

async def timeCNT (ctx):

    central_time = central()
    await ctx.send(central_time)


@client.command()

async def addnote(ctx, *, info):

    notes.append(info)
    await ctx.send("Note Recieved")


@client.command()

async def shownotes(ctx):
    
    string = ""
    for i in range(len(notes)):
        string += notes[i] + "\n "

    notes_embed = discord.Embed(title = "Notes", description = string, colour = discord.Colour.blue())
    await ctx.send(embed = notes_embed)



@client.command()

async def commands(context):

    commands_embed = discord.Embed(title = "Stock Mania Commands", description = "List of updated commands for the MilkyWay bot", colour = discord.Colour.blue())
    commands_embed.add_field(name = "-status", value = "Tells the user if Stock Mania is online", inline = False)
    commands_embed.add_field(name = "-stock (Ticker symbol)", value = "Tells the current information about the stock", inline = False)
    commands_embed.add_field(name = "-yeasterdaystockinfo (tickersymbol)", value = "tells the yeasterday information about the stock", inline = False)
    commands_embed.add_field(name = "-weeklystockinfo (ticker Symbol)", value = "Tells all of the information about the stock over the current week", inline = False)
    commands_embed.add_field(name = "-monthlystockinfo (ticker Symbol)", value = "Tells all of the information about the stock over the current Month", inline = False)
    commands_embed.add_field(name = "-yearlystockinfo (ticker Symbol)", value = "Tells all of the information about the stock over the current year", inline = False)
    commands_embed.add_field(name = "-timePST", value = "Tells the pacific standard time", inline = False)
    commands_embed.add_field(name = "-timeEST", value = "Tells the eastern standard time", inline = False)
    commands_embed.add_field(name = "-timeCNT", value = "Tells both central standard times", inline = False)
    commands_embed.add_field(name = "-timeJST", value = "Tells Japan standard time", inline = False)
    commands_embed.add_field(name = "-timeAEST", value = "Tells Australian standard time", inline = False)
    commands_embed.add_field(name = "-timeUK", value = "Tells British standard time", inline = False)
    commands_embed.add_field(name = "-addnote", value = "Adds notes to be taken down", inline = False)
    commands_embed.add_field(name = "-shownotes", value = "Shows all of the notes taken since the bot was online", inline = False)
    commands_embed.add_field(name = "-commands", value = "Returns list of all commands", inline = False)

    await context.send(embed = commands_embed)




#runs the client
client.run(Token)