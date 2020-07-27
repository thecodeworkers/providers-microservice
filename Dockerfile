######################################################################
# DOCKERFILE PARA CREAR IMAGEN DE PROYECTO EN PYTHON                 #
# ESTE DOCKERFILE DEBE SER UTILIZADO DENTRO DEL PROYECTO ESPECIFICO  #
# BAJO NINGUN CONCEPTO DEBE SER ARMADO Y SUBIDO A DOCKER HUB YA QUE  #
# UTILIZA EL requeriments.txt ESPECIFICO DE CADA PROYECTO            #
#                                                                    #
# PARA UTILIZAR ESTE CONTENEDOR DE FORMA INDIVIDUAL SE PUEDE         #
# EJECUTAR EL COMANDO Docker run -d --name [Nombre Contenedor]       #
# -p [Puerto Local]:[Puerto Contenedor] [RUTA DE IMAGEN]             #
#                                                                    #
# PARA MAS INFORMACION DE ESTE COMANDO VISITAR EL LINK               #
# https://docs.docker.com/engine/reference/run/                      #
#                                                                    #
# DESARROLLADOR POR: JORGE BASTIDAS                                  #
######################################################################

#IMAGEN RAIZ - FROM ESPECIFICA UNA IMAGEN DE DOCKER HUB 
FROM python:3.8-alpine
# RUN Corre un comando especifico en la imagen que se construira.
RUN mkdir /project
#WORKDIR Especifica la ruta que se usara
WORKDIR /project
#COPY copia un archivo o directorio del equipo host a la imagen que se construira
COPY ./requirements.txt /project/
#APK ADD agregar paquetes al sistema operativo de la imagen (ALPINE)
RUN apk add g++ linux-headers
#Corre el comando pip para instalar las librerias necesarias en python para correr el proyecto
RUN pip install -r requirements.txt
#CMD define el comando que se ejecutara al iniciar el contenedor de docker
CMD python run.py