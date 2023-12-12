# module pour lire les données EXIF du fichier image
import exifread as ef

# fonction retournant la valeur décimale de l'angle du paramètre
def calculer_angle (valeur):
    """ angle : valeur de clé du dictionnaire exif pour la latitude ou la longitude
        valeur retournée : un float de l'angle
    """
    # calcul de la partie degré de l'angle
    a=float(valeur.values[0].num) / float(valeur.values[0].den)
    # calcul de la partie minute de l'angle
    m=float(valeur.values[1].num) / float(valeur.values[1].den)
    # calcul de la partie seconde de l'angle
    s=float(valeur.values[2].num) / float(valeur.values[2].den)
    return a+m/60+s/3600 # calcul de l'angle

# ouvre le fichier image en lecture seule (r) et en mode binaire (b)
f = open("./images/gps12.jpg",'rb')
# lit les données Exif dans la variable dict_exif
tags = ef.process_file(f)
# fermer le fichier f
f.close ()
dict_exif = dict(tags)
for ff,ss in dict_exif.items():
   print(ff," : ",ss)
# balayer le dictionnaire dict_exif par cl� et valeur pour les afficher
for key,value in dict_exif.items():
    if key in ('GPS GPSLatitude', 'GPS GPSLongitude'):
        print (key,value)
# calculer en decimale la latitude et la longitude
# appel de la fonction calculer_angle. Ex : longitude=calculer_angle (dict_exif["la bonne cle"])
latitude = calculer_angle(dict_exif['GPS GPSLatitude'])
print(latitude)
longitude = calculer_angle(dict_exif['GPS GPSLongitude'])
print(longitude)
# afficher la latitude et la longitude calculer par la fonction calculer_angle

