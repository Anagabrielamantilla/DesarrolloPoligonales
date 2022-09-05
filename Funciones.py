# -- coding: utf-8 --
"""
Created on Sun Sep  4 20:38:19 2022

@author: Paul Goyes (goyes.yesid@gmail.com) y Ana Mantilla (anagmd2019@gmail.com)
"""

import numpy as np

def az2carto(azi):
  '''
  az2carto: Función para convertir azimut en coordenadas cartesianas medidas desde el eje x
  '''
  return -azi + 90

def cal_thick(L,I,a,b,f):
  '''
  cal_thick: Calcular el espesor real a partir de los datos medidos en una poligonal
  Hecho por: Paul Goyes (goyes.yesid@gmail.com) y Ana Mantilla (anagmd2019@gmail.com)

  Variables de entrada
  L:  Longitud de la via o segmento a calcular espesor aparente (metros)
  I: Inclinación de la capa en azimut del rumbo
  a: Direccion del bedding en azi del rumbo
  b: Direccion del bedding en azi del buzamiento
  f: Direccion del segmento en azi del rumbo'''
  ######## convertir de az2carto
  I=I*np.pi/180; 
  a=az2carto(a)*np.pi/180; #Direccion BEDDING; en azimut del rumbo
  b=az2carto(b)*np.pi/180; #Direccion de la inclinacion: en azimut del buzamiento
  f=az2carto(f)*np.pi/180; #Direccion del segmento: en azimut del rumbo
  ############# calcular variables aparentes
  omega=np.arctan(np.tan(I)*np.sin(abs(a-f)))*180/np.pi # Ángulo de inclinación aparente
  E=np.sin(omega*np.pi/180)*L #ESPESOR APARENTE EN EL SEGMENTO L
  # calcular variables reales
  L2=abs(np.cos((f-b))*L) # LONGITUD L PROYECTADA EN LA MISMA DIRECCIÓN DEL BUZAMIENTO
  E2=np.sin(I)*L2 #ESPESOR REAL
  return E2
