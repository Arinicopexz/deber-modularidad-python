import random

#  1. Función para leer datos de sensores de temperatura ---
def leer_datos_sensores(zona):
    """
    Simula la lectura de un sensor de temperatura en una zona específica.
    Retorna un valor aleatorio entre 15.0 y 35.0 grados.
    """
    temperatura_actual = round(random.uniform(15.0, 35.0), 1)
    print(f"[Sensor] La temperatura actual en {zona} es {temperatura_actual}°C")
    return temperatura_actual

# --- 2. Función para calcular la temperatura óptima en cada zona ---
def calcular_temperatura_optima(hora, hay_ocupacion):
    """
    Calcula la temperatura ideal basándose en si hay gente y la hora del día.
    """
    if not hay_ocupacion:
        return 24.0 # Temperatura de ahorro de energía si no hay nadie
    else:
        # Si es horario laboral/diurno (8 a 18 hrs), más fresco. Si es noche, más cálido.
        if 8 <= hora <= 18:
            return 22.0
        else:
            return 20.0

# 3. Procedimiento para enviar señales de ajuste ---
def enviar_senales_ajuste(zona, temp_actual, temp_optima):
    """
    Procedimiento (no retorna valor, solo ejecuta una acción) que enciende
    la calefacción o el aire acondicionado según sea necesario.
    """
    diferencia = temp_actual - temp_optima
    
    if diferencia > 1.0:
        print(f"[Ajuste] Encendiendo REFRIGERACIÓN en {zona}. Bajando {round(diferencia, 1)}°C.")
    elif diferencia < -1.0:
        print(f"[Ajuste] Encendiendo CALEFACCIÓN en {zona}. Subiendo {round(abs(diferencia), 1)}°C.")
    else:
        print(f"[Ajuste] Temperatura en {zona} está en el rango óptimo. Sistema en espera.")

# 4. Función para registrar y analizar el consumo de energía ---
def registrar_y_analizar_consumo(registro_kw):
    """
    Recibe una lista de consumos (en kW) y calcula el total y el promedio
    para analizar el gasto energético del edificio.
    """
    if len(registro_kw) == 0:
        return 0, 0
    
    total = sum(registro_kw)
    promedio = total / len(registro_kw)
    print(f"[Análisis] Consumo total: {total}kW | Consumo promedio: {promedio}kW")
    return total, promedio

# 5. Bloque principal (Simulación de prueba) ---
if __name__ == "__main__":
    print("--- INICIANDO SISTEMA DEL EDIFICIO ---")
    zona_prueba = "Oficina A"
    hora_actual = 14
    ocupado = True
    
    # Ejecución modular
    temp_leida = leer_datos_sensores(zona_prueba)
    temp_ideal = calcular_temperatura_optima(hora_actual, ocupado)
    enviar_senales_ajuste(zona_prueba, temp_leida, temp_ideal)
    
    consumos_del_dia = [12.5, 14.0, 9.2, 15.1]
    registrar_y_analizar_consumo(consumos_del_dia)