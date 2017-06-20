# -*- coding: utf-8 -*-


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
