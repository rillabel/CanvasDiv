from PyQt5 import QtCore, QtGui, QtWidgets
from krita import *

class cdiv(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        global doc, hOld, vOld, Size, Origin
        doc = Krita.instance().activeDocument()
        doc.setGuidesVisible(True)
        doc.setGuidesLocked(True)

        sel = doc.selection()
        if sel is not None:
            hOld = doc.horizontalGuides()
            vOld = doc.verticalGuides()
            Size = (sel.width(),sel.height())
            Origin = (sel.x(),sel.y())
        else:
            hOld = doc.horizontalGuides()
            vOld = doc.verticalGuides()
            Size = (doc.width(),doc.height())
            Origin = (0,0)

        self.setObjectName("cdiv")
        self.resize(250, 200)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.setFont(font)
        self.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.formLayout = QtWidgets.QFormLayout(self)
        self.formLayout.setObjectName("formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignLeft)
        self.formLayout.setFormAlignment(Qt.AlignCenter)
        self.hLabel = QtWidgets.QLabel(parent=self)
        self.hLabel.setObjectName("hLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.hLabel)
        self.vLabel = QtWidgets.QLabel(parent=self)
        self.vLabel.setObjectName("vLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.vLabel)
        self.pLabel = QtWidgets.QLabel(parent=self)
        self.pLabel.setObjectName("pLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.pLabel)
        self.hVal = QtWidgets.QSpinBox(parent=self)
        self.hVal.setObjectName("hVal")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.hVal)
        self.vVal = QtWidgets.QSpinBox(parent=self)
        self.vVal.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.vVal.setObjectName("vVal")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.vVal)
        self.pushButton = QtWidgets.QPushButton(parent=self)
        self.pushButton.setObjectName("pushButton")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.FieldRole, self.pushButton)
        self.checkBox = QtWidgets.QCheckBox(parent=self)
        self.checkBox.setTabletTracking(False)
        self.checkBox.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.checkBox.setText("")
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.checkBox)
        self.bCheck = QtWidgets.QCheckBox(parent=self)
        self.bCheck.setTabletTracking(False)
        self.bCheck.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.bCheck.setText("")
        self.bCheck.setChecked(False)
        self.bCheck.setObjectName("bCheck")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.bCheck)
        self.bLabel = QtWidgets.QLabel(parent=self)
        self.bLabel.setObjectName("bLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.bLabel)

        self.pushButton.clicked.connect(self.accept)
        self.bCheck.stateChanged.connect(self.scrupdate)
        self.checkBox.stateChanged.connect(self.scrupdate)
        self.vVal.valueChanged.connect(self.scrupdate)
        self.hVal.valueChanged.connect(self.scrupdate)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)


    def retranslateUi(self, cdiv):
        _translate = QtCore.QCoreApplication.translate
        cdiv.setWindowTitle(_translate("cdiv", "cDiv"))
        self.hLabel.setText(_translate("cdiv", "Horizontal Guides:"))
        self.vLabel.setText(_translate("cdiv", "Vertical Guides:"))
        self.pLabel.setText(_translate("cdiv", "Preserve Guides:"))
        self.pushButton.setText(_translate("cdiv", "OK"))
        self.bLabel.setText(_translate("cidv", "Border Guides:"))

    def reject(self):
        doc.setHorizontalGuides(hOld)
        doc.setVerticalGuides(vOld)
        self.done(0)

    def scrupdate(self):
        hDivs = self.hVal.value()+1
        vDivs = self.vVal.value()+1
        hNew = []
        vNew = []

        for i in range(1, hDivs):
            hNew.append(i * Size[1] / hDivs + Origin[1])
        for i in range(1, vDivs):
            vNew.append(i * Size[0] / vDivs + Origin[0])
        if self.checkBox.isChecked():
            hNew.extend(hOld)
            vNew.extend(vOld)
        if self.bCheck.isChecked():
            hNew.extend([Origin[1],Origin[1]+Size[1]])
            vNew.extend([Origin[0],Origin[0]+Size[0]])

        doc.setHorizontalGuides(set(hNew))
        doc.setVerticalGuides(set(vNew))
        doc.setGuidesLocked(True)

