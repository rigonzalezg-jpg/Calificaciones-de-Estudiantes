# =====================================================================
# 1. FUNCIONES DEL MENÚ
# =====================================================================

def mostrar_menu():
    """Muestra las opciones del menú principal en pantalla."""
    print("\n========== MENÚ PRINCIPAL ==========")
    print("1. Agregar estudiante")
    print("2. Buscar estudiante")
    print("3. Eliminar estudiante")
    print("4. Actualizar estados")
    print("5. Mostrar estudiantes")
    print("6. Salir")
    print("=====================================")


def leer_opcion():
    """Lee, valida y retorna la opción ingresada por el usuario."""
    while True:
        try:
            opcion = int(input("Elija una opción (1-6): "))
            if 1 <= opcion <= 6:
                return opcion
            else:
                print("Opción inválida. Debe ser un número entre 1 y 6.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")


# =====================================================================
# 2. FUNCIONES DE VALIDACIÓN (OPCIÓN 1)
# =====================================================================

def validar_nombre(nombre):
    """Retorna True si el nombre no está vacío ni son solo espacios."""
    return len(nombre.strip()) > 0


def validar_edad(edad_str):
    """Retorna True si la edad es un entero mayor que cero."""
    try:
        edad = int(edad_str)
        return edad > 0
    except ValueError:
        return False


def validar_nota(nota_str):
    """Retorna True si la nota es un decimal entre 1.0 y 7.0."""
    try:
        nota = float(nota_str)
        return 1.0 <= nota <= 7.0
    except ValueError:
        return False


# =====================================================================
# 3. LÓGICA DE LAS OPCIONES DEL SISTEMA
# =====================================================================

def agregar_estudiante(lista):
    """Solicita los datos, los valida y registra al estudiante."""
    nombre = input("Ingrese el nombre del estudiante: ")
    edad_str = input("Ingrese la edad del estudiante: ")
    nota_str = input("Ingrese la nota del estudiante: ")

    # Las validaciones solo retornan True/False. Los mensajes se muestran aquí.
    if not validar_nombre(nombre):
        print("Error: El nombre no puede estar vacío ni ser solo espacios en blanco.")
        return

    if not validar_edad(edad_str):
        print("Error: La edad debe ser un número entero mayor que cero.")
        return

    if not validar_nota(nota_str):
        print("Error: La nota debe ser un número decimal entre 1.0 y 7.0.")
        return

    # Si todo es válido, se crea el diccionario y se agrega a la lista
    nuevo_estudiante = {
        "nombre": nombre.strip(),
        "edad": int(edad_str),
        "nota": float(nota_str),
        "aprobado": False  # Estado inicial por defecto
    }
    lista.append(nuevo_estudiante)
    print(f"¡Estudiante '{nuevo_estudiante['nombre']}' registrado con éxito!")


def buscar_estudiante(lista, nombre):
    """Busca un estudiante por coincidencia exacta y retorna su posición o -1."""
    for i, estudiante in enumerate(lista):
        if estudiante["nombre"] == nombre:
            return i
    return -1


def actualizar_estados(lista):
    """Modifica el campo 'aprobado' de todos los estudiantes según su nota."""
    for estudiante in lista:
        if estudiante["nota"] >= 4.0:
            estudiante["aprobado"] = True
        else:
            estudiante["aprobado"] = False


def mostrar_estudiantes(lista):
    """Actualiza los estados y muestra la lista con el formato solicitado."""
    if not lista:
        print("\nNo hay estudiantes registrados en el sistema.")
        return

    # Primero se actualizan los estados llamando a la función de la Opción 4
    actualizar_estados(lista)

    print("\n=== LISTA DE ESTUDIANTES ===")
    for estudiante in lista:
        estado_str = "APROBADO" if estudiante["aprobado"] else "REPROBADO"
        print(f"Nombre: {estudiante['nombre']}")
        print(f"Edad: {estudiante['edad']}")
        print(f"Nota: {estudiante['nota']:.1f}")
        print(f"Estado: {estado_str}")
        print("********************************************")


# =====================================================================
# 4. PROGRAMA PRINCIPAL
# =====================================================================

def main():
    # Lista global del sistema que almacenará los diccionarios de estudiantes
    estudiantes = []

    while True:
        # Invocación obligatoria de ambas funciones en cada vuelta del ciclo
        mostrar_menu()
        opcion = leer_opcion()

        if opcion == 1:
            agregar_estudiante(estudiantes)

        elif opcion == 2:
            nombre_buscar = input("Ingrese el nombre del estudiante a buscar: ")
            # El programa principal recibe el valor y decide qué hacer
            posicion = buscar_estudiante(estudiantes, nombre_buscar)
            
            if posicion != -1:
                est = estudiantes[posicion]
                print(f"\n[Estudiante encontrado en la posición {posicion}]")
                print(f"Nombre: {est['nombre']} | Edad: {est['edad']} | Nota: {est['nota']}")
            else:
                print("Estudiante no encontrado.")

        elif opcion == 3:
            nombre_eliminar = input("Ingrese el nombre del estudiante que desea eliminar: ")
            # Reutiliza la función de búsqueda de la opción 2
            posicion = buscar_estudiante(estudiantes, nombre_eliminar)
            
            if posicion != -1:
                estudiantes.pop(posicion)
                print(f"Estudiante '{nombre_eliminar}' eliminado con éxito.")
            else:
                print("Estudiante no encontrado.")

        elif opcion == 4:
            actualizar_estados(estudiantes)
            print("Los estados de los estudiantes fueron actualizados con éxito.")

        elif opcion == 5:
            mostrar_estudiantes(estudiantes)

        elif opcion == 6:
            print("\n¡Gracias por usar el sistema! Hasta pronto.")
            break


if __name__ == "__main__":
    main()
