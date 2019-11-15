import os

cliente=os.sys.argv[1]
monto=float(os.sys.argv[2])

# Si el monto supera los 100 soles, mostrar tarjeta dorada
if ( monto > 100 ):
    print("Ud ha ganado la tarjeta Dorada")
if ( monto >= 90 and monto < 100):
    print("Ud casi casi gana la tarjeta")
if ( monto < 90):
    print("Vuelva pronto")

print(cliente)
print(monto)
