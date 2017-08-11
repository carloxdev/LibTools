# -*- coding: utf-8 -*-

# Python's Libraries
import re
import shutil
import os


# Own's Libraries
from data import Error

"""Estandariazacion de varibales:

    nombre : Nombre del archivo con todo y extension
    titulo : nombre del archivo sin extension
    extension : extension del archivo. Ejmplo: .xml

    basepath : ruta de un archivo o carpeta sin un nombre del archivo.
        Ejemplo:
            /user/files/ <--- aqui dentro esta el archivo: ejemplo.xml
            /user/files/ <--- aqui adentro hay una carpeta llamada "cosas"

    abspath : ruta de un archivo con todo y el nombre o la ruta completa de una carpeta.
        Ejemplo:
            /user/files/ejemplo.xml
            /user/files/cosas

    relativepath : ruta relativa de directorio o archivo, (Sin especificar el nombre)
        Ejemplo:
            /files
"""


class Carpeta(object):

    def __init__(self, _abspath):
        self.abspath = _abspath

    def __str__(self):
        return self.abspath

    def exist(self, _origin):

        if os.path.exists(self.abspath) is False:
            raise Error(
                "validacion",
                _origin,
                "carpeta no existe",
                "La carpeta '%s' no existe" % (self.abspath)
            )

    def not_Exist(self, _origin):

        if os.path.exists(self.abspath):
            raise Error(
                "validacion",
                _origin,
                "carpeta ya existe",
                "La carpeta '%s' ya existe" % (self.abspath)
            )

    def is_List(self, _origin, _list):

        if isinstance(_list, list) is False:
            raise Error(
                "validacion",
                _origin,
                "no se porporciono una lista",
                "No se proporciono una lista con los nuevos folders"
            )

    def get_Basepath(self, _origin):

        basepath = os.path.abspath(
            os.path.join(
                self.abspath,
                os.pardir
            )
        )

        return basepath

    def get_Files(self):

        origin = "Carpeta.get_Files()"

        self.exist(origin)

        lista_archivos = []

        try:
            archivos = os.walk(self.abspath)

            for directorio, subdirectorios, lista_nombreArchivos in archivos:

                for nombre_archivo in lista_nombreArchivos:
                    # (title, extension) = os.path.splitext(nombre_archivo)
                    folder = Carpeta(directorio)
                    lista_archivos.append(
                        Archivo(folder, nombre_archivo)
                    )

                    # if extension == _extension.upper() or extension == _extension.lower():

            return lista_archivos

        except Exception, error:

            raise Error(
                type(error).__name__,
                origin,
                "",
                str(error)
            )

    def create(self):

        origin = "Carpeta.create()"

        carpeta_base = Carpeta(self.get_Basepath(origin))
        carpeta_base.exist(origin)

        self.not_Exist(origin)

        try:

            code = os.system("mkdir " + self.abspath)

        except Exception as error:

            raise Error(
                type(error).__name__,
                origin,
                "",
                str(error)
            )

        if code == 0:
            print "Folder creado con exito: %s" % (self.abspath)

        else:
            raise Error(
                "validacion",
                origin,
                "error",
                "Creacion de folder finalizo con codigo %s" % (code)
            )

    def find_File(self, _file_name):
        origin = "Carpeta.find_File()"

        self.exist(origin)

        lista_archivos = []

        try:
            archivos = os.walk(self.abspath)

            for directorio, subdirectorios, lista_nombreArchivos in archivos:

                for nombre_archivo in lista_nombreArchivos:
                    (title, extension) = os.path.splitext(nombre_archivo)

                    (archivo_titulo, archivo_extension) = os.path.splitext(_file_name)

                    if title == archivo_titulo and extension == archivo_extension.upper():
                        lista_archivos.append(
                            Archivo(directorio, nombre_archivo)
                        )

                    if title == archivo_titulo and extension == archivo_extension.lower():
                        lista_archivos.append(
                            Archivo(directorio, nombre_archivo)
                        )

            return lista_archivos

        except Exception, error:
            raise Error(
                type(error).__name__,
                origin,
                "",
                str(error)
            )

    def find_File_ByExtension(self, _extension):
        """ Devuelve una lista con todos los archivos de determinada extencion.

            PARAMETROS:
                _extension: Tipo de archivos que se buscara. Formato: ".txt"

        """
        origin = "Carpeta.find_File_ByExtension()"

        self.exist(origin)

        lista_archivos = []

        try:
            archivos = os.walk(self.abspath)

            for directorio, subdirectorios, lista_nombreArchivos in archivos:

                for nombre_archivo in lista_nombreArchivos:
                    (title, extension) = os.path.splitext(nombre_archivo)

                    if extension == _extension.upper() or extension == _extension.lower():
                        lista_archivos.append(
                            Archivo(directorio, nombre_archivo)
                        )

            return lista_archivos

        except Exception, error:

            raise Error(
                type(error).__name__,
                origin,
                "",
                str(error)
            )

    def delete_DuplicateFiles_ByExtension(self, _extension):
        """ Elimina archivos duplicados de determinada ruta.

            PARAMETROS:
                _extension: Extension de los archivos que se eliminaran,
                            en caso de existir. Formato: ".txt"

        """
        origin = "Carpeta.delete_DuplicateFiles_ByExtension()"

        self.exist(origin)

        no_eliminados = 0

        try:

            # Se optiene la lista de archivos
            archivos = os.walk(self.abspath)

            # Se recorre la lista
            for directorio, subdirectorios, lista_nombreArchivos in archivos:

                for nombre_archivo in lista_nombreArchivos:

                    # Se separa el nombre y la extension de archivo
                    (name, extension) = os.path.splitext(nombre_archivo)

                    if extension == _extension.upper() or extension == _extension.lower():

                        if re.search('\(\d+\)$', name):

                            file_abspath = os.path.join(directorio, nombre_archivo)

                            os.remove(file_abspath)
                            no_eliminados += 1

            print "Se eliminaron %s archivos con extencion '%s'" % (
                no_eliminados,
                _extension
            )

            return no_eliminados

        except Exception, error:

            raise Error(
                type(error).__name__,
                origin,
                "",
                str(error)
            )

    def add_Folders(self, _new_listfolders):

        origin = "Carpeta.add_Folders()"

        self.is_List(origin, _new_listfolders)

        self.exist(origin)

        carpeta_nueva = Carpeta(
            os.path.join(
                self.abspath,
                *_new_listfolders
            )
        )

        carpeta_nueva.not_Exist(origin)

        path_temporal = self.abspath

        for folder_name in _new_listfolders:

            try:

                new_carpeta = Carpeta(
                    os.path.join(
                        path_temporal,
                        folder_name
                    )
                )

                new_carpeta.create()

                path_temporal = new_carpeta.abspath

            except Error as e:
                path_temporal = new_carpeta.abspath

                if e.control == "carpeta ya existe":
                    print e.mensaje

                else:
                    raise Error(
                        "validacion",
                        origin,
                        "error creando directorio",
                        e.mensaje
                    )

        print "Carpetas creadas con exito."


class Archivo(object):

    def __init__(self, _folder, _name):

        self.nombre = _name
        self.titulo = os.path.splitext(_name)[0]
        self.extension = os.path.splitext(_name)[1]
        self.carpeta = _folder
        self.carpeta_old = None
        self.file_object = None

    def get_Abspath(self):
        abspath = os.path.join(
            self.carpeta.abspath,
            self.nombre
        )

        return abspath

    def exist(self, _origin):

        if os.path.isfile(self.get_Abspath()) is False:

            raise Error(
                "validacion",
                _origin,
                "archivo no existe",
                "El archivo '%s' no existe en el folder '%s'" % (
                    self.nombre,
                    self.carpeta.abspath
                )
            )

    def not_Exist(self, _origin):

        if os.path.isfile(self.get_Abspath()):
            raise Error(
                "validacion",
                _origin,
                "archivo ya existe",
                "El archivo '%s' ya existe en el folder '%s'" % (
                    self.nombre,
                    self.carpeta.abspath
                )
            )

    def create(self):
        """ Metodo que crea el archivo en el sistema de archivos.

            Nota: Si el archivo ya existe, este se sobreescribe

        """
        origin = "Archivo.create()"

        self.carpeta.exist(origin)

        self.not_Exist(origin)

        try:
            self.file_object = open(self.get_Abspath(), "w")
            print "Archivo %s creado en el folder %s" % (self.nombre, self.carpeta.abspath)

        except Exception, error:
            raise Error(
                type(error).__name__,
                origin,
                "",
                str(error)
            )

    def copy(self, _folder_to, _replace=False):

        origin = "Archivo.copy()"

        self.exist(origin)

        carpeta_destino = _folder_to
        # carpeta_destino = Carpeta(_basepath_to)
        carpeta_destino.exist(origin)

        archivo_nuevo = Archivo(carpeta_destino, self.nombre)

        if _replace is False:
            archivo_nuevo.not_Exist(origin)

        try:
            shutil.copy(self.get_Abspath(), archivo_nuevo.get_Abspath())
            print "Se copio archivo %s al folder %s" % (
                archivo_nuevo.nombre,
                archivo_nuevo.carpeta.abspath
            )

        except Exception as error:
            raise Error(
                type(error).__name__,
                origin,
                "",
                str(error)
            )

    def move(self, _folder_to, _replace=False):

        origin = "Archivo.move()"

        self.exist(origin)

        carpeta_destino = _folder_to
        # carpeta_destino = Carpeta(_basepath_new)
        carpeta_destino.exist(origin)

        archivo_nuevo = Archivo(carpeta_destino, self.nombre)

        if _replace is False:
            archivo_nuevo.not_Exist(origin)

        try:

            shutil.move(self.get_Abspath(), archivo_nuevo.get_Abspath())

            self.carpeta_old = self.carpeta
            self.carpeta = carpeta_destino

            print "Se movio archivo %s al folder %s" % (
                archivo_nuevo.nombre,
                archivo_nuevo.carpeta.abspath
            )

        except Exception as error:
            raise Error(
                type(error).__name__,
                origin,
                "",
                str(error)
            )

    def write(self, _value):
        """ Metodo que permite escribir en un archivo.

            En caso de que no exista, crea el archivo

        """
        origin = "Archivo.write()"

        try:
            self.file_object = open(self.get_Abspath(), "wb")
            self.file_object.write(_value)
            self.file_object.close()

            print "Archivo %s guardado en el folder %s" % (self.nombre, self.carpeta.abspath)

        except Exception, error:
            raise Error(
                type(error).__name__,
                origin,
                "",
                str(error)
            )
