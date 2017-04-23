
class ErrorValidacion(Exception):

    def __init__(self, _function, _message):
        self.funcion = _function
        self.mensaje = _message

    def __str__(self):
        return repr(self.mensaje)


class ErrorEjecucion(Exception):

    def __init__(self, _function, _type, _message):
        self.funcion = _function
        self.tipo = _type
        self.mensaje = _message

        self.validar_Mensaje()

    def validar_Mensaje(self):

        if self.funcion == 'Comprobante.read_ComprobanteNode()':
            if self.mensaje == "'NoneType' object has no attribute 'get'":
                self.mensaje = "No existe este nodo"
        if self.funcion == 'Comprobante.read_EmisorNode()':
            if self.mensaje == "'NoneType' object has no attribute 'get'":
                self.mensaje = "No existe este nodo"
            if self.mensaje == "'NoneType' object has no attribute 'find'":
                self.mensaje = "No existe este nodo"
        if self.funcion == 'Comprobante.read_Emisor_DomicilioFiscal_Node()':
            if self.mensaje == "'NoneType' object has no attribute 'get'":
                self.mensaje = "No existe este nodo"
            if self.mensaje == "'NoneType' object has no attribute 'find'":
                self.mensaje = "No existe este nodo"
        if self.funcion == 'Comprobante.read_Emisor_ExpedidoEn_Node()':
            if self.mensaje == "'NoneType' object has no attribute 'get'":
                self.mensaje = "No existe este nodo"
        if self.funcion == 'Comprobante.read_Emisor_RegimenFiscal_Node()':
            if self.mensaje == "'NoneType' object has no attribute 'get'":
                self.mensaje = "No existe este nodo"
            if self.mensaje == "'NoneType' object has no attribute 'find'":
                self.mensaje = "No existe este nodo"
        if self.funcion == 'Comprobante.read_Receptor_Node()':
            if self.mensaje == "'NoneType' object has no attribute 'get'":
                self.mensaje = "No existe este nodo"
            if self.mensaje == "'NoneType' object has no attribute 'find'":
                self.mensaje = "No existe este nodo"
        if self.funcion == 'Comprobante.read_Receptor_Domicilio_Node()':
            if self.mensaje == "'NoneType' object has no attribute 'get'":
                self.mensaje = "No existe este nodo"
            if self.mensaje == "'NoneType' object has no attribute 'find'":
                self.mensaje = "No existe este nodo"
        if self.funcion == 'Comprobante.read_Impuestos_Node()':
            if self.mensaje == "'NoneType' object has no attribute 'get'":
                self.mensaje = "No existe este nodo"
            if self.mensaje == "'NoneType' object has no attribute 'find'":
                self.mensaje = "No existe este nodo"
        if self.funcion == 'Comprobante.read_Impuestos_Traslados()':
            if self.mensaje == "'NoneType' object is not iterable":
                self.mensaje = "No tiene detalle de impuestos"
        if self.funcion == 'Comprobante.read_Impuestos_Retenciones()':
            if self.mensaje == "'NoneType' object is not iterable":
                self.mensaje = "No tiene detalle de impuestos"
        if self.funcion == 'Comprobante.read_Conceptos_Node()':
            if self.mensaje == "'NoneType' object is not iterable":
                self.mensaje = "No tiene conceptos"
            if self.mensaje == "'NoneType' object has no attribute 'find'":
                self.mensaje = "No existe este nodo"
        if self.funcion == 'Comprobante.read_Complemento_Node()':
            if self.mensaje == "'NoneType' object has no attribute 'get'":
                self.mensaje = "No existe este nodo"
            if self.mensaje == "'NoneType' object has no attribute 'find'":
                self.mensaje = "No existe este nodo"
        if self.funcion == 'Comprobante.read_Nomina_Node()':
            if self.mensaje == "'NoneType' object has no attribute 'get'":
                self.mensaje = "No existe este nodo"
        if self.funcion == 'Comprobante.read_Nomina_Percepciones_Node()':
            if self.mensaje == "'NoneType' object has no attribute 'find'":
                self.mensaje = "No existe este nodo"
        if self.funcion == 'Comprobante.read_Nomina_Deducciones_Node()':
            if self.mensaje == "'NoneType' object has no attribute 'find'":
                self.mensaje = "No existe este nodo"
        if self.funcion == 'Comprobante.read_Nomina_Deducciones_Node()':
            if self.mensaje == "'NoneType' object has no attribute 'find'":
                self.mensaje = "No existe este nodo"
        if self.funcion == 'Comprobante.read_Nomina_HorasExtras()':
            if self.mensaje == "'NoneType' object is not iterable":
                self.mensaje = "No tiene Horas Extras"
            if self.mensaje == "'NoneType' object has no attribute 'find'":
                self.mensaje = "No existe este nodo"
        if self.funcion == 'ModeloFacturaProveedor.add()':
            if self.tipo == 'IntegrityError':
                self.mensaje = 'Factura de Proveedor ya existe en la BD'

        if self.funcion == 'ModeloFacturaCliente.add()':
            if self.tipo == 'IntegrityError':
                self.mensaje = 'Factura de Cliente ya existe en la BD'

        if self.funcion == 'ComprobanteEmpleado.add()':
            if self.tipo == 'IntegrityError':
                self.mensaje = 'Comprobante de Empleado ya existe en la BD'

        if self.funcion == 'ModeloResumen.add()':
            if self.tipo == "IntegrityError":
                self.mensaje = 'Ya existe el registro de resumen para este dia'

        if self.funcion == 'WebSAT.download()':
            if self.mensaje == "object of type 'NoneType' has no len()":
                self.mensaje = 'No se proporcionaron links a descargar'
                self.tipo = 'ErrorEjecucion'

    def __str__(self):

        cadena = "{} - [{}] : {}".format(
            self.funcion,
            self.tipo,
            self.mensaje
        )

        return repr(cadena)
