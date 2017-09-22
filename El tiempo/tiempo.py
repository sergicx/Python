# -*- coding: utf-8 -*-
import json
import urllib
import re
import datetime
from asciiWeather import *
import sys
reload(sys)
sys.setdefaultencoding('utf8')


def main():
	location = str(raw_input("Escribe tu ubicacion: "))
	dataActual = getJsonApiActual(location)
	dataPrevision = getJsonApiPrevision(location)
	maxMin = getMaxMin(dataActual)
	listaProximosDias = listaPrevision(dataPrevision)
	weatherIcon = getAsciiIcon(dataActual)
	if weatherIcon == None:
		weatherActualFull = getWeather(dataActual).upper()
	else:
		weatherActualFull = getWeather(dataActual).upper() +  "\n\r " + weatherIcon
	print " \n EL TIEMPO ACTUAL PARA LA UBICACION: %s \n" % (dataActual["name"])
	print "%s\n" % (weatherActualFull)
	print "La temperatura actual es: %s" % str(getTemperature(dataActual))
	print "La presion actual es: %s hPa" % str(getPressure(dataActual))
	print "La humedad actual es de: %s%%" % str(getHumidity(dataActual))
	print "La temperatura maxima de hoy es: %s" % str(maxMin[0])
	print "La temperatura minima de hoy es: %s\n" % str(maxMin[1])
	print "Prevision para los proximos dias: \n"
	for i in listaProximosDias:
		print i,
	entrada = raw_input("Desea hacer otra consulta? (s/n) ")
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

def getAsciiIcon(data):
	iconCode = data["weather"][0]["icon"]
	if iconCode == "01d" or iconCode == "01n":
		return asciiSun
	elif iconCode == "02d" or iconCode == "02n":
		return asciiPartiallyCloud
	elif iconCode == "03d" or iconCode == "03n" or iconCode == "04d" or iconCode == "04n":
		return asciiCloud
	elif iconCode == "09d" or iconCode == "09n" or iconCode == "10d" or iconCode == "10n":
		return asciiRain
	else:
		return None


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
	cantidad = data["cnt"] - 1
	j = 0

	for i in range(cantidad):
		dataWeather = data["list"][i]["weather"][0]["description"]
		regexDiaFecha = re.findall(r'\d{2}', str(data["list"][i]["dt_txt"]))
		diaFecha = regexDiaFecha[3]
		hora = regexDiaFecha[4]
		if int(diaFecha) != int(diaSistema):
			if diaFecha != dataAnterior and j <= 3:
				listaPrevision.append("Tiempo para el dia " + diaFecha + ": \n")
				dataAnterior = diaFecha
				j = j + 1
			else:
				if hora == "09":
					listaPrevision.append("Mañana: " + dataWeather + "\t")
				elif hora == "15":
					listaPrevision.append("Tarde: " + dataWeather + "\t")
				elif hora == "21":
					listaPrevision.append("Noche: " + dataWeather + "\n\n")

	return listaPrevision

if __name__ == '__main__':
	main()
