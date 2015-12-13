#coordImage = Point((img.getAnchor().getX()),(img.getAnchor().getY()))

from graphics import *
import time

def MoveRight(img):
    for i in range(1,9):
        time.sleep(0.25)
        img.move(10,0)
    img.move(1,0)
        
def MoveLeft(img):
    for i in range(1,9):
        time.sleep(0.25)
        img.move(-10,0)
    img.move(-1,0)

def MoveUp(img):
    for i in range(1,9):
        time.sleep(0.25)
        img.move(0,-10)
    img.move(0,-1)

def MoveDown(img):
    for i in range(1,9):
        time.sleep(0.25)
        img.move(0,10)
    img.move(0,1)

def btnEvent(entry):
    e = entry.getText()
    return e

#Retorna la imagen que equivale al "numero"
def getImage(numero, imagenes, nombres):
    for i in range(0,9):
        if nombres[i] == str(numero) :
            return imagenes[i]
    
def isRightSide(img1, img2): #retorna True si la imagen2 esta a la derecha de la imagen1 

    if img1.getAnchor().getX() + img1.getWidth() + 1 == img2.getAnchor().getX() and img1.getAnchor().getY() == img2.getAnchor().getY() :
        return True
    else :
        return False

def isLeftSide(img1, img2): #retorna True si la imagen2 esta a la derecha de la imagen1 
    if img1.getAnchor().getX() - img1.getWidth() - 1 == img2.getAnchor().getX() and img1.getAnchor().getY() == img2.getAnchor().getY() :
        return True
    else :
        return False

def isDownSide(img1, img2): #retorna True si la imagen2 esta a la derecha de la imagen1 
    if img1.getAnchor().getX() == img2.getAnchor().getX() and img1.getAnchor().getY() + img1.getHeight() + 1 == img2.getAnchor().getY() :
        return True
    else :
        return False

def isUpSide(img1, img2): #retorna True si la imagen2 esta a la derecha de la imagen1 
    if img1.getAnchor().getX() == img2.getAnchor().getX() and img1.getAnchor().getY() - img1.getHeight() - 1 == img2.getAnchor().getY() :
        return True
    else :
        return False

def ValidMovement(cero, img):
    if isRightSide(cero, img) or isLeftSide(cero, img) or isDownSide(cero, img) or isUpSide(cero, img) :
        return True
    else : 
        return False
    
def Move(cero, img): #Cambia de posicion dos imagenes
    if isRightSide(cero, img):
        MoveRight(cero)
        MoveLeft(img)
    elif isLeftSide(cero, img):
        MoveLeft(cero)
        MoveRight(img)
    elif isDownSide(cero, img):
        MoveDown(cero)
        MoveUp(img)
    else : #Deberia estar entonces arriba del cero
        MoveUp(cero)
        MoveDown(img)
 
def CreateImage(number, index, prev, i, array):
    
    if index == 0 : #la primera imagen
        if number == "1" :
            uno = Image(Point(150, 200), "1.png")
            array[index] = number
            return uno
        if number == "2" :
            dos = Image(Point(150, 200), "2.png")
            array[index] = number
            return dos
        if number == "3" :
            tres = Image(Point(150, 200), "3.png")
            array[index] = number
            return tres
        if number == "4" :
            cuatro = Image(Point(150, 200), "4.png")
            array[index] = number
            return cuatro
        if number == "5" :
            cinco = Image(Point(150, 200), "5.png")
            array[index] = number
            return cinco
        if number == "6" :
            seis = Image(Point(150, 200), "6.png")
            array[index] = number
            return seis
        if number == "7" :
            siete = Image(Point(150, 200), "7.png")
            array[index] = number
            return siete
        if number == "8" :
            ocho = Image(Point(150, 200), "8.png")
            array[index] = number
            return ocho
        else : #number == "0" :
            cero = Image(Point(150, 200), "0.png")
            array[index] = number
            return cero
    
    if index == 1 or index == 2 or index == 4 or index == 5 or index == 7 or index == 8:
        if number == "1" :
            uno = Image(Point((prev.getAnchor().getX()) + 1 + (prev.getWidth()), prev.getAnchor().getY()), "1.png")
            array[index] = number
            return uno
        if number == "2" :
            dos = Image(Point((prev.getAnchor().getX()) + 1 + (prev.getWidth()), prev.getAnchor().getY()), "2.png")
            array[index] = number
            return dos
        if number == "3" :
            tres = Image(Point((prev.getAnchor().getX()) + 1 + (prev.getWidth()), prev.getAnchor().getY()), "3.png")
            array[index] = number
            return tres
        if number == "4" :
            cuatro = Image(Point((prev.getAnchor().getX()) + 1 + (prev.getWidth()), prev.getAnchor().getY()), "4.png")
            array[index] = number
            return cuatro
        if number == "5" :
            cinco = Image(Point((prev.getAnchor().getX()) + 1 + (prev.getWidth()), prev.getAnchor().getY()), "5.png")
            array[index] = number
            return cinco
        if number == "6" :
            seis = Image(Point((prev.getAnchor().getX()) + 1 + (prev.getWidth()), prev.getAnchor().getY()), "6.png")
            array[index] = number
            return seis
        if number == "7" :
            siete = Image(Point((prev.getAnchor().getX()) + 1 + (prev.getWidth()), prev.getAnchor().getY()), "7.png")
            array[index] = number
            return siete
        if number == "8" :
            ocho = Image(Point((prev.getAnchor().getX()) + 1 + (prev.getWidth()), prev.getAnchor().getY()), "8.png")
            array[index] = number
            return ocho
        else : #number == "0" :
            cero = Image(Point((prev.getAnchor().getX()) + 1 + (prev.getWidth()), prev.getAnchor().getY()), "0.png")
            array[index] = number
            return cero
            
    else : # index = 3 or index = 6
        if number == "1" :
            uno = Image(Point(prev.getAnchor().getX(), (prev.getAnchor().getY()) + 1 + ((prev.getHeight())*i) ), "1.png")
            array[index] = number
            return uno
        if number == "2" :
            dos = Image(Point(prev.getAnchor().getX(), (prev.getAnchor().getY()) + 1 + ((prev.getHeight())*i) ), "2.png")
            array[index] = number
            return dos
        if number == "3" :
            tres = Image(Point(prev.getAnchor().getX(), (prev.getAnchor().getY()) + 1 + ((prev.getHeight())*i) ), "3.png")
            array[index] = number
            return tres
        if number == "4" :
            cuatro = Image(Point(prev.getAnchor().getX(), (prev.getAnchor().getY()) + 1 + ((prev.getHeight())*i) ), "4.png")
            array[index] = number
            return cuatro
        if number == "5" :
            cinco = Image(Point(prev.getAnchor().getX(), (prev.getAnchor().getY()) + 1 + ((prev.getHeight())*i) ), "5.png")
            array[index] = number
            return cinco
        if number == "6" :
            seis = Image(Point(prev.getAnchor().getX(), (prev.getAnchor().getY()) + 1 + ((prev.getHeight())*i) ), "6.png")
            array[index] = number
            return seis
        if number == "7" :
            siete = Image(Point(prev.getAnchor().getX(), (prev.getAnchor().getY()) + 1 + ((prev.getHeight())*i) ), "7.png")
            array[index] = number
            return siete
        if number == "8" :
            ocho = Image(Point(prev.getAnchor().getX(), (prev.getAnchor().getY()) + 1 + ((prev.getHeight())*i) ), "8.png")
            array[index] = number
            return ocho
        else : #number == "0" :
            cero = Image(Point(prev.getAnchor().getX(), (prev.getAnchor().getY()) + 1 + ((prev.getHeight())*i) ), "0.png")
            array[index] = number
            return cero

def main():
    win = GraphWin('Moving an image', 500, 500)
    goal =  ["1","2","3","4","5","6","7","8","0"]
    #arrayNumbers es el tablero que se debe cambiar para enviar
    arrayNumbers =  ["1","2","0","3","4","5","6","7","8"]
    Nada = Image(Point(0,0), "9.png")
    arrayImages = [Nada,Nada,Nada,Nada,Nada,Nada,Nada,Nada,Nada]
    arrayNames = ["","","","","","","","",""]
    
    n = 0
    #Cargamos las imagenes de los numeros
    for i in range(0, 9):
        
        if i == 3 or i == 6 or i == 0:
            img = CreateImage(arrayNumbers[i], i, arrayImages[0], n, arrayNames)
            arrayImages[i] = img #arreglo de imagenes
            n = n+1
        else :
            img = CreateImage(arrayNumbers[i], i, arrayImages[i-1], n, arrayNames)
            arrayImages[i] = img #arreglo de imagenes
            
    n = 0

    #Dibujamos las imagenes en la ventana
    for i in range(0,9):
        arrayImages[i].draw(win)
  
  
    #Texto que le pide al usuario ingresar los numeros para intercambiarlos
    message = Text(Point(win.getWidth()/2, 30), 'Ingrese el numero para cambiar de posicion:')
    message.setTextColor('red')
    message.setStyle('italic')
    message.setSize(15)
    message.draw(win)
    
    #Definimos la entrada del numero
    entry = Entry(Point(message.getAnchor().getX() ,message.getAnchor().getY() + 30), 5)
    
    entry.setTextColor("white")
    
    entry.draw(win)
    
    while True: #Mientras no haya ganado
        #Obtenemos la informacion de las entradas cuando presione en pantalla
        win.getMouse()
        e = btnEvent(entry)
        
        #Obtenemos la imagen
        img = getImage(e, arrayImages, arrayNames)
        
        #Obtenemos el cero
        cero = getImage("0",arrayImages, arrayNames)
        
        #Validamos que se puedan intercambiar
        if ValidMovement(cero, img):
            Move(cero, img) #Si el movimiento es valido, hagalo
        else :
            print "Invalid movement, try again"
            
        
    
    win.getMouse()

main()