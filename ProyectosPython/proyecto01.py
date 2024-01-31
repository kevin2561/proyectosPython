import string
import random
longitud= int(input("Ingrese su logintud de contraseña:  "))
caracteres= string.ascii_letters + string.digits + string.punctuation
contraseña = "".join(random.choice(caracteres) for i in range(longitud))
print(f"La contraseña generadas es   {contraseña}")
x= 5 + 5
print("La Rama secundaria estamos")
