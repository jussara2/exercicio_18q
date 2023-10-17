 PH = float(input('digite quanto voce ganha por hora:'))
HT = float(input('digite quantas horas voce trabalhou esse mes:'))
SB = PH*HT
IR = SB*(11/100)
INSS = SB*(8/100)
SIN = SB*(5/100)
SL = SB - IR - INSS - SIN
print('salario bruto:R${}\n IR (11%):R${}\n INSS (8%): R${}\n sindicato (5%):R${}\n salario liquido:R${}'.format(SB,IR,INSS,SIN,SL))