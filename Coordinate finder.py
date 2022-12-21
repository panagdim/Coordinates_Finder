# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 15:28:11 2022

@author: azade
"""

import pandas as pd
from geopandas.tools import geocode

#read the exel file 
villages = pd.read_excel("D:/GitHub Uploads/Automatic coordinate finder/villagenames.xlsx")


#read the csv file as a pandas data frame 
#villages = pd.read_csv("")

#add two cloumn for the excel file 

# for index, row in villages.iterrows():
#     print (row["NAME"])
    
#     information = geocode(row["NAME"], provider= "arcgis", user_agent= "xyz", timeout=5)
#     villages.loc[index, "Longtide"]= information.geometry.loc[0].x
#     villages.loc[index, "latitude"]= information.geometry.loc[0].y
    
# villages.to_csv("villages_with_coordinate.csv")


#if the coordinate of one place is not found but you want to continue the process
for index, row in villages.iterrows():
    try:
        print (row["NAME"])
    
        information = geocode(row["NAME"], provider= "geocodio", user_agent= "xyz", timeout=20)
        villages.loc[index, "Longtide"]= information.geometry.loc[0].x
        villages.loc[index, "latitude"]= information.geometry.loc[0].y
        
    except TypeError:
        print("Coordinates of " + row["NAME"]+ "are not availabe ")
    except IndexError:
        print("Coordinates of " + row["NAME"]+ "has index error ")

villages.to_csv("villages_with_coordinate.csv")