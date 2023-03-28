numero1 = float(input('primeiro numero: '))
numero2 = float(input('segudo numero: '))

print('1 - soma')
print('2 - subtração')
print('3 - multiplicação')
print('4 - divisão')

opcao = int(input('escolha uma opção'))

if opcao == 1:
    resultado = numero1 + numero2
    print(f'A soma de {numero1} e {numero2} é {resultado}')
elif opcao == 2:
    resultado = numero1 - numero2
    print(f'A subtração de {numero1} e {numero2} é {resultado}')
elif opcao == 3:
    resultado = numero1 * numero2
    print(f'A multiplicação de {numero1} e {numero2} é {resultado}')
elif opcao == 4:
    if numero2 != 0:
        resultado = numero1 / numero2
        print(f'A divisão de {numero1} e {numero2} é {resultado}')
    else:
        print('Erro: não é possivel fazer divisão por zero')
else:
    print('Opção invalida')