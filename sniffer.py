
from socket import*
from datetime import*

IPv4 = "172.31.12.72"
Port = 62150

Server = socket(AF_INET, SOCK_DGRAM)
Server.bind((IPv4,Port))

"""Esto para llevar un control de los mensajes recibidos"""
Cont = 0

"""**************************************************************"""
Espacio = ' '
Separador ='***************************************'
Cabecera = '************* New Report! *************'
Contenido = 'Contenido: '
Info = '******** Información Detallada ********'
Report = 'Report N°: '
"""**************************************************************"""

while True: 
	
	Cont = Cont + 1
	
	"""Extraemos la Data del mensaje que llega al puerto"""
	Data = Server.recvfrom(1024)
	
	"""Convertimos la Data a String para poder manipularla"""
	DataNew = str(Data)
	
	"""Comenzamos la interfaz"""
	print(Espacio)
	print(Separador)
	print(Cabecera)
	print("%s %.f" % (Report, Cont))
	print(Contenido)
	
	"""Mostramos el contenido del mensaje"""
	print(DataNew)
	
	print(Separador)
	
	
