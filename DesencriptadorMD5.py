
import hashlib 

# inputs
Diccionary = input("Dirección del diccionario: ")
hash1 = input("Hash a traducir: ")

# leyendo archivo 
listaslineas = open(Diccionary,"r").readlines()

#bucle 
for i in range(0,len(listaslineas)): 
	hash2 = hashlib.md5(listaslineas[i].replace("\n","").encode()).hexdigest()

	#comparando
	if hash1 == hash2:
		print("Clave encontrada: "+listaslineas[i].replace("\n",""))
		exit()

print("Clave no encontrada")