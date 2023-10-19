import tkinter as tk

def est_bien_parenthesee(chaine):
    pile = []
    ouvrantes_indices = []
    for i, char in enumerate(chaine):
        
        if char == '(':
            pile.append(i)
            ouvrantes_indices.append(i)
        elif char == ')':
            if not pile:
                return False
            ouvrante_index = pile.pop()
            print(f"La parenthèse ouvrante à l'indice {ouvrante_index} correspond à la parenthèse fermante à l'indice {i}")
    return len(pile) == 0

def verifier_parentheses():
    chaine = entree.get()
    if est_bien_parenthesee(chaine):
        resultat.config(text="La chaîne est bien parenthésée", fg="green")
    else:
        resultat.config(text="La chaîne n'est pas bien parenthésée", fg="red")

fenetre = tk.Tk()
fenetre.title("Vérification de Parenthèses")

entree = tk.Entry(fenetre, font=("Helvetica", 14))
entree.pack(pady=10, padx=10, ipadx=5, ipady=5, fill=tk.X)

bouton = tk.Button(fenetre, text="Vérifier", command=verifier_parentheses, font=("Helvetica", 14))
bouton.pack(pady=10)

resultat = tk.Label(fenetre, text="", font=("Helvetica", 14))
resultat.pack(pady=10)

fenetre.geometry("400x200")  # Définir la taille de la fenêtre

fenetre.mainloop()
