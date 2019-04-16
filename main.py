import pygame
import sys
from pygame.locals import *


class Termometro:

    # Función constructora.
    def __init__(self):
        # Disfraz del termometro.
        self.custome = pygame.image.load('images/termo.png')

    # Función para convertir
    def convertir(self, grados, tounidad):
        if tounidad == 'F':
            resultado = (grados * 9/5) + 32
        elif tounidad == 'C':
            resultado = (grados - 32) * 5/9
        else:
            resultado = grados
        # Devolvemos el resultado formateado.
        return '{:1.2f}'.format(resultado)


class Selector:
    __tipounidad = None

    def __init__(self, unidad='C'):
        # Los disfraces para el selector.
        self.__custome = ['images/C.png', 'images/F.png']
        self.__tipounidad = unidad

    # Para que nos cambie de disfraz si cambiamos la unidad.

    def custome(self):
        if self.__tipounidad == 'F':
            return self.__custome[1]
        else:
            return self.__custome[0]

    # Esto sirve para cambiar la unidad de F a C o viceversa. Es un Setter.

    def change(self):

        if self.__tipounidad == 'F':
            self.__tipounidad = 'C'
        else:
            self.__tipounidad = 'F'

    def unidad(self):
        return self.__tipounidad


class Numerinput:
    __value = 0
    __strvalue = ''
    __position = [0, 0]
    __size = [0, 0]
    __pointcount = 0

    # Función constructora.
    def __init__(self, value=0):
        # Creamos la fuente.
        self.__font = pygame.font.SysFont('Arial', 24)
        # Necesitamo saber si es self, o una variable de usar y tirar.
        # Con esta orden le digo que me transforme el valor por defecto en el que informamos al llamar a la función.
        # Llamamos a nuestra propia función value, dentro de una clase da igual el orden.
        self.value(value)
        # Usamos el setter en este caso.

    # Función para manejar los eventos.

    def on_event(self, event):
        # Si el evento es que se pulsa una tecla.
        if event.type == KEYDOWN:
            # Comprobamos que sea un número o el simbolo negativo y la longitud de la cadena.
            # También hacemos una comprobación de puntos para no poder introducir mas de uno.
            if event.unicode in '0123456789-' and len(self.__strvalue) <= 9 or event.unicode == '.' \
                    and self.__pointcount == 0:
                # Hacemos q los numeros se vayan concatenando.
                self.__strvalue += event.unicode

                # Usamos el setter de value para asignar el valor.

                self.value(self.__strvalue)
                print(self.__strvalue, self.__value)
                # Si hay un punto ponme el contador a 1.
                if event.unicode == '.':
                    self.__pointcount += 1

                # Perrmitimos que se pueda borrar.
            elif event.key == K_BACKSPACE:
                # Refrescamos el contador de puntos, por si acaso lo borramos.
                if self.__strvalue[:-1] == '.':
                    self.__pointcount -= 1
                # Reducimos la longitud de la cadeba.
                self.__strvalue = self.__strvalue[0:-1]

                # Llamamos al setter value para que me compruebe que se puede transformar.
                self.value(self.__strvalue)
                print(self.__strvalue, self.__value)

    def render(self):
        # Creación del texto.
        textblock = self.__font.render(self.__strvalue, True, (74, 74, 74))

        # Rectangulo del texto.
        rect = textblock.get_rect()
        # Posición.
        rect.left = self.__position[0]
        rect.top = self.__position[1]
        # Cambio de tamaño del rectangulo.
        rect.size = self.__size
        # Hacemos que nos devuelva los rectángulos en forma de diccionario o tupla.

        return rect, textblock

        # Creamos un setter y un getter del value, tamaño y posición.

    def value(self, val=None):

        # Getter de value.
        if val is None:
            return self.__value

        # Setter de value. Con compración de que se pueda transformar en float.
        else:
            val = str(val)
            # La comprobación.
            try:
                self.__value = float(val)
                self.__strvalue = val

                # Contador de puntos en la cadena, para que no de errores al trasformarlo en float.
                if '.' in self.__strvalue:
                    self.__pointcount = 1
                else:
                    self.__pointcount = 0
            except:
                pass
    '''
        def posy(self, val=None):
            if val == None:
                return self.__position[1]
            else:
                try:
                    self.__position[1] = int(val)
                except:
                    pass
    
        def posx(self, val=None):
            if val == None:
                return self.__position[0]
            else:
                try:
                    self.__position[0] = int(val)
                except:
                    pass
    '''

    def pos(self, val=None):
        # Getter de posición.
        if val is None:
            return self.__position

        # Setter de posición.
        else:
            try:
                self.__position = [int(val[0]), int(val[1])]
            except:
                pass

    def size(self, val=None):
        # Getter de Size.

        if val is None:
            return self.__size
        # Setter de Size
        else:
            try:
                w = int(val[0])
                h = int(val[1])
                self.__size = [w, h]
            except:
                pass


class Mainapp:

    termometro = None
    entrada = None
    selector = None

    # Función constructora.

    def __init__(self):

        # Creamos la pantalla.
        self.__screen = pygame.display.set_mode((550, 640))
        pygame.display.set_caption('Termómetro')
        self.__screen.fill((244, 236, 203))

        # Inicializamos termometro.

        self.termometro = Termometro()

        # Inicializamos la entrada.

        self.entrada = Numerinput()
        self.entrada.pos((256, 70))
        self.entrada.size((133, 50))

        # Inicializamos el selector.

        self.selector = Selector()

    # Función de apagado.

    def __on_close(self):
        pygame.quit()
        sys.exit()

    # Función de arranque.
    def start(self):

        # Ciclo de eventos.
        while True:

            # Comprobación de eventos.
            for event in pygame.event.get():
                if event.type == QUIT:
                    # Llamada a la función de apagado.
                    self.__on_close()

                # Si el evento no es apagar, nos vamos a entrada (Numerimput) a ver que ocurre.
                self.entrada.on_event(event)

                # Si el evento no es ni cerrar ni lo q entra por entrada, seguimos.
                # Si el evento es click.

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Primero cambiamos de F a C.
                    self.selector.change()
                    # Le decimos a nuestro getter de value q nos de el valor.
                    grados = self.entrada.value()
                    # Llamamos al getter de selector para que nos diga en que unidad esta.
                    nuevaunidad = self.selector.unidad()
                    print(nuevaunidad)
                    # Calculamos la temperatura llamando a conversor.
                    temperatura = self.termometro.convertir(grados, nuevaunidad)
                    print(temperatura)
                    # Asignamos la nueva temperatura a la entrada.
                    self.entrada.value(temperatura)

            # Pintar fondo de pantalla.
            self.__screen.fill((244, 236, 203))
            # Pintar el termometro
            self.__screen.blit(self.termometro.custome, (100, 70))
            # Para que me pinte el rectangulo, de un color y con un tamaño.
            text = self.entrada.render()
            pygame.draw.rect(self.__screen, (255, 255, 255), text[0])
            # Para que me pinte los números, los trataremos como un disfraz.
            self.__screen.blit(text[1], self.entrada.pos())
            # Para que me pinte el selector.
            self.__screen.blit(self.selector.custome(), (262, 153))

            # Refresco de pantalla.
            pygame.display.flip()

# Llamada principal.


if __name__ == '__main__':
    pygame.init()
    app = Mainapp()
    app.start()


