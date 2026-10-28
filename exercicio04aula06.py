print("O maior de 3 números")
num1=int(input("Primeiro Número: "))
num2=int(input("Segundo Número: "))
num3=int(input("Terceiro Número: "))
if num1>=num2:
    numgain=num1
else:
    numgain=num2
if numgain>=num3:
    numvence=numgain
else:
    numvence=num3
print(f"O maior de {num1}, {num2} e {num3} é: {numvence}")
