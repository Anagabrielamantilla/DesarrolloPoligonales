# Cálculo del espesor real de las capas mediante el método de poligonales usando Python

## Descripción del repositorio
Este es un código de Python que resuelve el cálculo del espesor real de las capas estratigráficas mediante el uso de funciones matemáticas que representan relaciones trigonométricas entre los datos tomados en campo. 

# Datos de entrada: 

- DistSegmento: Distancia de la vía o el segmento A-B 
- Azi_Segmento: Azimut segmento A-B
- Dip_Segmento: Inclinación segmento A-B
- Az_rumbo_bedding: Azimut de rumbo de las capas 
- Az_buz_bedding: Azimut de buzamiento de las capas
- dip_bedding: Buzamiento de las capas

# Datos de salida:
- espesor: Columna donde se guardan los espesores reales calculados

<p align="center">
<img src="https://github.com/Anagabrielamantilla/DesarrolloPoligonales/blob/main/Img0.png" width="800">
</p>

###### Funciones creadas

- az2carto(azi): donde el argumento de entrada <b>azi</b> es el ángulo en azimut. (en grados, 0 - 360). Esta es una función que convierte los datos de azimut del rumbo en ángulos euclidianos

```
out =  az2carto(azi)
```
- cal_thick(L,I,a,b,f): donde los argumentos de entrada son <b>L</b> (longitud de la vía), <b>I</b> (buzamiento de la capa), <b>a</b> (azimut de rumbo de las capas), <b>b</b> (azimut de buzamiento de las capas), <b>f</b> (azimut de rumbo del segmento)

```
out =  cal_thick(L,I,a,b,f)
```
Las variables de entrada están definidas de la siguiente forma:

```
I=I*np.pi/180
a=az2carto(a)*np.pi/180
b=az2carto(b)*np.pi/180
f=az2carto(f)*np.pi/180
```
El cálculo de las variables aparentes está dado por:

```
omega=np.arctan(np.tan(I)*np.sin(abs(a-f)))*180/np.pi #ángulo de dirección aparente
E=np.sin(omega*np.pi/180)*L #espesor aparente
```
El cálculo de las variables reales está dado por:

```
L2=abs(np.cos((f-b))*L) #longitud proyectada en la misma dirección del buzamiento
E2=np.sin(I)*L2 #espesor real
```

## Ejemplo en colab 

En este colab está un ejemplo completo del uso de las funciones, y el proceso automático para aplicarlas en un archivo de excel.
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1xms3EEhLpyYVl7YiIcuiTqt-IsWStdxS#scrollTo=ZwSqdcHlWbe9)


###### Exportar el resultado a un excel 
Este es un ejemplo para guardar el archivo csv con la poligonal desarrollada
> Aumentar la velocidad de los procesos 

<p align="center">
<img src="https://github.com/Anagabrielamantilla/DesarrolloPoligonales/blob/main/Captura%20de%20pantalla%202022-09-04%20212911.jpg" width="400">
</p>

## Usarlo en el disco local

Para usar en el disco local, se debe descargar la carpeta y usar alguna de las siguientes opciones:
- Para los usuarios de Jupyter-notebook: Usar el ejemplo presentado en el archivo <b>poligonal.ipynb</b>. 
- Para los usuarios de spyder u otro IDE:  Usar el ejemplo presentado en el archivo <b>poligonal.py</b>. 

## ¿Cómo colaborar con el proyecto ? 

Ayúdame difundiendo, envíame más ejemplos para hacer diferentes tests. Encuentra errores y repórtalos en un issue en github.

> Contáctanos


Ana Mantilla: anagmd2019@gmail.com </br> <a href="https://www.linkedin.com/in/ana-gabriela-mantilla-24377a21a/">
  <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" alt="HTML tutorial" style="width:30px;height:30px;">
</a> </br> 
Paul Goyes:   goyes.yesid@gmail.com </br> <a href="https://www.linkedin.com/in/paul-goyes-0212b810/">
  <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" alt="HTML tutorial" style="width:30px;height:30px;">
</a>
