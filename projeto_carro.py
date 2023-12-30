#Autor: Caio Randoli

#****TECLAS PARA O CARRO ANDAR É "W" E "S"!!!****

from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys
import math

name = 'Veiculo_P2'
especularidade = [1.0,1.0,1.0,1.0] 
especMaterial = 60
px = 0
py = 0
pz = 0
z = 0
distancia = 10 # Mudar para altera a distancia do objeto.

def drawC():
    
    glRotatef(px, 1, 0, 0) # Rotaciona em relação ao eixo X (Setas cima e baixo)
    glRotatef(py, 0, 1, 0) # Rotaciona em relação ao eixo Y (Setas direita e esquerda)
    glRotatef(pz, 0, 0, 1) # Rotaciona em relação ao eixo Z (teclas PgUp e PgDn)
    glTranslatef(0, 0, z)
    
#--------- PARTE DE BAIXO DO CARRO ---------#
    
    glBegin(GL_QUADS)
    glColor3f(0, 0.7, 0.9)
    glVertex3f(1.95, -1.2, 4.2)
    glVertex3f(-1.95, -1.2, 4.2)
    glVertex3f(-1.95, -1.2, -5.0)
    glVertex3f(1.95, -1.2, -5.0)
    glEnd()
#--------------FRENTE DO CARRO--------------#
    
    #Contorno Vidro
    glBegin(GL_QUADS)
    glColor3f(0, 0.7, 0.9)
    glVertex3f(1.7, 1.1, 0.9)
    glVertex3f(-1.7, 1.1, 0.9)
    glVertex3f(-1.7, 1, 1)
    glVertex3f(1.7, 1, 1)
    glEnd()
    
    glBegin(GL_QUADS)
    glColor3f(0, 0.7, 0.9)
    glVertex3f(-1.5, 1, 1)
    glVertex3f(-1.7, 1, 1)
    glVertex3f(-1.7, 0.2, 2.0)
    glVertex3f(-1.5, 0.2, 2.0)
    glEnd()
    
    glBegin(GL_QUADS)
    glColor3f(0, 0.7, 0.9)
    glVertex3f(1.5, 1, 1)
    glVertex3f(1.7, 1, 1)
    glVertex3f(1.7, 0.2, 2.0)
    glVertex3f(1.5, 0.2, 2.0)
    glEnd()

    #Vidro Frente
    glBegin(GL_QUADS)
    glColor3f(1, 1, 1)
    glVertex3f(1.5, 1, 1)
    glVertex3f(-1.5, 1, 1)
    glVertex3f(-1.5, 0.2, 2.0)
    glVertex3f(1.5, 0.2, 2.0)
    glEnd()
    
    #Retrovisor esquerdo
    glBegin(GL_QUADS)
    glColor3f(0, 0, 0)
    glVertex3f(-1.7, 0.5, 1.7)
    glVertex3f(-2, 0.5, 1.65)
    glVertex3f(-2, 0.2, 1.75)
    glVertex3f(-1.7, 0.2, 1.9)
    glEnd()
    
    #Retrovisor direito
    glBegin(GL_QUADS)
    glColor3f(0, 0, 0)
    glVertex3f(1.7, 0.5, 1.7)
    glVertex3f(2, 0.5, 1.65)
    glVertex3f(2, 0.2, 1.75)
    glVertex3f(1.7, 0.2, 1.9)
    glEnd()

    #Capo
    glBegin(GL_QUADS)
    glColor3f(0, 0.7, 0.9)
    glVertex3f(1.7, 0.2, 2.0)
    glVertex3f(-1.7, 0.2, 2.0)
    glVertex3f(-1.7, -0.1, 4)
    glVertex3f(1.7, -0.1, 4)
    glEnd()
    
    glBegin(GL_QUADS)
    glColor3f(0, 0.7, 0.9)
    glVertex3f(0.7, -0.11, 4)
    glVertex3f(-0.7, -0.11, 4)
    glVertex3f(-0.7, -0.25, 4.05)
    glVertex3f(0.7, -0.25, 4.05)
    glEnd()
    
    #Farol Direito
    glBegin(GL_QUADS)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(0.7, -0.11, 4)
    glVertex3f(1.7, -0.11, 4)
    glVertex3f(1.95, -0.5, 4.2)
    glVertex3f(0.6, -0.5, 4.2)
    glEnd()
    
    #Farol Esquerdo
    glBegin(GL_QUADS)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(-0.7, -0.11, 4)
    glVertex3f(-1.7, -0.11, 4)
    glVertex3f(-1.95, -0.5, 4.2)
    glVertex3f(-0.6, -0.5, 4.2)
    glEnd()
    
    #Grade
    glBegin(GL_QUADS)
    glColor3f(0, 0, 0)
    glVertex3f(0.68, -0.25, 4.05)
    glVertex3f(-0.68, -0.25, 4.05)
    glVertex3f(-0.61, -0.5, 4.2)
    glVertex3f(0.61, -0.5, 4.2)
    glEnd()
    
    #Para choque
    glBegin(GL_QUADS)
    glColor3f(0, 0, 0)
    glVertex3f(1.95, -0.5, 4.2)
    glVertex3f(-1.95, -0.5, 4.2)
    glVertex3f(-1.95, -0.55, 4.3)
    glVertex3f(1.95, -0.55, 4.3)
    glEnd()
    
    glBegin(GL_QUADS)
    glColor3f(0, 0, 0)
    glVertex3f(1.95, -0.55, 4.3)
    glVertex3f(-1.95, -0.55, 4.3)
    glVertex3f(-1.95, -0.7, 4.3)
    glVertex3f(1.95, -0.7, 4.3)
    glEnd()
    
    glBegin(GL_QUADS)
    glColor3f(0, 0, 0)
    glVertex3f(1.95, -0.7, 4.3)
    glVertex3f(-1.95, -0.7, 4.3)
    glVertex3f(-1.9, -1.2, 4.2)
    glVertex3f(1.9, -1.2, 4.2)
    glEnd()
    
#------------PARTE DE CIMA DO CARRO---------#    
    
    glBegin(GL_POLYGON)
    glColor3f(0, 0.7, 0.9)
    glVertex3f(1.7, 1.1, -2.0)
    glVertex3f(-1.7, 1.1, -2.0)
    glVertex3f(-1.7, 1.1, 1.0)
    glVertex3f(1.7, 1.1, 1.0)
    glEnd()    
    
#------------PARTE DE TRÁS DO CARRO---------#    
    
    #Contorno Vidro
    glBegin(GL_QUADS)
    glColor3f(0, 0.7, 0.9)
    glVertex3f(1.7, 1.1, -1.9)
    glVertex3f(-1.7, 1.1, -1.9)
    glVertex3f(-1.7, 1, -2)
    glVertex3f(1.7, 1, -2)
    glEnd()
    
    glBegin(GL_QUADS)
    glColor3f(0, 0.7, 0.9)
    glVertex3f(-1.5, 1, -2)
    glVertex3f(-1.7, 1, -2)
    glVertex3f(-1.7, 0.2, -3.0)
    glVertex3f(-1.5, 0.2, -3.0)
    glEnd()
    
    glBegin(GL_QUADS)
    glColor3f(0, 0.7, 0.9)
    glVertex3f(1.5, 1, -2)
    glVertex3f(1.7, 1, -2)
    glVertex3f(1.7, 0.2, -3.0)
    glVertex3f(1.5, 0.2, -3.0)
    glEnd()
    
    #Vidro atrás
    glBegin(GL_QUADS)
    glColor3f(1, 1, 1)
    glVertex3f(1.5, 1, -2)
    glVertex3f(-1.5, 1, -2)
    glVertex3f(-1.5, 0.2, -3.0)
    glVertex3f(1.5, 0.2, -3.0)
    glEnd()
    
    #Porta malas
    glBegin(GL_QUADS)
    glColor3f(0, 0.7, 0.9)
    glVertex3f(1.7, 0.2, -3)
    glVertex3f(1.7, 0.2, -5)
    glVertex3f(-1.7, 0.2, -5)
    glVertex3f(-1.7, 0.2, -3)
    glEnd()
    
    #Traseira
    glBegin(GL_POLYGON)
    glColor3f(0, 0.7, 0.9)
    glVertex3f(1.7, 0.2, -5)
    glVertex3f(1.9, 0, -5)
    glVertex3f(-1.9, 0, -5)
    glVertex3f(-1.7, 0.2, -5)
    glEnd()
    
    glBegin(GL_POLYGON)
    glColor3f(0, 0.7, 0.9)
    glVertex3f(1.35, 0, -5)
    glVertex3f(1.3, -0.5, -5)
    glVertex3f(-1.3, -0.5, -5)
    glVertex3f(-1.35, 0, -5)
    glEnd()
    
    glBegin(GL_POLYGON)
    glColor3f(0, 0, 0)
    glVertex3f(1.95, -0.5, -5)
    glVertex3f(1.9, -1.2, -5)
    glVertex3f(-1.9, -1.2, -5)
    glVertex3f(-1.95, -0.5, -5)
    glEnd()
    
    glBegin(GL_POLYGON)
    glColor3f(0, 0, 0)
    glVertex3f(1.35, 0, -5.001)
    glVertex3f(1.35, -0.03, -5.001)
    glVertex3f(-1.35, -0.03, -5.001)
    glVertex3f(-1.35, 0, -5.001)
    glEnd()
    
    glBegin(GL_POLYGON)
    glColor3f(0.3, 0.3, 0.3)
    glVertex3f(-0.5, -0.65, -5.001)
    glVertex3f(-0.5, -1, -5.001)
    glVertex3f(0.5, -1, -5.001)
    glVertex3f(0.5, -0.65, -5.001)
    glEnd()
    
    #Fechadura
    raioRoda = 0.05
    glColor3f(0.05, 0.05, 0.05)
    ang = 0
    glBegin(GL_TRIANGLE_STRIP)
    while (ang <= 2 *math.pi):
        glVertex3f(raioRoda*math.cos(ang)+(0), raioRoda*math.sin(ang)+(-0.2), (-5.001))
        ang = ang + math.pi/100.0
        glVertex3f(raioRoda*math.cos(ang)+(0), raioRoda*math.sin(ang)+(-0.2), (-5.001))
    glEnd()
    ang = 0
    glBegin(GL_POLYGON)
    while (ang < 2 *math.pi):
        glVertex3f(raioRoda*math.cos(ang)+(0), raioRoda*math.sin(ang)+(-0.2), (-5.001))
        ang = ang + math.pi/100
    glEnd()
    ang = 0
    glBegin(GL_POLYGON)
    while (ang < 2 *math.pi):
        glVertex3f(raioRoda*math.cos(ang)+(0), raioRoda*math.sin(ang)+(-0.2), (-5.001))
        ang = ang + math.pi/100
    glEnd()
    
    #Farol Esquerdo
    glBegin(GL_POLYGON)
    glColor3f(1, 0, 0)
    glVertex3f(-1.35, 0, -5)
    glVertex3f(-1.3, -0.5, -5)
    glVertex3f(-1.95, -0.5, -5)
    glVertex3f(-1.9, 0, -5)
    glEnd()
    
    glBegin(GL_POLYGON)
    glColor3f(1, 0.6, 0)
    glVertex3f(-1.34, -0.2, -5.001)
    glVertex3f(-1.31, -0.4, -5.001)
    glVertex3f(-1.95, -0.4, -5.001)
    glVertex3f(-1.92, -0.2, -5.001)
    glEnd()
    
    #Farol Direito
    glBegin(GL_POLYGON)
    glColor3f(1, 0, 0)
    glVertex3f(1.35, 0, -5)
    glVertex3f(1.3, -0.5, -5)
    glVertex3f(1.95, -0.5, -5)
    glVertex3f(1.9, 0, -5)
    glEnd()
    
    glBegin(GL_POLYGON)
    glColor3f(1, 0.6, 0)
    glVertex3f(1.34, -0.2, -5.001)
    glVertex3f(1.31, -0.4, -5.001)
    glVertex3f(1.95, -0.4, -5.001)
    glVertex3f(1.92, -0.2, -5.001)
    glEnd()

#------------LADO ESQUERDO CARRO------------#

    glBegin(GL_POLYGON)
    glColor3f(0, 0.7, 0.9)
    glVertex3f(-1.7, 0.2, 2.0)
    glVertex3f(-1.7, 0.2, -2.0)
    glVertex3f(-1.7, -1.2, -2.0)
    glVertex3f(-1.7, -1.2, 2.0)
    glEnd()
    
    glBegin(GL_POLYGON)
    glColor3f(0, 0.7, 0.9)
    glVertex3f(-1.95, -0.5, 4.2)
    glVertex3f(-1.7, -0.11, 4)
    glVertex3f(-1.7, 0.2, 2)
    glVertex3f(-1.7, 0.2, -5)
    glVertex3f(-1.95, -0.5, -5)
    glVertex3f(-1.95, -0.5, 4.4)
    glEnd()
    
    glBegin(GL_POLYGON)
    glColor3f(0, 0, 0)
    glVertex3f(-1.7, 0.2, -3.5)
    glVertex3f(-1.7, 0.2, -5.0)
    glVertex3f(-1.7, -1.2, -5.0)
    glVertex3f(-1.7, -1.2, -3.5)
    glEnd()
    
    glBegin(GL_POLYGON)
    glColor3f(0, 0, 0)
    glVertex3f(-1.9, -0.55, 4.2)
    glVertex3f(-1.9, -0.5, 4.3)
    glVertex3f(-1.9, -0.5, 3.3)
    glVertex3f(-1.9, -1.2, 3.3)
    glVertex3f(-1.9, -1.2, 4.2)
    glVertex3f(-1.9, -0.55, 4.3)
    glEnd()
    
    glBegin(GL_POLYGON)
    glColor3f(0, 0, 0)
    glVertex3f(-1.9, -0.5, 2.0)
    glVertex3f(-1.9, -0.5, -2.0)
    glVertex3f(-1.95, -0.7, -2.0)
    glVertex3f(-1.95, -0.7, 2.0)
    glEnd()
    
    glBegin(GL_POLYGON)
    glColor3f(0, 0, 0)
    glVertex3f(-1.91, 0, 0.1)
    glVertex3f(-1.91, 0, -0.3)
    glVertex3f(-1.96, -0.05, -0.3)
    glVertex3f(-1.96, -0.05, 0.1)
    glEnd()
    
    glBegin(GL_POLYGON)
    glColor3f(0.3, 0.3, 0.3)
    glVertex3f(-1.91, -0.05, 0.1)
    glVertex3f(-1.91, -0.05, -0.3)
    glVertex3f(-1.96, -0.1, -0.3)
    glVertex3f(-1.96, -0.1, 0.1)
    glEnd()
    
    #Maçaneta Carro
    glBegin(GL_POLYGON)
    glColor3f(0, 0, 0)
    glVertex3f(-1.91, 0, -2)
    glVertex3f(-1.91, 0, -2.4)
    glVertex3f(-1.96, -0.05, -2.4)
    glVertex3f(-1.96, -0.05, -2)
    glEnd()
    
    glBegin(GL_POLYGON)
    glColor3f(0.3, 0.3, 0.3)
    glVertex3f(-1.91, -0.05, -2)
    glVertex3f(-1.91, -0.05, -2.4)
    glVertex3f(-1.96, -0.1, -2.4)
    glVertex3f(-1.96, -0.1, -2)
    glEnd()
    
    #Fechadura
    raioRoda = 0.05
    glColor3f(0.05, 0.05, 0.05)
    ang = 0
    glBegin(GL_TRIANGLE_STRIP)
    while (ang <= 2 *math.pi):
        glVertex3f((2), raioRoda*math.sin(ang)+(-0.2), raioRoda*math.cos(ang)+(-0.1))
        ang = ang + math.pi/100.0
        glVertex3f((2), raioRoda*math.sin(ang)+(-0.2), raioRoda*math.cos(ang)+(-0.1))
    glEnd()
    ang = 0
    glBegin(GL_POLYGON)
    while (ang < 2 *math.pi):
        glVertex3f((2), raioRoda*math.sin(ang)+(-0.2), raioRoda*math.cos(ang)+(-0.1))
        ang = ang + math.pi/100
    glEnd()
    ang = 0
    glBegin(GL_POLYGON)
    while (ang < 2 *math.pi):
        glVertex3f((2), raioRoda*math.sin(ang)+(-0.2), raioRoda*math.cos(ang)+(-0.1))
        ang = ang + math.pi/100
    glEnd()
    
    #Contorno vidro
    glBegin(GL_POLYGON)
    glColor3f(0, 0.7, 0.9)
    glVertex3f(-1.7, 0.2, 2)
    glVertex3f(-1.7, 1.1, 1)
    glVertex3f(-1.7, 0.9, 1)
    glVertex3f(-1.7, 0.2, 1.8)
    glEnd()
    
    glBegin(GL_POLYGON)
    glColor3f(0, 0.7, 0.9)
    glVertex3f(-1.7, 1.1, 1)
    glVertex3f(-1.7, 1.1, -2)
    glVertex3f(-1.7, 0.9, -2)
    glVertex3f(-1.7, 0.9, 1.1)
    glEnd()
    
    glBegin(GL_POLYGON)
    glColor3f(0, 0.7, 0.9)
    glVertex3f(-1.7, 0.2, -3)
    glVertex3f(-1.7, 1.1, -2)
    glVertex3f(-1.7, 0.9, -2)
    glVertex3f(-1.7, 0.2, -2.8)
    glEnd()
    
    glBegin(GL_POLYGON)
    glColor3f(0, 0.7, 0.9)
    glVertex3f(-1.7, 1.1, -0.4)
    glVertex3f(-1.7, 1.1, -0.5)
    glVertex3f(-1.7, 0.2, -0.5)
    glVertex3f(-1.7, 0.2, -0.4)
    glEnd()
    
    #Vidro Lateral
    glBegin(GL_QUADS)
    glColor3f(1, 1, 1)
    glVertex3f(-1.7, 0.2, 1.8)
    glVertex3f(-1.7, 0.9, 1)
    glVertex3f(-1.7, 0.9, -0.4)
    glVertex3f(-1.7, 0.2, -0.4)
    glVertex3f(-1.7, 0.2, 1.8)
    glEnd()
    
    glBegin(GL_QUADS)
    glColor3f(1, 1, 1)
    glVertex3f(-1.7, 0.2, -2.8)
    glVertex3f(-1.7, 0.9, -2)
    glVertex3f(-1.7, 0.9, -0.5)
    glVertex3f(-1.7, 0.2, -0.5)
    glVertex3f(-1.7, 0.2, -2.8)
    glEnd()
    
#------------LADO DIREITO CARRO------------#

    glBegin(GL_POLYGON)
    glColor3f(0, 0.7, 0.9)
    glVertex3f(1.7, 0.2, 2.0)
    glVertex3f(1.7, 0.2, -2.0)
    glVertex3f(1.7, -1.2, -2.0)
    glVertex3f(1.7, -1.2, 2.0)
    glEnd()
    
    glBegin(GL_POLYGON)
    glColor3f(0, 0.7, 0.9)
    glVertex3f(1.95, -0.5, 4.2)
    glVertex3f(1.7, -0.11, 4)
    glVertex3f(1.7, 0.2, 2)
    glVertex3f(1.7, 0.2, -5)
    glVertex3f(1.95, -0.5, -5)
    glVertex3f(1.95, -0.5, 4.4)
    glEnd()
    
    glBegin(GL_POLYGON)
    glColor3f(0, 0, 0)
    glVertex3f(1.7, 0.2, -3.5)
    glVertex3f(1.7, 0.2, -5.0)
    glVertex3f(1.7, -1.2, -5.0)
    glVertex3f(1.7, -1.2, -3.5)
    glEnd()
    
    glBegin(GL_POLYGON)
    glColor3f(0, 0, 0)
    glVertex3f(1.9, -0.55, 4.2)
    glVertex3f(1.9, -0.5, 4.3)
    glVertex3f(1.9, -0.5, 3.3)
    glVertex3f(1.9, -1.2, 3.3)
    glVertex3f(1.9, -1.2, 4.2)
    glVertex3f(1.9, -0.55, 4.3)
    glEnd()
    
    glBegin(GL_POLYGON)
    glColor3f(0, 0, 0)
    glVertex3f(1.9, -0.5, 2.0)
    glVertex3f(1.9, -0.5, -2.0)
    glVertex3f(1.95, -0.7, -2.0)
    glVertex3f(1.95, -0.7, 2.0)
    glEnd()
    
    glBegin(GL_POLYGON)
    glColor3f(0, 0, 0)
    glVertex3f(1.91, 0, 0.1)
    glVertex3f(1.91, 0, -0.3)
    glVertex3f(1.96, -0.05, -0.3)
    glVertex3f(1.96, -0.05, 0.1)
    glEnd()
    
    glBegin(GL_POLYGON)
    glColor3f(0.3, 0.3, 0.3)
    glVertex3f(1.91, -0.05, 0.1)
    glVertex3f(1.91, -0.05, -0.3)
    glVertex3f(1.96, -0.1, -0.3)
    glVertex3f(1.96, -0.1, 0.1)
    glEnd()
    
    #Maçaneta Carro
    glBegin(GL_POLYGON)
    glColor3f(0, 0, 0)
    glVertex3f(1.91, 0, -2)
    glVertex3f(1.91, 0, -2.4)
    glVertex3f(1.96, -0.05, -2.4)
    glVertex3f(1.96, -0.05, -2)
    glEnd()
    
    glBegin(GL_POLYGON)
    glColor3f(0.3, 0.3, 0.3)
    glVertex3f(1.91, -0.05, -2)
    glVertex3f(1.91, -0.05, -2.4)
    glVertex3f(1.96, -0.1, -2.4)
    glVertex3f(1.96, -0.1, -2)
    glEnd()
    
    #Fechadura
    raioRoda = 0.05
    glColor3f(0.05, 0.05, 0.05)
    ang = 0
    glBegin(GL_TRIANGLE_STRIP)
    while (ang <= 2 *math.pi):
        glVertex3f((-2), raioRoda*math.sin(ang)+(-0.2), raioRoda*math.cos(ang)+(-0.1))
        ang = ang + math.pi/100.0
        glVertex3f((-2), raioRoda*math.sin(ang)+(-0.2), raioRoda*math.cos(ang)+(-0.1))
    glEnd()
    ang = 0
    glBegin(GL_POLYGON)
    while (ang < 2 *math.pi):
        glVertex3f((-2), raioRoda*math.sin(ang)+(-0.2), raioRoda*math.cos(ang)+(-0.1))
        ang = ang + math.pi/100
    glEnd()
    ang = 0
    glBegin(GL_POLYGON)
    while (ang < 2 *math.pi):
        glVertex3f((-2), raioRoda*math.sin(ang)+(-0.2), raioRoda*math.cos(ang)+(-0.1))
        ang = ang + math.pi/100
    glEnd()
    
    #Contorno vidro
    glBegin(GL_POLYGON)
    glColor3f(0, 0.7, 0.9)
    glVertex3f(1.7, 0.2, 2)
    glVertex3f(1.7, 1.1, 1)
    glVertex3f(1.7, 0.9, 1)
    glVertex3f(1.7, 0.2, 1.8)
    glEnd()
    
    glBegin(GL_POLYGON)
    glColor3f(0, 0.7, 0.9)
    glVertex3f(1.7, 1.1, 1)
    glVertex3f(1.7, 1.1, -2)
    glVertex3f(1.7, 0.9, -2)
    glVertex3f(1.7, 0.9, 1.1)
    glEnd()
    
    glBegin(GL_POLYGON)
    glColor3f(0, 0.7, 0.9)
    glVertex3f(1.7, 0.2, -3)
    glVertex3f(1.7, 1.1, -2)
    glVertex3f(1.7, 0.9, -2)
    glVertex3f(1.7, 0.2, -2.8)
    glEnd()
    
    glBegin(GL_POLYGON)
    glColor3f(0, 0.7, 0.9)
    glVertex3f(1.7, 1.1, -0.4)
    glVertex3f(1.7, 1.1, -0.5)
    glVertex3f(1.7, 0.2, -0.5)
    glVertex3f(1.7, 0.2, -0.4)
    glEnd()
    
    #Vidro Lateral
    glBegin(GL_QUADS)
    glColor3f(1, 1, 1)
    glVertex3f(1.7, 0.2, 1.8)
    glVertex3f(1.7, 0.9, 1)
    glVertex3f(1.7, 0.9, -0.4)
    glVertex3f(1.7, 0.2, -0.4)
    glVertex3f(1.7, 0.2, 1.8)
    glEnd()
    
    glBegin(GL_QUADS)
    glColor3f(1, 1, 1)
    glVertex3f(1.7, 0.2, -2.8)
    glVertex3f(1.7, 0.9, -2)
    glVertex3f(1.7, 0.9, -0.5)
    glVertex3f(1.7, 0.2, -0.5)
    glVertex3f(1.7, 0.2, -2.8)
    glEnd()

#------------RODAS------------#
    # Frente direito
    raioRoda = 0.6
    glColor3f(0.05, 0.05, 0.05)
    ang = 0
    glBegin(GL_TRIANGLE_STRIP)
    while (ang <= 2 *math.pi):
        glVertex3f((1.5), raioRoda*math.sin(ang)+(-1.1), raioRoda*math.cos(ang)+(2.7))
        ang = ang + math.pi/100.0
        glVertex3f((2), raioRoda*math.sin(ang)+(-1.1), raioRoda*math.cos(ang)+(2.7))
    glEnd()
    ang = 0
    glBegin(GL_POLYGON)
    while (ang < 2 *math.pi):
        glVertex3f((1.5), raioRoda*math.sin(ang)+(-1.1), raioRoda*math.cos(ang)+(2.7))
        ang = ang + math.pi/100
    glEnd()
    ang = 0
    glBegin(GL_POLYGON)
    while (ang < 2 *math.pi):
        glVertex3f((2), raioRoda*math.sin(ang)+(-1.1), raioRoda*math.cos(ang)+(2.7))
        ang = ang + math.pi/100
    glEnd()
    glColor3f(0.5, 0.5, 0.5)
    ang = 0
    glBegin(GL_POLYGON)
    while (ang < 2 *math.pi):
        glVertex3f((2.001), (raioRoda-0.2)*math.sin(ang)+(-1.1), (raioRoda-0.2)*math.cos(ang)+(2.7))
        ang = ang + math.pi/100
    glEnd()
    
    # Frente esquerdo
    raioRoda = 0.6
    glColor3f(0.05, 0.05, 0.05)
    ang = 0
    glBegin(GL_TRIANGLE_STRIP)
    while (ang <= 2 *math.pi):
        glVertex3f((-1.5), raioRoda*math.sin(ang)+(-1.1), raioRoda*math.cos(ang)+(2.7))
        ang = ang + math.pi/100.0
        glVertex3f((-2), raioRoda*math.sin(ang)+(-1.1), raioRoda*math.cos(ang)+(2.7))
    glEnd()
    ang = 0
    glBegin(GL_POLYGON)
    while (ang < 2 *math.pi):
        glVertex3f((-1.5), raioRoda*math.sin(ang)+(-1.1), raioRoda*math.cos(ang)+(2.7))
        ang = ang + math.pi/100
    glEnd()
    ang = 0
    glBegin(GL_POLYGON)
    while (ang < 2 *math.pi):
        glVertex3f((-2), raioRoda*math.sin(ang)+(-1.1), raioRoda*math.cos(ang)+(2.7))
        ang = ang + math.pi/100
    glEnd()
    glColor3f(0.5, 0.5, 0.5)
    ang = 0
    glBegin(GL_POLYGON)
    while (ang < 2 *math.pi):
        glVertex3f((-2.001), (raioRoda-0.2)*math.sin(ang)+(-1.1), (raioRoda-0.2)*math.cos(ang)+(2.7))
        ang = ang + math.pi/100
    glEnd()
    
    # Tras direito
    raioRoda = 0.6
    glColor3f(0.05, 0.05, 0.05)
    ang = 0
    glBegin(GL_TRIANGLE_STRIP)
    while (ang <= 2 *math.pi):
        glVertex3f((1.5), raioRoda*math.sin(ang)+(-1.1), raioRoda*math.cos(ang)+(-2.8))
        ang = ang + math.pi/100.0
        glVertex3f((2), raioRoda*math.sin(ang)+(-1.1), raioRoda*math.cos(ang)+(-2.8))
    glEnd()
    ang = 0
    glBegin(GL_POLYGON)
    while (ang < 2 *math.pi):
        glVertex3f((1.5), raioRoda*math.sin(ang)+(-1.1), raioRoda*math.cos(ang)+(-2.8))
        ang = ang + math.pi/100
    glEnd()
    ang = 0
    glBegin(GL_POLYGON)
    while (ang < 2 *math.pi):
        glVertex3f((2), raioRoda*math.sin(ang)+(-1.1), raioRoda*math.cos(ang)+(-2.8))
        ang = ang + math.pi/100
    glEnd()
    glColor3f(0.5, 0.5, 0.5)
    ang = 0
    glBegin(GL_POLYGON)
    while (ang < 2 *math.pi):
        glVertex3f((2.001), (raioRoda-0.2)*math.sin(ang)+(-1.1), (raioRoda-0.2)*math.cos(ang)+(-2.8))
        ang = ang + math.pi/100
    glEnd()
    
    # Tras esquerdo
    raioRoda = 0.6
    glColor3f(0.05, 0.05, 0.05)
    ang = 0
    glBegin(GL_TRIANGLE_STRIP)
    while (ang <= 2 *math.pi):
        glVertex3f((-1.5), raioRoda*math.sin(ang)+(-1.1), raioRoda*math.cos(ang)+(-2.8))
        ang = ang + math.pi/100.0
        glVertex3f((-2), raioRoda*math.sin(ang)+(-1.1), raioRoda*math.cos(ang)+(-2.8))
    glEnd()
    ang = 0
    glBegin(GL_POLYGON)
    while (ang < 2 *math.pi):
        glVertex3f((-1.5), raioRoda*math.sin(ang)+(-1.1), raioRoda*math.cos(ang)+(-2.8))
        ang = ang + math.pi/100
    glEnd()
    ang = 0
    glBegin(GL_POLYGON)
    while (ang < 2 *math.pi):
        glVertex3f((-2), raioRoda*math.sin(ang)+(-1.1), raioRoda*math.cos(ang)+(-2.8))
        ang = ang + math.pi/100
    glEnd()
    glColor3f(0.5, 0.5, 0.5)
    ang = 0
    glBegin(GL_POLYGON)
    while (ang < 2 *math.pi):
        glVertex3f((-2.001), (raioRoda-0.2)*math.sin(ang)+(-1.1), (raioRoda-0.2)*math.cos(ang)+(-2.8))
        ang = ang + math.pi/100
    glEnd()
    
    # # Coordenadas
    # glBegin(GL_LINES)
    # glColor3f(1, 0, 0)
    # glVertex3f(1000, 0, 0)
    # glVertex3f(-1000, 0, 0)
    # glColor3f(0, 1, 0)
    # glVertex3f(0, 1000, 0)
    # glVertex3f(0, -1000, 0)
    # glColor3f(0, 0, 1)
    # glVertex3f(0, 0, 1000)
    # glVertex3f(0, 0, -1000)
    # glEnd()
    
    glFlush()                

def buttons(key,x,y):
    global px, py, pz
    if key == GLUT_KEY_LEFT:
        py -= 10
        
    elif key == GLUT_KEY_RIGHT:
        py += 10
        
    elif key == GLUT_KEY_UP:
        px += 10
        
    elif key == GLUT_KEY_DOWN:
        px -= 10
    
    elif key == GLUT_KEY_PAGE_UP:
        pz -= 10
    
    elif key == GLUT_KEY_PAGE_DOWN:
        pz += 10
    
    elif key == GLUT_KEY_HOME: # # Voltar para a vista frental (tecla Home)
        px = 0
        py = 0
        pz = 0
        
    elif key == GLUT_KEY_END: # Vista em perspectiva (tecla End)
        px = 25
        py = 40
        pz = 0
        
    glutPostRedisplay()

def movimento(key,x,y):
    global z
    
    if (key == b'w') or (key == b'W'):
        z += 3
    
    elif (key == b's') or (key == b'S'):
        z -= 3
    glutPostRedisplay()

def main():
    global distancia
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 700)
    glutCreateWindow(name)

    glClearColor(0.2, 0.2, 0.2, 1)
    glShadeModel(GL_SMOOTH)
    glFrontFace(GL_CCW)
    glEnable(GL_DEPTH_TEST)
    lightZeroPosition = [1.,4.,50.,1.]
    lightZeroColor = [0.8,1.0,0.8,1.0] #green tinged
    glLightfv(GL_LIGHT0, GL_POSITION, lightZeroPosition)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, lightZeroColor)
    glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.1)
    glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.05)
    glEnable(GL_LIGHT0)
    glutDisplayFunc(display)
    glutSpecialFunc(buttons)
    glutKeyboardFunc(movimento)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(50,(1/1),1,50)
    glMatrixMode(GL_MODELVIEW)
    gluLookAt(4.083,-4.083,distancia,
                0,0,0,
                -0.07,1,0)
    glPushMatrix()
    glutMainLoop()
    return

def display():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    glRotatef(30,1,1,0);
    drawC()
    glPopMatrix()
    glutSwapBuffers()
    return

if __name__ == '__main__': main()
