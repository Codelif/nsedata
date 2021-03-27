# nse_data
Library for getting NSE data super easy.
# Overview
You can get many types of NSE data using the library:
 - Get all the available NSE stock symbols. 
 - Get intraday stock data like open, close, volume, etc of a particular stock.
 - Get Historical Data
 - Get Live Stock Price. 
## Usage

In the following paragraphs, I am going to describe how you can get and use Scrapeasy for your own projects.

###  Getting it
To download nse-data, either fork this github repo or simply use Pypi via pip.
```sh
$ pip install nse-data
```
### Using it
You can use nse-data in you project by importing it like this
```Python
from nse-data import Nse

nse = Nse()
```

This imports the ```Nse``` class which has all the functions into your project.

### Nse.all_codes()
This function will get all the available stock codes for NSE.
```Python
nse.all_codes()
```
This will give a dictionary:
```
{'20MICRONS': '20 Microns Limited', '21STCENMGM': '21st Century Management Services Limited', '3IINFOTECH': '3i Infotech Limited', '3MINDIA': '3M India Limited', '3PLAND': '3P Land Holdings Limited', '5PAISA': '5Paisa Capital Limited', '63MOONS': '63 moons technologies limited', 
...
...
...
...
, 'ZODIACLOTH': 'Zodiac Clothing Company Limited', 'ZODJRDMKJ': 'Zodiac JRD- MKJ Limited', 'ZOTA': 'Zota Health Care LImited', 'ZUARI': 'Zuari Agro Chemicals Limited', 'ZUARIGLOB': 'Zuari Global Limited', 'ZYDUSWELL': 'Zydus Wellness Limited'}
```

### Nse.get_intraday()
This will give you data for today on a particular stock:
 - date
 - close
 - open
 - previous close
 - volume

```Python
nse.get_intraday("atgl")
```
This will output a dictionary:
```
{'Date': '2021-3-28', 'Price': '905.45', 'Open': '914.00', 'Volume': '1785429', 'Prev Close': '881.75'}
```
### Nse.historical_data() 
This will give data between given dates in the interval of a day:
```Python
nse.historical_data("reliance", (2020, 1, 1), (2021, 1, 1))
```
This will output a list of dictionaries:
```
[{'Date': '2020-12-31', 'Open': 1993.5, 'High': 2011.900024, 'Low': 1978.599976, 'Close': 1985.300049, 'Adj Close': 1985.300049, 'Volume': 8667516.0}, {'Date': '2020-12-30', 'Open': 1995.25, 'High': 2007.199951, 'Low': 1975.550049, 'Close': 1995.5, 'Adj Close': 1995.5, 'Volume': 10173132.0}, {'Date': '2020-12-29', 'Open': 2009.0, 'High': 2012.300049, 'Low': 1982.550049, 'Close': 1990.050049, 'Adj Close': 1990.050049, 'Volume': 8589407.0},
...
...
...
...
{'Date': '2020-01-02', 'Open': 1497.802368, 'High': 1526.480469, 'Low': 1497.802368, 'Close': 1520.883545, 'Adj Close': 1515.194214, 'Volume': 8173308.0}, {'Date': '2020-01-01', 'Open': 1503.745972, 'High': 1512.760498, 'Low': 1491.363403, 'Close': 1495.424927, 'Adj Close': 1489.830811, 'Volume': 6463060.0}]
```


### Nse.live_quote()
This will get the latest price of a stock.
```Python
nse.live_quote("reliance")
```
This will output a string of the price:
```
'1994.65'
```




