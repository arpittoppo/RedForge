"""
Main window for RedForge.
"""

from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
)

from redforge.ui.widgets.content_area import ContentArea
from redforge.ui.widgets.sidebar import Sidebar
from redforge.ui.widgets.status_bar import StatusBar
from redforge.ui.widgets.top_bar import TopBar


class MainWindow(QMainWindow):
    """
    Main application window.
    """

    def __init__(self):
        super().__init__()

        self.setWindowTitle("RedForge")
        self.resize(1400, 900)

        self.sidebar = Sidebar()
        self.sidebar.navigation_requested.connect(self._navigate_to_page)

        self.top_bar = TopBar()
        self.content_area = ContentArea()
        self.status_bar = StatusBar()

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.main_layout = QVBoxLayout()
        self.workspace_layout = QHBoxLayout()

        self.workspace_layout.addWidget(self.sidebar)
        self.workspace_layout.addWidget(self.content_area)

        self.main_layout.addWidget(self.top_bar)
        self.main_layout.addLayout(self.workspace_layout)
        self.main_layout.addWidget(self.status_bar)

        self.central_widget.setLayout(self.main_layout)

    def _navigate_to_page(self, page_id):
        """
        Navigate to the requested page.
        """

        print(page_id)