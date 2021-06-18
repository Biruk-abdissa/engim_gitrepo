### SOMMARE GLI ELEMENTI DI UNA LISTA CON CICLO FOR

# definisco una lista
lista = [10, 12, 7, 5, 9]
# inizializzo una variabile somma, con risultato iniziale = 0
somma = 0
#ciclo for
for elemento in lista:
    print(f"la somma prima di sommare l'elemento nel ciclo è: {somma}")
    print(f"l'elemento nel ciclo è: {elemento}")
    somma += elemento
    print(f"la somma dopo aver sommato l'elemento nel ciclo è: {somma}")
    print("il ciclo passa all'elemento successivo")
