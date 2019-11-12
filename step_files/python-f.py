import sys

from PySide2.QtSql import QSqlDatabase
from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog
from sqliteeditor import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.button_change_file.clicked.connect(self.get_file)
        self.db = None

    def get_file(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', "c://", "SQLite files (*.db)")
        self.connect_db(fname[0])

    def connect_db(self, fname):
        if fname.endswith(".db"):
            db = QSqlDatabase.addDatabase("QSQLITE")
            db.setDatabaseName(fname)
            db.open()
            self.ui.label_current_file.setText(fname)
            self.db = db
        else:
            self.ui.label_current_file.setText("Invalid File Selected")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())