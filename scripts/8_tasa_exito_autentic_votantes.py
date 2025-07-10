import random

# ------------------------------
# 1) Parámetros de la simulación
# ------------------------------
num_intentos_autenticacion = 10000
autenticaciones_exitosas = 0
autenticaciones_fallidas = 0

# ------------------------------
# 2) Ejecutar simulación
# ------------------------------

print(f" Simulando autenticación de {num_intentos_autenticacion} votantes...")

for i in range(num_intentos_autenticacion):
    # Simula un 98% de éxito y 2% de fallos aleatorios
    resultado = random.choices(["exito", "fallo"], weights=[98, 2])[0]

    if resultado == "exito":
        autenticaciones_exitosas += 1
    else:
        autenticaciones_fallidas += 1

# ------------------------------
# 3) Calcular tasa de éxito
# ------------------------------
tasa_exito_autenticacion = (autenticaciones_exitosas / num_intentos_autenticacion) * 100

print(f"\n Autenticaciones exitosas: {autenticaciones_exitosas}")
print(f" Autenticaciones fallidas: {autenticaciones_fallidas}")
print(f" Tasa de Éxito en Autenticación de Votantes: {tasa_exito_autenticacion:.2f}%")
