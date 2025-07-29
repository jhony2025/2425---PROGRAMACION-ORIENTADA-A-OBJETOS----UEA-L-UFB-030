import os

def mostrar_codigo(ruta_script):
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r', encoding='utf-8') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")

def mostrar_menu():
    ruta_base = os.path.dirname(__file__)

    opciones = {
        '1': 'Semana 02/1.2.1. Ejemplo Tecnicas de Programacion.py',
        '2': 'Semana 03/2.1-1. Ejemplo Programacion tradicional frente a POO.py',
        '3': 'Semana 03/2.1-2. Ejemplo No. 02 - POO.py',
        '4': 'Semana 04/2.2-1. Ejemplo - Carro y Acciones.py',
        '5': 'Semana 04/2.2-2. Ejemplo - Carro Relacion Persona.py',
        '6': 'Semana 05/2.2-4. Ejemplo - Libro, Bibliotecario y Rol.py',
        '7': 'Semana 06/2.1.2-1 - Ejemplo Clase y Objeto (Coche).py',
        '8': 'Semana 06/2.1.2-2 - Ejemplo Sobrecarga de Métodos.py',
        '9': 'Semana 06/2.1.2-3 - Ejemplo Herencia.py',
        '10': 'Semana 06/2.1.2-4 - Ejemplo Polimorfismo (Sobrecarga).py',
        '11': 'Semana 07/2.2.1-1 - Uso de constructor.py',
        '12': 'Semana 07/2.2.1-2 - Uso del destructor.py',
    }

    while True:
        print("\n********* Menu Principal - Dashboard *********")
        for key in opciones:
            print(f"{key} - {opciones[key]}")
        print("0 - Salir")

        eleccion = input("Elige un script para ver su código o '0' para salir: ")
        if eleccion == '0':
            break
        elif eleccion in opciones:
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            mostrar_codigo(ruta_script)
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    mostrar_menu()
