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
	if s < 4*n:
		return True
	return False


n = 10
m = n
conjunto = [3, 10, 22, 37, 40, 52, 60, 70, 82, 95]
p = primo(n)
tabla = [{} for x in range(n)]
m_i = []

while 1:
	a,b = a_b(p)
	c = [0 for i in range(n)]
	m_i = []
	for k in conjunto:
		h = hash(a,b,p,m)
		i = h(k)
		c[i] = c[i] + 1
	if h_buena(c, n):
		for i in c:
			m_i.append(i**2)
		break


for i in range(n):
	if m_i[i] != 0:
		tabla[i]['m'] = m_i[i]
		tabla[i]['S'] = [0 for i in range(m_i[i])]


#insertar
for i in range(len(conjunto)):
	k = conjunto[i]
	a,b = a_b(p)
	if m_i[i] != 0:
		hi = hash(a,b,p,m_i[i]) ##continuar aquí
		if tabla[h(k)]['S'][hi(k)] == 0:
			print(hi(k))
			tabla[h(k)]['S'][hi(k)] = k
	


#print(conjunto)

print(tabla)
#print(c)
#print(m_i)

