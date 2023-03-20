usuario = {}
nombre = input("introduce tu nombre: ")
apellido = input("introduce tu apellido: ")

usuario['nombre'] = nombre
usuario['apellido'] = apellido

print(usuario)
print(usuario.get("edad", 'No existe todavia'))
dato = usuario['nombre']
assert dato is not None, 'No existe'
print("---------------------------------------")
for name, surname in usuario.items():
    print(f"{name} : {surname}")

