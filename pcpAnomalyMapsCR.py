# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 14:28:01 2023

@author: Roberto Camilo Vindas (rvindas/DMSA/IMN) 


Script de python para graficar datos de anomalía de precipitación mensual y acumulado total. El script original corre de manera operativa en un servidor del IMN
y se actualiza a diario tomando los datos directamente de una base de datos.

##### Este script es una versión de ejemplo que contiene unicamente la parte gráfica y no la parte de conexión a la base de datos ###########################

Este script fue probado existosamente con las siguientes versiones de la librerias:
cartopy 0.21.1
matplotlib 3.8.0
numpy 1.26.2
pillow 10.0.1

"""



#import oracledb
import datetime
import cartopy
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import matplotlib.colors as mcolors
import os
from PIL import Image




def creaDirectorios(ruta_directorio):
    
    """ Funcion que crea directorios cada dia -si no existen- para guardar distintos tipos de archivos según se necesite """ 
    
    if not (os.path.exists(ruta_directorio)):
        print ("----- Directorios no exiten previamente... Creando directorios...")
        os.mkdir(ruta_directorio)
        return (ruta_directorio)
        
    else:    
        return (ruta_directorio) 






def sacaColores(tipo, variable):

    """
    Esta funcion decide el color para graficar dependiendo del valor de la anomalia
    
    
    Colores: https://matplotlib.org/stable/gallery/color/named_colors.html 
    """
    
    if tipo == "anomPorc_lluvia": 
        anomalia = float(variable)
        color = ""

        if anomalia < -150:
            color = "red"

        if -150 <= anomalia <-100:
            color = "firebrick"

        if -100 <= anomalia <-75:
            color = "indianred"

        if -75 <= anomalia < -50:
            color = "chocolate"

        if -50 <= anomalia <-25:
            color = "coral"

        if -25 <= anomalia < -10:
            color = "khaki"

        if -10 <= anomalia <= 10:
            color = "floralwhite"

        if  10 < anomalia <= 25:
            color = "mediumspringgreen"

        if 25 < anomalia <= 50:
            color = "mediumseagreen"

        if 50 < anomalia <= 75:
            color = "green"

        if 75 < anomalia <= 100:
            color = "royalblue"

        if 100 < anomalia <= 150:
            color = "blue"

        if 150 < anomalia:
            color = "darkblue"


    if tipo == "anomMM_lluvia": 
        anomalia = float(variable)
        color = ""

        if anomalia < -200:
            color = "maroon"

        if -200 <= anomalia <-150:
            color = "firebrick"

        if -150 <= anomalia <-100:
            color = "red"

        if -100 <= anomalia < -70:
            color = "indianred"

        if -70 <= anomalia <-50:
            color = "orange"

        if -50 <= anomalia < -30:
            color = "lightcoral"
        
        if -30 <= anomalia < -10:
            color = "lightsalmon"    

        if -10 <= anomalia <= 10:
            color = "floralwhite"

        if  10 < anomalia <= 30:
            color = "lightskyblue"

        if 30 < anomalia <= 50:
            color = "darkturquoise"

        if 50 < anomalia <= 70:
            color = "deepskyblue"

        if 70 < anomalia <= 100:
            color = "royalblue"

        if 100 < anomalia <= 150:
            color = "blue"

        if 150 < anomalia <= 200:
            color = "darkblue"
            
        if 200 < anomalia:
            color = "purple"    
      
    if tipo == "acumulado_mensual": 
        acumulado = float(variable)
        color = ""

        if 0 <= acumulado < 10:
            color = "azure"

        if 10 <= acumulado < 20:
            color = "lightcyan"

        if 20 <= acumulado < 40:
            color = "paleturquoise"

        if 40 <= acumulado < 60:
            color = "lightskyblue"

        if  60 <= acumulado < 80:
            color = "deepskyblue"

        if 80 <= acumulado < 100:
            color = "steelblue"

        if 100 <= acumulado < 140:
            color = "dodgerblue"

        if  140 <= acumulado < 180:
            color = "royalblue"

        if 180 <= acumulado < 220:
            color = "blue"

        if 220 <= acumulado < 260:
            color = "mediumblue"

        if 260 <= acumulado < 300:
            color = "darkblue"

        if 300 <=acumulado < 350:
            color = "mediumorchid"
        
        if 350 <=acumulado < 400:
            color = "darkviolet"  

        if 400 < acumulado:
            color = "indigo"


    #print (tipo, color)
    codigoColor =  mcolors.CSS4_COLORS[color]
    return codigoColor   



def sacaElementosLeyenda(tipo):
    
    """
    Esta funcion define los colores y las etiquetas de la leyenda dependiendo del tipo de gráfico.
    
    Recibe: 
        tipo(str): El mombre de tipo de grafico ---> 'anomPorc_lluvia' para la anomalia porcentual de lluvia, 'anoma_abs' para la anomalia en mm 
                                                     'acumulado_mensual' para el acumulado de precipitacion en lo que va del mes 
   
   Colores: https://matplotlib.org/stable/gallery/color/named_colors.html 
   """
    
    if tipo == "anomPorc_lluvia":
        
        elementosLeyenda = [Line2D([0], [0], marker="o", color=mcolors.CSS4_COLORS["red"], lw=4, label='[an < -150%]'),
                            Line2D([0], [0], marker="o", color=mcolors.CSS4_COLORS["firebrick"], lw=4, label="[-150% <= an < -100%]"),
                            Line2D([0], [0], marker="o", color= mcolors.CSS4_COLORS["indianred"], lw=4, label='[-100% <= an < -75%]'),
                            Line2D([0], [0], marker="o", color=mcolors.CSS4_COLORS["chocolate"], lw=4, label='[-75% <= an < -50%]'),
                            Line2D([0], [0], marker="o", color=mcolors.CSS4_COLORS["coral"], lw=4, label='[-50% <= an < -25%]'),
                            Line2D([0], [0], marker="o", color=mcolors.CSS4_COLORS["khaki"], lw=4, label='[-25% <= an < -10%]'),
                            Line2D([0], [0], marker="o", color=mcolors.CSS4_COLORS["floralwhite"], lw=4, label='[-10% <= an <= 10%]'),
                            Line2D([0], [0], marker="o", color=mcolors.CSS4_COLORS["mediumspringgreen"], lw=4, label='[10% < an <= 25%]'),
                            Line2D([0], [0], marker="o", color=mcolors.CSS4_COLORS["mediumseagreen"], lw=4, label='[25% < an <= 50%]'),
                            Line2D([0], [0], marker="o", color=mcolors.CSS4_COLORS["green"], lw=4, label='[50% < an <= 75%]'),
                            Line2D([0], [0], marker="o", color=mcolors.CSS4_COLORS["royalblue"], lw=4, label='[75% < an <= 100%]'),
                            Line2D([0], [0], marker="o", color=mcolors.CSS4_COLORS["blue"], lw=4, label='[100% < an <= 150%]'),
                            Line2D([0], [0], marker="o", color=mcolors.CSS4_COLORS["darkblue"], lw=4, label='[150% < an ]')]


        tituloLegenda = "Anomalía %"
        
        
    if tipo == "anomMM_lluvia":
        
        elementosLeyenda = [Line2D([0], [0], marker="o", color=mcolors.CSS4_COLORS["maroon"], lw=4, label='[an < -200]'),
                            Line2D([0], [0], marker="o", color=mcolors.CSS4_COLORS["firebrick"], lw=4, label="[-200 <= an < -150]"),
                            Line2D([0], [0], marker="o", color= mcolors.CSS4_COLORS["red"], lw=4, label='[-150 <= an < -100]'),
                            Line2D([0], [0], marker="o", color=mcolors.CSS4_COLORS["indianred"], lw=4, label='[-100 <= an < -70]'),
                            Line2D([0], [0], marker="o", color=mcolors.CSS4_COLORS["orange"], lw=4, label='[-70 <= an < -50]'),
                            Line2D([0], [0], marker="o", color=mcolors.CSS4_COLORS["lightcoral"], lw=4, label='[-50 <= an < -30]'),
                            Line2D([0], [0], marker="o", color=mcolors.CSS4_COLORS["lightsalmon"], lw=4, label='[-30 <= an < -10]'),
                            Line2D([0], [0], marker="o", color=mcolors.CSS4_COLORS["floralwhite"], lw=4, label='[10 <= an <= 10]'),
                            Line2D([0], [0], marker="o", color=mcolors.CSS4_COLORS["lightskyblue"], lw=4, label='[10 < an <= 30]'),
                            Line2D([0], [0], marker="o", color=mcolors.CSS4_COLORS["darkturquoise"], lw=4, label='[30 < an <= 50]'),
                            Line2D([0], [0], marker="o", color=mcolors.CSS4_COLORS["deepskyblue"], lw=4, label='[50 < an <= 70]'),
                            Line2D([0], [0], marker="o", color=mcolors.CSS4_COLORS["royalblue"], lw=4, label='[70 < an <= 100]'),
                            Line2D([0], [0], marker="o", color=mcolors.CSS4_COLORS["blue"], lw=4, label='[100 < an <= 150 ]'),
                            Line2D([0], [0], marker="o", color=mcolors.CSS4_COLORS["darkblue"], lw=4, label='[150 < an <= 200 ]'),
                            Line2D([0], [0], marker="o", color=mcolors.CSS4_COLORS["purple"], lw=4, label='[200 < an ]')]


        tituloLegenda = "Anomalía (mm)"    
        
        
        
        
    if tipo == "acumulado_mensual":
        
        elementosLeyenda = [Line2D([0], [0], marker="o", color=mcolors.CSS4_COLORS["azure"], lw=4, label='[0-10 mm]'),
                            Line2D([0], [0], marker="o", color=mcolors.CSS4_COLORS["lightcyan"], lw=4, label="[10-20 mm]"),
                            Line2D([0], [0], marker="o", color= mcolors.CSS4_COLORS["paleturquoise"], lw=4, label='[20-40 mm]'),
                            Line2D([0], [0], marker="o", color=mcolors.CSS4_COLORS["lightskyblue"], lw=4, label='[40-60 mm]'),
                            Line2D([0], [0], marker="o", color=mcolors.CSS4_COLORS["deepskyblue"], lw=4, label='[60-80 mm]'),
                            Line2D([0], [0], marker="o", color=mcolors.CSS4_COLORS["steelblue"], lw=4, label='[80-100 mm]'),
                            Line2D([0], [0], marker="o", color=mcolors.CSS4_COLORS["dodgerblue"], lw=4, label='[100-140 mm]'),
                            Line2D([0], [0], marker="o", color=mcolors.CSS4_COLORS["royalblue"], lw=4, label='[140-180 mm]'),
                            Line2D([0], [0], marker="o", color=mcolors.CSS4_COLORS["blue"], lw=4, label='[180-220 mm]'),
                            Line2D([0], [0], marker="o", color=mcolors.CSS4_COLORS["mediumblue"], lw=4, label='[220-260 mm]'),
                            Line2D([0], [0], marker="o", color=mcolors.CSS4_COLORS["darkblue"], lw=4, label='[250-300 mm]'),
                            Line2D([0], [0], marker="o", color=mcolors.CSS4_COLORS["mediumorchid"], lw=4, label='[300-350 mm]'),
                            Line2D([0], [0], marker="o", color=mcolors.CSS4_COLORS["darkviolet"], lw=4, label='[350-400 mm]'),
                            Line2D([0], [0], marker="o", color=mcolors.CSS4_COLORS["indigo"], lw=4, label='[400 mm < acum ]')]
    
        tituloLegenda = "Acumulado (mm)"

    return [elementosLeyenda, tituloLegenda]




def parametrosGrafico(tipo, fecha, mesAnomalia):
    
    """
    Esta funcion determina los parámetros para el titulo del gráfico dependiendo del tipo de variable.
    Recibe:
        tipo(str): Un string con el tipo de variable a graficar. De la forma: "acumulado_mensual", "anomPorc_lluvia" 
        
    fecha(datetime): Un objeto tipo fecha con los datos del día a graficar    
    """
    
    dia = fecha.day
    mes = fecha.month
    anno = fecha.year
    


    if tipo == "anomPorc_lluvia":
        titulo = "Mapa de Anomalia porcentual de lluvia %s %d \n Datos actualizados al %d/%d/%d"%(mesAnomalia, anno, dia, mes, anno)
        colorLetra = "purple"
        colorMapa = mcolors.CSS4_COLORS["ivory"]
    
    if tipo == "anomMM_lluvia":
        titulo = "Mapa de Anomalía de lluvia (mm) %s %d \n Datos actualizados al %d/%d/%d"%(mesAnomalia, anno, dia, mes, anno)
        colorLetra = "red"
        colorMapa = mcolors.CSS4_COLORS["lightgrey"]    
    
    if tipo == "acumulado_mensual":
        titulo = "Mapa de Acumulado total de lluvia %s %d \n Datos actualizados al %d/%d/%d"%(mesAnomalia, anno, dia, mes, anno)
        colorLetra = "blue"
        colorMapa = mcolors.CSS4_COLORS["palegreen"]
        
        

    return [titulo, colorLetra, colorMapa]    
    
    
    
    

def graficaMapas(rutaGuardarGrafico, datos, tipo, logo, parametrosGrafico):
    
    """
    Esta funcion grafica el mapa con las anomalias de una variable especifica para cada 
    estación.
    
    Recibe: 
        rutaGuardarGrafico(str): Ruta y nombre para guardar el grafico generado. Ej C:\\Users\\oraweb\\Desktop\\tareas-clima\\anomaPorcentual.png
        
        variable(str): Nombre de la variable para colocar en el 
    
    """

    proyeccion = cartopy.crs.PlateCarree()
    fig = plt.figure(figsize=(20,20))
    ax = plt.subplot(1,1,1,projection = proyeccion)
    dominio = [-86, -82.5, 8, 11.3]
    ax.set_extent(dominio, proyeccion)
    ax.set_facecolor(cartopy.feature.COLORS['water'])
    
    
    colorMapa = parametrosGrafico[2]
    ax.add_feature(cartopy.feature.LAND, facecolor = colorMapa)
    ax.add_feature(cartopy.feature.COASTLINE)
    ax.add_feature(cartopy.feature.BORDERS, linewidth=1, edgecolor='green', linestyle='--')
    ax.add_feature(cartopy.feature.STATES, linewidth=0.3, edgecolor='black')
    ax.text(-85.1,9,"Océano Pacífico", fontsize = 45, fontstyle = "oblique", fontfamily = 'cursive', weight = "bold")
    ax.text(-83.2,10.2,"Mar Caribe", fontsize = 45, fontstyle = "oblique", fontfamily = 'cursive', weight = "bold")
    ax.text(-85.0,11.15,"Nicaragua", fontsize = 40, fontstyle = "oblique", fontfamily = 'cursive', weight = "bold")
    ax.text(-82.7,8.8,"Panamá", fontsize = 40, fontstyle = "oblique", fontfamily = 'cursive', weight = "bold", rotation = "vertical")
    
    colorTitulo = parametrosGrafico[1]
    textotitulo = parametrosGrafico[0]
    ax.set_title(textotitulo, fontsize=30, fontweight=0, color=colorTitulo, loc='center', style='italic')
    
    
    elementosLeyenda = sacaElementosLeyenda(tipo)
    plt.legend(handles=elementosLeyenda[0], prop={'size': 15}, title = elementosLeyenda[1], title_fontsize = 15)
    plt.tight_layout()
    
    
    ciudades = {"Liberia" : [10.6350403, -85.4377213],"Golfito": [8.6032696,-83.1134186], "San Jose": [9.9333296, -84.0833282], "Alajuela": [10.0162497, -84.2116318], 
            "Cd. Quesada":[10.3238096, -84.4271393], "Cartago":[9.86444, -83.9194412], "Siquirres":[10.0974798, -83.5065918], "San Vito": [8.8207903, -82.9709167], 
            "Upala":[10.899065, -85.017947], "Los Chiles":[11.03333,-84.7166672],"Sarapiquí":[10.452225, -84.018191], "Palmares":[10.060881, -84.43], 
            "Limon": [9.9907398, -83.0359573], "Quepos": [9.4306297, -84.1623077],"Nosara":[9.979184, -85.649843], "Tortuguero":[10.541779, -83.502059]}

    for ciudad in ciudades.keys():
        lon = ciudades[ciudad][1]
        lat = ciudades[ciudad][0]
        ax.plot(lon, lat, "k*", markersize=2,zorder=1, transform=proyeccion)
        ax.text(lon + 0.01, lat + 0.01, ciudad, fontsize=10, color = "purple",transform=proyeccion)

    if tipo == "anomPorc_lluvia":
        indice = -1
    if tipo == "anomMM_lluvia":
        indice = -2    
    if tipo == "acumulado_mensual":
        indice = -3    

    for estacion in datos:
        variable = estacion[indice]
        lon = float(estacion[4])
        lat = float(estacion[3])
        color = sacaColores(tipo, variable)
        print(lon, lat, variable)
        ax.plot(lon, lat, marker = "o", color = color, markersize=22,zorder=1, transform=proyeccion)

    im4 = Image.open(logo)
    newax = fig.add_axes([0.015, 0.03, 0.15, 0.15], anchor='SE', zorder=1000) #[movimiento en x,movimiento en y, medida de imagen, medida de imagen ]
    newax.imshow(im4)
    newax.axis('off')

    plt.savefig(rutaGuardarGrafico)  


    
            
        
def extraeDatos(rutaArchivoDatos):
    
    """
    Esta funcion extrae los datos de las estaciones de un archivo específico separado por comas
    """
    
    ptr = open(rutaArchivoDatos, "r")
    lineas = ptr.readlines()
    ptr.close()
    datosTotales = []
    for linea in lineas[1:]:
        datos = linea.strip().split(",")
        datosTotales.append(datos)
    
    return datosTotales    
        
        



#########################################################################################################################
################################### Corrida del script ##################################################################
#########################################################################################################################

#fecha = datetime.datetime.now()
fecha = datetime.datetime(2024,4,23) #fecha para este ejemplo específico
ayer = fecha - datetime.timedelta(days = 1)
dia_ayer = ayer.day
mes_ayer = ayer.month
anno_ayer = ayer.year



if mes_ayer < 10:
    mes_ayer_str = "0%d"%(mes_ayer)
else:
    mes_ayer_str = str(mes_ayer)
    
    



archivoDatos = "datosEstaciones.txt"
datosAnomalias = extraeDatos(archivoDatos)
logo = "imn.jpg"
meses = {1:"enero", 2:"febrero", 3:"marzo", 4:"abril", 
         5:"mayo", 6:"junio", 7:"julio", 8:"agosto", 
         9:"setiembre", 10:"octubre", 11:"noviembre", 12:"diciembre"}

mesAnomalia = meses[mes_ayer]


ruta_directorio_anno = "maps\\%d"%(anno_ayer)
creaDirectorios(ruta_directorio_anno)


ruta_directorio = ruta_directorio_anno + "\\%s"%(mesAnomalia)
creaDirectorios(ruta_directorio)

#Mapa de anomalia %
rutaGuardarGrafico = ruta_directorio + "\\anomalia_PREC_%s.png"%(mesAnomalia)
tipo = "anomPorc_lluvia"
paraGraf = parametrosGrafico(tipo, fecha, mesAnomalia)
graficaMapas(rutaGuardarGrafico, datosAnomalias, tipo, logo, paraGraf)

#Mapa de anomalia (mm)
rutaGuardarGrafico = ruta_directorio + "\\anomalia_PRECmm_%s.png"%(mesAnomalia)
tipo = "anomMM_lluvia"
paraGraf = parametrosGrafico(tipo, fecha, mesAnomalia)
graficaMapas(rutaGuardarGrafico, datosAnomalias, tipo, logo, paraGraf)

#Mapa de acumulado
rutaGuardarGrafico = ruta_directorio + "\\acumulado_PREC_%s.png"%(mesAnomalia)
tipo = "acumulado_mensual"
paraGraf = parametrosGrafico(tipo, fecha, mesAnomalia)
graficaMapas(rutaGuardarGrafico, datosAnomalias, tipo, logo, paraGraf)



print ("¡Mapas finalizados!")