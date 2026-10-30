import random
utilisateur = int(input("Quel est le nombre de caracteres de votre mdp: "))

for i in range(utilisateur):
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    mdp = random.choice(caracteres)
    print(mdp, end="")
print(i)
