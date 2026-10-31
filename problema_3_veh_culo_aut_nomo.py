import random

# 1. Función para leer datos de sensores de proximidad y cámaras ---
def leer_datos_sensores():
    """
    Simula la distancia al objeto más cercano en metros.
    """
    distancia = round(random.uniform(0.5, 50.0), 1)
    print(f"[Sensores] Objeto más cercano detectado a {distancia} metros.")
    return distancia

# 2. Procedimiento para calcular la ruta óptima ---
def calcular_ruta_optima(origen, destino, hay_trafico):
    """
    Imprime la ruta calculada dependiendo de las condiciones del tráfico.
    """
    if hay_trafico:
        print(f"[Navegación] Calculando ruta alternativa de {origen} a {destino} para evitar tráfico.")
    else:
        print(f"[Navegación] Calculando ruta principal directa de {origen} a {destino}.")

# 3. Función para detectar y evitar obstáculos ---
def detectar_evitar_obstaculos(distancia_obstaculo):
    """
    Evalúa si la distancia es peligrosa. Retorna True si hay que esquivar.
    """
    umbral_peligro = 5.0 # metros
    if distancia_obstaculo < umbral_peligro:
        print("[Acción] ¡Obstáculo inminente! Realizando maniobra de evasión.")
        return True
    else:
        print("[Acción] Camino despejado. Manteniendo el rumbo.")
        return False

# 4. Procedimiento para ajustar la velocidad ---
def ajustar_velocidad(esquivando, nivel_trafico):
    """
    Modifica la velocidad del vehículo basado en las acciones previas.
    """
    if esquivando:
        print("[Velocidad] Reduciendo velocidad a 10 km/h por maniobra.")
    elif nivel_trafico == "Alto":
        print("[Velocidad] Trafico alto. Velocidad máxima ajustada a 30 km/h.")
    else:
        print("[Velocidad] Condiciones óptimas. Velocidad de crucero a 60 km/h.")

# 5. Bloque principal (Simulación de prueba) ---
if __name__ == "__main__":
    print("--- SISTEMA DE VEHÍCULO AUTÓNOMO ---")
    
    # Ejecución modular
    distancia_frente = leer_datos_sensores()
    trafico = "Alto"
    
    calcular_ruta_optima("Centro", "Universidad", hay_trafico=(trafico=="Alto"))
    maniobra = detectar_evitar_obstaculos(distancia_frente)
    ajustar_velocidad(maniobra, trafico)