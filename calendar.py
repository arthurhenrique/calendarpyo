def qtd_dia(dia, mes, ano):
    #VARIAVEIS
    dia_contado = 0
 
    #CALCULO DIA
    dia_contado+=dia
 
    #CALCULO MÊS
    #1  jan 31
    #2  fev 28 | 29
    #3  mar 31
    #4  abr 30
    #5  mai 31
    #6  jun 30
    #7  jul 31
    #8  ago 31
    #9  set 30
    #10 out 31
    #11 nov 30
    #12 dez 31
   
    # O modelo de condições a abaixo, e.g: mes>n, onde n é
    # o número referente ao mês, impede que adicione a qtd de dias
    # do mês inteiro,
    # EVITANDO o problema de entrada, como:
    # dia 2, mes 1
    # retorno 2 + 31  = 33
    #
    # passando a ser:
    #
    # retorno 2 + 0   = 2
 
    if mes>1:
        dia_contado+=31
    if mes>2 and ano%4==0: #se ano bissexto acrescenta + 1
        dia_contado+=29
    if mes>2 and ano%4!=0:
        dia_contado+=28
    if mes>3:
        dia_contado+=31
    if mes>4:
        dia_contado+=30
    if mes>5:
        dia_contado+=31
    if mes>6:
        dia_contado+=30
    if mes>7:
        dia_contado+=31
    if mes>8:
        dia_contado+=31
    if mes>9:
        dia_contado+=30
    if mes>10:
        dia_contado+=31
    if mes>11:
        dia_contado+=30
    if mes>12:
        dia_contado+=31
           
    #CALCULO ANO
 
    # Contagem de ano caso bissexto ou não,
    # retirando 1 logo do começo do loop, pois o ano atual não
    # não conta.
    # O loop termina assim que o ano for maior que 1, pois 0 não é ano.
 
    i   = ano
    while i > 1:
        i-=1
        if i%4==0:
            dia_contado+=366
        else:
            dia_contado+=365
       
    return dia_contado
 
 
#VETOR CUJO A VARIAVEL dia_mes É EXPLORADA
meses = [31,28,31,30,31,30,31,31,30,31,30,31]
 
 
#ENTRADA
#dia = 1
#mes = 1
ano = 2020
 
#SAIDA
print ("        ",ano,"        ")
for m in range(1,12 + 1):  # + 1, pois range vai de 1 a n + 1
    print ("\n")
    print ("      --",m,"--    ")
    print ("d  s  t  q  q  s  s")
 
    if m == 2 and ano%4==0:
        dia_mes = 29
    else:
        dia_mes = meses[m-1]
 
    for d in range (1,dia_mes + 1):
 
        if d==1 and qtd_dia(1,m,ano)%7==2:
            print ("   ",end ='')
        if d==1 and qtd_dia(1,m,ano)%7==3:
            print ("      ",end ='')
        if d==1 and qtd_dia(1,m,ano)%7==4:
            print ("         ",end ='')
        if d==1 and qtd_dia(1,m,ano)%7==5:
            print ("            ",end ='')
        if d==1 and qtd_dia(1,m,ano)%7==6:
            print ("               ",end ='')
        if d==1 and qtd_dia(1,m,ano)%7==0:
            print ("                  ",end ='')
           
        if qtd_dia(d,m,ano)%7==1:
            print ('%(d)02d' %  {'d':d},end =' ')
        if qtd_dia(d,m,ano)%7==2:
            print ('%(d)02d' %  {'d':d},end =' ')
        if qtd_dia(d,m,ano)%7==3:
            print ('%(d)02d' %  {'d':d},end =' ')
        if qtd_dia(d,m,ano)%7==4:
            print ('%(d)02d' %  {'d':d},end =' ')
        if qtd_dia(d,m,ano)%7==5:
            print ('%(d)02d' %  {'d':d},end =' ')
        if qtd_dia(d,m,ano)%7==6:
            print ('%(d)02d' %  {'d':d},end =' ')
        if qtd_dia(d,m,ano)%7==0:
            print ('%(d)02d' %  {'d':d},"\n")
