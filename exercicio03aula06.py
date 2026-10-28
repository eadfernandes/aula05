x=int(input("Quantidade de Testes: "))
x=x+1
for i in range (1,x):
    nome=input(f"{i}º Nome: ")
    sal= float(input(f"{i}º Salário: "))
    if sal>=5000:
        desc=sal*0.14
    elif sal>=4000:
        desc=sal*0.12
    elif sal>=2000:
        desc=sal*0.11
    else:
        desc=sal*0.09
    salfinal=sal-desc
    print(f"Salário Bruto: {sal:.2f}")
    print(f"Desconto: {desc:.2f}")
    print(f"Salário Final: {salfinal:.2f}")
print("\nFim do Programa")