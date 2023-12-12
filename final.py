# -*- coding: utf-8 -*-

###############################################################################
###############################################################################
# Zone à compléter
###############################################################################
###############################################################################


# module pour tracer la carte avec le marqueur
import folium
# module pour exécuter le navigateur web
import webbrowser
# lire les données EXIF du fichier image
import exifread


def calculer_angle(valeur):
    """convertir la valeur du la coordonnes GPS EXIF en degr d'angle au format nombre flottant
    :paramtre value : valeur associ  une cl d'un dictionnaire exifread pour la latitude ou la longitude'
        list [¡ d'angle, minute d'angle, seconde d'angle]
    :type value: exifread.utils.Ratio :list [¡ d'angle, minute d'angle, seconde d'angle]
    :return type: float type de la valeur de retour angle en ¡ dcimal"""
    ###########################################################################
    ###########################################################################
    # calcul de la partie degrÃ© de l'angle
    a=float(valeur.values[0].num) / float(valeur.values[0].den)
    # calcul de la partie minute de l'angle
    m=float(valeur.values[1].num) / float(valeur.values[1].den)
    # calcul de la partie seconde de l'angle
    s=float(valeur.values[2].num) / float(valeur.values[2].den)
    return a+m/60+s/3600 # calcul de l'angle

# ouvre le fichier image en lecture seule (r) et en mode binaire (b)
nom_fichier_photo="gps29.jpg";
f = open("./images/"+nom_fichier_photo, 'rb')
# lit les données Exif
dict_exif=exifread.process_file(f)
# Calcule en la latitude dans la variable latitude
# et la longitude dans la variable longitude
# en degrée décimal : fonction calculer_angle
longitude=calculer_angle(dict_exif["GPS GPSLongitude"])
latitude=calculer_angle(dict_exif["GPS GPSLatitude"])
print (dict_exif["GPS GPSLongitudeRef"],dict_exif["GPS GPSLatitudeRef"])
###############################################################################
###############################################################################
# traite la latitude SUD et la longitude OUEST pour que le marqueur soit bien positionné

###############################################################################
###############################################################################
# créer une carte centrée sur la lattitude et la longitude avec un zoom de 4
ma_carte=folium.Map(location=[latitude,longitude],zoom_start=4)

# positionne un marqueur (icone_marqueur) cliquable sur la lattitude et la longitude avec un popup C'est ici (label)
label="C'est ici";# le label du popup
icone_marqueur=folium.Icon(color="red"); # le marqueur sur la carte
folium.Marker(location=[latitude,longitude],popup=label,icon=icone_marqueur).add_to(ma_carte)

# génère le fichier html de la carte avec le marqueur
ma_carte.save('final.html')
# exécute le navigateur web par défaut et affiche la carte avec le marqueur
webbrowser.open_new_tab('final.html')