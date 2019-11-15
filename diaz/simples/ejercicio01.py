import os

cliente=os.sys.argv[1]
monto=float(os.sys.argv[2])

# Si el monto supera los 100 soles, mostrar tarjeta dorada
if ( monto > 100 ):
    print("Ud ha ganado la tarjeta Dorada")
#fin_if

print(cliente)
print(monto)
