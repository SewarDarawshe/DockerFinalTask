from flask import Flask, render_template, request
import requests

app = Flask(__name__)



# this function extracts and returns the current bitcoin price in USD based on real time data

def api_callNow():
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    response = (requests.get(url))
    data = response.json()
    price = data['bpi']['USD']['rate']
    return str(price)+" USD"


# this function extracts Bitcoin price in the last 10 min in USD based on real time data
# then calculates and returns the priceAvg .
def api_callAvg():
    url = "https://min-api.cryptocompare.com/data/v2/histominute?fsym=BTC&tsym=USD&limit=10"
    response = (requests.get(url))
    data = response.json()
    #saving the historical price change for the last 10 min
    history =[]
    for i in range(10):
        price = data['Data']["Data"][i]['close']
        history.append(price)

#calculating avg
    average = sum(history) / len(history)
    return  " avg of:   "+str(average)+" USD"





@app.route('/')
def index_post_route():
    return render_template('html.html',
                           messageNow=api_callNow(),messageAvg=api_callAvg())


if __name__ == "__main__":
    app.run(port=3000)