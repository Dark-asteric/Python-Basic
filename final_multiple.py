# -*- coding: utf-8 -*-

###############################################################################
###############################################################################
# Zone à compléter
###############################################################################
###############################################################################



# lire les données EXIF du fichier image
import exifread as ef;
# module pour tracer la carte avec le marqueur
import folium;
# module pour exécuter le navigateur web
import webbrowser;
# module d'accès au fonction systeme
import os;

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

# couleur disponible pour les marqueurs sur la carte
marker_colors = ['red','blue','gray','darkred','lightred','orange','beige','green','darkgreen','lightgreen','darkblue','lightblue','purple',
    'darkpurple','pink','cadetblue','lightgray','black'];

###############################################################################
###############################################################################
# Crée la carte centrée sur 0° de latitude et 30° de longitude avec un zoom de 3 : variable ma_carte
ma_carte=folium.Map(location=[0,0],zoom_start=4)
###############################################################################
###############################################################################

# liste contenant le nom des fichier .jpg dans le dossier images
lnamefile=[name for name in os.listdir("./images") if name.endswith(".jpg")]


mc =[]
# boucle pour traiter les fichiers image un par un gps0.jpg puis gps1.jpg puis ...
for i in range (len(lnamefile)): # i contient l'indice du nom du fichier dans lnamefile
    # ouvre le fichier image : ./images/lnamefile[i]
    f = open("./images/"+lnamefile[i],'rb')
    ###########################################################################
    ###########################################################################
    # lit les données Exif dnas la variable dict_exif
    tags = ef.process_file(f)
    ###########################################################################
    ###########################################################################
    # fermer le fichier f
    f.close();
    dict_exif = dict(tags)
    
    ###########################################################################
    ###########################################################################
    # Calcule en la latitude dans la variable latitude
    # et la longitude dans la variable longitude
    # en degrée décimal : fonction calculer_angle
    x = (calculer_angle(dict_exif['GPS GPSLatitude']))
    y = (calculer_angle(dict_exif['GPS GPSLongitude']))
    
    # traite la latitude SUD et la longitude OUEST pour que le marqueur soit bien positionné
    if dict_exif["GPS GPSLatitudeRef"].values == "S":
        x = -x
    if dict_exif["GPS GPSLongitudeRef"].values == "W":
        y = -y
    # positionne un marqueur (icone_marqueur) cliquable sur la lattitude et la longitude avec un popup au n° du fichier (label)
    label=lnamefile[i].split(".jpg")[0][3:]; # le label du popup
    icone_marqueur=folium.Icon(color=marker_colors[i%len(marker_colors)]); # le marqueur sur la carte
    
    folium.Marker(location=[x,y],popup=label,icon=icone_marqueur).add_to(ma_carte)

ma_carte.save("final_multiple.html")
    #webbrowser.open_new_tab("final_multiple.html")
    ###########################################################################
    ###########################################################################

webbrowser.open_new_tab("final_multiple.html")
#for it in llatitude:
 #   print(it)
# génèe le fichier html de la carte avec le marqueur
#ma_carte.save('final_multiple.html');
# exécute le navigateur web et affiche la carte avec les marqueurs
#webbrowser.open_new_tab('final_multiple.html');