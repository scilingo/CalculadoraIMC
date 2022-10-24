print("Bem-vindo(a) a sua calculadora de IMC!")
nome = input("Digite seu nome: ")
genero = input("Digite seu gênero (M ou F): ")
peso = int(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura: "))

IMC = (peso / altura ** 2)
print("Seu imc é de %s" % IMC)


def resultados_m():
    if IMC < 20:
        print("A classificação do seu IMC está abaixo do normal.")
    elif 20 <= IMC < 25:
        print("A classificação do seu IMC está normal/saudável.")
    elif 25 <= IMC < 30:
        print("A classificação do seu IMC indica obesidade leve.")
    elif 30 <= IMC < 40:
        print("A classificação do seu IMC indica obesidade moderada.")
    elif IMC >= 40:
        print("A classificação do seu IMC indica obesidade mórbida.")


def resultados_f():
    if IMC < 19:
        print("A classificação do seu IMC está abaixo do normal.")
    elif 19 <= IMC < 24:
        print("A classificação do seu IMC está Normal/Saudável.")
    elif 24 <= IMC < 29:
        print("A classificação do seu IMC indica obesidade leve.")
    elif 29 <= IMC < 39:
        print("A classificação do seu IMC indica obesidade moderada.")
    elif IMC >= 39:
        print("A classificação do seu IMC indica obesidade mórbida.")


if genero == "M":
    resultados_m()
elif genero == "F":
    resultados_f()
