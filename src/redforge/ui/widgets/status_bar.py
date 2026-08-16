"""
Status bar widget for RedForge.
"""

from PySide6.QtWidgets import QLabel, QHBoxLayout, QWidget

from redforge.ui.styles.tokens import STATUSBAR_HEIGHT


class StatusBar(QWidget):

    def __init__(self):
        super().__init__()

        self.setObjectName("statusBar")
        self.setFixedHeight(STATUSBAR_HEIGHT)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(16, 0, 16, 0)

        self.status_label = QLabel("Ready")
        self.status_label.setObjectName("statusText")

        layout.addWidget(self.status_label)
        layout.addStretch()

        self.version_label = QLabel("RedForge")
        self.version_label.setObjectName("statusText")
        layout.addWidget(self.version_label)

    def set_status(self, text: str):
        self.status_label.setText(text)
