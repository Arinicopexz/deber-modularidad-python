import random

# 1. Función para leer datos de sensores de humedad del suelo ---
def leer_sensores_humedad(seccion):
    """
    Retorna un valor de porcentaje (0 a 100) simulando la humedad de la tierra.
    """
    humedad = random.randint(10, 90)
    print(f"[Sensor] Humedad en la sección '{seccion}': {humedad}%")
    return humedad

# 2. Función para consultar las previsiones meteorológicas ---
def consultar_previsiones():
    """
    Simula una API del clima devolviendo el pronóstico.
    """
    climas = ["Lluvia intensa", "Nublado", "Soleado", "Ola de calor"]
    clima_hoy = random.choice(climas)
    print(f"[Clima] Pronóstico actual: {clima_hoy}")
    return clima_hoy

# 3. Procedimiento para calcular la cantidad óptima de riego ---
def calcular_cantidad_riego(humedad_actual, pronostico, tipo_cultivo):
    """
    Calcula cuántos litros por metro cuadrado se necesitan y los retorna.
    """
    litros = 0
    if humedad_actual < 40:
        if pronostico == "Lluvia intensa":
            print("[Cálculo] La tierra está seca, pero va a llover. No se requiere riego manual.")
            litros = 0
        elif pronostico == "Ola de calor":
            print("[Cálculo] Tierra seca y ola de calor. Riego máximo requerido.")
            litros = 15
        else:
            print("[Cálculo] Riego estándar requerido.")
            litros = 8
    else:
        print("[Cálculo] La tierra tiene humedad suficiente.")
        litros = 0
    return litros

# 4. Función para controlar las válvulas de riego ---
def controlar_valvulas(seccion, cantidad_litros):
    """
    Abre o cierra las válvulas dependiendo de la cantidad de litros calculados.
    """
    if cantidad_litros > 0:
        print(f"[Válvulas] ABRIENDO válvulas en '{seccion}'. Dispensando {cantidad_litros} L/m2.")
    else:
        print(f"[Válvulas] Válvulas CERRADAS en '{seccion}'.")

# 5. Bloque principal (Simulación de prueba) ---
if __name__ == "__main__":
    print("--- SISTEMA DE RIEGO AGRÍCOLA ---")
    seccion_cultivo = "Tomates - Sector Norte"
    
    # Ejecución modular
    hum_actual = leer_sensores_humedad(seccion_cultivo)
    clima = consultar_previsiones()
    agua_necesaria = calcular_cantidad_riego(hum_actual, clima, "Tomate")
    controlar_valvulas(seccion_cultivo, agua_necesaria)