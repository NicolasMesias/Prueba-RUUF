def calculo_n ():
    print("-" * 60)

    try:
        a = int(input("Ingrese alto de panel: "))
        b = int(input("Ingrese ancho de panel: "))
        x = int(input("Ingrese alto de techo: "))
        y = int(input("Ingrese ancho de techo: "))

        if a<=0 or b<=0 or x<=0 or y<=0:
            print("-" * 60)
            print("Porfavor, ingrese un numero positivo")
            print("-" * 60)
            return

    except ValueError:
        print("-" * 60)
        print("Porfavor, ingrese un numero valido")
        print("-" * 60)
        return

    print("-" * 60)

    if a>x and b>x:
        print("Las dimensiones del techo no cumplen con el alto de un panel")
        print("-" * 60)
        return
    elif a>y and b>y:
        print("Las dimensiones del techo no cumplen con el ancho de un panel")
        print("-" * 60)
        return

    dim_paneles = a*b
    dim_techo   = x*y

    cantidad = dim_techo//dim_paneles

    mensaje = f"En un techo de dimensiones {x}x{y} tienen capacidad para: {cantidad} paneles \n{'-' * 60}"

    print(mensaje)

calculo_n()
