#Para crear un conjunto vacio
conjunto1=set()
conjunto_meses={  
                    "Enero",
                    "Febrero",
                    "Marzo",
                    "Abril",
                    "Mayo",
                    "Junio",
                    "Julio",
                    "Agosto",
                    "Septiembre",
                    "Octubre",
                    "Noviembre"
                
               }
print("Conjunto de 11 meses")
print(conjunto_meses)
conjunto_meses.add("Diciembre")
print("Conjunto de 12 meses")
print(conjunto_meses)

lenguajes={  
            "Pascal",
            "C",
            "C#",
            "PHP",
            "Python"
          }
print("Conjunto de lenguajes")
print(lenguajes)
lenguajes2={  
            "HTML",
            "CSS",
            "Java",
            "Java Script",
            "R",
            "Swith",
            "Kotlin"
          }
l=len(lenguajes)
print(l)
lenguajes.update(lenguajes2)
print(lenguajes)
l=len(lenguajes)
print("La cantidad de lenguajes es de:",l)

lenguajes.discard("Swith")
print("Conjunto con el lenguaje Swith eliminado")
print(lenguajes)
eliminado=lenguajes.pop()
print("Conjunto con un lenguaje aleatorio eliminado")
print("El lenguaje eliminado fue:")
print(eliminado)
l=len(lenguajes)
print(l)

num={1,2,3,4,5,6,7,8,9,10,11,12}
num2={9,10,11,12,13,14,15,16,17,18,19,20}
print("El numero menor dentro del conjunto es:")
print(min(num))
print("El numero mayor dentro del conjunto es:")
print(max(num))
print("El numero menor dentro del conjunto es:")
print(min(num))
print("La suma del conjunto es:")
print(sum(num))

orden=sorted(num)
print("Conjunto ordenado")
print(orden)
print("conjunto Enumerado")
print(list(enumerate(num)))

print("Unir 2 conjuntos")
print(num.union(num2))

print("Interseccion de conjuntos comunes")
union=num.intersection(num2)
print(union)

print("Elementos no comunes")
nocomun =num^num2
print("Elementos no comunes entre los 2 conjuntos")
print(nocomun)

print("Datos exclusivos de un conjunto y que no estan en el otro conjunto")
dif=num.difference(num2)
print(dif)






