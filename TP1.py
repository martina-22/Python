from random import choice, randrange
from datetime import datetime

# Operadores posibles
operators = ["+", "-", "/", "*"]

# Cantidad de cuentas a resolver
times = 5

# Contador inicial de tiempo.
# Esto toma la fecha y hora actual.
correct = 0
incorrect = 0
init_time = datetime.now()

print(f"¡Veremos cuanto tardas en responder estas {times} operaciones!")
for i in range(0, times):
    number_1 = randrange(10)
    number_2 = randrange(10) 
    operator = choice(operators)

    # Se imprime la cuenta.
    print(f"{i+1}- ¿Cuánto es {number_1} {operator} {number_2}?")

    # Le pedimos al usuario el resultado
    result = int(input("resultado: "))

    if operator == '+':
        resultado = number_1 + number_2
    elif operator == '-':
        resultado = number_1 - number_2
    elif operator == '*':
        resultado = number_1 * number_2
    else:
        if number_2 != 0:
            resultado = number_1 / number_2
        else:
            print("No se puede dividir por cero")
            continue # Pasar a la siguiente iteración

    if result == resultado:
        correct += 1
        print('correcto')
    else:
        incorrect += 1
        print('incorrecto')

# Al terminar toda la cantidad de cuentas por resolver.
# Se vuelve a tomar la fecha y la hora.
end_time = datetime.now()

# Restando las fechas obtenemos el tiempo transcurrido.
total_time = end_time - init_time

# Mostramos ese tiempo en segundos.
print(f"\n Tardaste {total_time.seconds} segundos.")
print(f"\n  {correct} fue la cantidad de respuestas correctas.")
print(f"\n  {incorrect} fue la cantidad de respuestas incorrectas.")
