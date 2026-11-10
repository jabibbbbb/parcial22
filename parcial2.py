inventario = []

while True:
    print("\n--- INVENTARIO DE ROBÓTICA ---")
    print("1. Registrar componente")
    print("2. Consultar inventario")
    print("3. Filtrar por categoría")
    print("4. Actualizar stock")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        id = input("ID: ")

        if any(c["id"] == id for c in inventario):
            print("ID repetido.")
            continue

        componente = {
            "id": id,
            "nombre": input("Nombre: "),
            "categoria": input("Categoría: "),
            "stock": int(input("Stock: ")),
            "precio_unitario": float(input("Precio: "))
        }

        inventario.append(componente)
        print("Componente registrado.")

    elif opcion == "2":
        for c in inventario:
            print(c)

    elif opcion == "3":
        categoria = input("Categoría: ")

        for c in inventario:
            if c["categoria"].lower() == categoria.lower():
                print(c)

    elif opcion == "4":
        id = input("ID del componente: ")

        for c in inventario:
            if c["id"] == id:
                cantidad = int(input("Cantidad (+ agregar / - retirar): "))

                if c["stock"] + cantidad >= 0:
                    c["stock"] += cantidad
                    print("Stock actualizado.")
                else:
                    print("Stock insuficiente.")
                break
        else:
            print("Componente no encontrado.")

    elif opcion == "5":
        print("¡Hasta pronto!")
        break

    else:
        print("Opción inválida.")
