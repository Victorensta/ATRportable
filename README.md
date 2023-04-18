# ATRportable

Modules: (seules versions testées)
numpy 1.21.6
opencv-python 4.6.0.66
face-recognition 1.3.0
face-recognition-models 0.3.0
dlib 19.24.0
imutils 0.5.4

Fichiers python nécessaires:
ATRComplete.py
faces_database_auto.py
tracker.py

Le fichier principal est ATRComplete, c'est celui à exécuter pour lancer le processus de détection/suivi/identification. On peut changer entre la caméra de l'ordinateur et celle du téléphone portable en modifiant les commentaires dans les premières lignes avec "camera_input". Avant de faire cela, il faut charger la base de données grâce à faces_database_auto, qui prend toutes les photos de personnes dans Test_material/Images et prépare la BDD.

Ainsi, pour faire fonctionner l'application, il faut avoir dans un même répertoire: ATRComplete.py, faces_database_auto.py, tracker.py et un répertoire "Test_material" contenant un autre répertoire "Images" dans lequel sont stockées les photos des visages. Pour ajouter à la base de données, il suffit de rajouter des photos de visages dans "Images", idéalement sous le format Prénom_Nom pour garder une cohérence avec le reste. Puis il faut relancer faces_data_auto.py pour mettre à jour les données.
