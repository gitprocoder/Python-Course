def Converter(C):
    F = C * 9 / 5 + 32
    return(F)

C=int(input("Enter Temperature In Celsius:"))
print(Converter(C))

def DeConverter(F):
    C =  5/9 *(F- 32)
    return(C)

C=int(input("Enter Temperature In Farehnite:"))
print(DeConverter(C))