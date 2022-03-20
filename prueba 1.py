from csv import Dialect


fecha1 = int("ingresar la primera fecha")  
fecha2 = int("ingrsar la segunda fecha")
ano_fecha1 = fecha1//10000
ano_fecha2 = fecha2//10000
dia_fecha1 = fecha1%100
dia_fecha2 = fecha2%100 
print(Dia_fecha1, dia_fecha2) 
k = 0 
while k < 3:
     
    mes_fecha1 = fecha1%10
    mes_fecha2 = fecha2%10
    fecha1 = (fecha1-mes_fecha1)//10
    fecha2 = (fecha2.mes_fecha2)//10
     k = k+1 
if  (mes_fecha1 < mes_fecha2)
     anofinal = ano_fecha2-ano_fecha1
else:
    anofinal1 = (ano_fecha2-ano_fecha1)-1
if (mes_fecha1 > mes_fecha2):
    mesfinal = (mes_fecha2+12)-mes_fecha1
elif (mes_fecha1 == mes_fecha2):
    mesfinal = 0 
else:
    mesfinal = (mes_fecha1+12)-mes_fecha2
if (dia_fecha1 > dia_fecha2):
    diafinal = dia_fecha1-dia_fecha2
else diafinal = dia_fecha2-dia_fecha1
fechafinal = ((anofinal*100)+mesfinal)
 fechafinal = ((anofinal*100)+diafinal)
 print(fechafinal)