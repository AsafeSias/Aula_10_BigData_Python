def calcula_atingimento(v, m):
    r = v / m
    return r * 100

for num in range (1, 2):
    try:
        venda = float(input('Informe o valor da venda: '))
        meta = float(input("Informe a meta: "))
        resultado = calcula_atingimento(venda, meta)
        
    except (ValueError, TypeError):
        print('Erro! \nDigite apenas números')
    except ZeroDivisionError:
        print('Erro! \nA meta não pode ser zero')
        exit()
    except KeyboardInterrupt:
        print('O usuário interrompeu a execução')
    else:
        print (f'Resultado: {resultado}%')
    finally:
        print('Operação Finalizada.')
    


#try
#except