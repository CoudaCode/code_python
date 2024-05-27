#Une variable de type global peut être récuperer dans une fonction 
#en ajoutant le mot clé "global" suivi de la variable en question

"""
def next_year():
  global year
  print("Fin de l'année", year)
  year+= 1
  print("Début de l'année ", year)

year = 2018
next_year()
next_year()
"""
"""
def add():

  result = 5+5
  return result

print('la somme est {}'.format(add()))

"""
"""
def max(a,b):
  if a  > b:
    return a
  else:
    return b
  
first_value = int(input("Entrer la valeur de a (la première)"))
seconde_value = int(input("Entrer la valeur de b (la seconde)"))

print("La maxi est ", max(first_value, seconde_value))

"""


def count_vowels_numbers(mot):
  count = 0
  vowels = ['a','o','u','i','y','e']
  for let in mot:
    
    if let in vowels:
      count +=1

  return count


print(count_vowels_numbers("Bonjour"))



