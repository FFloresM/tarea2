import random as rd

def S(n):
	return set(rd.randint(0,1000) for x in range(n))

def primo(n):
	for x in range(1,n*n):
		if x > 1: 
			for i in range(2,x):
				if (x % i) == 0:
					break
			else:
				if x > n:
					return x


def hash(k, a, b, p, m):
	return ((a*k+b)%p)%m


def a_b(p):
	l = [x for x in range(p)]
	f = rd.sample(l,2)
	return f[0], f[1]

def h_buena(c,n):
	x=[]
	for i in range(n):
		x.append(c[i]**2)
	s = sum(x)
	if s < 4*n:
		return True
	return False


n = 10
m = n
conjunto = S(n)
p = primo(n)
tabla = [{} for x in range(n)]
count = 0

while 1:
	a,b = a_b(p)
	c = [0 for i in range(n)]
	for k in conjunto:
		i = hash(k,a,b,p,m)
		tabla[i] = k
		c[i] = c[i] + 1
	##print(a,b) funciona
	if h_buena(c, n):
		break

print(conjunto)
print(tabla)
print(c)

