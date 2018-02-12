from sys import stdin


global num1,num2, dic
primos = [2]

def voltearNumero(x):
	j = str(x)
	u = [int(n) for n in j]
	contador = 0
	suma = 0
	flag = 0
	while contador < len(u)-1:
		k = u.pop(0)
		u.append(k)
		h =''.join(str(e) for e in u)
		
		contador = contador + 1
	return 1

def solve(x,y):
	cont = x
	flag = 0
	cont2 = 0
	numPrim  = 0
	while cont < y:
		h = cont
		cont2= 0
		while generarl(h) == 1:
			h = voltearNumero(h)
			cont2+=1
		if cont2 == len(str(cont)):
			numPrim +=1

def esPrimo(x):
	for j in range(2,i):
		if(i%j)==0:
			flag = 1
			break
	if flag == 0:
		dic[i] = 1
		return 1
	return 0



def generarPrimos(l,r):
	global dic
	for i in range(l,r):
		flag = 0
		for j in range(2,i):
			if(i%j)==0:
				flag = 1
				break
		if flag == 0:
			dic[i] = 1
	print(dic)

def  generarl(x):
	if dic.get(x) == 1:
		print("esPrimo")
		return 1
	else:
		if esPrimo(x) == 1:
			return 1
	return 0






def main():
  inp = stdin
  cas = 1
  num1 = 0
  num = tuple()
  ans1 = 0
  while num1 != -1:
  	x = [inp.readline().split() ]
  	if int(x[0][0]) ==-1: break
  	num1 = int(x[0][0]) 
  	num2 = int(x[0][1])
  	ans1 = solve(num1,num2)
  	if ans1 ==0:
  		print("No Circular Primes.")
  	elif ans1 == 1:
  		print("1 Circular Prime.")
  	else:
  		print(ans1,"Circular Primes.")
  	

dic = {}
generarPrimos(100,10000)
main()