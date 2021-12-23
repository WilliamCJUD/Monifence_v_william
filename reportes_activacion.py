from datetime import datetime

def checkFileExistance(filePath):
    try:
        with open(filePath, 'r') as f:
            return True
    except FileNotFoundError as e:
        return False
    except IOError as e:
        return False
def reporte(dispositivo,cerca):
    if len(cerca)>0:
        cerca_num=[]
        cerca_reporte=[]
        mensaje_reporte=""
        mensaje_reporte_2=""
        cerca_array=list(cerca)
        cont=0
        for n in cerca_array:
            if cerca_array[cont]=="1":
                cerca_reporte.append("ON;")

            elif cerca_array[cont]=="0":
                cerca_reporte.append("OFF;")
            cerca_num.append("cerca_"+str(cont+1)+";")
            mensaje_reporte=mensaje_reporte+cerca_reporte[cont]
            mensaje_reporte_2=mensaje_reporte_2+cerca_num[cont]
            cont=cont+1


        fecha=datetime.today().strftime('%Y-%m-%d')
        hora=datetime.today().strftime('%H:%M:%S')
        mensaje_reporte=mensaje_reporte+""+hora
        a="Reporte_"+fecha+".csv"
        if dispositivo=="Rpi1":
            nombre_carpeta="Reportes_cerca/Nodo_1/"
        elif dispositivo=="Rpi2":
            nombre_carpeta="Reportes_cerca/Nodo_2/"
        elif dispositivo=="Rpi3":
            nombre_carpeta="Reportes_cerca/Nodo_3/"
        nombre=nombre_carpeta+a
        if checkFileExistance(nombre)==False:
            archivo = open(nombre,"a")
            archivo.write(mensaje_reporte_2+"Hora")
            archivo.write("\n")
        archivo = open(nombre,"a")
        archivo.write(mensaje_reporte)
        archivo.write("\n")
        archivo.close()
