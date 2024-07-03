user_text=input('ingrese una palabra')
inversa=''
for i in user_text:
    inversa=i+inversa
while True:
    if user_text==inversa:
        print('esta palabra es un palindromo')
        break
    else:
        print('esta palabra no es un palindromo')
        break