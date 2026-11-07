import os
import subprocess

chemin_projets = r"C:\Users\Administrateur\Documents\Projets"
nom_projet = input("Quel est le nom de ton projet : ")

dossier = os.path.join(chemin_projets, nom_projet)
os.makedirs(dossier, exist_ok=True)

# Créer main.py
with open(os.path.join(dossier, "main.py"), "w") as f:
    f.write(f"# Projet : {nom_projet}\n\n")

# Créer README.md
with open(os.path.join(dossier, "README.md"), "w") as f:
    f.write(f"# {nom_projet}\n\nDescription du projet ici.")

# Ouvrir dans VS Code
subprocess.run(["code", dossier])

print(f"Projet '{nom_projet}' créé et ouvert dans VS Code !")
