# -*- coding: utf-8 -*-

###############################################################################
###############################################################################
#                 Zone de traitement pour vous
###############################################################################
###############################################################################

# module pour tracer la carte avec le marqueur
import folium
# module pour exécuter le navigateur web
import webbrowser


###############################################################################
###############################################################################
# latitude et longitude de Paris :
latitude = 48.866667; longitude = 2.333333

# latitude et longitude pour New York :
latitude_2 = 40.712784; longitude_2 = -74.005941

# latitude et longitude pour Sydney :
latitude_3 = -33.856159; longitude_3 = 151.215256

# latitude et longitude pour La Paz:
latitude_4 = -16.5; longitude_4 = 68.15

###############################################################################
###############################################################################

# créer une carte centrée sur la lattitude et la longitude
ma_carte=folium.Map(location=[latitude,longitude],zoom_start=4)
ma_carte_2=folium.Map(location=[latitude_2,longitude_2],zoom_start=4)
ma_carte_3=folium.Map(location=[latitude_3,longitude_3],zoom_start=4)
ma_carte_4=folium.Map(location=[latitude_4,longitude_4],zoom_start=4)

# positionne un marqueur (icone_marqueur) cliquable sur la lattitude et la longitude avec un popup C'est ici (label)
label="C'est ici"; # le label du popup
icone_marqueur=folium.Icon(color="blue"); # le marqueur sur la carte
#positionne un marqueur cliquable sur la lattitude et la longitude avec un popup C'est ici
folium.Marker(location=[latitude,longitude],popup=label,icon=icone_marqueur).add_to(ma_carte)
folium.Marker(location=[latitude_2,longitude_2],popup=label,icon=icone_marqueur).add_to(ma_carte_2)
folium.Marker(location=[latitude_3,longitude_3],popup=label,icon=icone_marqueur).add_to(ma_carte_3)
folium.Marker(location=[latitude_4,longitude_4],popup=label,icon=icone_marqueur).add_to(ma_carte_4)

# génère le fichier html de la carte avec le marqueur
ma_carte.save('pos_marq.html')
ma_carte_2.save('pos_marq_2.html')
ma_carte_3.save('pos_marq_3.html')
ma_carte_4.save('pos_marq_4.html')
# exécute le navigateur web par défaut et affiche la carte avec le marqueur
#webbrowser.open_new_tab('pos_marq.html')
#webbrowser.open_new_tab('pos_marq_2.html')
#webbrowser.open_new_tab('pos_marq_3.html')
webbrowser.open_new_tab('pos_marq_4.html')
