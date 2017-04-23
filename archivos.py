# -*- coding: utf-8 -*-

# Librerias Python
import re
import shutil
import os

# Librerias Propias
from errores import ErrorEjecucion
from errores import ErrorValidacion

"""Estandariazacion de varibales:

basepath : ruta de un archivo(s) sin un nombre del archivo. Ejemplo:
/user/files <--- aqui dentro esta el archivo: ejemplo.xml

abspath : ruta de un archivo con todo y el nombre. Ejemplo:
/user/files/ejemplo.xml

relativepath : ruta relativa de directorio o archivo, (Sin especificar el nombre)
Ejemplo:
/files

titulo : nombre del archivo sin extension

extension : extension del archivo: .xml
"""


class Archivo(object):

    def __init__(self, _basepath, _name):

        # titulo = nombre del archivo sin extension
        self.nombre = _name
        self.titulo = os.path.splitext(_name)[0]
        self.extension = os.path.splitext(_name)[1]
        self.basepath = _basepath
        self.abspath = os.path.join(self.basepath, self.nombre)
        self.abspath_old = ""
        self.file = None

    def move(self, _basepath_new):

        abspath_new = os.path.join(_basepath_new, self.name)

        shutil.move(self.abspath, abspath_new)

        self.abspath_old = self.abspath
        self.abspath = abspath_new

        print "Se movio archivo a: {}".format(abspath_new)

    def copy(self, _abspath_new):

        shutil.copy(self.abspath, _abspath_new)
        print "Se copio archivo a: {}".format(_abspath_new)

    def create(self):

        if os.path.isfile(self.abspath):
            print "El archivo {} ya existe".format(self.abspath)
        else:
            try:
                self.file = open(self.abspath, "w")
                return "Archivo {} creado".format(self.abspath)

            except Exception, error:
                raise ErrorEjecucion(
                    'Archivo.create()',
                    type(error).__name__,
                    str(error)
                )


class FileManager(object):

    @classmethod
    def get_Files_ByExtension(self, _abspath, _extension):
        """ Devuelve una lista con todos los archivos de determinada extenxion"""

        lista_archivos = []

        try:

            if os.path.exists(_abspath):

                archivos = os.walk(_abspath)

                for directorio, subdirectorios, lista_nombreArchivos in archivos:

                    for nombre_archivo in lista_nombreArchivos:
                        (title, ext) = os.path.splitext(nombre_archivo)

                        if ext == _extension.upper() or ext == _extension.lower():
                            lista_archivos.append(
                                Archivo(directorio, nombre_archivo)
                            )
            else:
                print "El folder no existe: {}".format(_abspath)

            return lista_archivos

        except Exception, error:

            raise ErrorEjecucion(
                "FileManager.get_Files()",
                type(error).__name__,
                str(error)
            )

    @classmethod
    def delete_DuplicateFiles_ByExtension(self, _abspath, _extension):
        """ Elimina archivos duplicados de determinada ruta """

        no_eliminados = 0

        try:

            if os.path.exists(_abspath):

                # Se optiene la lista de archivos
                archivos = os.walk(_abspath)

                # Se recorre la lista
                for directorio, subdirectorios, lista_nombreArchivos in archivos:

                    for nombre_archivo in lista_nombreArchivos:

                        # Se separa el nombre y la extension de archivo
                        (name, ext) = os.path.splitext(nombre_archivo)

                        if ext == _extension.upper() or ext == _extension.lower():

                            if re.search('\(\d+\)$', name):

                                file_abspath = os.path.join(
                                    directorio, nombre_archivo)

                                os.remove(file_abspath)
                                # Eliminar
                                no_eliminados += 1

                print "Eliminar archivos {} repetidos: {}".format(
                    _extension,
                    no_eliminados
                )

            else:
                print "El folder no existe: {}".format(_abspath)

            return no_eliminados

        except Exception, error:

            raise ErrorEjecucion(
                "FileManager.delete_DuplicateFiles()",
                type(error).__name__,
                str(error)
            )

    @classmethod
    def create_Folder(self, _abspath):
        """ Crea folder dando la ruta base de este mismo """
        try:

            if os.path.exists(_abspath):
                print "El folder ya existe: {}".format(_abspath)
            else:
                code = os.system("mkdir " + _abspath)
                if code == 0:
                    print "Folder creado con exito: {}".format(_abspath)
                else:
                    raise ErrorValidacion(
                        "Creacion de folder finalizo con codigo {}".format(
                            code)
                    )

        except Exception, error:
            raise ErrorEjecucion(
                "FileManager.create_Folder()",
                type(error).__name__,
                str(error)
            )

    @classmethod
    def create_Directory(self, _basepath, _new_nameFolders):

        """ Crea una estructura de directorios """

        try:
            directory_abspath = os.path.join(_basepath, _new_nameFolders)

            if os.path.exists(directory_abspath):
                print "El directorio ya existe: {}".format(directory_abspath)
            else:

                list_new_namefolders = _new_nameFolders.split('/')
                folder_abspath = ''

                for folderName in list_new_namefolders:

                    folder_abspath = os.path.join(
                        _basepath, folder_abspath, folderName)
                    self.create_Folder(folder_abspath)

                print "Directorio creado con exito: {}".format(
                    directory_abspath
                )

        except Exception, error:

            raise ErrorEjecucion(
                "FileManager.create_Directory()",
                type(error).__name__,
                str(error)
            )

    @classmethod
    def find_File(self, _archivo, _abspath):

        """
            Busca un archivo en una ruta y devuelve las coincidencias en una lista
            con objetos de archivo con informacion del mismo
        """

        lista_archivos = []

        try:
            if os.path.exists(_abspath):

                archivos = os.walk(_abspath)

                for directorio, subdirectorios, lista_nombreArchivos in archivos:

                    for nombre_archivo in lista_nombreArchivos:
                        (title, ext) = os.path.splitext(nombre_archivo)

                        if title == _archivo.titulo and ext == _archivo.extension.upper():
                            lista_archivos.append(
                                Archivo(directorio, nombre_archivo)
                            )

                        if title == _archivo.titulo and ext == _archivo.extension.lower():
                            lista_archivos.append(
                                Archivo(directorio, nombre_archivo)
                            )

            else:
                print "El folder no existe: {}".format(_abspath)

            return lista_archivos

        except Exception, error:
            raise ErrorEjecucion(
                "FileManager.find_File()",
                type(error).__name__,
                str(error)
            )
