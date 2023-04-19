# ATRportable
> Author : [Eliot JACQUEMIN, Salman ALMUTAIRI, Nicolas LE ROUX, Ahmed ALOTAIBI, Victor XU / SOIA-MASSEL2024]

## Description
Ce projet, codé dans le cadre du projet système en 2e année à l'ENSTA Bretagne, consiste en la création d'un système de détection, suivi et identification de personnes utilisant comme caméra, le téléphone portable.

## Python Version
Version utilisée : Python 3.7

Environnement utilisé : PyCharm 2022.3.2

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

multi_cam.py

multi_cam_complete.py

faces_database.py

Test_material/Images (un répertoire "Test_material" au niveau des fichiers .py, dans lequel se trouve "Images", dans lequel se trouvent les photos des visages)

## 'Logiciels' prérequis

Un environnement pour du code Python

Connexion Wi-Fi stable : le(s) téléphone(s) portable(s) et l'ordinateur doivent être connectés au même réseau Wi-Fi


### En fonction du besoin
EpocCam Webcam for Mac et PC 2023.1.1 et Camera Hub 1.5.1 (mono-caméra)

DroidCam Webcam & OBS Camera 1.9.3 (multi-caméra)


## Lancement de l'algorithme avec EpocCam et Camera Hub (version mono-caméra)

1. Remplir "Images" avec les photos de personnes à identifier, format idéal pour le nom de la photo: Prénom_Nom (convention fixée par le groupe).
2. Exécuter faces_database_auto.py (ce qui va charger la base de données avec les données des photos précédentes).
3. Lancer EpocCam sur le téléphone portable à utiliser, et Camera Hub sur l'ordinateur central.
4. Exécuter ATRComplete.py

**Remarques** : Si tout fonctionne comme prévu, une fenêtre apparait à l'écran de l'ordinateur avec le flux vidéo du téléphone portable. Pour changer entre la caméra de l'ordinateur principal et celle du téléphone portable, il faut mettre en commentaire (ou dé-commenter pour l'inverse) la ligne 8 ou 10 de ATRComplete.py pour changer l'entrée vidéo.

## Lancement de l'algorithme avec Droidcam (version multi-caméra)

1. idem partie EpocCam
2. idem partie EpocCam
3. Lancer Droidcam sur le téléphone portable.
4. Dans le programme 'multi_cam.py' (resp. 'multi_cam_complete.py'), rajouter la caméra souhaitée (à partir de la ligne 12 (resp. 42)) avec la syntaxe suivante : **NomCamera**=cv2.VideoCapture('http://**IP**:**PORT**/video') en remplaçant **IP** et **PORT** par ceux fournis par droidcam et en choissant le nom de caméra que vous souhaitez (attention à ne pas utiliser 2 fois le même nom)
5. Dans le programme 'multi_cam.py', rajouter dans la liste captures (ligne 19 (resp. 45)) la variable **NomCamera**
6. Exécuter le programme 'multi_cam.py' (resp. 'multi_cam_complete.py').

> _NB_: Plus le nombre de caméras utilisées est grand, plus le système prend du temps pour répondre et risque de crasher.

> _NB2_: 'multi_cam.py' ne permet que la reconnaissance faciale mais a été testé et fonctionne. 'multi_cam_complete.py' permet toutes les autres fonctionnalités mais n'a jamais réussi à fonctionner plus d'une minute (demande de puissance de calculs trop grande).
