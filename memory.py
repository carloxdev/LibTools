# -*- coding: utf-8 -*-

import logging


class Log(object):

    def __init__(self):

        self.file = None

        self.writer = logging.getLogger()
        self.writer.setLevel(logging.INFO)

    def set_show_InConsole(self):

        # create console handler and set level to info
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
        handler.setFormatter(formatter)
        self.writer.addHandler(handler)

    def set_save_InFile(self):
        # create file handler and set level to error
        handler = logging.FileHandler(
            self.file.get_Abspath(),
            "w",
            encoding=None
        )
        formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
        handler.setFormatter(formatter)
        self.writer.addHandler(handler)

    def set_log(self, _archivo):

        self.file = _archivo

        for hdlr in self.writer.handlers[:]:  # remove all old handlers
            self.writer.removeHandler(hdlr)
        self.set_show_InConsole()
        self.set_save_InFile()

    def get_Writer(self):
        return self.writer


class LogMemory(object):

    def __init__(self):

        self.texto = "\n"

    def clear(self):

        self.texto = "\n"

    def section(self, _message):

        txt = '\n{}'.format(_message.upper())
        self.texto += '\n{}\n'.format(_message.upper())
        print txt

    def line(self, _message):

        txt = '{}'.format(_message)
        self.texto += '{}\n'.format(_message)
        print txt
