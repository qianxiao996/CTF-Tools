from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget, QMessageBox
from GUI.Xiandaimima import Ui_Form_Xiandaimima
from module.func_aes import Class_Aes


class QWidget_XiandaiMima(QWidget):

    def __init__(self):
        super().__init__()
        self.Ui_X = Ui_Form_Xiandaimima()
        self.Ui_X.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('./logo.ico'))
        self.Ui_X.AES_Encrypto.clicked.connect(self.AES_Encrypto)
        self.Ui_X.AES_Decrypto.clicked.connect(self.AES_Decrypto)
        self.Ui_X.AES_Mode.activated[str].connect(self.change_aes_setting)
    def change_aes_setting(self):
        AES_Mode = self.Ui_X.AES_Mode.currentText()
        if AES_Mode == 'ECB':
            self.Ui_X.AES_Pianyi.setEnabled(False)
        else:
            self.Ui_X.AES_Pianyi.setEnabled(True)

    def AES_Encrypto(self):
        aes_mode = self.Ui_X.AES_Mode.currentText()
        aes_zifuji = self.Ui_X.AES_zifuji.currentText()
        aes_tianchong = self.Ui_X.AES_Tianchong.currentText()
        aes_iv = self.Ui_X.AES_Pianyi.text()
        aes_encode = self.Ui_X.AES_Bianma.currentText()
        aes_key = self.Ui_X.AES_Miyao.text()
        aes_m_text = self.Ui_X.AES_Source.toPlainText()
        aes_type = self.Ui_X.comboBox_type.currentText()

        result_text = getattr(Class_Aes(), 'encrypt')(aes_type,aes_mode, aes_zifuji, aes_tianchong, aes_iv, aes_encode, aes_key,aes_m_text)
        if result_text[0] == 'success':
            self.Ui_X.AES_Result.setPlainText(result_text[1])
        elif result_text[0] == 'error':
            QMessageBox.critical(self, 'Error', result_text[1])
        else:
            QMessageBox.information(self, 'INFO', result_text[1])

    def AES_Decrypto(self):
        aes_mode = self.Ui_X.AES_Mode.currentText()
        aes_zifuji = self.Ui_X.AES_zifuji.currentText()
        aes_iv = self.Ui_X.AES_Pianyi.text()
        aes_encode = self.Ui_X.AES_Bianma.currentText()
        aes_key = self.Ui_X.AES_Miyao.text()
        aes_m_text = self.Ui_X.AES_Result.toPlainText()
        aes_type = self.Ui_X.comboBox_type.currentText()

        result_text = getattr(Class_Aes(), 'decrypt')(aes_type,aes_mode, aes_zifuji, aes_iv, aes_encode, aes_key,aes_m_text)
        if result_text[0] == 'success':
            self.Ui_X.AES_Source.setPlainText(result_text[1])
        elif result_text[0] == 'error':
            QMessageBox.critical(self, 'Error', result_text[1])
        else:
            QMessageBox.information(self, 'INFO', result_text[1])
