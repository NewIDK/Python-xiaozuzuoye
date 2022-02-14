from pythonProject2.main_window impoet MainUi_From
from pythonProject2.hello import Ui-Form

class Main(QMainWindow,MainUi_Form):
    def __init__(self):
        super(Main,self).__init__()
class Main_login(QWidget,Ui_Form):
    lists = []
    def __init__(self):
        super(Main, self).__init__()

if __name__ = '__main__':
    app = QApplication(sys.argv)
    main_login = Main_Login()
    main_login.show()
    sys.xit(app.exec())

main = Main()
main.show()
self.close()