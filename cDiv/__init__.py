from .cdiv import *
from krita import *

class cDiv(Extension):

    def __init__(self, parent):
        super().__init__(parent)

    def setup(self):
        pass

    def createActions(self, window):
        action = window.createAction("canvasDiv","cDiv","tools")
        action.triggered.connect(self.canvasDiv)

    def canvasDiv(self):
        doc = Krita.instance().activeDocument()
        if doc is not None:
            cdiv().exec()

Krita.instance().addExtension(cDiv(Krita.instance()))
