# ATIVIDADE 01

def soma_pares(v1, v2):
    soma = v1 + v2
    return soma

lst_pares = []

for v in range(3):
    try:
        valor1 = float(input('Informe o primeiro valor: '))
        valor2 = float (input('Informe o segundo valor: '))    
    except (ValueError, TypeError):
        print('Informe apenas números')
        break
    except KeyboardInterrupt:
        print('Finalizado pelo usuário')
    else:
        soma = soma_pares(valor1, valor2)
        lst_pares.append(soma)
print(lst_pares)
