## establecer una calificacion según el rango de categorias 

calif = float(input("Ingresa la calificacion del estudiante: "))

if calif >= 0 and calif <= 1.8:
    print("La calificacion fue deficiente")
elif calif > 1.8 and calif <= 2.9:
    print("La calificacion fue insuficiente")
elif calif >= 3.0 and calif <= 3.5:
    print ("La calificacion fue aceptable") 
elif calif >= 3.6 and calif <= 4.2:
    print ("La calificacion fue sobresaliente")
elif calif >= 4.2 and calif <= 5.0:
    print ("La calificacion fue Excelente")
    if calif >= 4.7:
        print("Merece medalla de honor")

        

