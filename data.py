# -*- coding: utf-8 -*-

# Python's Libraries

# import time
# import calendar
import os

from datetime import datetime
from dateutil import parser


class Error(Exception):
    """ Error personalizado para mayor control en los programas.

        ATRIBUTOS:
            tipo = Especifica el tipo de error, en caso de ser un
                   error lanzado por el usuario se sugiere utilizar el valor 'validacion'.
            origen = Funcion donde se dispara el error.
            control = Variable utilizada por otros programas para validar resultado.
            mensaje = Descripcion del error.
    """

    def __init__(self, _type, _origin, _control, _message):
        self.tipo = _type
        self.origen = _origin
        self.control = _control
        self.mensaje = _message

    def __str__(self):

        cadena = "%s....[%s] - %s" % (
            self.mensaje,
            self.tipo,
            self.origen
        )

        return repr(cadena)


class Validator(object):

    @classmethod
    def convert_ToJulianJDE(self, _date):

        jdedate = (1000 * (_date.year - 1900) + int(_date.strftime("%j")))

        return int(jdedate)

    @classmethod
    def convert_ToInt(self, _data, default=0):
        try:
            value = int(_data)
        except Exception:
            value = default

        return value

    @classmethod
    def convert_ToFloat(self, _data, default=0.0):
        try:
            value = float(_data)
        except Exception:
            value = default

        return value

    @classmethod
    def convert_ToChar(self, _data, default=""):
        if _data is None:
            return ""
        elif isinstance(_data, int):
            return str(_data)
        else:
            return _data.encode("utf-8")

    @classmethod
    def convert_ToDate(self, _data, hora=True):

        if _data is None:
            return None
        else:

            _data = _data.replace("Z", "")

            if hora:

                fecha = parser.parse(_data)
                fecha = fecha.replace(microsecond=0)

                return fecha

            else:
                return datetime.strptime(_data, '%Y-%m-%d')

    @classmethod
    def convert_ToUrl(self, ruta, file_name):
        url = os.path.join(ruta, file_name)

        return url.replace("\\", "/")
