#for 
"""
for nom_client in range(1,6):
  print('Vous etes le client {}'.format(nom_client))
"""
#FOR EACH : pour chaque valeur d'une liste donnée
"""
blacklist = ["diarama@gmail.com","diarasita@gmail.com"]
emails = ["couda.dm@gmail.com", "diarama@gmail.com", "diarammadou471@gmail.com", "diarasita@gmail.com", "diarakadi@gmail.com"]

for email in emails:
  if email in blacklist:
    print(email in blacklist)
    print("Email n'est pas envoyé à {} !!!".format(email))
    break
  print('email envoyé à : ', email)
"""

"""
#WHILE BOUCLE

salary = 1500

while salary < 2000:
  salary += 120

  print("Votre salaire actuel est {}".format(salary))

"""

#Le juste prix
le_prix = int(input('entrer un prix '))

while le_prix > 1 and le_prix < 1000:
  le_prix = int(input('entrer un prix '))
  
  if le_prix > 1 and le_prix < 1000:
    print("C'est gagné")
  elif le_prix < 1:
    print("C'est court")
  else:
    print("C'est moins")
