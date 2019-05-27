import os
"""
exist = os.path.isfile("t_crear_tabla")
if exist:
	os.remove('t_crear_tabla')
for i in range(1,21):
	n = 2**i
	cmd = 'python3 puntos.py {} 8'.format(n)
	cmd = cmd+' >> t_crear_tabla'
	#print(cmd)
	os.system(cmd)
"""
exist = os.path.isfile("t_busqueda_ale")
if exist:
	os.remove('t_busqueda_ale')
for i in range(1,21):
	n = 2**i
	cmd = 'python3 puntos.py {}'.format(n)
	cmd = cmd+' >> t_busqueda_ale'
	#print(cmd)
	os.system(cmd)