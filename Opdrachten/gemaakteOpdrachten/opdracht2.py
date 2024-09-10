# Containers
unloaded_containers = 331
loaded_containers = 287
unload_time = 441
load_time = 287

average_load_time = load_time / loaded_containers
average_unload_time = unload_time / unloaded_containers

print(f'De gemiddelde lostijd is {average_unload_time} minuten per container')
print(f'De gemiddelde laadtijd is {average_load_time} minuten per container')

# Berekening 1
import math
x = 9.1                 
y = math.sqrt(3 * x + (1 + x) ** 2)

print(f"De waarde van y = {y} als x = {x}.")

# Berekening 2

a = 0.87
b = 22.7
c = 5.03

step1 = b**2
step2 = 4 * a * c
step3 = step1 - step2
step4 = math.sqrt(step3)
step5 = -b + step4
step6 = 2 * a
y = step5 / step6

print(f"De waarde van y = {y} als a = {a}, b = {b} en c = {c}")

# Berekening 3

# Information
t = 4
v = 179875474.8
c = 299_792_458

# Breakup the formula
step1 = v**2
step2 = c**2
step3 = step1 / step2
step4 = 1 - step3

step5 = v * step4
step6 = 1 / step5
delta = t * step6

# Display result
print(f'Vanaf een komeet gezien zit u {delta} uur op de tuinstoel.')
print(f'Vanaf een komeet gezien zit u {delta * 60} minuten op de tuinstoel.')
print(f'Vanaf een komeet gezien zit u {delta * 60 * 60} seconden op de tuinstoel.')
