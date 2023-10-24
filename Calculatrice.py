def calculatrice():
    print("Sélectionnez une opération:")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")

    choix = input("Entrez le numéro de l'opération (1/2/3/4) : ")

    num1 = float(input("Entrez le premier nombre : "))
    num2 = float(input("Entrez le deuxième nombre : "))

    if choix == '1':
        resultat = num1 + num2
        print(f"Résultat : {resultat}")
    elif choix == '2':
        resultat = num1 - num2
        print(f"Résultat : {resultat}")
    elif choix == '3':
        resultat = num1 * num2
        print(f"Résultat : {resultat}")
    elif choix == '4':
        if num2 != 0:
            resultat = num1 / num2
            print(f"Résultat : {resultat}")
        else:
            print("Erreur : Division par zéro.")
    else:
        print("Opération non valide.")

calculatrice()
