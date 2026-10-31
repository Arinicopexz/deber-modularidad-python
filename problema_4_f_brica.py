import random

# 1. Función para monitorear el estado de las máquinas ---
def monitorear_estado(maquinas):
    """
    Recibe una lista de máquinas y asigna un estado aleatorio
    (Optimo, Advertencia, Critico) a cada una.
    """
    estados = ["Óptimo", "Advertencia", "Crítico"]
    estado_actual = {}
    for maquina in maquinas:
        estado_actual[maquina] = random.choice(estados)
        print(f"[Monitoreo] {maquina}: {estado_actual[maquina]}")
    return estado_actual

# 2. Procedimiento para planificar el mantenimiento preventivo ---
def planificar_mantenimiento(estado_maquinas):
    """
    Revisa los estados e imprime una orden de mantenimiento si es necesario.
    """
    for maquina, estado in estado_maquinas.items():
        if estado == "Crítico":
            print(f"[Mantenimiento] URGENTE: Detener {maquina} para reparación inmediata.")
        elif estado == "Advertencia":
            print(f"[Mantenimiento] Programar revisión para {maquina} al final del turno.")

# 3. Función para analizar el rendimiento de la producción ---
def analizar_rendimiento(piezas_producidas, meta_esperada):
    """
    Calcula el porcentaje de eficiencia y retorna un mensaje de estado.
    """
    eficiencia = (piezas_producidas / meta_esperada) * 100
    print(f"[Rendimiento] Eficiencia actual: {round(eficiencia, 2)}%")
    
    if eficiencia >= 95:
        return "Excelente"
    elif eficiencia >= 80:
        return "Aceptable"
    else:
        return "Deficiente"

# 4. Procedimiento para ajustar la programación de la producción ---
def ajustar_programacion(rendimiento, demanda):
    """
    Ajusta la velocidad de producción según el rendimiento y la demanda del mercado.
    """
    if demanda == "Alta" and rendimiento != "Excelente":
        print("[Programación] Aumentando velocidad de cintas y abriendo turno extra.")
    elif demanda == "Baja":
        print("[Programación] Reduciendo velocidad para ahorrar costos operativos.")
    else:
        print("[Programación] Manteniendo ritmo de producción normal.")

# 5. Bloque principal (Simulación de prueba) ---
if __name__ == "__main__":
    print("--- SISTEMA DE PRODUCCIÓN EN FÁBRICA ---")
    lista_maquinas = ["Ensambladora 1", "Brazo Robótico 2", "Empacadora A"]
    
    # Ejecución modular
    estados = monitorear_estado(lista_maquinas)
    planificar_mantenimiento(estados)
    
    calidad = analizar_rendimiento(piezas_producidas=900, meta_esperada=1000)
    ajustar_programacion(calidad, demanda="Alta")