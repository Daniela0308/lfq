def generate_fixture(teams):
    """
    Algoritmo Round-Robin.
    Recibe la lista de objetos de un torneo (los equipos)
    Retorna la lista de jornadas, cada jornada es lista de tuplas (local, visitante).
    """
    teams = list(teams) #pasamos los objetos a una lista
    n = len(teams) #calculamos la cantidad

    # Si número impar, agrega un None -> un equipo debe descansar si la cantidad es impar
    if n % 2 != 0:
        teams.append(None)
        n += 1

    total_matchday = n - 1 #si son 10 equipos, se juegan 9 fechas
    matches_of_day = n // 2  #si son 10 equipos se juegan 5 partidos en esa jornada
    matchday = []

    for j in range(total_matchday):
        maches = []
        for i in range(matches_of_day):
            local_team = teams[i]
            away_team = teams[n - 1 - i]
            if local_team is not None and away_team is not None:
                maches.append((local_team, away_team))
        matchday.append(maches)
        # Rotar todos menos el primero
        teams = [teams[0]] + [teams[-1]] + teams[1:-1]

    return matchday