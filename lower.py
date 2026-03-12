first_Name=input("Introduzca su primer nombre:")
last_Name=input("Introduzca su apellido:")
full_Name=f"{first_Name} {last_Name}"
print("Usando el metodo islower()")
print(f"El formato del metodo title se ha aplicado?: {full_Name.islower()}")


first_Name=input("Introduzca su primer nombre:")
last_Name=input("Introduzca su apellido:")
full_Name=f"{first_Name} {last_Name}"
print("Usando el metodo lower()")
print(f"El formato del metodo title se ha aplicado sr./sra.: {full_Name.partitionlower()}")