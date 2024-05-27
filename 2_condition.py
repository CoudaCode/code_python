"""
#Systeme de verification de password

password = input("Entrez votre mot de passe: ")
password_length = len(password)

if password_length <= 8:
  print("Mot de passe trop court")
# elif password_length <= 12 and password_length > 8:
elif 8 < password_length <= 12:
  print('Mot de passe moyen')
else:
  print('Mot de passe valide')

"""

#place de cinema

age = int(input("Quel est votre age ? "))
montant = 0
if 5 < age < 18:
  montant = 7
  print("Vous payez 7£")
elif age > 18:
  montant = 12
  print("Vous payez 12£")
else:
  print("Vous n'êtes pas autorisé a ce bar")

pop_corn = input('Souhaitez-vous du pop corn ? ')

if pop_corn == "oui":
  montant+= 5
  print('le prix total est {}'.format(montant))
elif pop_corn == "non":
  print('le prix total est {}'.format(montant))

