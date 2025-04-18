#  1)Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print("Hello world")

# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
# el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
# por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
# realizar la impresión por pantalla.

name = input("Please, enter your name:")
print(f"Hello {name}!")

# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
# imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
# “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
# años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
# la impresión por pantalla.

name = input("Enter your nombre:")
surname = input("Enter your surname:")
age = input("Enter your age:")
place_of_residence = input("Enter your place of residence:")

print(f"Hello, i am {name} {surname}, i have {age} years old and im living in {place_of_residence}")

# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
# su perímetro.

pi = 3.1416
radius = float(input("Enter the radius of the circle: "))

area = pi * radius ** 2
perimeter = 2 * pi * radius

print(f"The area of ​​the circle is: {area:.2f}")
print(f"The perimeter of the circle is: {perimeter:.2f}")

# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
# cuántas horas equivale.

seconds = float(input('Enter a number of seconds '))

print(f"The second to Hours: {seconds / 3600}")

# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
# multiplicar de dicho número.

number = int(input("Enter a number:"))
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
# pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))

print(f"suma:{num1 + num2} ,division: {num1/num2}, multiplicacion: {num1*num2}, resta: {num1 - num2}")

# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
# de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
# modo:

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))
bmi = weight / (height ** 2)

print(f"Your Body Mass Index (BMI) is: {bmi:.2f}")

# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
# pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:

celsius = float(input("Enter la temperatura en grados Celsius: "))
fahrenheit = (9/5) * celsius + 32

print(f"{celsius:.2f}°C equivale a {fahrenheit:.2f}°F")

# 10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
# dichos números.

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

average = (num1 + num2 + num3) / 3

print(f"The average of the entered numbers is: {average:.2f}")
