import random as rd

def S(n):
	return set(rd.randint(0,1000) for x in range(n))

def primo(n,c):
	for x in range(1,max(c)**2):
		if x > 1: 
			for i in range(2,x):
				if (x % i) == 0:
					break
			else:
				if x > max(c):
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
p = primo(n,conjunto)
tabla = [{} for x in range(n)]
m_i = []
sub_conj = {i:[] for i in range(n)}

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
			elif ci[j] == 1:
				ci[j] = -1
		if -1 not in ci:
			tabla[i]['a'] = a
			tabla[i]['b'] = b
			break
		
print(tabla)


