# ATRportable

https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax

## Python Version
Version utilisée : Python 3.7

## Modules (seules versions testées)
numpy 1.21.6 

opencv-python 4.6.0.66 

face-recognition 1.3.0 

face-recognition-models 0.3.0

dlib 19.24.0

imutils 0.5.4

## Fichiers python et répertoires nécessaires
ATRComplete.py

faces_database_auto.py

tracker.py

Test_material/Images (un répertoire "Test_material" au niveau des fichiers .py, dans lequel se trouve "Images", dans lequel se trouvent les photos des visages)

## 'Logiciels' prérequis

Un environnement pour du code Python



### En fonction du besoin
EpocCam Webcam for Mac et PC 2023.1.1 et Camera Hub 1.5.1 (mono-caméra)

DroidCam Webcam & OBS Camera 1.9.3 (multi-caméra)


## Lancement de l'algorithme avec EpocCam et Camera Hub (version mono-caméra)

1. Remplir "Images" avec les photos de personnes à identifier, format idéal pour le nom de la photo: Prénom_Nom (convention fixée par le groupe).
2. Exécuter faces_database_auto.py (ce qui va charger la base de données avec les données des photos précédentes).
3. Lancer EpocCam sur le téléphone portable à utiliser, et Camera Hub sur l'ordinateur central.
4. Exécuter ATRComplete.py

**Remarques** : Si tout fonctionne comme prévu, une fenêtre apparait à l'écran de l'ordinateur avec le flux vidéo du téléphone portable. Pour changer entre la caméra de l'ordinateur principal et celle du téléphone portable, il faut mettre en commentaire (ou dé-commenter pour l'inverse) la ligne 9 ou 11 de ATRComplete.py pour changer l'entrée vidéo.

## Lancement de l'algorithme avec Droidcam (version multi-caméra)

1. cf partie EpocCam
2. cf partie EpocCam
3. 

## Le reste

Le fichier principal est ATRComplete, c'est celui à exécuter pour lancer le processus de détection/suivi/identification. On peut changer entre la caméra de l'ordinateur et celle du téléphone portable en modifiant les commentaires dans les premières lignes avec "camera_input". Avant de faire cela, il faut charger la base de données grâce à faces_database_auto, qui prend toutes les photos de personnes dans Test_material/Images et prépare la BDD.

Ainsi, pour faire fonctionner l'application, il faut avoir dans un même répertoire: ATRComplete.py, faces_database_auto.py, tracker.py et un répertoire "Test_material" contenant un autre répertoire "Images" dans lequel sont stockées les photos des visages. Pour ajouter à la base de données, il suffit de rajouter des photos de visages dans "Images", idéalement sous le format Prénom_Nom pour garder une cohérence avec le reste. Puis il faut relancer faces_data_auto.py pour mettre à jour les données.
