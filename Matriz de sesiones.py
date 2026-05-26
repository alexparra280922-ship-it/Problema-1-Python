# Matriz de sesiones
sesiones = [
    ["C001", 240, 12],
    ["C002", 45, 2],
    ["C003", 120, 5],
    ["C004", 300, 15],
    ["C005", 70, 1]
]

# Función de clasificación
def clasificar_compromiso(duracion, clics):

    if duracion > 180 and clics > 8:
        return "Alto"

    elif duracion < 60 or clics < 3:
        return "Bajo"

    else:
        return "Medio"


# Encabezado de la tabla
print("-----------------------------------------------------")
print("| ID Cliente | Duración (s) | Clics | Clasificación |")
print("-----------------------------------------------------")

# Recorrer matriz
for sesion in sesiones:

    id_cliente = sesion[0]
    duracion = sesion[1]
    clics = sesion[2]

    clasificacion = clasificar_compromiso(duracion, clics)

    # Mostrar fila
    print(f"| {id_cliente:^10} | {duracion:^12} | {clics:^6} | {clasificacion:^13} |")

print("-----------------------------------------------------")