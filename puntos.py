import random as rd
import sys
from time import time

def S(n):
	return set(rd.randint(0,10000000) for x in range(n))

def primo(n,c):
	for x in range(1,len(c)*2):
		if x > 1: 
			for i in range(2,x):
				if (x % i) == 0:
					break
			else:
				if x > len(c):
					return x


def hash(a, b, p, m):
	return lambda k : ((a*k+b)%p)%m


def a_b(p):
	l = [x for x in range(p)]
	f = rd.sample(l,2)
	return f[0], f[1]

def h_buena(c,n):
	x=[]
	for i in range(n):
		x.append(c[i]**2)
	s = sum(x)
	print(s,4*n)
	if s < 4*n:
		return True
	return False

def buscar(x, h, t):
	i = h(x)
	try:
		a = t[i]['a']
		b = t[i]['b']
		m = t[i]['m']
		hi = hash(a,b,p,m)
		k = hi(x)
		if t[i]['S'][k] == x:
			print ("elemento",x,"en\nTabla 1 pos:",i,"\nTabla 2 pos:",k)
		else:
			print(x,"no existe en la tabla :|")
	except KeyError:
		print("KeyError:",x,"no existe en la tabla :(")
	
	
	

n = int(sys.argv[1])
#find = int(sys.argv[2])
m = n
conjunto = S(n)
#print(conjunto)
p = primo(n,conjunto)
tabla = [{} for x in range(n)]
m_i = []
sub_conj = {i:[] for i in range(n)}

#ini_t = time()
#determinar h de primer nivel
while 1:
	a,b = a_b(p)
	c = [0 for i in range(n)]
	m_i = []
	for k in conjunto:
		h = hash(a,b,p,m)
		i = h(k)
		c[i] = c[i] + 1
		sub_conj[i].append(k)
	if h_buena(c, n):
		for i in c:
			m_i.append(i**2)
		break



#elimina innecesarios
for i in range(n):
	if len(sub_conj[i])==0:
		del(sub_conj[i])

for i in range(n):
	if m_i[i] != 0:
		tabla[i]['m'] = m_i[i]
		tabla[i]['S'] = [None for i in range(m_i[i])]

ci = [] 
#determinar h_i para tabla de segundo nivel
for i in sub_conj:
	#print(sub_conj[i])
	while 1:
		a,b = a_b(p)
		m = tabla[i]['m']
		ci = [0 for x in range(m)]
		hi = hash(a,b,p,m)
		for k in sub_conj[i]:
			j = hi(k)
			tabla[i]['S'][j] = k
			if ci[j] == 0:
				ci[j] = 1
			elif ci[j] >= 1:
				ci[j] = -1
		if -1 not in ci:
			tabla[i]['a'] = a
			tabla[i]['b'] = b
			break

##buscar 10 numero aleatorios

ini_t = time()
for i in range(10):
	find = rd.choice(list(conjunto))	
	buscar(find,h,tabla)
total_t = time() - ini_t



print('{0} {1:.2f}'.format(len(tabla), total_t))