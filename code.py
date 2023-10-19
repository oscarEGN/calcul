def est_bien_parenthesee(chaine):
    stack = []  # Utilisation d'une liste comme pile

    for i, char in enumerate(chaine):
        if char == '(':
            stack.append(i)  # Si c'est une parenthèse ouvrante, ajoute son indice à la pile
        elif char == ')':
            if not stack:
                return False  # Si on trouve une parenthèse fermante sans correspondante, la chaîne est mal parenthésée
            stack.pop()  # Si c'est une parenthèse fermante, retire la dernière parenthèse ouvrante de la pile

    return len(stack) == 0  # La chaîne est bien parenthésée si la pile est vide à la fin

# Exemples d'utilisation
chaine = "()((())))"

print(est_bien_parenthesee(chaine))  # Renvoie False
