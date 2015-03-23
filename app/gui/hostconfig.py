# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QDialog, QLabel
from app.gui.hostconfig_ui import Ui_HostConfig


class HostConfigDialog(QDialog):
    def __init__(self, hosts):
        super(HostConfigDialog, self).__init__()
        self.ui = Ui_HostConfig()
        self.ui.setupUi(self)
        self.hosts = hosts
        # label to use to show errors
        self.errorLabel = None

        self.attributes = ['name', 'address', 'user', 'password']

    def getTextFieldValue(self, field):
        """ field value or None
        :param field: object id
        :return: value or None
        """
        field = getattr(self.ui, field)
        value = field.text()
        if value == '':
            return None
        return value

    def collectFieldsValues(self):
        attributesDict = {}
        for attr in self.attributes:
            attributesDict[attr] = self.getTextFieldValue(attr)
        return attributesDict

    def acceptAddHost(self):
        attributesDict = self.collectFieldsValues()
        try:
            self.hosts.create(**attributesDict)
        except Exception as e:
            self.setErrorLabel(e.message)
        else:
            self.accept()

    def acceptEditHost(self, host):
        attributesDict = self.collectFieldsValues()
        try:
            self.hosts.updateHostValues(host, attributesDict)
        except Exception as e:
            self.setErrorLabel(e.message)
        else:
            self.accept()

    def setErrorLabel(self, text):
        if self.errorLabel is None:
                self.errorLabel = QLabel()
        self.errorLabel.setText(text)
        self.ui.errorArea.addWidget(self.errorLabel)

    def add(self):
        self.ui.acceptButton.clicked.connect(self.acceptAddHost)
        retCode = self.exec_()
        self.ui.acceptButton.disconnect()

        return retCode

    def edit(self, hostName):
        """
        :param hostName:
        :type hostName: app.hosts.Hosts
        :return:
        """
        host = self.hosts.get(hostName)
        for attribute in self.attributes:
            field = getattr(self.ui, attribute)
            field.setText(getattr(host, attribute))

        self.ui.acceptButton.clicked.connect(lambda: self.acceptEditHost(host))
        retCode = self.exec_()
        self.ui.acceptButton.disconnect()

        return retCode