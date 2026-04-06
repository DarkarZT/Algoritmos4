lista_milton = {
    "Shape of You",
    "Blinding Lights",
    "Bad Guy",
    "Levitating",
    "Watermelon Sugar",
    "Stay",
    "Peaches",
    "As It Was"
}

lista_pepe = {
    "Levitating",
    "Stay",
    "Happier Than Ever",
    "Industry Baby",
    "Save Your Tears",
    "Anti-Hero",
    "Flowers",
    "Calm Down"
}

playlist_comun = lista_milton.intersection(lista_pepe)
playlist_recomendados = lista_pepe.difference(lista_milton)
catalogo = lista_milton | lista_pepe
a = {lista_milton <= lista_pepe}
exclusivas = lista_milton ^ lista_pepe
print("Lista de comunes",playlist_comun)
print("Lista de recomendados",playlist_recomendados)
print("catalogo",catalogo)
print("Lista de solo escucha milton",a)
print("Lista de de ambos",exclusivas)




#armar una playlist con las canciones que le gusten a los 2 