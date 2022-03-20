
def anos_cumplidos (f1,f2):
    '''Seudocodigo:
    se establecen las variables:
    res igual 0
    cont igual a 1
    anos1 igual a f1 division entera entre 10 potencia 4
    anos2 igual a f2 division entera entre 10 potencia 4
    res igual a res
    difanos igual a anos2 menos anos1
    difanos igual adifanos*10**4
    res=res+difanos
    f1=f1%10**7
    f2=f2%10**7       
    f1=f1%10**6
    f2=f2%10**6
    f1=f1%10**5
    f2=f2%10**5
    f1=f1%10**4
    f2=f2%10**4
    temp1=f1//10**2
    temp2=f2//10**2
    difmes=temp2-temp1
    '''
    res=0
    cont=1
    anos1=f1//10**4
    anos2=f2//10**4
    res=res
    difanos=anos2-anos1
    difanos=difanos*10**4
    res=res+difanos
    f1=f1%10**7
    f2=f2%10**7       
    f1=f1%10**6
    f2=f2%10**6
    f1=f1%10**5
    f2=f2%10**5
    f1=f1%10**4
    f2=f2%10**4
    temp1=f1//10**2
    temp2=f2//10**2
    difmes=temp2-temp1
    if(difmes<0):
        difmes=abs(difmes)
        res=res-10000
    res=res+difmes*10**2
    f1=f1%10**3
    f2=f2%10**3
    f1=f1%10**2
    f2=f2%10**2
    difdia=f2-f1
    if(difdia<0):
        difdia=abs(difdia)
    res=res+difdia
    print(res)  

anos_cumplidos(19810807,20220314)





