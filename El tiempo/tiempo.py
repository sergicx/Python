import json
import urllib


def main():
	location = str(raw_input("Escribe tu ubicacion: "))
	data = getJsonApi(location)
	maxMin = getMaxMin(data)

	entrada = None
	print " \n EL TIEMPO PARA LA UBICACION: %s \n" % (data["name"])
	print "El tiempo actual es: %s" % (getWeather(data))
	print "La temperatura actual es: %s" % str(getTemperature(data))
	print "La presion actual es: %s" % str(getPressure(data))
	print "La humedad actual es de: %s%%" % str(getHumidity(data))
	print "La temperatura maxima de hoy es: %s" % str(maxMin[0])
	print "La temperatura minima de hoy es: %s" % str(maxMin[1])
	entrada = raw_input("\nDesea hacer otra consulta? (s/n) ")
	if entrada != "n" or entrada != "N":
	    main()


def getJsonApi(location):
	url = "http://api.openweathermap.org/data/2.5/weather?q=%s&appid=eb8cb2cf0cd7cb44ded287804edcb7dc&mode=json&units=metric&lang=es" % (location)
	response = urllib.urlopen(url)
	data = json.loads(response.read())
	return data

def getWeather(data):
	return data["weather"][0]["description"]

def getTemperature(data):
	return data["main"]["temp"]

def getPressure(data):
	return data["main"]["pressure"]

def getHumidity(data):
	return data["main"]["humidity"]

def getMaxMin(data):
	return [data["main"]["temp_max"],data["main"]["temp_min"]]

if __name__ == '__main__':
	main()
