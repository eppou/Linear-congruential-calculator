
#---------------------------------------FUNÇÃO PRINTA VALORES---------------------------------------------------#
def PrintValores(value1,value2,module_value):

    print("\nOs valores que verifiquei a congruencia são %s=%s, modulo %s" %(value1,value2,module_value))

#----------------------------------------FUNÇÂO CALCULA MDC-----------------------------------------------------#

def CalculaMDC(value1,module_value):

    while module_value !=0:
        resto = int(value1) % int(module_value)
        value1=module_value
        module_value=resto
    
    return (value1)

#----------------------------------------FUNÇÂO POSSIBILIDADE DE CL---------------------------------------------#

def Verifica(value2,mdc):

    if int (value2)%int (mdc) ==0:
        return (1)

    else:
        return(0)

#-----------------------------------LOOP BASEADO NO ALGORITMO DE EUCLIDES PARA ACHAR X0 Y0----------------------#
def Euclidean_algorithm(V1,V2):

    if int(V1) >= int(V2) and int(V2) >= 0 and int(V1)+int(V2)>0:

        if int(V2)==0:
            D,x,y = V1,1,0

        else:
            (D,P,Q) = Euclidean_algorithm(V2, int(V1)%int(V2))
            x=Q
            y=P-Q * (int(V1)//int(V2))
            
        assert int(V1) % int(D)==0 and int(V2) % int(D)==0
        return(D,x,y)
    else:
        print("alguma(s) das seguintes condiçoes para prosseguir calculando a equação diofantina não foram cumpridas, A>=B ou B>=0 ou A+B>0 ")


#----------------------------------------EQUAÇÂO DIOFANTINA-----------------------------------------------------#

def diophantine_equation(V1,V2,V3):
        if V1>V2:
            vetorResultados=Euclidean_algorithm(V1,V2)
            x1=vetorResultados[1]
            y1=vetorResultados[2]
        else:
            vetorResultados=Euclidean_algorithm(V1,V2)
            x1=vetorResultados[2]
            y1=vetorResultados[1]
        d=vetorResultados[0]
        if int(V3) % int(d)==0:
            p=int(V3)/int(d)
            return (int(p*x1),int(p*y1))
        else:
            print("não há solução para essa equação diofantina")





#----------------------------------------MAIN------------------------------------------------------#

#inserindo os valores da congruencia linear e printando eles

value1 = input("coloque o valor de A: ")
value2 = input("coloque o valor de B: ")
module_value = input("coloque o valor do Modulo: ")

PrintValores(value1,value2,module_value)

#PASSO 1-calculando MDC

mdc=CalculaMDC(value1,module_value)
print("\nMDC=",mdc)

#verificando se é possivel achar a congruencia linear
if Verifica(value2,mdc)==1:

    #PASSO 2-usando equação diofantina para achar o R
    D,X0,Y0= Euclidean_algorithm(value1,module_value)
    R,S = diophantine_equation(value1,module_value,mdc)

    #PASSO 3-calculando B1
    b1 = int(value2)/int(mdc)

    #PASSO 4-calculando o X0(caso particular)
    x = list(range(0,int(mdc)))
    x0= R*b1

    #PASSO 5-achando conjunto solução X
    for ind in range(int(mdc)):
        x[ind]=x0+ind*(int(module_value)/int(mdc))

    #FIM DO CALCULO, printando resultado
    print("\nO conjunto solução é:")
    print(x)

else:
    print ("não é possivel verificar a congruencia linear neste caso pois B não é divisivel pelo mdc(a,m)")

