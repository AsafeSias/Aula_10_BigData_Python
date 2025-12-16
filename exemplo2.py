lst_vendas =  []
resposta = 's'
venda = 1
tentativa = 1

while resposta != 'n':
    try:
        valor = float(input(f'informe a {venda}ª venda:'))
    except ValueError:
        print('Informe apenas números: ')
    except KeyboardInterrupt:
        print('\nUsuário encerrou.')
        break
    else:
        lst_vendas.append(valor)
        resposta = input('Deseja continuar? [s/n]')[0].lower()
        venda += 1
        print()
    finally:
        print(f'tentativa {tentativa}')
        tentativa += 1

print(f'O valor das vendas é:{lst_vendas}')