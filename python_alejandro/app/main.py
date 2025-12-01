from app.modulo1.funciones import esPalindromo

def interactivo():
    while True:
        frase = input("Introduce una frase (o escribe 'exit' para terminar): ")
        
        if frase.strip().lower() == "exit":
            print("Programa finalizado.")
            break
        
        try:
            if esPalindromo(frase):
                print("La frase es palíndroma.")
            else:
                print("La frase no es palíndroma.")
        except TypeError as e:
            print(f"Entrada inválida: {e}")

if __name__ == "__main__":
    interactivo()

