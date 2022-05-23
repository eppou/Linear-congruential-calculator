#---------------------------------------FUNÇÃO PRINTA VALORES---------------------------------------------------#
def PrintValores(texto,value1,value2):
    print(texto,value1,value2)

#----------------------------------------FUNÇÂO CALCULA MDC-----------------------------------------------------#

def CalculaMDC(value1,value2):
    while value2 !=0:
        resto = int(value1) % int(value2)
        value1=value2
        value2=resto
    
    return (value1)
#----------------------------------------MAIN------------------------------------------------------#

value1 = input("coloque o primeiro valor: ")
value2 = input("coloque o segundo valor: ")
PrintValores('\nOs valores que verifiquei a congruencia são',value1,value2)
mdc=CalculaMDC(value1,value2)
print("\nMDC=",mdc)