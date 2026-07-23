"""
Top bar widget for RedForge.
"""

from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QHBoxLayout
from PySide6.QtWidgets import QWidget


class TopBar(QWidget):

    def __init__(self):
        super().__init__()

        layout = QHBoxLayout()

        title = QLabel("RedForge")

        layout.addWidget(title)

        self.setLayout(layout)