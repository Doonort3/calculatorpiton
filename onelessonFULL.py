# Calculator by doonort3-v3

from colorama import init
from colorama import Fore, Back, Style
init()

print( Fore.BLACK )
print( Back.GREEN )

action = input( "Что делать? (+, -, /, *,): " )

print( Back.CYAN )

oneNumber = float(input("Введите первое число: "))
secondNumber = float(input("Введите второе число: "))

print( Back.YELLOW )

if action == "+":
	value = oneNumber + secondNumber
	print("Результат: " + str(value))
if action == "-":
	value = oneNumber + secondNumber
	print("Результат: " + str(value))
if action == "/":
	value = oneNumber / secondNumber
	print("Результат: " + str(value))
elif action == "*":
	value = oneNumber * secondNumber
	print("Результат: " + str(value))
else:
	print( Back.RED )
	print("Выбрана неверная операция! \n\terror 010.")

