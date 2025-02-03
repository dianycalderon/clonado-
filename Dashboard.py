import os
import subprocess

def mostrar_codigo(ruta_script):
    """Muestra el contenido de un script en la consola."""
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r', encoding='utf-8') as archivo:
            codigo = archivo.read()
            print(f"\n--- Código de {ruta_script} ---\n{codigo}")
            return codigo
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")

def ejecutar_codigo(ruta_script):
    """Ejecuta un script en una terminal separada."""
    try:
        comando = ['cmd', '/k', 'python', ruta_script] if os.name == 'nt' else ['xterm', '-hold', '-e', 'python3', ruta_script]
        subprocess.Popen(comando)
    except Exception as e:
        print(f"Ocurrió un error al ejecutar el código: {e}")

def mostrar_menu():
    """Muestra el menú principal y gestiona la navegación entre unidades."""
    ruta_base = os.path.dirname(__file__)
    unidades = {'1': 'Unidad 1', '2': 'Unidad 2'}

    while True:
        print("\nMenu Principal - Dashboard")
        for key, value in unidades.items():
            print(f"{key} - {value}")
        print("0 - Salir")

        eleccion = input("Elige una unidad o '0' para salir: ")
        if eleccion == '0':
            print("Saliendo del programa.")
            break
        if eleccion in unidades:
            mostrar_sub_menu(os.path.join(ruta_base, unidades[eleccion]))
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

def mostrar_sub_menu(ruta_unidad):
    """Muestra el submenú de unidades y permite seleccionar una subcarpeta."""
    try:
        sub_carpetas = [f.name for f in os.scandir(ruta_unidad) if f.is_dir()]
    except FileNotFoundError:
        print("No se encontró la unidad seleccionada.")
        return

    while True:
        print("\nSubmenú - Selecciona una subcarpeta")
        for i, carpeta in enumerate(sub_carpetas, start=1):
            print(f"{i} - {carpeta}")
        print("0 - Regresar al menú principal")

        try:
            eleccion = int(input("Elige una subcarpeta o '0' para regresar: "))
            if eleccion == 0:
                break
            if 1 <= eleccion <= len(sub_carpetas):
                mostrar_scripts(os.path.join(ruta_unidad, sub_carpetas[eleccion - 1]))
            else:
                print("Opción no válida. Intenta de nuevo.")
        except ValueError:
            print("Entrada inválida. Ingresa un número.")

def mostrar_scripts(ruta_sub_carpeta):
    """Muestra los scripts disponibles y permite ver y ejecutar uno."""
    try:
        scripts = [f.name for f in os.scandir(ruta_sub_carpeta) if f.is_file() and f.name.endswith('.py')]
    except FileNotFoundError:
        print("No se encontró la carpeta seleccionada.")
        return

    while True:
        print("\nScripts - Selecciona un script para ver y ejecutar")
        for i, script in enumerate(scripts, start=1):
            print(f"{i} - {script}")
        print("0 - Regresar al submenú anterior")
        print("9 - Regresar al menú principal")

        try:
            eleccion = int(input("Elige un script, '0' para regresar o '9' para ir al menú principal: "))
            if eleccion == 0:
                break
            if eleccion == 9:
                return
            if 1 <= eleccion <= len(scripts):
                ruta_script = os.path.join(ruta_sub_carpeta, scripts[eleccion - 1])
                if mostrar_codigo(ruta_script):
                    ejecutar = input("¿Desea ejecutar el script? (1: Sí, 0: No): ")
                    if ejecutar == '1':
                        ejecutar_codigo(ruta_script)
                input("\nPresiona Enter para volver al menú de scripts.")
            else:
                print("Opción no válida. Intenta de nuevo.")
        except ValueError:
            print("Entrada inválida. Ingresa un número.")

# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()






