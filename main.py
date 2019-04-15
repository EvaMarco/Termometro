import pygame
import sys
from pygame.locals import *


class Termometro:
    def __init__(self):
        self.custome = pygame.image.load('images/termo.png')


class Numerinput:
    __value = 0
    __strvalue = '0'
    __position = [0, 0]
    __size = [0, 0]

    def __init__(self, value = 0):

        self.__font = pygame.font.SysFont('Arial', 24)

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

        return(rect, textblock)

        # Creamos un setter y un getter del value y hacemos que solo acepte enteros.
        # Lo vamos a hacer para el tamaño y la posicion.
    def value(self, val=None):

        if val == None:
            return self.__value
        else:
            val = str(val)
            # La comprobación.
            try:
                self.__value = int(val)
                self.__strvalue = val
            except:
                pass

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

    def pos(self, val=None):
        if val == None:
            return self.__position
        else:
            try:
                self.__position= [int(val[0]), int(val[1])]
            except:
                pass

    def size(self, val=None):

        if val == None:
            return self.__size
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

    def __init__(self):
        self.__screen = pygame.display.set_mode((550, 640))
        pygame.display.set_caption('Termómetro')
        self.__screen.fill((244, 236, 203))

        self.termometro = Termometro()
        self.entrada = Numerinput()
        self.entrada.pos((256, 70))
        self.entrada.size((133, 50))

    def __on_close(self):
        pygame.quit()
        sys.exit()

    def start(self):

        # Ciclo de eventos.
        while True:
            # Comprobación de eventos.

            for event in pygame.event.get():
                if event.type == QUIT:
                    self.__on_close()
            # Modifica los inputs.

            # Pinta las modificaciones.
            # Termometro
            self.__screen.blit(self.termometro.custome, (100, 70))

            # Para que me pinte el rectangulo, de un color y con un tamaño.
            text = self.entrada.render()
            pygame.draw.rect(self.__screen, (255, 255, 255), text[0])
            # Para que me pinte los números, los trataremos como un disfraz.
            self.__screen.blit(text[1], self.entrada.pos())
            # Refresco de pantalla.
            pygame.display.flip()

# Llamada principal.


if __name__ == '__main__':
    pygame.init()
    app = Mainapp()
    app.start()


