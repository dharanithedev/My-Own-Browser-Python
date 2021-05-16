# Imports
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

# Main Class
class MyBrowser(QMainWindow):
    def __init__(self):
        super(MyBrowser, self).__init__()
        # Will give us we view
        self.browser = QWebEngineView()

        # Set initial URL
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # Navbar setup
        navigation = QToolBar()
        self.addToolBar(navigation)

        # Going Home
        home_btn = QAction('Home', self)
        home_btn.triggered.connect(self.go_home)
        navigation.addAction(home_btn)

        # Going Back
        backward_btn = QAction('<', self)
        backward_btn.triggered.connect(self.browser.back)
        navigation.addAction(backward_btn)

        # Proceeding Forward
        forward_btn = QAction('>', self)
        forward_btn.triggered.connect(self.browser.forward)
        navigation.addAction(forward_btn)

        reload_btn = QAction('Reload', self)
        reload_btn.triggered.connect(self.browser.reload)
        navigation.addAction(reload_btn)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.go_to_url)
        navigation.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.switch_url)

    def go_home(self):
        self.browser.setUrl(QUrl('https://www.linkedin.com/in/dharanitharan-murugan-264b11165/'))

    def go_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def switch_url(self, q):
        self.url_bar.setText(q.toString())


app = QApplication(sys.argv)
QApplication.setApplicationName('Dharanitharan')
window = MyBrowser()
app.exec_()