from PySide6.QtWidgets import (
    QComboBox,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QLineEdit,
    QMessageBox,
    QTextEdit,
    QVBoxLayout,
)


class NewEngagementDialog(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("New Engagement")
        self.setMinimumWidth(500)

        self._build_ui()
        self._connect_signals()

    # ------------------------------------------------------------------
    # UI
    # ------------------------------------------------------------------

    def _build_ui(self):

        main_layout = QVBoxLayout(self)

        form_layout = QFormLayout()

        # Program Name
        self.program_name_input = QLineEdit()
        self.program_name_input.setPlaceholderText(
            "e.g. Acme Bug Bounty"
        )

        # Platform
        self.platform_input = QComboBox()
        self.platform_input.addItems(
            [
                "HackerOne",
                "Bugcrowd",
                "Intigriti",
                "Comolho",
                "YesWeHack",
                "Private",
                "Internal",
                "other",
            ]
        )

        # Engagement Type
        self.engagement_type_input = QComboBox()
        self.engagement_type_input.addItems(
            [
                "Bug Bounty",
                "VDP",
                "External Pentest",
                "Internal Pentest",
                "Red Team Exercise",
                "Personal Lab",
            ]
        )

        # Description
        self.description_input = QTextEdit()
        self.description_input.setPlaceholderText(
            "Describe this engagement..."
        )
        self.description_input.setFixedHeight(120)

        form_layout.addRow(
            "Program Name:",
            self.program_name_input,
        )

        form_layout.addRow(
            "Platform:",
            self.platform_input,
        )

        form_layout.addRow(
            "Engagement Type:",
            self.engagement_type_input,
        )

        form_layout.addRow(
            "Description:",
            self.description_input,
        )

        main_layout.addLayout(form_layout)

        self.button_box = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Cancel
            | QDialogButtonBox.StandardButton.Ok
        )

        self.button_box.button(
            QDialogButtonBox.StandardButton.Ok
        ).setText("Create")

        main_layout.addWidget(self.button_box)

    # ------------------------------------------------------------------
    # Signals
    # ------------------------------------------------------------------

    def _connect_signals(self):

        self.button_box.accepted.connect(self._validate)
        self.button_box.rejected.connect(self.reject)

    # ------------------------------------------------------------------
    # Validation
    # ------------------------------------------------------------------

    def _validate(self):

        if not self.program_name_input.text().strip():

            QMessageBox.warning(
                self,
                "Validation Error",
                "Program Name cannot be empty.",
            )
            return

        self.accept()

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def get_data(self) -> dict:

        return {
            "program_name": self.program_name_input.text().strip(),
            "platform": self.platform_input.currentText(),
            "engagement_type": self.engagement_type_input.currentText(),
            "description": self.description_input.toPlainText().strip(),
        }