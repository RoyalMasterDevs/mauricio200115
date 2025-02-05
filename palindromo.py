def es_palindromo(texto: str) -> bool:
    # Eliminamos espacios y convertimos a minúsculas
    texto = ''.join(texto.split()).lower()
    # Comparamos el texto original con su reverso
    return texto == texto[::-1]

# Ejemplo de uso
palabra = input("Ingresa una palabra o frase: ")
if es_palindromo(palabra):
    print("Es un palíndromo")
else:
    print("No es un palíndromo")

