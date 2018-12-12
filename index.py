# coding: utf-8

import time
from sense_hat import SenseHat

sense = SenseHat()
sense.clear()
msleep = lambda x: time.sleep(x / 1000.0)

#Initialisation des variables : coordonnées de la balle
x = 2
y = 6

#Affichage de la balle
sense.set_pixel(x,y,255,0,0)

#Affichage de la raquette
z = (0,1,2)
sense.set_pixel(0,z[0],0,0,255)
sense.set_pixel(0,z[1],0,0,255)
sense.set_pixel(0,z[2],0,0,255)

#Boucle déplacement balle & raquette
i = 1
j = 1
while True:
  x += i
  y += j
  msleep(600)
  sense.clear()
  sense.set_pixel(x,y,255,0,0)
  sense.set_pixel(0,z[0],0,0,255)
  sense.set_pixel(0,z[1],0,0,255)
  sense.set_pixel(0,z[2],0,0,255)
  if x == 7:
    i = -i
  if y == 0 or y == 7:
    j = -j
  if x == 0:
    msleep(600)
    sense.set_pixel(x,y,255,0,0)
    sense.clear()
    break
  

