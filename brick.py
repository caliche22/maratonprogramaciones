from sys import stdin
global num

dic = {}
def solve(x):
	temp = 1
	aux = 0
	auxb = 0
	for i in range(int(x)):
		auxb = temp
		temp = temp + aux
		aux = auxb
	return temp


def main():
   inp = stdin
   num = inp.readline().split() 
   while int(num[0])!= 0:
   	print(solve(num[0]))
   	num = inp.readline().split()
   	 

main()