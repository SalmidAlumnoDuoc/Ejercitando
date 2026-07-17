usuarios={
    "U01":["Salmid","Escobar",30,"salmid.escobar@gmail.com","123456"],
    "U02":["Ana","Gonzalez",25,"ana.gonzalez@gmail.com","654321"],
    "U03":["Carlos","Rodriguez",35,"carlos.rodriguez@gmail.com","987654"],
    "U04":["Maria","Lopez",28,"maria.lopez@gmail.com","456789"],
    "U05":["Juan","Martinez",32,"juan.martinez@gmail.com","321654"]
}

permisos={
    "U01":["admin","read","write"],
    "U02":["read"],
    "U03":["read","write"],
    "U04":["read"],
    "U05":["read","write"]
}

def menu():
    print('''============ Administrador de Usuarios ============
          1. Listar usuarios
          2. Agregar usuario
          3. Modificar usuario
          4. Eliminar usuario
          5. Listar permisos
          6. Agregar permiso
          7. Modificar permiso
          8. Eliminar permiso
          9. Salir
======================================================'''
          )
    
def opt():
    while True:
        try:
            opcion = int(input("Ingrese una opción: "))
            if opcion >= 1 and opcion <= 9:
                return opcion
                break
            else:
                print("Opción inválida. Por favor, ingrese un número entre 1 y 9.")
        except ValueError:
            print("La opción debe ser un numero entero")

def listar_usuarios(usuarios):
    listado = []
    for clave,datos in usuarios.items():
        listado.append(f"ID: {clave}, Nombre: {datos[0]} {datos[1]}, Edad: {datos[2]}, Email: {datos[3]}")
    return listado

def main():
    while True:
        menu()
        opcion = opt()

        if opcion == 1:
            listado = listar_usuarios(usuarios)
            print("\n".join(listado))

        elif opcion == 2:
            pass
        elif opcion == 3:
            pass
        elif opcion == 4:
            pass
        elif opcion == 5:
            pass
        elif opcion == 6:
            pass
        elif opcion == 7:
            pass
        elif opcion == 8:
            pass
        elif opcion == 9:
            print("Programa Finalizado, Adiós")
            break

main()