import pygame,sys
import time
# from serie_moni import envioserie as e_s
from pygame.locals import *

NEGRO = (0, 0, 0)
GRIS = (35, 36, 37 )
BLANCO = (222, 224, 200)
VERDE=(41, 211, 66)
ROJO=(247, 55, 55 )
AZUL=(10, 139, 191)

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
rect_zona4_bu = zona_bu.get_rect()
rect_zona5_bu = zona_bu.get_rect()
rect_zona6_bu = zona_bu.get_rect()
rect_zona7_bu = zona_bu.get_rect()
rect_zona8_bu = zona_bu.get_rect()
rect_zona9_bu = zona_bu.get_rect()
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

dimensiones = [1024, 600]
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
    print ("mouse:",pos)


def main():
    global botones, zonas, panels
    pantalla.fill(NEGRO)
    game_over = False
    clock = pygame.time.Clock()
    cz1=VERDE
    cz2=VERDE
    selected="Selecionar zona"

###############             MAPA
    rect_mapa.topleft = [200,150]
    pantalla.blit(mapa, rect_mapa)

###############            PANEL
    rect_signal_on.topleft = [10,150]
    rect_alarm_off.topleft = [10,200]
    rect_armed.topleft = [10,250]
    rect_ener_on.topleft = [10,300]
    rect_batt_f.topleft = [10,350]

    panels = []
    panels.append({'texto_ok': "Con señal",'texto_f': "Sin señal",'imagen_ok': signal_on, 'imagen_f': signal_off, 'rect': rect_signal_on,'on_click': False})
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
    rect_zona1_bu.topleft = [800,530]
    rect_zona2_bu.topleft = [930,410]
    rect_zona3_bu.topleft = [840,300]
    rect_zona4_bu.topleft = [710,250]
    rect_zona5_bu.topleft = [630,180]
    rect_zona6_bu.topleft = [500,160]
    rect_zona7_bu.topleft = [330,160]
    rect_zona8_bu.topleft = [200,200]
    rect_zona9_bu.topleft = [170,350]
    zonas = []
    zonas.append({'texto': "Zona 1", 'imagen': zona_bu, 'imagen_pressed': zona_bp, 'rect': rect_zona1_bu,'on_click': False})
    zonas.append({'texto': "Zona 2", 'imagen': zona_bu, 'imagen_pressed': zona_bp, 'rect': rect_zona2_bu,'on_click': False})
    zonas.append({'texto': "Zona 3", 'imagen': zona_bu, 'imagen_pressed': zona_bp, 'rect': rect_zona3_bu,'on_click': False})
    zonas.append({'texto': "Zona 4", 'imagen': zona_bu, 'imagen_pressed': zona_bp, 'rect': rect_zona4_bu,'on_click': False})
    zonas.append({'texto': "Zona 5", 'imagen': zona_bu, 'imagen_pressed': zona_bp, 'rect': rect_zona5_bu,'on_click': False})
    zonas.append({'texto': "Zona 6", 'imagen': zona_bu, 'imagen_pressed': zona_bp, 'rect': rect_zona6_bu,'on_click': False})
    zonas.append({'texto': "Zona 7", 'imagen': zona_bu, 'imagen_pressed': zona_bp, 'rect': rect_zona7_bu,'on_click': False})
    zonas.append({'texto': "Zona 8", 'imagen': zona_bu, 'imagen_pressed': zona_bp, 'rect': rect_zona8_bu,'on_click': False})
    zonas.append({'texto': "Zona 9", 'imagen': zona_bu, 'imagen_pressed': zona_bp, 'rect': rect_zona9_bu,'on_click': False})



    while not game_over:
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
        pygame.draw.lines(pantalla,cz1,False,[(797, 504),(837, 520),(848, 509),(836, 492),(824, 478),(805, 466),(808, 451),(808, 451),(820, 444),(834, 459),(857, 463),(870, 463),(883, 469),(881, 485),(892, 489)], 8) #Zona 1
        pygame.draw.lines(pantalla,cz2,False,[(894, 489),(909, 485),(917, 468),(918, 449),(918, 430),(916, 413),(902, 409),(886, 403),(885, 394),(888, 387),(897, 376),(913, 369),(928, 368),(931, 358)], 8) #Zona 2
        texto=font_c.render(selected,1,BLANCO)
        pantalla.blit(texto,[20,110])

        if zonas[0]['on_click']:
            selected="Zona 1"
            cz1=ROJO
            panels[0]["on_click"]=True
            panels[1]["on_click"]=True
            panels[2]["on_click"]=False
            panels[3]["on_click"]=True
            panels[4]["on_click"]=False
            crear_panel(panels,selected)
        if zonas[1]['on_click']:
            selected="Zona 2"
            cz2=ROJO
            panels[0]["on_click"]=True
            panels[1]["on_click"]=False
            panels[2]["on_click"]=False
            panels[3]["on_click"]=True
            panels[4]["on_click"]=True
            crear_panel(panels,selected)

        if zonas[2]['on_click']:
            selected="Zona 3"
            cz2=ROJO
            panels[0]["on_click"]=False
            panels[1]["on_click"]=False
            panels[2]["on_click"]=False
            panels[3]["on_click"]=False
            panels[4]["on_click"]=False
            crear_panel(panels,selected)

        if zonas[3]['on_click']:
            selected="Zona 4"
            cz2=ROJO
            panels[0]["on_click"]=True
            panels[1]["on_click"]=True
            panels[2]["on_click"]=True
            panels[3]["on_click"]=True
            panels[4]["on_click"]=True
            crear_panel(panels,selected)

        crear_boton(botones)
        crear_zona(zonas)
        # crear_panel(panels,selected)
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()

if __name__ == '__main__':
    main()
