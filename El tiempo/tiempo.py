import json
import urllib


def getJsonApi(location):
	url = "http://api.openweathermap.org/data/2.5/weather?q=%s&appid=eb8cb2cf0cd7cb44ded287804edcb7dc&mode=json&units=metric&lang=es" % (location)
	response = urllib.urlopen(url)
	data = json.loads(response.read())
	return data

location = str(raw_input("Escribe tu ubicacion: "))
data = getJsonApi(location)

def getWeather():
	return data["weather"][0]["description"]

def getTemperature():
	return data["main"]["temp"]

def getPressure():
	return data["main"]["pressure"]

def getHumidity():
	return data["main"]["humidity"]

def getMaxMin():
	return [data["main"]["temp_max"],data["main"]["temp_min"]]


maxMin = getMaxMin()
print " \n EL TIEMPO PARA LA UBICACION: %s \n" % (data["name"])
print "El tiempo actual es: %s" % (getWeather())
print "La temperatura actual es: %s" % str(getTemperature())
print "La presion actual es: %s" % str(getPressure())
print "La humedad actual es de: %s%%" % str(getHumidity())
print "La temperatura maxima de hoy es: %s" % str(maxMin[0])
print "La temperatura minima de hoy es: %s" % str(maxMin[1])
