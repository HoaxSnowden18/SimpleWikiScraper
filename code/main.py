from PyQt5 import QtCore, QtGui, QtWidgets
import wikipediaapi as wikiapi
from PyQt5.QtWidgets import QMessageBox

def getFullArticle(artname):
    wiki = wikiapi.Wikipedia(language='en', extract_format=wikiapi.ExtractFormat.HTML)
    article = wiki.page(artname)
    return article.text

def getSummaryArt(artname):
    wiki = wikiapi.Wikipedia(language='en', extract_format=wikiapi.ExtractFormat.WIKI)
    article = wiki.page(artname)
    return article.summary

def checkArticle(artname):
    wiki = wikiapi.Wikipedia(language='en', extract_format=wikiapi.ExtractFormat.WIKI)
    article = wiki.page(artname)
    return article.exists()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(505, 674)
        MainWindow.setMinimumSize(QtCore.QSize(505, 674))
        MainWindow.setMaximumSize(QtCore.QSize(505, 674))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QMainWindow{\n"
"    background: #3F3C78\n"
"}\n"
"\n"
"QFrame#mainFrame{\n"
"    background: rgba(0,0,0,150);\n"
"    border-radius: 20px;\n"
"}\n"
"\n"
"QLabel#mainTitle{\n"
"    color:white;\n"
"}\n"
"\n"
"QPushButton{\n"
"    border: none;\n"
"    background: transparent;\n"
"    color: white;\n"
"    border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(100,100,255);\n"
"}\n"
"\n"
"QLineEdit#searchQuery{\n"
"    background: transparent;\n"
"    border: none;\n"
"    color: white;\n"
"    border-bottom: 1px solid gray;\n"
"}\n"
"\n"
"QLineEdit#searchQuery:hover{\n"
"    border-bottom: 1px solid rgb(100,100,255);\n"
"}\n"
"\n"
"QTextEdit{\n"
"    background: rgba(100,100,255,100);\n"
"    border: none;\n"
"    border-radius: 25px;\n"
"    color:white;\n"
"    padding: 7px;\n"
"}\n"
"\n"
"QScrollBar:vertical{\n"
"    border: 1px solid rgb(100,100,255);\n"
"    background: transparent;\n"
"    width: 12px;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mainFrame = QtWidgets.QFrame(self.centralwidget)
        self.mainFrame.setGeometry(QtCore.QRect(20, 20, 461, 641))
        self.mainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainFrame.setObjectName("mainFrame")
        self.mainTitle = QtWidgets.QLabel(self.mainFrame)
        self.mainTitle.setGeometry(QtCore.QRect(0, 20, 461, 51))
        font = QtGui.QFont()
        font.setFamily("Imprint MT Shadow")
        font.setPointSize(28)
        font.setBold(False)
        font.setWeight(50)
        self.mainTitle.setFont(font)
        self.mainTitle.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.mainTitle.setLineWidth(1)
        self.mainTitle.setTextFormat(QtCore.Qt.AutoText)
        self.mainTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.mainTitle.setWordWrap(True)
        self.mainTitle.setObjectName("mainTitle")
        self.searchQuery = QtWidgets.QLineEdit(self.mainFrame)
        self.searchQuery.setGeometry(QtCore.QRect(30, 90, 401, 41))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        font.setPointSize(14)
        font.setKerning(False)
        self.searchQuery.setFont(font)
        self.searchQuery.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.searchQuery.setText("")
        self.searchQuery.setDragEnabled(False)
        self.searchQuery.setObjectName("searchQuery")
        self.summaryButton = QtWidgets.QPushButton(self.mainFrame)
        self.summaryButton.setGeometry(QtCore.QRect(80, 140, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        font.setPointSize(14)
        self.summaryButton.setFont(font)
        self.summaryButton.setObjectName("summaryButton")
        self.wikiContent = QtWidgets.QTextEdit(self.mainFrame)
        self.wikiContent.setGeometry(QtCore.QRect(30, 190, 401, 431))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        font.setPointSize(12)
        self.wikiContent.setFont(font)
        self.wikiContent.setReadOnly(True)
        self.wikiContent.setObjectName("wikiContent")
        self.fulltextButton = QtWidgets.QPushButton(self.mainFrame)
        self.fulltextButton.setGeometry(QtCore.QRect(260, 140, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        font.setPointSize(14)
        self.fulltextButton.setFont(font)
        self.fulltextButton.setObjectName("fulltextButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.summaryButton.clicked.connect(self.getSummary)
        self.fulltextButton.clicked.connect(self.getFull)
        
    def getSummary(self):
        artname = self.searchQuery.text()
        article = getSummaryArt(artname)
        if checkArticle(artname):
            self.wikiContent.setHtml(f"{article}")
            self.searchQuery.setText = ""
        else:
            self.showError()

    def getFull(self):
        artname = self.searchQuery.text()
        article = getFullArticle(artname)
        if checkArticle(artname):
            self.wikiContent.setHtml(f"{article}")
            self.searchQuery.setText = ""
        else:
            self.showError()

    def showError(self):
        msg = QMessageBox()
        msg.setWindowTitle("Search Error")
        msg.setText("Article doesn't exists in the database")
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowIcon(QtGui.QIcon('images/icon.png'))
        x = msg.exec_()
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.mainTitle.setText(_translate("MainWindow", "Wikipedia Searcher"))
        self.searchQuery.setPlaceholderText(_translate("MainWindow", "Search for articles"))
        self.summaryButton.setText(_translate("MainWindow", "Summary"))
        self.wikiContent.setHtml(_translate("MainWindow", ""))
        self.fulltextButton.setText(_translate("MainWindow", "Full Text"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
