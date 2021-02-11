




"""Programa Logica Difusa
	4 Variables
	Temperatura = T
	Corriente = I
	Velocidad = Vel
	Vibracion = Vx, Vy, Vz

"""

def FPT_Corriente(x):
	Se="Corriente"
	if x<=3:
		a=0
		b=0
		c=2.5
		d=3
		IB="BAJO"
		FPB=Trapecio(x,a,b,c,d)
	else: 
		IB=''
		FPB=0
	
	if x>=2.5 and x<=4:
		a=2.5
		b=3.5
		c=4
		IM="MEDIO"
		FPM=Triangulo(x,a,b,c)
	else: 
		IM=''
		FPM=0
	
	if x>=3.7:
		a=3.7
		b=4.5
		c=0
		d=0
		IA="ALTO"
		FPA=Trapecio(x,a,b,c,d)
	else: 
		IA=''
		FPA=0

	FB=[IB,FPB,IM,FPM,IA,FPA,Se]
	return FB

def FPT_Temperatura(y):
	Se="Temperatura"
	if y<=15:
		a=0
		b=0
		c=10
		d=15
		TB="BAJO"
		FPB=Trapecio(y,a,b,c,d)
	else: 
		TB=''
		FPB=0

	if y>=10 and y<=30:
		a=10
		b=20
		c=30
		TM="MEDIO"
		FPM=Triangulo(y,a,b,c)
	else: 
		TM=''
		FPM=0

	if y>=28:
		a=28
		b=45
		c=0
		d=0
		TA="ALTA"
		FPA=Trapecio(y,a,b,c,d)
	else: 
		TA=''
		FPA=0	

	FY=[TB,FPB,TM,FPM,TA,FPA,Se]
	return FY

def FPT_Velocidad(v):
	Se="Velocidad"
	if v<=900:
		a=0
		b=0
		c=700
		d=900
		VB="BAJO"
		FPB=Trapecio(v,a,b,c,d)
	else: 
		VB=''
		FPB=0

	if v>=700 and v<=1800:
		a=700
		b=1100
		c=1800
		VM="MEDIO"
		FPM=Triangulo(v,a,b,c)
	else: 
		VM=''
		FPM=0

	if v>=1500:
		a=1500
		b=2600
		c=0
		d=0
		VA="ALTA"
		FPA=Trapecio(v,a,b,c,d)
	else: 
		VA=''
		FPA=0	

	FV=[VB,FPB,VM,FPM,VA,FPA,Se]
	return FV

def FPT_VibracionXY(hx):
	Se="Vibracion"
	if hx<=50:
		a=0
		b=0
		c=35
		d=50
		viB="BAJO"
		FPB=Trapecio(hx,a,b,c,d)
	else: 
		viB=''
		FPB=0

	if hx>=30 and hx<=450:
		a=30
		b=210
		c=450
		viM="MEDIO"
		FPM=Triangulo(hx,a,b,c)
	else: 
		viM=''
		FPM=0

	if hx>=400:
		a=400
		b=1000
		c=0
		d=0
		viA="ALTA"
		FPA=Trapecio(hx,a,b,c,d)
	else: 
		viA=''
		FPA=0	

	FVi=[viB,FPB,viM,FPM,viA,FPA,Se]
	return FVi

def FPT_VibracionZ(hz):
	Se="Vibracion Z"
	if hz<=30:
		a=0
		b=0
		c=15
		d=30
		viB="BAJO"
		FPB=Trapecio(hz,a,b,c,d)
	else: 
		viB=''
		FPB=0

	if hz>=15 and hz<=60:
		a=15
		b=37.5
		c=60
		viM="MEDIO"
		FPM=Triangulo(hz,a,b,c)
	else: 
		viM=''
		FPM=0

	if hz>=40:
		a=40
		b=100
		c=0
		d=0
		viA="ALTA"
		FPA=Trapecio(hz,a,b,c,d)
	else: 
		viA=''
		FPA=0	

	FVi=[viB,FPB,viM,FPM,viA,FPA,Se]
	return FVi


def Comparativo(C):
	if (C[0]!='' and C[2]!=''):
		if C[1]>C[3]:
			#print ("\nDos Funciones de Pertencias de "+C[6]+ " Activas: "+C[0]+"/"+C[2]+" Mayor", C[0] )
			Fuzzy= C[0] #Termino Linguistico
		else:
			#print ("\nDos Funciones de Pertencias de "+C[6]+ " Activas: "+C[0]+"/"+C[2]+" Mayor=", C[2] )
			Fuzzy= C[2] #Termino Linguistico

	if (C[2]!='' and C[4]!=''):
		if C[3]>C[5]:
			#print ("\nDos Funciones de Pertencias de "+C[6]+ " Activas: "+C[2]+"/"+C[4]+" Mayor=", C[2] )
			Fuzzy= C[2] #Termino Linguistico
		else:
			#print ("\nDos Funciones de Pertencias de "+C[6]+ " Activas: "+C[2]+"/"+C[4]+" Mayor=", C[4] )
			Fuzzy= C[4] #Termino Linguistico
	
	elif C[0]!=''and C[2]==''and C[4]=='':
		#print ("\nUna Funcion de Pertenencia Activa:",C[6],C[0] )
		Fuzzy= C[0] #Termino Linguistico
	elif C[2]!=''and C[0]==''and C[4]=='':
		#print ("\nUna Funcion de Pertenencia Activa:",C[6],C[2] )
		Fuzzy= C[2] #Termino Linguistico
	elif C[4]!=''and C[0]==''and C[2]=='':
		#print ("\nUna Funcion de Pertenencia Activa:",C[6],C[4] )
		Fuzzy= C[4] #Termino Linguistico

	return Fuzzy


def ReglasI(RC,RI):#Y=temperatura; X=Corriente
	if RC=='BAJO' and RI=='BAJO':
		print("Corriente:     NORMAL")
	elif RC=='MEDIO' and RI=='BAJO':
		print("Corriente:     POSIBLE ANOMALIA")
	elif RC=='ALTA' and RI=='BAJO':
		print("Corriente:     POSIBLE ANOMALIA")

	elif RC=='BAJO' and RI=='MEDIO':
		print("Corriente:     NORMAL")
	elif RC=='MEDIO' and RI=='MEDIO':
		print("Corriente:     NORMAL")
	elif RC=='ALTA' and RI=='MEDIO':
		print("Corriente:     MAL FUNCIONAMIENTO")

	elif RC=='BAJO' and RI=='ALTO':
		print("Corriente:     NORMAL")
	elif RC=='MEDIO' and RI=='ALTO':
		print("Corriente:     POSIBLE ANOMALIA")
	elif RC=='ALTA' and RI=='ALTO':
		print("Corriente:     FALLO")

def ReglasT(RC,RI):#Y=temperatura; X=Corriente
	if RC=='BAJO' and RI=='BAJO':
		print("Temperatura:   NORMAL")
	elif RC=='MEDIO' and RI=='BAJO':
		print("Temperatura:   POSIBLE ANOMALIA")
	elif RC=='ALTA' and RI=='BAJO':
		print("Temperatura:   POSIBLE ANOMALIA")

	elif RC=='BAJO' and RI=='MEDIO':
		print("Temperatura:   NORMAL")
	elif RC=='MEDIO' and RI=='MEDIO':
		print("Temperatura;   NORMAL")
	elif RC=='ALTA' and RI=='MEDIO':
		print("Temperatura:   MAL FUNCIONAMIENTO")

	elif RC=='BAJO' and RI=='ALTO':
		print("Temperatura:   NORMAL")
	elif RC=='MEDIO' and RI=='ALTO':
		print("Temperatura:   POSIBLE ANOMALIA")
	elif RC=='ALTA' and RI=='ALTO':
		print("Temperatura:   FALLO")

def ReglasV(RC,RI):#V=velocidad; X=Corriente
	if RC=='BAJO' and RI=='BAJO':
		print("Velocidad:     NORMAL")
	elif RC=='MEDIO' and RI=='BAJO':
		print("Velocidad:     NORMAL")
	elif RC=='ALTA' and RI=='BAJO':
		print("Velocidad:     FALLO")

	elif RC=='BAJO' and RI=='MEDIO':
		print("Velocidad:     POSIBLE ANOMALIA")
	elif RC=='MEDIO' and RI=='MEDIO':
		print("Velocidad:     NORMAL")
	elif RC=='ALTA' and RI=='MEDIO':
		print("Velocidad:     MAL FUNCIONAMIENTO")

	elif RC=='BAJO' and RI=='ALTO':
		print("Velocidad:     FALLO")
	elif RC=='MEDIO' and RI=='ALTO':
		print("Velocidad:     POSIBLE ANOMALIA")
	elif RC=='ALTA' and RI=='ALTO':
		print("Velocidad:     NORMAL")

def ReglasViX(RC,RI):#hx=vibracionX; hy=VibracionY
	if RC=='BAJO' and RI=='BAJO':
		print("Vibracion ejex:    NORMAL")
	elif RC=='MEDIO' and RI=='BAJO':
		print("Vibracion ejex:    MAL FUNCIONAMIENTO")
	elif RC=='ALTA' and RI=='BAJO':
		print("Vibracion ejex:    POSIBLE ANOMALIA")

	elif RC=='BAJO' and RI=='MEDIO':
		print("Vibracion ejex:    MAL FUNCIONAMIENTO")
	elif RC=='MEDIO' and RI=='MEDIO':
		print("Vibracion ejex:    NORMAL")
	elif RC=='ALTA' and RI=='MEDIO':
		print("Vibracion ejex:    POSIBLE ANOMALIA")

	elif RC=='BAJO' and RI=='ALTO':
		print("Vibracion ejex:    POSIBLE ANOMALIA")
	elif RC=='MEDIO' and RI=='ALTO':
		print("Vibracion ejex:    POSIBLE ANOMALIA")
	elif RC=='ALTA' and RI=='ALTA':
		print("Vibracion ejex:    FALLO")

def ReglasViY(RI,RC):#hx=vibracionX; hy=VibracionY
	if RC=='BAJO' and RI=='BAJO':
		print("Vibracion ejeY:    NORMAL")
	elif RC=='MEDIO' and RI=='BAJO':
		print("Vibracion ejeY:    MAL FUNCIONAMIENTO")
	elif RC=='ALTA' and RI=='BAJO':
		print("Vibracion ejeY:    POSIBLE ANOMALIA")

	elif RC=='BAJO' and RI=='MEDIO':
		print("Vibracion ejeY:    MAL FUNCIONAMIENTO")
	elif RC=='MEDIO' and RI=='MEDIO':
		print("Vibracion ejeY:    NORMAL")
	elif RC=='ALTA' and RI=='MEDIO':
		print("Vibracion ejeY:    POSIBLE ANOMALIA")

	elif RC=='BAJO' and RI=='ALTO':
		print("Vibracion ejeY:    POSIBLE ANOMALIA")
	elif RC=='MEDIO' and RI=='ALTO':
		print("Vibracion ejeY:    POSIBLE ANOMALIA")
	elif RC=='ALTA' and RI=='ALTA':
		print("Vibracion ejeY:    FALLO")

def ReglasViZ(RC):#hx=vibracionX; hy=VibracionY
	if RC=='BAJO':
		print("Vibracion ejeZ:    NORMAL")
	elif RC=='MEDIO':
		print("Vibracion ejeZ:    MAL FUNCIONAMIENTO")
	elif RC=='ALTA':
		print("Vibracion ejeZ:    FALLO")

#Funcionciones de Pertenencia

def Trapecio(x,a,b,c,d):
	if c==0 and d==0:
		if x>=b:
			mt=1
		else:
			mt=(x-a)/(b-a)
	if a==0 and b==0:
		if x<=c:
			mt=1
		else:
			mt=(d-x)/(d-c)	
	
	return round(mt,4)

def Triangulo(x,a,b,c):
	if x==b:
		mu=1
	elif x>=a and x<b:
		mu=(x-a)/(b-a)
	elif x>b and x<=c:
		mu=(c-x)/(c-b)

	return round (mu,4)

##Entrada de Sensores
x =  float(input("\tIntroduce Corriente= "))
y =  float(input("\tIntroduce Tempereatura= "))
v =  float(input("\tIntroduce Velocidad= "))
hx = float(input("\tIntroduce Vibracion ejeX= "))
hy = float(input("\tIntroduce Vibracion ejeY= "))
hz = float(input("\tIntroduce Vibracion ejeZ= "))
##Funcion Principal

##Fuzificacion Corriente
X=FPT_Corriente(x)
#print (X)
XFuzzy=Comparativo(X)
print("\n"+X[6]+ " Defusificada = ", XFuzzy) #Comparativos

##Fuzificacion Temperatura
Y=FPT_Temperatura(y)
#print(Y)
YFuzzy=Comparativo(Y)
print("\n"+Y[6]+ " Defusificada = ", YFuzzy) #Comparativos

##Fuzificacion Velocidad
V=FPT_Velocidad(v)
#print(V)
VFuzzy=Comparativo(V)
print("\n"+V[6]+ " Defusificada = ", VFuzzy) #Comparativos

##Fuzificacion Vibracion X
Hx=FPT_VibracionXY(hx)
#print(Hx)
HxFuzzy=Comparativo(Hx)
print("\n"+Hx[6]+ " Defusificada = ", HxFuzzy) #Comparativos

##Fuzificacion Vibracion Y
Hy=FPT_VibracionXY(hy)
#print(Hy)
HyFuzzy=Comparativo(Hy)
print("\n"+Hy[6]+ " Defusificada = ", HyFuzzy) #Comparativos

##Fuzificacion Vibracion Z
Hz=FPT_VibracionZ(hz)
#print(Hz)
HzFuzzy=Comparativo(Hz)
print("\n"+Hz[6]+ " Defusificada = ", HzFuzzy) #Comparativos

print("\n|----ESTADO DE LA MAQUINA----|" ) #Comparativos

##Defuzificacion
ReglasI(YFuzzy,XFuzzy) #Y Corriente vs X Temperatura -> Corriente
ReglasT(YFuzzy,XFuzzy) #Y Temperatura vs X Corriente -> Temperatura
ReglasV(VFuzzy,XFuzzy) #V Velocidad vs X Corriente   -> Velocidad 
ReglasViX(HxFuzzy,HyFuzzy) #Hx VibracionX vs Hy VibracioY -> Vibracion 
ReglasViY(HyFuzzy,HxFuzzy) #Hy VibracionY vs Hx VibracioZ -> Vibracion 
ReglasViZ(HzFuzzy) #Hz VibracioZ -> Vibracion 
print("\n|------------------------------|" ) #Comparativos







