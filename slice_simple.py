def slice_simple():
    texto = "Awesome"
    # Código a implementar, se debe utilizar la variable 'texto' para resolver el ejercicio.
    # No se debe modificar la definición de la función, ni ingresar otro valor mediante input.
    # A es la 0, w es la 1, e es la 2, s es la 3, o es la 4, m es la 5, e es la 6.
    print(texto[0:3].lower()) #primeras 3 letras 
    print(texto[2:5].lower()) #3 letras del medio "eso" que son la 2 3 4
    print(texto[0:4].lower()+texto[4:7].lower()) #de la primer letra a la cuarta y de la antepenultima a la ultima.

slice_simple()
# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_slice_simple_test.py` o `python tp3_slice_simple_test.py`

