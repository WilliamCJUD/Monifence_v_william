import pygame,sys
import time
from pygame.locals import *
from modulo_comunicacion import comunicacion_tcp as comu

#########################################################
NEGRO = (0, 0, 0)
GRIS = (35, 36, 37 )
BLANCO = (222, 224, 200)
VERDE=(41, 211, 66)
VERDE_CLARO=(41, 180, 66)
ROJO=(247, 55, 55 )
AZUL=(10, 120, 191)
AMARILLO=( 247,191,0)

############################    ASIGNAR IMAGENES     #####################
mapa= pygame.image.load('images/reserva.jpg')
reports_bu= pygame.image.load('images/reports.png')
reports_bp= pygame.image.load('images/reports_pressed.png')
stats_bu= pygame.image.load('images/stats.png')
stats_bp= pygame.image.load('images/stats_pressed.png')
zona_bu= pygame.image.load('images/zona.png')
zona_bp= pygame.image.load('images/zona_pressed.png')
batt_f= pygame.image.load('images/batt_f.png')
batt_e= pygame.image.load('images/batt_e.png')
ener_on= pygame.image.load('images/ener_on.png')
ener_off= pygame.image.load('images/ener_off.png')
armed= pygame.image.load('images/armed.png')
disarmed= pygame.image.load('images/disarmed.png')
signal_on= pygame.image.load('images/signal_on.png')
signal_off= pygame.image.load('images/signal_off.png')
alarm_on= pygame.image.load('images/alarm_on.png')
alarm_off= pygame.image.load('images/alarm_off.png')

rect_reports_bu = reports_bu.get_rect()
rect_stats_bu = stats_bu.get_rect()
rect_zona1_bu = zona_bu.get_rect()
rect_zona2_bu = zona_bu.get_rect()
rect_zona3_bu = zona_bu.get_rect()
rect_batt_f = batt_f.get_rect()
rect_ener_on = zona_bu.get_rect()
rect_armed = armed.get_rect()
rect_disarmed = disarmed.get_rect()
rect_signal_on = signal_on.get_rect()
rect_alarm_off = alarm_off.get_rect()
rect_mapa = mapa.get_rect()

############################        INICIO      ###################
pygame.init()
font_b = pygame.font.SysFont("Arial", 15)
font_c = pygame.font.SysFont("Arial", 20)
font_s = pygame.font.SysFont("Arial Narrow", 18)

dimensiones = [820, 600]
pantalla = pygame.display.set_mode(dimensiones)
pygame.display.set_caption("Monifence")


def crear_boton(lista_botones):
    for boton in lista_botones:
            if boton['on_click']:
                pantalla.blit(boton['imagen_pressed'], boton['rect'])
            else:
                pantalla.blit(boton['imagen'], boton['rect'])
            textoboton=font_b.render(boton['texto'],2,BLANCO)
            centro_b = boton['rect']
            pantalla.blit(textoboton,[centro_b[0]+10,centro_b[1]+70])

def crear_zona(lista_zonas):
    for zona in lista_zonas:
            if zona['on_click']:
                pantalla.blit(zona['imagen_pressed'], zona['rect'])
            else:
                pantalla.blit(zona['imagen'], zona['rect'])
            textoboton=font_b.render(zona['texto'],3,BLANCO)
            centro_b = zona['rect']
            pantalla.blit(textoboton,[centro_b[0]+20,centro_b[1]+6])

def crear_panel(lista_panel,selected):
    for panel in lista_panel:
            if panel['on_click']:
                pantalla.blit(panel['imagen_f'], panel['rect'])
                textoboton=font_b.render(panel['texto_f'],3,BLANCO)
            else:
                pantalla.blit(panel['imagen_ok'], panel['rect'])
                textoboton=font_b.render(panel['texto_ok'],3,BLANCO)
            centro_b = panel['rect']
            pantalla.blit(textoboton,[centro_b[0]+50,centro_b[1]+15])

def posicion_mouse():
    global xm,ym
    pos = pygame.mouse.get_pos()
    xm=int(pos[-2])
    ym=int(pos[-1])
    #print ("mouse:",pos)


def main():

    global botones, zonas, panels
    pantalla.fill(NEGRO)
    game_over = False
    clock = pygame.time.Clock()
    c_cerca_1=AMARILLO
    c_cerca_2=AMARILLO
    c_cerca_3=AMARILLO
    c_cerca_4=AMARILLO
    c_cerca_5=AMARILLO
    c_cerca_6=AMARILLO
    c_cerca_7=AMARILLO
    c_cerca_8=AMARILLO
    c_cerca_9=AMARILLO
    c_cerca_10=AMARILLO
    c_cerca_11=AMARILLO
    c_cerca_12=AMARILLO
    c_cerca_13=AMARILLO

    selected="Selecionar zona"

###############             MAPA
    rect_mapa.topleft = [180,150]
    pantalla.blit(mapa, rect_mapa)

###############            PANEL
    rect_signal_on.topleft = [10,150]
    rect_alarm_off.topleft = [10,200]
    rect_armed.topleft = [10,250]
    rect_ener_on.topleft = [10,300]
    rect_batt_f.topleft = [10,350]

    panels = []
    panels.append({'texto_ok': "",'texto_f': "",'imagen_ok': signal_on, 'imagen_f': signal_off, 'rect': rect_signal_on,'on_click': False})
    panels.append({'texto_ok': "Sin alarma",'texto_f': "En alarma",'imagen_ok': alarm_off, 'imagen_f': alarm_on, 'rect': rect_alarm_off,'on_click': False})
    panels.append({'texto_ok': "Armado",'texto_f': "Desarmado",'imagen_ok': armed, 'imagen_f': disarmed, 'rect': rect_armed,'on_click': False})
    panels.append({'texto_ok': "Energizado",'texto_f': "Desenergizado",'imagen_ok': ener_on, 'imagen_f': ener_off, 'rect': rect_ener_on,'on_click': False})
    panels.append({'texto_ok': "Bateria",'texto_f': "Bateria",'imagen_ok': batt_f, 'imagen_f': batt_e, 'rect': rect_batt_f,'on_click': False})

###############            BOTONES
    rect_reports_bu.topleft = [10,10]
    rect_stats_bu.topleft = [100,10]

    botones = []
    botones.append({'texto': "Reportes", 'imagen': reports_bu, 'imagen_pressed': reports_bp, 'rect': rect_reports_bu,'on_click': False})
    botones.append({'texto': "Estadísticas", 'imagen': stats_bu, 'imagen_pressed': stats_bp, 'rect': rect_stats_bu,'on_click': False})

###############            ZONAS

    rect_zona3_bu.topleft = [347,198]
    rect_zona2_bu.topleft = [263,299]
    rect_zona1_bu.topleft = [230,420]
    zonas = []
    zonas.append({'texto': "Zona 1", 'imagen': zona_bu, 'imagen_pressed': zona_bp, 'rect': rect_zona1_bu,'on_click': False})
    zonas.append({'texto': "Zona 2", 'imagen': zona_bu, 'imagen_pressed': zona_bp, 'rect': rect_zona2_bu,'on_click': False})
    zonas.append({'texto': "Zona 3", 'imagen': zona_bu, 'imagen_pressed': zona_bp, 'rect': rect_zona3_bu,'on_click': False})

    alarma_z1=False
    estado_comu_z1=True
    alarma_z2=False
    estado_comu_z2=True
    alarma_z3=False
    estado_comu_z3=True

    while not game_over:

        estado_comu_z1=True
        estado_comu_z2=True
        estado_comu_z3=True
        #alarma_z1=False
        datos=comu()
        if len(datos)>0:
            #print(datos)
            indice_a = datos.index('+')
            indice_b = datos.index('*')
            dispositivo= datos[0:indice_a]
            estado = datos[indice_a+1:indice_b]
            cerca = datos[indice_b+1:len(datos)]
            #print(dispositivo)
            #print(estado)
            #print(cerca)
            cerca_array=list(cerca)
            #print(cerca_array)
# ################################rpi1#############################
            if(dispositivo=="Rpi1"):
                estado_comu_z1=False
                if estado=="on":
                    alarma_z1=True
                    if cerca_array[0]== "1":
                        c_cerca_1=ROJO
                    if cerca_array[1]== "1":
                        c_cerca_2=ROJO
                    if cerca_array[2]== "1":
                        c_cerca_3=ROJO
                    if cerca_array[3]== "1":
                        c_cerca_4=ROJO
                    if cerca_array[4]== "1":
                        c_cerca_5=ROJO
                elif estado== "off":
                    alarma_z1=False
#####################################################################

################################rpi2#############################
            if(dispositivo=="Rpi2"):
                estado_comu_z2=False
                if estado=="on":
                    alarma_z2=True
                    if cerca_array[0]== "1":
                        c_cerca_6=ROJO
                    if cerca_array[1]== "1":
                        c_cerca_7=ROJO
                    if cerca_array[2]== "1":
                        c_cerca_8=ROJO
                    if cerca_array[3]== "1":
                        c_cerca_9=ROJO
                elif estado== "off":
                    alarma_z2=False
#####################################################################

################################rpi2#############################
            if(dispositivo=="Rpi3"):
                estado_comu_z3=False
                if estado=="on":
                    alarma_z3=True
                    if cerca_array[0]== "1":
                        c_cerca_10=ROJO
                    if cerca_array[1]== "1":
                        c_cerca_11=ROJO
                    if cerca_array[2]== "1":
                        c_cerca_12=ROJO
                    if cerca_array[3]== "1":
                        c_cerca_13=ROJO
                elif estado== "off":
                    alarma_z3=False
####################################################################


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.MOUSEBUTTONUP:
                posicion_mouse()
                for boton in botones:
                    boton['on_click'] = boton['rect'].colliderect([xm, ym, 1, 1])
                for zona in zonas:
                    zona['on_click'] = zona['rect'].colliderect([xm, ym, 1, 1])
                # for panel in panels:
                #     panel['on_click'] = panel['rect'].colliderect([xm, ym, 1, 1])
            if event.type == pygame.MOUSEBUTTONDOWN:
                posicion_mouse()

        rect_mapa.topleft = [200,200]
        pygame.draw.rect(pantalla,GRIS,[0,0,1024,100],0) #Fondo superior
        pygame.draw.rect(pantalla,GRIS,[0,110,150,600],0) #Fondo inzquierda
        pygame.draw.rect(pantalla,GRIS,[670,110,150,600],0) #Fondo derecho
        pygame.draw.lines(pantalla,c_cerca_1,False,[(344,470),(347,449)], 8)  #cerca1
        pygame.draw.lines(pantalla,c_cerca_2,False,[(347,449),(350,428)], 8)  #cerca2
        pygame.draw.lines(pantalla,c_cerca_3,False,[(350,428),(357,407)], 8)  #cerca3
        pygame.draw.lines(pantalla,c_cerca_4,False,[(357,407),(363,386)], 8)  #cerca4
        pygame.draw.lines(pantalla,c_cerca_5,False,[(363,386),(368,365)], 8)  #cerca5
        pygame.draw.lines(pantalla,c_cerca_6,False,[(368,365),(375,344)], 8)  #cerca6
        pygame.draw.lines(pantalla,c_cerca_7,False,[(375,344),(385,323)], 8)  #cerca7
        pygame.draw.lines(pantalla,c_cerca_8,False,[(385,323),(395,302)], 8)  #cerca8
        pygame.draw.lines(pantalla,c_cerca_9,False,[(395,302),(420,281)], 8)  #cerca9
        pygame.draw.lines(pantalla,c_cerca_10,False,[(420,281),(445,260)], 8)  #cerca10
        pygame.draw.lines(pantalla,c_cerca_11,False,[(445,260),(471,239)], 8)  #cerca11
        pygame.draw.lines(pantalla,c_cerca_12,False,[(471,239),(472,218)], 8)  #cerca12
        pygame.draw.lines(pantalla,c_cerca_13,False,[(472,218),(472,197)], 8)  #cerca13
        texto=font_c.render(selected,1,BLANCO)
        pantalla.blit(texto,[20,110])


        if zonas[0]['on_click']:
            selected="Zona 1"
            c_cerca_1=VERDE
            c_cerca_2=VERDE
            c_cerca_3=VERDE
            c_cerca_4=VERDE
            c_cerca_5=VERDE
            c_cerca_6=AMARILLO
            c_cerca_7=AMARILLO
            c_cerca_8=AMARILLO
            c_cerca_9=AMARILLO
            c_cerca_10=AMARILLO
            c_cerca_11=AMARILLO
            c_cerca_12=AMARILLO
            c_cerca_13=AMARILLO
            panels[0]["on_click"]=estado_comu_z1
            panels[1]["on_click"]=alarma_z1
            panels[2]["on_click"]=False
            panels[3]["on_click"]=False
            panels[4]["on_click"]=False
            crear_panel(panels,selected)
        elif zonas[1]['on_click']:
            selected="Zona 2"
            c_cerca_1=AMARILLO
            c_cerca_2=AMARILLO
            c_cerca_3=AMARILLO
            c_cerca_4=AMARILLO
            c_cerca_5=AMARILLO
            c_cerca_6=VERDE
            c_cerca_7=VERDE
            c_cerca_8=VERDE
            c_cerca_9=VERDE
            c_cerca_10=AMARILLO
            c_cerca_11=AMARILLO
            c_cerca_12=AMARILLO
            c_cerca_13=AMARILLO
            panels[0]["on_click"]=estado_comu_z2
            panels[1]["on_click"]=alarma_z2
            panels[2]["on_click"]=False
            panels[3]["on_click"]=False
            panels[4]["on_click"]=False
            crear_panel(panels,selected)
        elif zonas[2]['on_click']:
            selected="Zona 3"
            c_cerca_1=AMARILLO
            c_cerca_2=AMARILLO
            c_cerca_3=AMARILLO
            c_cerca_4=AMARILLO
            c_cerca_5=AMARILLO
            c_cerca_6=AMARILLO
            c_cerca_7=AMARILLO
            c_cerca_8=AMARILLO
            c_cerca_9=AMARILLO
            c_cerca_10=VERDE
            c_cerca_11=VERDE
            c_cerca_12=VERDE
            c_cerca_13=VERDE
            panels[0]["on_click"]=estado_comu_z3
            panels[1]["on_click"]=alarma_z3
            panels[2]["on_click"]=False
            panels[3]["on_click"]=False
            panels[4]["on_click"]=False
            crear_panel(panels,selected)
        else:
            c_cerca_1=AMARILLO
            c_cerca_2=AMARILLO
            c_cerca_3=AMARILLO
            c_cerca_4=AMARILLO
            c_cerca_5=AMARILLO
            c_cerca_6=AMARILLO
            c_cerca_7=AMARILLO
            c_cerca_8=AMARILLO
            c_cerca_9=AMARILLO
            c_cerca_10=AMARILLO
            c_cerca_11=AMARILLO
            c_cerca_12=AMARILLO
            c_cerca_13=AMARILLO
            selected="Seleccionar Zona"
        crear_boton(botones)
        crear_zona(zonas)
        #crear_panel(panels,selected)
        pygame.display.flip()
        clock.tick(0)

    pygame.quit()

if __name__ == '__main__':
    main()
