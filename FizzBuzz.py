#python 3.7.2
import msvcrt

# ''' FizzBuzz
#Imprimir los números del 0 al 99. Si el número es divisible por 3 imprimir “Fizz” en vez del número.
# Si el número es divisible es por 5 imprimir “Buzz” en vez del número. Si el número es divisible por
#5 y 3 debe imprimir “FizzBuzz” en vez del número.'''

try:
  print("=====FizzBuzz=====")
  res =""
  for i in range(100):
    if i % 3 == 0: res = "Fizz"
    if i % 5 == 0: res = res + "Buzz"
    if res == "" or i==0: res = i
    print(res)
    res = ""

except:
  print("An exception occurred: ") 

msvcrt.getch()
