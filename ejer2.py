def tictac(n1,n2,n3):
    if(n1==111):
        return(1)
    if(n1==0):
        return(0)
    if(n2==111):
        return(1)
    if(n2==0):
        return(0)
    if(n3==111):
        return(1)
    if(n3==0):
        return(0)
    if(n1>99 and n2>99 and n3>99):
        return(1)
    if(n1<99 and n2<99 and n3<99):
        return(0)
    if(n1<99 and n2<99 and n3<99 and n1>9 and n2>9 and n3>9):
        return(1)
    if (n1<9 and n2<9 and n3<9):
        return(0)
    if(n1==1 and n2==1 and n3==1):
        return(1)
    if (n1==0 and n2==0 and n3==0):
        return(0)
    if(n1==100 and n2==10 and n3==1):
        return(1)
    if (n1<99 and (n2==101 or n2==1) and (n3==100 or n3==10)):
        return(0)
    if(n1%10==1 and (n2==10 or n2==111 or n2==110 or n2==11) and n3>99):
        return(1)
    if (n1==100 or n1==10)and(n2==101 or n2==1) and (n3==10 or n3==1):
        return(0)
    else: 
        return("Empate")
print(tictac(100,101,11))
