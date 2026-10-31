# Soluciones Modulares - Fundamentos de Programación

Este repositorio contiene las soluciones a cinco problemas reales resueltos utilizando los principios fundamentales de la **modularidad** (funciones y procedimientos). Los códigos están diseñados para ser claros, secuenciales y utilizar estructuras de datos básicas, ideal para un nivel de primer semestre de programación.

## ¿Qué es la modularidad y cómo afecta al rendimiento?
La modularidad consiste en dividir un problema grande en partes más pequeñas y manejables (funciones/procedimientos). 
* **En el rendimiento computacional:** Al usar funciones, evitamos repetir bloques de código. Esto hace que el programa ocupe menos espacio en memoria y sea más fácil de cargar para el procesador.
* **En el rendimiento de desarrollo:** Permite a los programadores reutilizar código, encontrar errores más rápido (debugging) y trabajar en equipo, ya que cada persona puede programar una función diferente sin afectar el código de los demás.

---

## Explicación de los Problemas

### 1. Control de Temperatura (edificio_inteligente.py)
* **`leer_datos_sensores()`:** Obtiene los datos del ambiente. Permite separar la lógica de lectura (hardware) del procesamiento.
* **`calcular_temperatura_optima()`:** Aplica reglas de negocio simples (si hay gente o es de día/noche).
* **`enviar_senales_ajuste()`:** Actúa como el controlador que decide si encender frío o calor.
* **`registrar_y_analizar_consumo()`:** Modularizar esta parte permite llevar estadísticas sin entorpecer el ciclo principal del aire acondicionado.

### 2. Gestión de Inventario (inventario_almacen.py)
* **`registrar_entrada()` y `registrar_salida()`:** Separan las operaciones matemáticas del diccionario, protegiendo los datos de que se resten productos que no existen.
* **`calcular_nivel_optimo()`:** Utiliza una fórmula matemática estática que puede ser modificada en el futuro en un solo lugar.
* **`generar_alertas()`:** Al estar separada, esta función puede ser programada para ejecutarse solo al final del día para ahorrar recursos.

### 3. Navegación Vehículo Autónomo (vehiculo_autonomo.py)
* **`leer_datos_sensores()`:** Se encarga exclusivamente de las "ojos" del coche.
* **`calcular_ruta_optima()`:** Maneja la lógica de mapas de alto nivel.
* **`detectar_evitar_obstaculos()`:** Una función de seguridad crítica aislada para que se ejecute rápidamente sin esperar cálculos pesados de mapas.
* **`ajustar_velocidad()`:** Recibe los inputs de las funciones anteriores para controlar el motor, demostrando cómo los módulos se comunican entre sí.

### 4. Producción en Fábrica (optimizacion_fabrica.py)
* **`monitorear_estado()`:** Retorna rápidamente cómo están las máquinas.
* **`planificar_mantenimiento()`:** Separa la responsabilidad humana de revisar las máquinas.
* **`analizar_rendimiento()`:** Compara la realidad con la expectativa matemática.
* **`ajustar_programacion()`:** Modifica la línea de producción basada en el rendimiento, demostrando el uso de múltiples variables (demanda y calidad) en un solo módulo de decisión.

### 5. Riego Automatizado (riego_automatizado.py)
* **`leer_sensores_humedad()` y `consultar_previsiones()`:** Obtienen las variables independientes de distintas fuentes (tierra física y nube de internet).
* **`calcular_cantidad_riego()`:** Es el "cerebro" central que junta la humedad y el clima para tomar una decisión lógica y ahorrar agua.
* **`controlar_valvulas()`:** El "músculo" que se asegura de ejecutar solo las acciones requeridas por el cerebro. Al ser modular, si el hardware de las válvulas cambia, solo se modifica esta pequeña función.

## Instrucciones de Ejecución
Cada script de Python es autoejecutable y contiene un bloque `if __name__ == "__main__":` con datos simulados (mock data) para comprobar el funcionamiento lógico de los módulos por consola.