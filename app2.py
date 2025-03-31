import csv

#Dictionnaire pour classer les liens par catégorie
liens_par_categorie = {}

# Lecture du fichier CSV avec gestion des guillemets
with open('liens.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    next(reader)  # sauter la première ligne (en-tête)
    for row in reader:
        if len(row) < 5:
            print(" Ligne ignorée (colonnes manquantes) :", row)
            continue

        categorie = row[0].strip()
        nom = row[1].strip()
        ville = row[2].strip()
        lien = row[3].strip()
        description = row[4].strip()

        ville_html = f' – {ville}' if ville else ""        
        #Créer une liste si elle n'existe pas encore
        if categorie not in liens_par_categorie :
            liens_par_categorie[categorie] = []
        
        # Générer le lien HTML
        html_lien = f'<a href="{lien}" target="_blank"><strong>{nom}</strong>{ville_html} ↗</a> : {description}'
        liens_par_categorie[categorie].append(html_lien)
        
# Génération du code HTML
html = """<!DOCTYPE html>
<html lang="fr">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Réunion Wiki</title>
    <link rel="stylesheet" href="style.css" />
    <link rel="icon" type="image/x-icon" href="/images/favicon.ico" />
  </head>
  <body>
    <h1>Réunion Wiki - Votre portail local</h1>
    <p>
      Bienvenue sur <strong>Réunion Wiki 🌴</strong> <br />
      Un portail <em>simple, rapide et local</em> pour accéder aux sites
      essentiels de La Réunion : emploi, démarches, culture, santé, et plus
      encore. <br />
      Un seul endroit pour tout trouver, adapté aux besoins des Réunionnais.
    </p>
    """
    
# Parcours des catégories pour générer les blocs 
for categorie, liens in liens_par_categorie.items():
    html += f'<div class ="category">\n <h2>{categorie}</h2> \n <div class="links">\n'
    
    for lien in liens:
        html += f' {lien} <br>\n'
    html += '   </div>\n</div>\n'

#fin du document
html += "</body>\n</html>"

#Sauvegarde dans un fichier HTML
with open ('index.html', 'w', encoding='utf-8') as f:
    f.write(html)


print("Fichier HTML généré !")