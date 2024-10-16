cliente = {
    "nombre":"nicolas",
    "apellido": "ruiz",
    "edad": "21",
    "telefono":"3219393097",
    "saldo":"300.000"
}
print(cliente["nombre"])
cliente["profesion"] = "ingeniero"
del(cliente["telefono"])
print(cliente)
claves = cliente.keys ()
print(claves)
