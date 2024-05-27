def main():
    """
    #print("Hello world")
    #tout les nom sont en minuscule et du pascalcase  
    username = "Graven"
    print(username)
    #.... les numbers
    age = 19

    wallet = 125.7
    print(age, wallet)
    #... le boolen

    is_happy = True
    print(is_happy)

    #Changement de valeur
    username = "Diara madou"

    age = 35

    age+= 13
    print(username, age+1)

    ##Calcule de moyenne
    note1 = int(input("Entrez la premiere note "))
    note2 = int(input("entrez la deuxieme note "))
    note3 = int(input("Entrez la derniere note "))

    result = (note1 + note2 + note3)/3
    print("Le resultat est " + str(result))

    ## Recolter la valeur du porte monnaie
    """
    value_porte_monnaie = int(input('Entrez la valeur de votre porte monnaie'))

    mangez = 2000

    monnaie = value_porte_monnaie - mangez

    print("Apres achat voici votre monnaie : " + str(monnaie))




## input == permet de saisie des valeurs venant de du user
## int == convertir du string en int

## str == convertir un valeur number string en string
  

if __name__ == '__main__': # Condition qui verifie a quel momeent le fichier est executé
    main()