notas = [0, 0, 9.0, 8.0, 5.0, 10.0, 7.0, 7.5, 4.0, 10.0, 7.0, 7.0, 8.0, 8.0, 7.5]

cantidad_alumnos_media = 0
for notas in notas:
    if 7.0 <= nota <= 8.0:
        cantidad_alumnos_media +=1

print (cantidad_alumnos_media)