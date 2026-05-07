def generar_fixture(equipos):
    """
    Algoritmo Round-Robin.
    Recibe lista de objetos Equipo.
    Retorna lista de jornadas, cada jornada es lista de tuplas (local, visitante).
    """
    equipos = list(equipos)
    n = len(equipos)

    # Si número impar, agrega un "descanso"
    if n % 2 != 0:
        equipos.append(None)
        n += 1

    total_jornadas = n - 1
    partidos_por_jornada = n // 2
    jornadas = []

    for jornada in range(total_jornadas):
        partidos = []
        for i in range(partidos_por_jornada):
            local    = equipos[i]
            visitante = equipos[n - 1 - i]
            if local is not None and visitante is not None:
                partidos.append((local, visitante))
        jornadas.append(partidos)
        # Rotar todos menos el primero
        equipos = [equipos[0]] + [equipos[-1]] + equipos[1:-1]

    return jornadas