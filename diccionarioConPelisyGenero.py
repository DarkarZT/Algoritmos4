peliculas = {
    "Inception": {"Ciencia ficción", "Acción", "Suspenso"},
    "Titanic": {"Romance", "Drama"},
    "The Dark Knight": {"Acción", "Crimen", "Drama"},
    "Interstellar": {"Ciencia ficción", "Aventura", "Drama"},
    "Toy Story": {"Animación", "Aventura", "Comedia"},
    "The Matrix": {"Ciencia ficción", "Acción"},
    "Gladiator": {"Acción", "Drama", "Histórico"},
    "La La Land": {"Romance", "Musical", "Drama"},
    "a":{"Drama","Acción"},
    "b":{"Drama","Acción"}
}

pelicula = list(peliculas.keys())
peliculas_comunes = []

for i in range (len(pelicula)):
    for j in range(i+1, len(pelicula)):
        p1, p2 = pelicula[i], pelicula[j]
        comunes = peliculas[p1] & peliculas[p2]
        if len(comunes) >= 2:
            peliculas_comunes.append((p1,p2,comunes))
        
print(peliculas_comunes)
    