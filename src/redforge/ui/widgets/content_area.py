from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QStackedWidget,
)
from redforge.ui.pages.dashboard_page import DashboardPage

class ContentArea(QWidget):

    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()
        self.stack = QStackedWidget()

        self.layout.addWidget(self.stack)
        self.setLayout(self.layout)
        self.dashboard_page = DashboardPage()
        self.stack.addWidget(self.dashboard_page)