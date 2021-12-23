import pygame,sys
import time
from pygame.locals import *
from modulo_comunicacion import comunicacion_tcp as comu
from reportes_activacion import reporte as report
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
zona_bu= pygame.image.load('images/zona.png')
zona_bp= pygame.image.load('images/zona_pressed.png')
cerca_on= pygame.image.load('images/cerca_off.png')
cerca_off= pygame.image.load('images/cerca_on.png')
signal_on= pygame.image.load('images/signal_on.png')
signal_off= pygame.image.load('images/signal_off.png')
alarm_on= pygame.image.load('images/alarm_on.png')
alarm_off= pygame.image.load('images/alarm_off.png')
state_on= pygame.image.load('images/punto_rojo.png')
state_off= pygame.image.load('images/punto_verde.png')


rect_zona1_bu = zona_bu.get_rect()
rect_zona2_bu = zona_bu.get_rect()
rect_zona3_bu = zona_bu.get_rect()
rect_s1_bu = state_on.get_rect()
rect_s2_bu = state_on.get_rect()
rect_s3_bu = state_on.get_rect()
rect_cerca_1 = cerca_on.get_rect()
rect_cerca_2 = cerca_on.get_rect()
rect_cerca_3 = cerca_on.get_rect()
rect_cerca_4 = cerca_on.get_rect()
rect_cerca_5 = cerca_on.get_rect()
rect_signal_on = signal_on.get_rect()
rect_alarm_off = alarm_off.get_rect()
rect_mapa = mapa.get_rect()
rect_signal_on_1 = signal_on.get_rect()
rect_signal_on_2 = signal_on.get_rect()
rect_signal_on_3 = signal_on.get_rect()
############################        INICIO      ###################
pygame.init()
font_b = pygame.font.SysFont("Arial", 15)
font_c = pygame.font.SysFont("Arial", 20)
font_s = pygame.font.SysFont("Arial Narrow", 18)

dimensiones = [680, 500]
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





def crear_panel_2(lista_panel,selected):
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
    rect_mapa.topleft = [180,50]
    pantalla.blit(mapa, rect_mapa)

###############            PANEL
    rect_signal_on.topleft = [10,50]
    rect_alarm_off.topleft = [10,100]
    rect_cerca_1.topleft = [10,150]
    rect_cerca_2.topleft = [10,200]
    rect_cerca_3.topleft = [10,250]
    rect_cerca_4.topleft = [10,300]
    rect_cerca_5.topleft = [10,350]
    rect_signal_on_1.topleft = [10,50]
    rect_signal_on_2.topleft = [10,100]
    rect_signal_on_3.topleft = [10,150]

    rect_s3_bu.topleft = [351,105]
    rect_s2_bu.topleft = [267,206]
    rect_s1_bu.topleft = [234,327]

    panels = []
    panels.append({'texto_ok': "Señal",'texto_f': "Señal",'imagen_ok': signal_on, 'imagen_f': signal_off, 'rect': rect_signal_on,'on_click': False})
    panels.append({'texto_ok': "Alarma",'texto_f': "Alarma",'imagen_ok': alarm_off, 'imagen_f': alarm_on, 'rect': rect_alarm_off,'on_click': False})
    panels.append({'texto_ok': "Cerca 1",'texto_f': "Cerca 1",'imagen_ok': cerca_on, 'imagen_f': cerca_off, 'rect': rect_cerca_1,'on_click': False})
    panels.append({'texto_ok': "Cerca 2",'texto_f': "Cerca 2",'imagen_ok': cerca_on, 'imagen_f': cerca_off, 'rect': rect_cerca_2,'on_click': False})
    panels.append({'texto_ok': "Cerca 3",'texto_f': "Cerca 3",'imagen_ok': cerca_on, 'imagen_f': cerca_off, 'rect': rect_cerca_3,'on_click': False})
    panels.append({'texto_ok': "Cerca 4",'texto_f': "Cerca 4",'imagen_ok': cerca_on, 'imagen_f': cerca_off, 'rect': rect_cerca_4,'on_click': False})
    panels.append({'texto_ok': "Cerca 5",'texto_f': "Cerca 5",'imagen_ok': cerca_on, 'imagen_f': cerca_off, 'rect': rect_cerca_5,'on_click': False})

    panels_2 = []
    panels_2.append({'texto_ok': "Señal Zona 1",'texto_f': "Señal Zona 1",'imagen_ok': signal_on, 'imagen_f': signal_off, 'rect': rect_signal_on_1,'on_click': False})
    panels_2.append({'texto_ok': "Señal Zona 2",'texto_f': "Señal Zona 2",'imagen_ok': signal_on, 'imagen_f': signal_off, 'rect': rect_signal_on_2,'on_click': False})
    panels_2.append({'texto_ok': "Señal Zona 3",'texto_f': "Señal Zona 3",'imagen_ok': signal_on, 'imagen_f': signal_off, 'rect': rect_signal_on_3,'on_click': False})

    panels_3 = []
    panels_3.append({'texto_ok': "",'texto_f': "",'imagen_ok': state_off, 'imagen_f': state_on, 'rect': rect_s1_bu,'on_click': False})
    panels_3.append({'texto_ok': "",'texto_f': "",'imagen_ok': state_off, 'imagen_f': state_on, 'rect': rect_s2_bu,'on_click': False})
    panels_3.append({'texto_ok': "",'texto_f': "",'imagen_ok': state_off, 'imagen_f': state_on, 'rect': rect_s3_bu,'on_click': False})
###############            ZONAS

    rect_zona3_bu.topleft = [347,98]
    rect_zona2_bu.topleft = [263,199]
    rect_zona1_bu.topleft = [230,320]

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
    estado_c1=False
    estado_c2=False
    estado_c3=False
    estado_c4=False
    estado_c5=False
    estado_c6=False
    estado_c7=False
    estado_c8=False
    estado_c9=False
    estado_c10=False
    estado_c11=False
    estado_c12=False
    estado_c13=False

    estado_anterior_n1="00000"
    estado_anterior_n2="00000"
    estado_anterior_n3="00000"
    while not game_over:

        estado_comu_z1=True
        estado_comu_z2=True
        estado_comu_z3=True

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
                estado_actual_n1=cerca
                estado_comu_z1=False
                if estado=="on":
                    alarma_z1=True
                    try:
                        if estado_anterior_n1 != estado_actual_n1:
                            report(dispositivo,estado_actual_n1)
                            estado_anterior_n1=estado_actual_n1
                    except:
                        print("archivo reporte abierto")
                elif estado== "off":
                    alarma_z1=False
                if cerca_array[0]== "1":
                    estado_c1=True
                elif cerca_array[0]=="0":
                    estado_c1=False
                if cerca_array[1]== "1":
                    estado_c2=True
                elif cerca_array[1]=="0":
                    estado_c2=False
                if cerca_array[2]== "1":
                    estado_c3=True
                elif cerca_array[2]=="0":
                    estado_c3=False
                if cerca_array[3]== "1":
                    estado_c4=True
                elif cerca_array[3]=="0":
                    estado_c4=False
                if cerca_array[4]== "1":
                    estado_c5=True
                elif cerca_array[4]=="0":
                    estado_c5=False

#####################################################################

################################rpi2#############################
            if(dispositivo=="Rpi2"):
                estado_actual_n2=cerca
                estado_comu_z2=False
                if estado=="on":
                    alarma_z2=True
                    try:
                        if estado_anterior_n2 != estado_actual_n2:
                            report(dispositivo,estado_actual_n2)
                            estado_anterior_n2=estado_actual_n2
                    except:
                        print("archivo reporte abierto")
                elif estado== "off":
                    alarma_z2=False
                if cerca_array[0]== "1":
                    estado_c6=True
                elif cerca_array[0]=="0":
                    estado_c6=False
                if cerca_array[1]== "1":
                    estado_c7=True
                elif cerca_array[1]=="0":
                    estado_c7=False
                if cerca_array[2]== "1":
                    estado_c8=True
                elif cerca_array[2]=="0":
                    estado_c8=False
                if cerca_array[3]== "1":
                    estado_c9=True
                elif cerca_array[3]=="0":
                    estado_c9=False
#####################################################################

################################rpi2#############################
            if(dispositivo=="Rpi3"):
                estado_comu_z3=False
                estado_actual_n3=cerca
                if estado=="on":
                    alarma_z3=True
                    try:
                        if estado_anterior_n3 != estado_actual_n3:
                            report(dispositivo,estado_actual_n3)
                            estado_anterior_n3=estado_actual_n3
                    except:
                        print("archivo reporte abierto")
                elif estado== "off":
                    alarma_z3=False
                if cerca_array[0]== "1":
                    estado_c10=True
                elif cerca_array[0]=="0":
                    estado_c10=False
                if cerca_array[1]== "1":
                    estado_c11=True
                elif cerca_array[1]=="0":
                    estado_c11=False
                if cerca_array[2]== "1":
                    estado_c12=True
                elif cerca_array[2]=="0":
                    estado_c12=False
                if cerca_array[3]== "1":
                    estado_c13=True
                elif cerca_array[3]=="0":
                    estado_c13=False
####################################################################


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.MOUSEBUTTONUP:
                posicion_mouse()

                for zona in zonas:
                    zona['on_click'] = zona['rect'].colliderect([xm, ym, 1, 1])
                # for panel in panels:
                #     panel['on_click'] = panel['rect'].colliderect([xm, ym, 1, 1])
            if event.type == pygame.MOUSEBUTTONDOWN:
                posicion_mouse()

        rect_mapa.topleft = [200,200]
        pygame.draw.rect(pantalla,GRIS,[0,10,150,480],0) #Fondo inzquierda
        pygame.draw.lines(pantalla,c_cerca_1,False,[(344,370),(347,349)], 8)  #cerca1
        pygame.draw.lines(pantalla,c_cerca_2,False,[(347,349),(350,328)], 8)  #cerca2
        pygame.draw.lines(pantalla,c_cerca_3,False,[(350,328),(357,307)], 8)  #cerca3
        pygame.draw.lines(pantalla,c_cerca_4,False,[(357,307),(363,286)], 8)  #cerca4
        pygame.draw.lines(pantalla,c_cerca_5,False,[(363,286),(368,265)], 8)  #cerca5
        pygame.draw.lines(pantalla,c_cerca_6,False,[(368,265),(375,244)], 8)  #cerca6
        pygame.draw.lines(pantalla,c_cerca_7,False,[(375,244),(385,223)], 8)  #cerca7
        pygame.draw.lines(pantalla,c_cerca_8,False,[(385,223),(395,202)], 8)  #cerca8
        pygame.draw.lines(pantalla,c_cerca_9,False,[(395,202),(420,181)], 8)  #cerca9
        pygame.draw.lines(pantalla,c_cerca_10,False,[(420,181),(445,160)], 8)  #cerca10
        pygame.draw.lines(pantalla,c_cerca_11,False,[(445,160),(471,139)], 8)  #cerca11
        pygame.draw.lines(pantalla,c_cerca_12,False,[(471,139),(472,118)], 8)  #cerca12
        pygame.draw.lines(pantalla,c_cerca_13,False,[(472,118),(472,97)], 8)  #cerca13
        texto=font_c.render(selected,1,BLANCO)
        pantalla.blit(texto,[15,10])


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
            c1="Cerca1"
            panels[0]["on_click"]=estado_comu_z1
            panels[1]["on_click"]=alarma_z1
            panels[2]["on_click"]=estado_c1
            panels[3]["on_click"]=estado_c2
            panels[4]["on_click"]=estado_c3
            panels[5]["on_click"]=estado_c4
            panels[6]["on_click"]=estado_c5
            crear_panel_2(panels,selected)
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
            panels[2]["on_click"]=estado_c6
            panels[3]["on_click"]=estado_c7
            panels[4]["on_click"]=estado_c8
            panels[5]["on_click"]=estado_c9
            panel2=[panels[0],panels[1],panels[2],panels[3],panels[4],panels[5]]
            crear_panel_2(panel2,selected)
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
            panels[2]["on_click"]=estado_c10
            panels[3]["on_click"]=estado_c11
            panels[4]["on_click"]=estado_c12
            panels[5]["on_click"]=estado_c13
            panel2=[panels[0],panels[1],panels[2],panels[3],panels[4],panels[5]]
            crear_panel_2(panel2,selected)
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
            selected="ZONAS"
            panels_2[0]["on_click"]=estado_comu_z1
            panels_2[1]["on_click"]=estado_comu_z2
            panels_2[2]["on_click"]=estado_comu_z3
            crear_panel_2(panels_2,selected)
        crear_zona(zonas)
        panels_3[0]["on_click"]=estado_comu_z1
        panels_3[1]["on_click"]=estado_comu_z2
        panels_3[2]["on_click"]=estado_comu_z3
        crear_panel_2(panels_3,selected)
        pygame.display.flip()
        clock.tick(0)

        if estado_c1:
            c_cerca_1=ROJO
        if estado_c2:
            c_cerca_2=ROJO
        if estado_c3:
            c_cerca_3=ROJO
        if estado_c4:
            c_cerca_4=ROJO
        if estado_c5:
            c_cerca_5=ROJO
        if estado_c6:
            c_cerca_6=ROJO
        if estado_c7:
            c_cerca_7=ROJO
        if estado_c8:
            c_cerca_8=ROJO
        if estado_c9:
            c_cerca_9=ROJO
        if estado_c10:
            c_cerca_10=ROJO
        if estado_c11:
            c_cerca_11=ROJO
        if estado_c12:
            c_cerca_12=ROJO
        if estado_c13:
            c_cerca_13=ROJO
    pygame.quit()

if __name__ == '__main__':
    main()
