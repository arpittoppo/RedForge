from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QLineEdit,
    QTextEdit,
    QComboBox,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
)


class NewEngagementPage(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        title = QLabel("New Engagement")

        self.program_name = QLineEdit()
        self.program_name.setPlaceholderText("Enter program name...")

        self.platform = QComboBox()
        self.platform.addItems([
            "HackerOne",
            "Bugcrowd",
            "Intigriti",
            "comolho",
            "BugBase",
            "Direct Client",
            "Internal Pentest",
            "Other",
        ])

        self.engagement_type = QComboBox()
        self.engagement_type.addItems([
            "Bug Bounty",
            "VDP",
            "External Pentest",
            "Internal Pentest",
            "Red Team",
            "Lab",
        ])

        self.description = QTextEdit()
        self.description.setPlaceholderText(
            "Describe this engagement..."
        )

        button_layout = QHBoxLayout()

        self.cancel_button = QPushButton("Cancel")
        self.save_button = QPushButton("Save")

        button_layout.addStretch()
        button_layout.addWidget(self.cancel_button)
        button_layout.addWidget(self.save_button)

        layout.addWidget(title)

        layout.addWidget(QLabel("Program Name"))
        layout.addWidget(self.program_name)

        layout.addWidget(QLabel("Platform"))
        layout.addWidget(self.platform)

        layout.addWidget(QLabel("Engagement Type"))
        layout.addWidget(self.engagement_type)

        layout.addWidget(QLabel("Description"))
        layout.addWidget(self.description)

        layout.addStretch()

        layout.addLayout(button_layout)