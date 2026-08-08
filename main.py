def mostrar_progreso():
    total = len(tareas)
    if total == 0:
        print("Sin tareas")
        return

    completadas = 0
    for tarea in tareas:
        if tarea["completada"]:
            completadas += 1

    porcentaje = (
        completadas * 100 / total
    )
    print(porcentaje, "%")