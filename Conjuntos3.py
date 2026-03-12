misFrutas=         {"Fresas",
                    "Naranjas",
                    "Limas",
                    "Limones",
                    "Arandanos",
                    "Moras",
                    "Peras",
                    "Manzanas",
                    "Mandarinas",
                    "Pina",
                    "Kiwi",
                    "Tamarindos"
                    }

misFrutas2=         {
                    "Arandanos",
                    "Peras",
                    "Limas",
                    "Limones",
                    "Arandanos",
                    "Moras",
                    "Peras",
                    "Manzanas",
                    "Mandarinas",
                    "Pina",
                    "Kiwi",
                    "Tamarindos"
                    }

print(misFrutas.intersection(misFrutas2))#intersepta los valores que coinciden en ambos conjuntos
misFrutas.discard("Tamarindos")
misFrutas.discard("Manzanas")
misFrutas.add("Aguacate")
print(*misFrutas, sep=",")