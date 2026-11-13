chef_aprendiz = 0
chef_maestro = 0
contador_chefs = 0

while contador_chefs <= 0:
    try:
        contador_chefs = int(input("agrega la cantidad de chefs a registrar: "))

        if contador_chefs < 0:
        
            print("el numero debe ser positivo y mayor a 0")  
    except ValueError:
        print("“¡Ingrediente inválido! Ingresa un entero positivo para continuar el registro.”")

for i in range (contador_chefs):
    experiencia = 0
    while experiencia <= 0:
        try:
            experiencia = int(input("ingresa la experiencia del chef (1 al 10): "))
            if experiencia > 5:
                print("registrado con exito")
                chef_maestro = chef_maestro +  1
            else:
                print("registrado con exito")
                chef_aprendiz = chef_aprendiz + 1
        except ValueError:
            print("“¡Ingrediente inválido! Ingresa un entero positivo para continuar el registro.”")


    codigo_culinario = ""
    while len(codigo_culinario) < 8:
        codigo_culinario = input("ingrese su codigo culinario(8 digitos como minimo): ").lower().replace()
        if len(codigo_culinario) >= 8:
            print("codigo culineario registrado")
        else:
            print("el codigo culinario debe ser mayor a 8")

print ( "la escuela cuenta con ", chef_aprendiz, "chefs aprendices y", chef_maestro, "chefs maestros, !A COCINAR¡")


