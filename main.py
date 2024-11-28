import datetime

# Clase para representar un experimento
class Experimento:
    def __init__(self, nombre, fecha, tipo, resultados):
        self.nombre = nombre
        self.fecha = fecha
        self.tipo = tipo
        self.resultados = resultados

# Lista para almacenar los experimentos
experimentos = []

# Función para agregar un experimento
def agregar_experimento():
    nombre = input("Nombre del experimento: ")
    fecha_str = input("Fecha de realización (DD/MM/AAAA): ")
    try:
        fecha = datetime.datetime.strptime(fecha_str, "%d/%m/%Y")
    except ValueError:
        print("Fecha no válida. Use el formato DD/MM/AAAA.")
        return
    tipo = input("Tipo de experimento (Quimica/Biologia/Fisica): ")
    if tipo not in ["Quimica", "Biologia", "Fisica"]:
        print("Tipo de experimento no reconocido. Use Quimica, Biologia o Fisica.")
        return
    try:
        resultados = list(map(float, input("Resultados obtenidos (separados por comas): ").split(",")))
    except ValueError:
        print("Resultados no válidos. Deben ser números separados por comas.")
        return
    experimento = Experimento(nombre, fecha, tipo, resultados)
    experimentos.append(experimento)
    print("Experimento agregado exitosamente.")

# Función para visualizar los experimentos
def visualizar_experimentos():
    if not experimentos:
        print("No hay experimentos registrados.")
        return
    for i, experimento in enumerate(experimentos, start=1):
        print(f"\nExperimento {i}:")
        print(f"Nombre: {experimento.nombre}")
        print(f"Fecha: {experimento.fecha.strftime('%d/%m/%Y')}")
        print(f"Tipo: {experimento.tipo}")
        print(f"Resultados: {experimento.resultados}")

# Función para analizar los resultados
def analizar_resultados():
    if not experimentos:
        print("No hay experimentos registrados.")
        return
    for experimento in experimentos:
        promedio = sum(experimento.resultados) / len(experimento.resultados)
        maximo = max(experimento.resultados)
        minimo = min(experimento.resultados)
        print(f"\nAnálisis de {experimento.nombre}:")
        print(f"Promedio: {promedio:.2f}")
        print(f"Máximo: {maximo}")
        print(f"Mínimo: {minimo}")

# Función para comparar resultados entre experimentos
def comparar_experimentos():
    if len(experimentos) < 2:
        print("Se necesitan al menos dos experimentos para realizar la comparación.")
        return
    mejores_resultados = sorted(experimentos, key=lambda x: sum(x.resultados) / len(x.resultados), reverse=True)
    print(f"\nEl experimento con los mejores resultados es: {mejores_resultados[0].nombre}")
    print(f"El experimento con los peores resultados es: {mejores_resultados[-1].nombre}")

# Función para generar un informe
def generar_informe():
    if not experimentos:
        print("No hay experimentos registrados.")
        return
    with open("informe.txt", "w") as archivo:
        for experimento in experimentos:
            archivo.write(f"Nombre: {experimento.nombre}\n")
            archivo.write(f"Fecha: {experimento.fecha.strftime('%d/%m/%Y')}\n")
            archivo.write(f"Tipo: {experimento.tipo}\n")
            archivo.write(f"Resultados: {experimento.resultados}\n")
            promedio = sum(experimento.resultados) / len(experimento.resultados)
            maximo = max(experimento.resultados)
            minimo = min(experimento.resultados)
            archivo.write(f"Promedio: {promedio:.2f}\n")
            archivo.write(f"Máximo: {maximo}\n")
            archivo.write(f"Mínimo: {minimo}\n\n")
    print("Informe generado exitosamente.")

# Función para eliminar un experimento
def eliminar_experimento():
    if not experimentos:
        print("No hay experimentos registrados.")
        return
    visualizar_experimentos()
    try:
        index = int(input("Ingrese el número del experimento que desea eliminar: ")) - 1
        if 0 <= index < len(experimentos):
            eliminado = experimentos.pop(index)
            print(f"Experimento '{eliminado.nombre}' eliminado exitosamente.")
        else:
            print("Número de experimento no válido.")
    except ValueError:
        print("Entrada no válida. Debe ingresar un número.")

# Menú de opciones
def menu():
    while True:
        print("\n=== Menú ===")
        print("1. Agregar experimento")
        print("2. Visualizar experimentos")
        print("3. Analizar resultados")
        print("4. Comparar experimentos")
        print("5. Generar informe")
        print("6. Eliminar experimento")
        print("7. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            agregar_experimento()
        elif opcion == "2":
            visualizar_experimentos()
        elif opcion == "3":
            analizar_resultados()
        elif opcion == "4":
            comparar_experimentos()
        elif opcion == "5":
            generar_informe()
        elif opcion == "6":
            eliminar_experimento()
        elif opcion == "7":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

# Ejecutar el menú
menu()
