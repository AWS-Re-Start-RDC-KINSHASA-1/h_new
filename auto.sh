#!/bin/bash

# lien de téléchargement de l'url
url="https://cdn.wsform.com/wp-content/uploads/2020/06/industry.csv"
output_file="industry.csv"

curl -o "$industry.csv" "$https://cdn.wsform.com/wp-content/uploads/2020/06/industry.csv"

# vérification
if [ $? -eq 0 ]; then
  echo "Votre fichier a été téléchargé avec succès"
else
  echo "téléchargement échoué"
fi
