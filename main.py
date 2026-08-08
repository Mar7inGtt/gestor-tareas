tareas = []

def mostrar_menu():
    print("\nGESTOR DE TAREAS")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Mostrar progreso")
    print("4. Salir")

def agregar_tarea():

    nombre = input("Tarea: ")

    if nombre == "":
        print("Debe ingresar una tarea")
        return

    tarea = {
        "nombre": nombre,
        "completada": False
    }

    tareas.append(tarea)

    print("Tarea agregada")