# 1. Función para registrar la entrada de productos ---
def registrar_entrada(inventario, producto, cantidad):
    """
    Añade cantidad al producto en el diccionario de inventario.
    Si el producto no existe, lo crea.
    """
    if producto in inventario:
        inventario[producto] += cantidad
    else:
        inventario[producto] = cantidad
    print(f"[Entrada] Se ingresaron {cantidad} unidades de '{producto}'. Total: {inventario[producto]}")
    return inventario

# 2. Función para registrar la salida de productos ---
def registrar_salida(inventario, producto, cantidad):
    """
    Resta cantidad del inventario si hay suficientes existencias.
    """
    if producto in inventario:
        if inventario[producto] >= cantidad:
            inventario[producto] -= cantidad
            print(f"[Salida] Se despacharon {cantidad} unidades de '{producto}'. Restan: {inventario[producto]}")
        else:
            print(f"[Error] No hay suficiente stock de '{producto}'. Stock actual: {inventario[producto]}")
    else:
        print(f"[Error] El producto '{producto}' no existe en el inventario.")
    return inventario

# 3. Procedimiento para calcular el nivel óptimo de inventario ---
def calcular_nivel_optimo(ventas_promedio_diarias, dias_para_proveedor):
    """
    Procedimiento que calcula e imprime el stock de seguridad y el punto de reorden.
    """
    stock_seguridad = ventas_promedio_diarias * 2 # Colchón para 2 días extra
    punto_reorden = (ventas_promedio_diarias * dias_para_proveedor) + stock_seguridad
    print(f"[Análisis] El nivel óptimo (punto de reorden) es de {punto_reorden} unidades.")

# 4. Función para generar alertas de reabastecimiento ---
def generar_alertas(inventario, umbral_minimo):
    """
    Revisa todos los productos y avisa si alguno está por debajo del umbral.
    """
    alertas = []
    for producto, cantidad in inventario.items():
        if cantidad <= umbral_minimo:
            alertas.append(producto)
            print(f"[ALERTA] El producto '{producto}' requiere reabastecimiento urgente (Stock: {cantidad}).")
    
    if len(alertas) == 0:
        print("[Ok] Todos los productos tienen buen nivel de stock.")
    return alertas

# 5. Bloque principal (Simulación de prueba) ---
if __name__ == "__main__":
    print("--- SISTEMA DE INVENTARIO ---")
    mi_inventario = {"Tornillos": 500, "Tuercas": 100, "Clavos": 50}
    
    # Ejecución modular
    registrar_entrada(mi_inventario, "Tuercas", 200)
    registrar_salida(mi_inventario, "Clavos", 40)
    
    calcular_nivel_optimo(ventas_promedio_diarias=20, dias_para_proveedor=3)
    generar_alertas(mi_inventario, umbral_minimo=100)