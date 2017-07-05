import urllib2
import easyprint.easyprint as EP
import json

apiKey="9b3e4c512edee68450efd6e92f703836"
city="Montreal"
URL="http://api.openweathermap.org/data/2.5/forecast?q="+city+"&mode=json&appid="+apiKey

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
  with open("city.list.json","r") as f:
    data = json.loads(f.read())
    EP.eprint(data)
'''

def getWeather():
  global URL
  try:
    WeatherData = urllib2.urlopen(URL).read()
    parsed = json.loads(WeatherData)
    keys = parsed.keys()
    #EP.eprint(parsed) #Debugging
    print(keys) #Debugging
    #date
    #for item in parsed['list']: #Debugging
      #print(str(item['dt_txt'])) #Debugging
    print(parsed['list'][0]['dt_txt'])
    print(parsed['list'][0]['weather'][0]['description'])

  except urllib2.URLError as err:
    print("[Network] - connection to " + URL + " unsucessfull")

verifyInternet()
getWeather()