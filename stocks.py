import re
import urllib.request

#re.search(string1 , string2) -- > vars
#then var.start() -- > beginnning of string1 in string2
#and var.end() -- > ending of string 1 in string2

#sample stock --> https://www.google.com/finance?q=NSE%3ARELIANCE&ei=-Mn0VuHlJ8WHuQT74ZLQAQ
#required url --> https://www.google.com/finance?q=
# sorry for not considering space complexity in this code....i am noobie

url_basic = "https://www.google.com/finance?q="
url_input = input("Enter the stock you wish to see:")
url_complete = url_basic + url_input

stock_binary = urllib.request.urlopen(url_complete).read()
stocks_decode = stock_binary.decode("utf-8") # convert unicode

var_search_further = re.search('meta itemprop="price"',stocks_decode)
start = var_search_further.start()
end = start + 50
stocks_metadata = stocks_decode[start:end] #slices metadata out of all unicode fetched

#print(stocks_metadata)

var_search_further = re.search('content="',stocks_metadata)
price_start = var_search_further.end()
stocks_price_metadata_start = stocks_metadata[price_start:]

#print(stocks_price_metadata_start)

var_search_further = re.search("/",stocks_price_metadata_start)
price_start  = 0
price_end = var_search_further.end() - 3

final_stock_price = stocks_price_metadata_start[0:price_end]
print("The value of "+url_input+" stock is:" , final_stock_price)