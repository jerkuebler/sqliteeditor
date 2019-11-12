import sys

from PySide2.QtSql import QSqlDatabase, QSqlTableModel
from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog
from sqliteeditor import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.button_change_file.clicked.connect(self.get_file)
        self.db = None
        self.model = None
        self.tables = None

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
            self.tables = self.db.tables()
            self.populate_combo()
            self.show_table()
        else:
            self.ui.label_current_file.setText("Invalid File Selected")

    def populate_combo(self):
        self.ui.combo_table_select.clear()
        self.ui.combo_table_select.addItems(self.tables)
        self.ui.combo_table_select.activated.connect(self.update_table)

    def show_table(self):
        self.model = QSqlTableModel(db=self.db)
        self.ui.table_view.setModel(self.model)
        self.ui.table_view.show()

    def update_table(self, table):
        self.model.setTable(self.tables[table])
        self.model.select()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
