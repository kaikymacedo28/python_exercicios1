print(f"Programa de empréstimo"
      f"Responda: (0-Não ou 1-Sim)")
nome_negativando=int(input('Possui nome negativado?: '))
if nome_negativando == 1:
    print('Não pode realizar empréstimo')
else:
    carteira_assinada=int(input('Possui carteira assinada?: '))
    if carteira_assinada ==0:
        print('Não pode realizar empréstimo')
    else: 
        casa_propria=int(input('Possui casa própria?: '))
        if casa_propria == 0:
            print('Não pode realizar empréstimo')
        else:
            print('Conceder empréstimo')