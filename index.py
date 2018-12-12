#!/usr/bin/python
# coding: utf-8

try:
  from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
  sense = SenseHat()
except:
  from sense_emu import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
  sense = SenseHat()
    
import time, random
from time import sleep
from signal import pause

sense = SenseHat()
sense.clear()
msleep = lambda x: time.sleep(x / 1000.0)

#Variables d'incrémentation pour les déplacements
x_balle = random.randint(3,7)
y_balle = random.randint(0,7)
y_raqu = 2
incre_x = 1
incre_y = 1

#Message d'accueil
def messAccueil():
  sense.show_message("Pong!", text_colour=[255, 0, 255])
  for i in range(5,0,-1):
    sense.show_letter(str(i),[0, 0, 0],[255, 255, 255])
    sleep(1)
  sense.clear()
  
messAccueil()

#Affichage de la raquette
def afficherRaquette():
  global y_raqu
  sense.set_pixel(0,y_raqu,0,0,255)
  sense.set_pixel(0,y_raqu+1,0,0,255)
  sense.set_pixel(0,y_raqu+2,0,0,255)

afficherRaquette()

#Déplacement raquette
def stick_up(event):
  global y_raqu
  if event.action == ACTION_PRESSED:
    if y_raqu > 0:
      y_raqu -= 1
    else:
      y_raqu == 0
  
def stick_down(event):
  global y_raqu  
  if event.action == ACTION_PRESSED:
    if y_raqu < 5:
      y_raqu += 1
    else:
      y_raqu = 5

sense.stick.direction_up = stick_up
sense.stick.direction_down = stick_down

#Affichage de la balle
def afficherBalle():
  global x_balle
  global y_balle
  global incre_x
  global incre_y
  global y_raqu
  
  #Rebond contre les murs
  if x_balle == 7:
    incre_x = -incre_x
    
  if y_balle == 0 or y_balle == 7:
    incre_y = -incre_y
  
  #Rebond sur la raquette  
  if x_balle == 1 and (y_balle == y_raqu or y_balle == y_raqu+1 or y_balle == y_raqu+2):
    incre_x = -incre_x
  
  sense.set_pixel(x_balle,y_balle,255,0,0)
  
  x_balle += incre_x
  y_balle += incre_y

afficherBalle()

#Boucle principale du jeu
while True:
  #Afficher balle & raquette + déplacement balle
  msleep(300)
  sense.clear()
  afficherBalle()
  afficherRaquette()

  #Game over
  if x_balle == 0:
    msleep(300)
    afficherBalle()
    sense.clear()
    sense.show_message("RIP..:(", text_colour=[0, 255, 0])
    messAccueil()
    x_balle = random.randint(3,7)
    y_balle = random.randint(0,7)
    

