listaA = [1,2]
listaB = [1,1,1,2,1,1,2]
listaAB = [listaA,listaB]

CA = set(listaA)
CB= set(listaB)
CD = (CA, CB)

print ('##### LISTAS #####')
print (listaA)
print (listaB)
print (listaAB)

print ('##### CONJUNTOS #####')
print ("CA: ",CA)
print ("CB: ",CB)
print("CD: ",CD)

print()
print ("######################")
print ('##### CONJUNTOS ######')
print ("######################")
print()

print('##### IGUALDADE #####')
if CA==CB:
    print ('Os conjuntos CA:',CA,' e CB:',CB,' são iguais')
else:
    print('Os conjuntos CA:',CA,' e CB:',CB,' NAO são iguais')

validar = 1
for ca1 in CA:
    if (validar==1):
            validar =0
            for cb1 in CB:
                if ca1 == cb1:
                    validar = 1 #achou igual
                    break
    else:
        break
    
print()
print ('#####  SUBCONJUNTO #####')
if(validar == 1):
    print('CA é um subconjunto de CB')
elif(validar == 0):
    print('CA não é subconjunto de CB')
    
print()
print ('##### CONTINÊNCIA #####')
if(validar == 1 and len(CB)>len(CA)):
    print ('CA:',CA,'é subconjunto próprio de CB:',CB)
elif(CB==CA):
    print ('CA:',CA,' é subjunto ou igual a CB:',CB)
else:
    print('Não há continência')
print()
print ('##### PERTINÊNCIA #####')
#verificando pertinencia em conjuntos
num = 1
if num in CA:
    print(num , ' pertence a CA')
else:
    print(num, 'não pertence a CA')
if num in CB:
    print(num , ' pertence a CB')
else:
    print(num, 'não pertence a CB')
if num in CD:
    print(num , ' pertence a CD')
else:
    print(num, 'não pertence a CD')
num = CA
if num in CD:
    print(num , ' pertence a CD')
else:
    print(num, 'não pertence a CD')

print()
print()
print ("###################")
print ('##### LISTAS ######')
print ("###################")
print()

print('##### IGUALDADE #####')
if listaA==listaB:
    print ('listas são iguais')
else:
    print('listas diferentes')

validar = 1
for ca1 in listaA:
    if (validar==1):
            validar =0
            for cb1 in listaB:
                if ca1 == cb1:
                    validar = 1 #achou igual
                    break
    else:
        break
    
print()
print ('#####  SUBCONJUNTO #####')
if(validar == 1):
    print('listaA é um sublista de listaB')
elif(validar == 0):
    print('listaA NÃO é sublista listaB')
    
print()
print ('##### CONTINÊNCIA #####')
if(validar == 1 and len(listaB)>len(listaA)):
    print ('listaA:',listaA,'é sublista próprio de listaB:',listaB)
elif(CB==CA):
    print ('listaA:',listaA,' é subjunto ou igual a listaB:',listaB)
else:
    print('Não há continência')
print()
print()
print ('##### PERTINÊNCIA #####')
#verificando pertinencia em conjuntos
num = 1
if num in listaA:
    print(num , ' pertence a listaA')
else:
    print(num, 'não pertence a listaA')
if num in listaB:
    print(num , ' pertence a listaB')
else:
    print(num, 'não pertence a listaB')
if num in listaAB:
    print(num , ' pertence a listaAB')
else:
    print(num, 'não pertence a listaAB')
num = listaA
if num in listaAB:
    print(num , ' pertence a listaAB')
else:
    print(num, 'não pertence a listaAB')
