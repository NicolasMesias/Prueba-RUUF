def calculo_n ():

    pregunta = input("Para calcular en un techo Triangular, ingrese T / Para techo Rectangular, ingrese R: ")
    pregunta = pregunta.upper()

    if pregunta != "R" and pregunta != "T":
        print("Opcion no valida")
        return

    elif pregunta == "R":
    
        a = int(input("Ingrese alto de panel: "))
        b = int(input("Ingrese ancho de panel: "))

        x = int(input("Ingrese alto de techo: "))
        y = int(input("Ingrese ancho de techo: "))

        dim_paneles = a*b
        dim_techo = x*y

        cantidad = dim_techo//dim_paneles

    elif pregunta == "T":
        a = int(input("Ingrese alto de panel: "))
        b = int(input("Ingrese ancho de panel: "))

        x = int(input("Ingrese alto de techo: "))
        y = int(input("Ingrese ancho de techo: "))

        dim_paneles = a*b
        dim_techo   = x*y*0.5
        cantidad    = dim_techo//dim_paneles

    return print(cantidad)

calculo_n()