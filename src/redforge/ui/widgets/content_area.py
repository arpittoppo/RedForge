from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QStackedWidget,
)

from redforge.ui.pages.home_dashboard_page import HomeDashboardPage


class ContentArea(QWidget):

    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()
        self.stack = QStackedWidget()

        self.layout.addWidget(self.stack)
        self.setLayout(self.layout)