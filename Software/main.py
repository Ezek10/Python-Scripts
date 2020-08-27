"""[summary] 
    la consigna va a ser que te mandes un mail con un asunto 
    aleatorio de 13 digitos y de mensaje los ascii que sean numeros impares.
    si le queres hacer un plus
    podes adjuntar un archivo
"""

import randomizer as rnd
import enviarmail as em

largo = 13
asu = rnd.digit_random_string(largo)
print("Random string of length", largo, "is:", asu)
result_list = []
for i in range(0, largo):
    a = int(asu[i])
    print(a)
    if a == 1:
        result_list.append(a)
    elif a == 3:
        result_list.append(a)
    elif a == 5:
        result_list.append(a)
    elif a == 7:
        result_list.append(a)
    elif a == 9:
        result_list.append(a)
print(result_list)
numeritos = str(result_list)
msj = "Los numeros impares del asunto son:" + numeritos
em.mail(msj, asu)