"""
Status bar widget for RedForge.
"""

from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QHBoxLayout
from PySide6.QtWidgets import QWidget


class StatusBar(QWidget):

    def __init__(self):
        super().__init__()

        layout = QHBoxLayout()

        status = QLabel("Ready")

        layout.addWidget(status)

        self.setLayout(layout)