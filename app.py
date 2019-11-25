import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt5.QtGui import QCursor
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtWebEngineWidgets import QWebEngineView

class MyApp(QWidget):

	def __init__(self):
		super().__init__()
		QApplication.setOverrideCursor(QCursor(Qt.WaitCursor))
		self.initUI()

	def closeEvent(self, event):

		msg_box = QMessageBox()
		msg_box.setIcon(QMessageBox.Warning)
		msg_box.setWindowTitle("Alert")
		msg_box.setText("Are you sure you want to exit the program?")
		# msg_box.setWindowIcon(QIcon("resources/icons/xray.ico"))
		msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

		retval = msg_box.exec_()

		if retval == QMessageBox.Yes:
			event.accept()
		else:
			event.ignore()

	def initUI(self):

		self.web = QWebEngineView()
		self.web.setWindowTitle("Trello")
		# self.web.setWindowIcon(QIcon("resources/icons/xray.ico"))
		self.web.load(QUrl("https://trello.com/"))
		self.web.showMaximized()
		self.web.setContextMenuPolicy(Qt.NoContextMenu)
		self.web.show()
		self.web.loadFinished.connect(self.webpageLoaded)

		self.web.closeEvent = self.closeEvent

	def webpageLoaded(self):
		QApplication.restoreOverrideCursor()

if __name__ == '__main__':
	
	app = QApplication(sys.argv)
	my_app = MyApp()
	sys.exit(app.exec_())