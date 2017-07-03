import urllib2
import easyprint.easyprint as EP
import json

apiKey="9b3e4c512edee68450efd6e92f703836"
city="Montreal"
URL="http://api.openweathermap.org/data/2.5/forecast?q="+city"&mode=json&appid="+apiKey

def verifyInternet():
  try:
    urllib2.urlopen("HTTP://google.com", timeout=1)
    print("[Network] - Network Status: Active with Internet Access")
    return True
  except urllib2.URLError as err:
    print("[Network] - Network Status: Inactive")
    return False

'''
def getCityID(city):
  f=file.open("city.list.json")
'''

def getWeather():
  global URL
  try:
    WeatherData = urllib2.urlopen(URL).read()
    EP.eprint(json.loads(WeatherData))
  except urllib2.URLError as err:
    print("[Network] - connection to " + URL + " unsucessfull")

verifyInternet()
getWeather()