# -*- coding: utf-8 -*-
import json
import urllib
import re
import datetime


def main():
	location = str(raw_input("Escribe tu ubicacion: "))
	dataActual = getJsonApiActual(location)
	dataPrevision = getJsonApiPrevision(location)
	maxMin = getMaxMin(dataActual)
	listaProximosDias = listaPrevision(dataPrevision)

	entrada = None
	print " \n EL TIEMPO ACTUAL PARA LA UBICACION: %s \n" % (dataActual["name"])
	print "%s\n" % (getWeather(dataActual).upper())
	print "La temperatura actual es: %s" % str(getTemperature(dataActual))
	print "La presion actual es: %s hPa" % str(getPressure(dataActual))
	print "La humedad actual es de: %s%%" % str(getHumidity(dataActual))
	print "La temperatura maxima de hoy es: %s" % str(maxMin[0])
	print "La temperatura minima de hoy es: %s\n" % str(maxMin[1])
	print "Previsión para los próximos dias: \n"
	for i in range(4):
		print str(listaProximosDias[i])
	entrada = raw_input("\nDesea hacer otra consulta? (s/n) ")
	if entrada != "n":
		main()


def getJsonApiActual(location):
	url = "http://api.openweathermap.org/data/2.5/weather?q=%s&appid=eb8cb2cf0cd7cb44ded287804edcb7dc&mode=json&units=metric&lang=es" % (location)
	response = urllib.urlopen(url)
	data = json.loads(response.read())
	return data

def getJsonApiPrevision(location):
	url = "http://api.openweathermap.org/data/2.5/forecast?q=%s&appid=eb8cb2cf0cd7cb44ded287804edcb7dc&mode=json&units=metric&lang=es" % (location)
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
def listaPrevision(data):
	diaSistema = datetime.datetime.now()
	diaSistema = diaSistema.day
	listaPrevision = []
	dataAnterior = None
	for i in range(39):
		dataWeather = data["list"][i]["weather"][0]["description"]
		regexDiaFecha = re.findall(r'\d{2}', str(data["list"][i]["dt_txt"]))
		diaFecha = regexDiaFecha[3]
		hora = regexDiaFecha[4]
		if int(diaFecha) != int(diaSistema) and diaFecha != dataAnterior and hora == "15":
			dataAnterior = diaFecha
			listaPrevision.append("Tiempo para el dia " + diaFecha + ": " + dataWeather)

	return listaPrevision

if __name__ == '__main__':
	main()
