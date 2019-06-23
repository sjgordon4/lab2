


import processing #import QGIS processing tools
Police_Districts = "S:/682/Summer19/selagrdn/Police_Districts.shp"#save shapefile as new variable
iface.addVectorLayer(Police_Districts,"Police_Districts","ogr")
##THIS ADDED POLICE DISTRICTS

Crime_Incidents_in_2017 = "S:/682/Summer19/selagrdn/Crime_Incidents_in_2017.shp"#save shapefile as new variable
iface.addVectorLayer(Crime_Incidents_in_2017,"Crime_Incidents_in_2017","ogr")
##THIS ADDED THE CRIME

#processing.alghelp("qgis:joinattributesbylocation")
processing.runalg("qgis:joinattributesbylocation", 
    {'TARGET':Police_Districts,'JOIN':Crime_Incidents_in_2017,'PREDICATE':u"contains",'SUMMARY':1,'STATS':"sum,mean,median,max,min",'KEEP':1,'OUTPUT':'S:/682/Summer19/selagrdn/joinshp4.shp'})
    
iface.addVectorLayer( "S:/682/Summer19/selagrdn/joinshp4.shp","join","ogr")

##The third district had the most crimes --5964 crimes occured. 