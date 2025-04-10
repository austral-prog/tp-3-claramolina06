def check_vowels():
    # Código a implementar utilizando input.
    # Pedimos un nombre al usuario
    nombre = input("Ingresá un nombre: ")

    # Lo pasamos a minúscula para que no haya problema con mayúsculas
    nombre = nombre.lower()

    # Verificamos si contiene cada vocal
    print("Contiene a:", 'a' in nombre)
    print("Contiene e:", 'e' in nombre)
    print("Contiene i:", 'i' in nombre)
    print("Contiene o:", 'o' in nombre)
    print("Contiene u:", 'u' in nombre)


check_vowels()
# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_in_string_test.py` o `python tp3_in_string_test.py`
