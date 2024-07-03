print('elige una opcion: ')
print('1. codificar un mensaje')
print('2. decodificar un mensaje')
print('3. contar frecuencia de letras en el mensaje codificado')
print('4. salir')
opcion=int(input('opcion: '))
abc='ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
primos=[1]
numero=1
while numero<=102:
    contador_1=1
    contador_2=0
    while contador_1<=numero:
        if numero%contador_1==0:
            contador_2+=1
        contador_1+=1
    if contador_2==2:
        primos.append(numero)
    numero+=1
if opcion==1:
    user_text_1=input('ingrese un texto para codificar: ')
    dict_1={}
    for i in range(len(abc)):
        dict_1[abc[i]]=primos[i]
    for letra_1 in suer_text:
print()