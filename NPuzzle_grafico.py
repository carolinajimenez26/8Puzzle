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

def getImage(numero, uno, dos, tres, cuatro, cinco, seis, siete, ocho):
    if numero == "1":
        return uno
    if numero == "2":
        return dos
    if numero == "3":
        return tres
    if numero == "4":
        return cuatro
    if numero == "5":
        return cinco
    if numero == "6":
        return seis
    if numero == "7":
        return siete
    if numero == "8":
        return ocho
    
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
    

def main():
    win = GraphWin('Moving an image', 500, 500)
    
    #Cargamos las imagenes de los numeros
    uno    = Image(Point(150, 200), "1.png")
    
    dos    = Image(Point((uno.getAnchor().getX()) + 1 + (uno.getWidth()), uno.getAnchor().getY()), "2.png")
    
    tres   = Image(Point((dos.getAnchor().getX()) + 1 + (dos.getWidth()), dos.getAnchor().getY()), "3.png")
                   
    cuatro = Image(Point(uno.getAnchor().getX(), (uno.getAnchor().getY()) + 1 + (uno.getHeight())), "4.png")
    
    cinco  = Image(Point((cuatro.getAnchor().getX()) + 1 + (cuatro.getWidth()), cuatro.getAnchor().getY()),  "5.png")
                   
    seis   = Image(Point((cinco.getAnchor().getX()) + 1 + (cinco.getWidth()), cinco.getAnchor().getY()),  "6.png")
                   
    siete  = Image(Point(cuatro.getAnchor().getX(), (cuatro.getAnchor().getY()) + 1 + (cuatro.getHeight())), "7.png")
                   
    ocho   = Image(Point((siete.getAnchor().getX()) + 1 + (siete.getWidth()), siete.getAnchor().getY()), "8.png")
                   
    cero  = Image(Point((ocho.getAnchor().getX()) + 1 + (ocho.getWidth()), ocho.getAnchor().getY()), "0.png")

    
    #Dibujamos las imagenes en la ventana
    uno.draw(win)
    dos.draw(win)
    tres.draw(win)
    cuatro.draw(win)
    cinco.draw(win)
    seis.draw(win)
    siete.draw(win)
    ocho.draw(win)
    cero.draw(win)

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
        img = getImage(e, uno, dos, tres, cuatro, cinco, seis, siete, ocho)

        #print isRightSide(ocho, cero)
        
        #Validamos que se puedan intercambiar
        if ValidMovement(cero, img):
            Move(cero, img) #Si el movimiento es valido, hagalo
        else :
            print "Invalid movement, try again"
            
        print "Xcero : " + str(cero.getAnchor().getX()) + " Ycero : " + str(cero.getAnchor().getY()) + " Ximg : " + str(img.getAnchor().getX()) + " Yimg : " + str(cero.getAnchor().getY())
            

main()