import random
def palabra_secreta():
    indice_categoria = random.randrange(0,2)
    indice_palabra = random.randrange(0,20)
    palabra_secreta=[
    [
    "perro", "gato", "tigre", "elefante", "jirafa", 
    "cebra", "zorro", "oso", "lobo", "rana", 
    "pato", "caballo", "vaca", "oveja", "cerdo", 
    "gallina", "tortuga", "conejo", "mono", "loro"
    ],
    [
    "Carlos", "Marcos", "Lucas", "Sara", "Daniel", 
    "David", "Pablo", "Mateo", "Alejandro", "Carmen", 
    "Elena", "Paula", "Laura", "Alba", "Hugo", 
    "Diego", "Gabriel", "Manuel", "Bruno", "Gonzalo"
    ]]
    
    print("Bienvenido al juego de ahorcados")
    if indice_categoria == 0:
        print("La categoria es: Animales")
        print(palabra_secreta[0])
    else:
        print("La categoria es: Nombres de personas")
        print(palabra_secreta[1])
    
    return palabra_secreta[indice_categoria][indice_palabra].lower()

def juego_ahorcado(palabra):
    vandera = True
    contador = 5
    print("Tines 6 intentos")
    while vandera==True:
        mi_palabra = input("Ingrese la palabra: ").lower().strip()
        if palabra == mi_palabra:
            print("Correcto, adivinaste la palabra 😁")
            print(f"Tu palabra {mi_palabra}")
            print(f"Palabra correcta {palabra}")
        else:
            if contador>0 and contador<=6:
                print("Palabra incorrecta, intentalo de nuevo")
                print(f"Te quedan {contador} intentos")
                contador-=1
            else:
                print("Perdiste, ya no te quedan mas intentos 😵")
                print(f"La palabra correcta era {palabra}")
                print("Fin del juego")
                vandera=False
                
    
juego_ahorcado(palabra_secreta())
    