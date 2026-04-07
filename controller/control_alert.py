# CODIGOS DE COLOR

ROJO = "\033[91m"
VERDE = "\033[92m"
AMARILLO = "\033[93m"
NARANJA_REAL = "\033[38;5;208m"
RESET = "\033[0m"  # Vuelve al color original

# DEFINICION DE FUNCIONES PARA CONTROL DE ALERTAS

def obtener_alerta_temperatura(temperatura):
    if temperatura >= 42:
        return f"{ROJO}ALERTA ROJA: {RESET} Riesgo extremo por calor - Riesgo para la salud muy alto. {RESET}"
    elif temperatura <= -10:
        return f"{ROJO}ALERTA ROJA: {RESET} Frío extremo. Riesgo de heladas y nevadas severas. {RESET}"
    elif temperatura >= 39:
        return f"{NARANJA_REAL}ALERTA NARANJA: {RESET} Riesgo importante por calor - Se recomienda no salir en horas centrales del día. {RESET}"
    elif temperatura <= -6:
        return f"{NARANJA_REAL}ALERTA NARANJA: {RESET} Temperaturas gélidas. Riesgo de heladas y nevadas. Peligro en tuberías y la salud. {RESET}"
    elif temperatura >= 36:
        return f"{AMARILLO}ALERTA AMARILLA: {RESET} Riesgo por calor - Se recomienda no realizar actividades al aire libre. {RESET}"
    elif temperatura <= -4:
        return f"{AMARILLO}ALERTA AMARILLA: {RESET} Precaución por heladas. {RESET}"
    else:
        return f"{VERDE}Nivel Verde{RESET} (Sin riesgo).{RESET}"

# DEFINICION DE FUNCIONES PARA CONTROL DE ALERTAS DE VIENTO

def obtener_alerta_viento(viento):
    if viento >= 110:
        return f"{ROJO}ALERTA ROJA: Viento extremo - Peligro de caída de objetos y daños estructurales. {RESET}"
    elif viento >= 90:
        return f"{NARANJA_REAL}ALERTA NARANJA: Cierre preventivo de parques. {RESET}"
    elif viento >= 70:
        return f"{AMARILLO}ALERTA AMARILLA: Balizas en zonas infantiles y de mayores. {RESET}"
    else:
        return f"{VERDE}Nivel Verde{RESET} (Sin riesgo).{RESET}"

# Pongo float porque la temperatura y el viento pueden tener decimales, y el input devuelve un string, entonces lo convierto a float para poder hacer las comparaciones numéricas.
try:
    temperatura = float(input("Introduce la temperatura actual en °C: ")) # Solicitar al operario que ingrese la temperatura actual
    viento = float(input("Introduce la velocidad del viento en km/h: ")) # Solicitar al usuario que ingrese la velocidad del viento

    print("\n" + "="*50)
    print("   ESTADO DEL SISTEMA SMART CITY")
    print("="*50)
    print(f"Temperatura: {obtener_alerta_temperatura(temperatura)}")
    print(f"Viento:      {obtener_alerta_viento(viento)}")
    print("="*50)
except ValueError:
    print(f"{ROJO}Error: Por favor, introduce números válidos.{RESET}")