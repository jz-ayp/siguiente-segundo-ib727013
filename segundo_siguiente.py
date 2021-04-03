
# Entradas
Horas = int(input("Horas: "))
Minutos = int(input("Minutos: "))
Segundos = int(input("Segundos: "))

# Proceso
Segundos += 1
if Segundos > 59:
    Segundos = 0
    Minutos += 1
if Minutos > 59:
    Minutos = 0
    Horas += 1

# Salidas
print("Horas:", Horas)
print("Minutos:", Minutos)
print("Segundos:", Segundos)
