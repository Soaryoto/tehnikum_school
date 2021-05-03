from PySide2 import QtWidgets
from PySide2.QtWidgets import QLabel
from PySide2.QtGui import QPixmap
import sys
from ui import Ui_Form

app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
ui = Ui_Form()
ui.setupUi(Form)
Form.show()

# QListWidgetItem *item = new QListWidgetItem(textEdit->toPlainText());
# listWidget->addItem(item);
# textEdit->clear();


# Масштабирование картинки бо блоку label
pixmap = QPixmap("img.jpg")
pixmap = pixmap.scaledToWidth(ui.label.width())
pixmap = pixmap.scaledToHeight(ui.label.height())
ui.label.setPixmap(pixmap)

sys.exit(app.exec_())