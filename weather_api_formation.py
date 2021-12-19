#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 16:08:48 2021

@author: fitec
"""



from IPython.display import Image
from IPython.core.display import HTML
import os
import csv
from termcolor import colored, cprint


import json
import urllib.request

import datetime
import unidecode

import pandas as pd


import os.path

from pandas.io.json import json_normalize #package for flattening json in pandas df


import time

# from datetime import datetime

def url_builder(city_id,city_name,country):
    
    user_api = "c392bab71081ce6b45c440c44ce4385b"
    
    # bloque
    
    # user_api = '169f45b41a0d369db1e9555b59625083'
    # user_api = 'aa0b0e4e253be09f81ab241afae65ff4'
    #user_api = '4e0f8959dab541379b863bd8868196a6'  # Obtain yours form: http://openweathermap.org/
    
    unit = 'metric'  # For Fahrenheit use imperial, for Celsius use metric, and the default is Kelvin.
    if(city_name!=""):
        api = 'http://api.openweathermap.org/data/2.5/weather?q=' # "http://api.openweathermap.org/data/2.5/weather?q=Tunis,fr
        full_api_url = api + str(city_name) +','+ str(country)+ '&mode=json&units=' + unit + '&APPID=' + user_api
    else:
        api = 'http://api.openweathermap.org/data/2.5/weather?id='     # Search for your city ID here: http://bulk.openweathermap.org/sample/city.list.json.gz
        full_api_url = api + str(city_id) + '&mode=json&units=' + unit + '&APPID=' + user_api
   
    return full_api_url



city_name='Angle Bas'
country='France'
city_id='3037624'
url=url_builder(city_id,city_name,country)
 

url=url_builder(city_id,'','')



def data_fetch(full_api_url):
    

    
    #exemple de base fonctionne
    url = urllib.request.urlopen(full_api_url)
    
    
    output = url.read().decode('utf-8')
    
    
    raw_api_dict = json.loads(output)
    
    
    url.close()
    
    
    return raw_api_dict



full_api_url=url_builder(city_id,'','')
data=data_fetch(full_api_url)
# print(colored(data, 'yellow',attrs=['bold']))



# ts = 1543219200.0
# print(datetime.datetime.fromtimestamp(ts))


# d = datetime.datetime(year=2018, month=11,day=26, hour=9, minute=00)


# print(d.timestamp())


def time_converter(time):
    converted_time = datetime.datetime.fromtimestamp(
        int(time)
    ).strftime('%I:%M %p')
    return converted_time


def data_organizer(raw_api_dict):
    data = dict(
        city=raw_api_dict.get('name'),
        #country=raw_api_dict.get('sys').get('country'),
        temp=raw_api_dict.get('main').get('temp'),
        temp_max=raw_api_dict.get('main').get('temp_max'),
        temp_min=raw_api_dict.get('main').get('temp_min')#,
        # humidity=raw_api_dict.get('main').get('humidity'),
        # pressure=raw_api_dict.get('main').get('pressure'),
        # sky=raw_api_dict['weather'][0]['main'],
        # sunrise=time_converter(raw_api_dict.get('sys').get('sunrise')),
        # sunset=time_converter(raw_api_dict.get('sys').get('sunset')),
        # wind=raw_api_dict.get('wind').get('speed'),
        # wind_deg=raw_api_dict.get('deg'),
        # dt=time_converter(raw_api_dict.get('dt'))#,
        # cloudiness=raw_api_dict.get('clouds').get('all')
    )
    # print (data)
    return data


def data_output(data):
    m_symbol = '\xb0' + 'C'
    print('---------------------------------------')
    print('Current weather in: {}, {}:'.format(data['city'], data['country']))
    print(data['temp'], m_symbol, data['sky'])
    print('Max: {}, Min: {}'.format(data['temp_max'], data['temp_min']))
    print('')
    print('Wind Speed: {}, Degree: {}'.format(data['wind'], data['wind_deg']))
    print('Humidity: {}'.format(data['humidity']))
    print('Cloud: {}'.format(data['cloudiness']))
    print('Pressure: {}'.format(data['pressure']))
    print('Sunrise at: {}'.format(data['sunrise']))
    print('Sunset at: {}'.format(data['sunset']))
    print('')
    print('Last update from the server: {}'.format(data['dt']))
    print('---------------------------------------')



def WriteCSV(data,path_file):
    
    file_exists = os.path.isfile(path_file)

    
    if not file_exists:
        
        
        with open(path_file, 'w') as f:  # Just use 'w' mode in 3.x
            w = csv.DictWriter(f, data.keys())
            
            
            w.writeheader()
            w.writerow(data)
            
    else : 
    
        with open(path_file, 'a') as f:  # Just use 'w' mode in 3.x
            w = csv.DictWriter(f, data.keys())
            

            w.writerow(data)


# fonctionne
# def WriteCSV(data):
    
#     with open('weatherOpenMap.csv', 'a') as f:  # Just use 'w' mode in 3.x
#         w = csv.DictWriter(f, data.keys())
        
        
#         w.writeheader()
#         w.writerow(data)


def  ReadCSV():
    try:
    #ouverture de fichier en mode lecture en specifiant le encodage
        with open("weatherOpenMap.csv",'r') as Fichier:
        #lecture – utilisation du parseur csv en specifiant délimiteur
            csv_contenu = csv.reader(Fichier,delimiter=",") 
            reader = csv.DictReader(Fichier)
            dic={}
            for row in reader:
                # print (row['city'])
                dic.update(row)
            #fermeture du fichier avec la méthode close()
            Fichier.close()
            return dic
    except IOError:
        print("Fichier n'est pas trouvé")
        

        
#load json object

def getVilles():
    with open('city.list.json') as f:
        d = json.load(f)
        villes=pd.DataFrame(d)  
        return villes

        
        
villes=getVilles()      



villes_france = villes[villes['country'] == "FR"] 



liste_ville = sorted(list(set(villes_france['name'])))




date_for_path = "_" + str(datetime.datetime.now()).replace("-","_").replace(":","_").replace(" ","_").replace(".","_")[:-7]


path_1 = "weatherOpenMap" + date_for_path + ".csv"

path_2 = "weatherOpenMap_mean_city" + date_for_path + ".csv"

if __name__ == '__main__':
    try:
        
        country='France'
        
        for ville_to_get in liste_ville : 
            
            city_name = ""

            
            liste_id_city = list(villes_france.id[villes_france["name"]==ville_to_get])

            
            dic_ville_global = {}
            compteur_ville = 0
            
            for id_to_get in liste_id_city : 
                
                
                compteur_ville +=1
                
                city_id = id_to_get
                

                url=url_builder(city_id,city_name,country)

                data=data_fetch(url)

                time.sleep(3)

                data_orgnized=data_organizer(data)

                dic_ville_global[compteur_ville] = data_orgnized

              
            
                WriteCSV(data_orgnized,path_1)

            
            dic_ville_moyenne = {}
            
            
            dic_ville_moyenne["city"]=dic_ville_global[1]["city"]

            
            liste_temp = []
            
            liste_temp_max = []
            
            liste_temp_min = []
            
            
            for count in list(dic_ville_global.keys()) :
                

                liste_temp.append(dic_ville_global[count]["temp"])
                
                liste_temp_max.append(dic_ville_global[count]["temp_max"])
                
                liste_temp_min.append(dic_ville_global[count]["temp_min"])
                
                
            dic_ville_moyenne["temp"] = round(sum(liste_temp)/len(liste_temp),2)
            
            dic_ville_moyenne["temp_max"] = round(sum(liste_temp_max)/len(liste_temp_max),2)
            
            dic_ville_moyenne["temp_min"] = round(sum(liste_temp_min)/len(liste_temp_min),2)
            
            
            WriteCSV(dic_ville_moyenne,path_2)
            

         
    except IOError:
        print('no internet')       


# exemple qui fonctionne
# if __name__ == '__main__':
#     try:
        
# #         # exemple
#         # city_name='Tunis'
#         # country='Tunisia'
#         # city_id='2464470'
        
#         # city_name='Angle Bas'
#         city_name=''
#         country='France'
#         city_id='3037624'
        
        
# #         #Generation de l url
#         print(colored('Generation de l url ', 'red',attrs=['bold']))
#         url=url_builder(city_id,city_name,country)
        
# #         #Invocation du API afin de recuperer les données
#         print(colored('Invocation du API afin de recuperer les données', 'red',attrs=['bold']))
#         data=data_fetch(url)
#         print(json.dumps(data, sort_keys=True, indent=2));
# #         #Formatage des données
#         print(colored('Formatage des donnée', 'red',attrs=['bold']))
#         data_orgnized=data_organizer(data)
#         #Affichage de données
#         print(colored('Affichage de données ', 'red',attrs=['bold']))
#         data_output(data_orgnized)
#         #Enregistrement des données à dans un fichier CSV 
#         print(colored('Enregistrement des données à dans un fichier CSV ', 'green',attrs=['bold']))
#         WriteCSV(data_orgnized)
#         #WriteCassandra(data_orgnized)
#         print(colored('Lecture des données à partir un fichier CSV ', 'green',attrs=['bold']))
#         #Lecture des données a partir de fichier CSV 
#         data=ReadCSV()
#         print(colored('Affichage des données lues de CSV ', 'green',attrs=['bold']))
#         #Affichage des données 
#         data_output(data)
         
#     except IOError:
#         print('no internet')       
        
