from os import system, name

system("cls") if name == "nt" else system("clear")
a = {4, 2, 5, 6, 7}
b = {5, 6, 7, 8, 2, 3}
print("Valores comuns às duas listas: " + str(a & b))  # comuns
print("Valores que só existem em a: " + str(a - b))  # só de a
print("Valores que só existem em b: " + str(b - a))  # só de b
print("Elementos não repetidos das duas listas: " + str(b | a))  # união
print("Lista a, sem os elementos repetidos de b: " + str(a - b))

# A ^ B resulta nos elementos de A não presentes em B unidos
# com os elementos de B não presentes em A
print("Elementos de A não presentes em B unidos com os elementos de B não presentes em A: " + str(a ^ b))
