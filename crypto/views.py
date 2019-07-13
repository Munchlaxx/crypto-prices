from django.shortcuts import render

# Create your views here.

# Creating home view

def home(request):
	import requests
	import json

	# Setting the API variables for Crypto Prices
	price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,EOS,LTC,XLM,ADA,USDT,MIOTA,TRX&tsyms=USD&api_key=7938dbbea4c25afff7552598bab6aa02b57eb7ecd0a196dcb6d526730e1e487d")
	price = json.loads(price_request.content)

	# Setting the API variables for Crypto News
	api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN&api_key=7938dbbea4c25afff7552598bab6aa02b57eb7ecd0a196dcb6d526730e1e487d")
	api = json.loads(api_request.content)
	return render(request, 'home.html', {"api":api, "price": price})

def prices(request):
	import requests
	import json

	if request.method == 'POST':
		quote = request.POST['quote']
		crypto_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=" + quote.upper() + "&tsyms=USD&api_key=7938dbbea4c25afff7552598bab6aa02b57eb7ecd0a196dcb6d526730e1e487d")
		crypto = json.loads(crypto_request.content)
		return render(request, 'prices.html', {"quote": quote, "crypto": crypto})

	else:
		notFound = 'Please enter a crypto symbol in the search bar above...'
		return render(request, 'prices.html', {"notFound": notFound})
