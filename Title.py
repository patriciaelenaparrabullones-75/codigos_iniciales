first_Name=input("Introduzca su primer nombre:")
last_Name=input("Introduzca su apellido:")
full_Name=f"{first_Name} {last_Name}"
print("Usando el metodo istitle()")
print(f"El formato del metodo title se ha aplicado?: {full_Name.istitle()}")


first_Name=input("Introduzca su primer nombre:")
last_Name=input("Introduzca su apellido:")
full_Name=f"{first_Name} {last_Name}"
print("Usando el metodo title()")
print(f"El formato del metodo title se ha aplicado sr./sra.: {full_Name.title()}")