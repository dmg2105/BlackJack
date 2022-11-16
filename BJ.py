import random


def As(Suma_total, a_sumar):
    if a_sumar == 11 and Suma_total + a_sumar > 21:
        a_sumar = 1
    Suma_total += a_sumar
    return Suma_total


def figura(x):
    if x == 'J' or x == 'Q' or x == 'K':
        x = 10
    if x == 'A':
        x = 11
    return x


def cartas():
    x = [random.randint(1, 13)]
    if x == [1]:
        x = ['A']
    if x == [11]:
        x = ['J']
    if x == [12]:
        x = ['Q']
    if x == [13]:
        x = ['K']
    lista = ['\u2663', '\u2666', '\u2665', '\u2660']
    b = lista[random.randint(0, 3)]
    (x.append(b))
    devolver = (", ".join(map(str, x))).replace(",", "").replace(" ", "")
    return devolver


print('BIENVENIDO AL BLACK JACK')
Monedero = 100
jugar = True

while jugar:
    print('COMIENZA EL JUEGO')

    if Monedero > 0:
        print('Tienes', Monedero, 'monedas')
        print('Cuanto apuestas?')
        apuesta = abs(int(input()))

        while apuesta > Monedero:
            print('Demasiado apuestas cariño')
            apuesta = int(input('Prueba otra cantidad:\n'))

        Monedero = Monedero - apuesta
        Jugador_1 = cartas()
        Jugador_2 = cartas()
        Crupier_1 = cartas()
        Crupier_2 = cartas()

        valor1 = int(
            figura(Jugador_1.replace('\u2663', "").replace('\u2666', "").replace('\u2665', "").replace('\u2660', "")))
        valor2 = int(
            figura(Jugador_2.replace('\u2663', "").replace('\u2666', "").replace('\u2665', "").replace('\u2660', "")))
        valor3 = int(
            figura(Crupier_1.replace('\u2663', "").replace('\u2666', "").replace('\u2665', "").replace('\u2660', "")))
        valor4 = int(
            figura(Crupier_2.replace('\u2663', "").replace('\u2666', "").replace('\u2665', "").replace('\u2660', "")))

        print('Tus cartas son:', Jugador_1, Jugador_2)
        print('Carta del cupier:', Crupier_1)
        Crupier = As((figura(valor3)), (figura(valor4)))
        Jugador = As((figura(valor1)), (figura(valor2)))
        if Jugador == 21 and Crupier == 21:
            print('AMBOS TENÉIS BLACKJACK')
            Monedero += apuesta

        elif Crupier == 21:
            print('BLACKJACK DEL DEALER')
            print(Crupier_2)

        elif Jugador == 21:
            print('BLACKJACK')
            Monedero = int(Monedero + 5 / 2 * apuesta)

        else:
            print('Plantarse: 1')
            if Monedero >= apuesta:
                print('Duplicar: 2')
            print('Más cartas: 3')

            Decision = int(input())

            if Decision == 1:
                print('Cartas del crupier:', Crupier_1, Crupier_2)
                while Crupier < 17:
                    Extra_Crupier = cartas()
                    print('Carta del cupier:', Extra_Crupier)
                    Extra_Crupier = int(figura(
                        Extra_Crupier.replace('\u2663', "").replace('\u2666', "").replace('\u2665', "").replace(
                            '\u2660', "")))
                    Crupier = As(Crupier, Extra_Crupier)
                if Jugador == Crupier:
                    print('EMPATE')
                    Monedero += apuesta
                elif Crupier > 21 or Jugador > Crupier:
                    print('Ganaste')
                    Monedero = Monedero + 2 * apuesta
                elif Jugador < Crupier:
                    print('Perdiste')

            elif Decision == 2 and Monedero >= apuesta:
                Jugador_3 = cartas()
                valor5 = int(figura(
                    Jugador_3.replace('\u2663', "").replace('\u2666', "").replace('\u2665', "").replace('\u2660', "")))
                print('Nueva carta:', Jugador_3)
                Monedero = Monedero - apuesta
                if As(Jugador, (figura(valor5))) > 21:
                    print('PERDISTE')
                print('Cartas del crupier:', Crupier_1, Crupier_2)
                if As(Jugador, (figura(valor5))) <= 21:
                    while Crupier < 17:
                        Extra_Crupier = cartas()
                        print('Carta del cupier:', Extra_Crupier)
                        Extra_Crupier = int(figura(
                            Extra_Crupier.replace('\u2663', "").replace('\u2666', "").replace('\u2665', "").replace(
                                '\u2660', "")))
                        Crupier = As(Crupier, Extra_Crupier)
                    if As(Jugador, (figura(valor5))) == Crupier:
                        print('EMPATE')
                        Monedero = Monedero + 2 * apuesta
                    elif Crupier > 21 or As(Jugador, (figura(valor5))) > Crupier:
                        print('Ganaste')
                        Monedero = Monedero + 4 * apuesta
                    elif As(Jugador, (figura(valor5))) < Crupier:
                        print('Perdiste')

            elif Decision == 3:
                Suma = As(valor1, valor2)
                Otra_Jugador = True

                while Otra_Jugador:

                    Extra_Jugador = cartas()
                    print('Carta nueva:', Extra_Jugador)
                    Extra_Jugador = int(figura(
                        Extra_Jugador.replace('\u2663', "").replace('\u2666', "").replace('\u2665', "").replace(
                            '\u2660', "")))
                    Suma = As(Suma, Extra_Jugador)
                    if Suma > 21:
                        Otra_Jugador = False
                    else:
                        print('¿Quieres otra carta?   (s/n)')
                        respuesta = input()
                        if respuesta != 's' and respuesta != 'S':
                            respuesta = input('¿Seguro que no quieres?    (s/n)')
                            if respuesta == 's' or respuesta == 'S':
                                Otra_Jugador = False

                print('Cartas del crupier:', Crupier_1, Crupier_2)
                if Suma <= 21:
                    while Crupier < 17:
                        Extra_Crupier = cartas()
                        print('Carta del cupier:', Extra_Crupier)
                        Extra_Crupier = int(figura(
                            Extra_Crupier.replace('\u2663', "").replace('\u2666', "").replace('\u2665', "").replace(
                                '\u2660', "")))
                        Crupier = As(Crupier, Extra_Crupier)
                    if Suma == Crupier:
                        print('EMPATE')
                        Monedero = Monedero + apuesta
                    elif Crupier > 21 or Suma > Crupier:
                        print('Ganaste')
                        Monedero = Monedero + 2 * apuesta
                    elif Suma < Crupier:
                        print('Perdiste')
                else:
                    print('Perdiste')

        print('Tus monedas son:', Monedero)

        jugar1 = input('¿Otra partida?   (s/n)\n')
        if jugar1 != 's':
            jugar = input('¿Otra partida? (¿Seguro?)   (s/n)')
            if jugar1 != 's':
                jugar = False
            else:
                jugar = True

    if Monedero <= 0:
        print('Te quedaste sin monedas.')
        jugar = False
print('Fue un placer. ¡¡Adiós!!')