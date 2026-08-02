"""
Findings page.
"""

from PySide6.QtCore import Qt

from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QComboBox,
    QLineEdit,
    QListWidget,
    QListWidgetItem,
    QTextEdit,
    QHBoxLayout,
    QVBoxLayout,
)

from redforge.services.finding_service import (
    FindingService,
)


class FindingsPage(QWidget):
    """
    Workspace page for managing findings.
    """

    def __init__(
        self,
        finding_service: FindingService,
        parent=None,
    ):
        super().__init__(parent)

        # ==================================================
        # Services
        # ==================================================

        self.finding_service = finding_service

        # ==================================================
        # Data
        # ==================================================

        self.engagement = None
        self.finding = None

        # ==================================================
        # Widgets
        # ==================================================

        self.new_finding_button = QPushButton(
            "New Finding"
        )

        self.delete_finding_button = QPushButton(
            "Delete"
        )

        self.findings_label = QLabel(
            "Findings"
        )

        self.findings_list = QListWidget()

        self.title_label = QLabel(
            "Title"
        )

        self.title_edit = QLineEdit()

        self.severity_label = QLabel(
            "Severity"
        )

        self.severity_combo = QComboBox()

        self.severity_combo.addItems(
            [
                "Critical",
                "High",
                "Medium",
                "Low",
                "Info",
            ]
        )

        self.status_label = QLabel(
            "Status"
        )

        self.status_combo = QComboBox()

        self.status_combo.addItems(
            [
                "Open",
                "Verified",
                "Reported",
                "Closed",
            ]
        )

        self.description_label = QLabel(
            "Description"
        )

        self.description_edit = QTextEdit()

        # ==================================================
        # Layouts
        # ==================================================

        button_layout = QHBoxLayout()

        button_layout.addWidget(
            self.new_finding_button
        )

        button_layout.addWidget(
            self.delete_finding_button
        )

        layout = QVBoxLayout(self)

        layout.addLayout(
            button_layout
        )

        layout.addWidget(
            self.findings_label
        )

        layout.addWidget(
            self.findings_list
        )

        layout.addWidget(
            self.title_label
        )

        layout.addWidget(
            self.title_edit
        )

        layout.addWidget(
            self.severity_label
        )

        layout.addWidget(
            self.severity_combo
        )

        layout.addWidget(
            self.status_label
        )

        layout.addWidget(
            self.status_combo
        )

        layout.addWidget(
            self.description_label
        )

        layout.addWidget(
            self.description_edit
        )

        # ==================================================
        # Signals
        # ==================================================

        self.new_finding_button.clicked.connect(
            self._create_finding
        )

        self.delete_finding_button.clicked.connect(
            self._delete_finding
        )

        self.findings_list.itemClicked.connect(
            self._select_finding
        )

        self.title_edit.textChanged.connect(
            self._save_finding
        )

        self.severity_combo.currentTextChanged.connect(
            self._save_finding
        )

        self.status_combo.currentTextChanged.connect(
            self._save_finding
        )

        self.description_edit.textChanged.connect(
            self._save_finding
        )

    # ==================================================
    # Public Methods
    # ==================================================

    def load_engagement(
        self,
        engagement,
    ):
        """
        Load the selected engagement.
        """

        self.engagement = engagement

        self.finding = None

        self.title_edit.clear()

        self.severity_combo.setCurrentText(
            "Info"
        )

        self.status_combo.setCurrentText(
            "Open"
        )

        self.description_edit.clear()

        self._load_findings()
        # ==================================================
    # Private Methods
    # ==================================================

    def _load_findings(
        self,
    ):
        """
        Load all findings.
        """

        self.findings_list.clear()

        if self.engagement is None:
            return

        findings = self.finding_service.get_findings(
            self.engagement.id
        )

        for finding in findings:

            item = QListWidgetItem(
                f"[{finding.severity}] {finding.title}"
            )

            item.setData(
                Qt.UserRole,
                finding.id,
            )

            self.findings_list.addItem(
                item
            )

    def _create_finding(
        self,
    ):
        """
        Create a new finding.
        """

        if self.engagement is None:
            return

        finding = self.finding_service.create_finding(
            self.engagement.id
        )

        self._load_findings()

        self._select_finding_by_id(
            finding.id
        )

    def _select_finding_by_id(
        self,
        finding_id: int,
    ):
        """
        Select a finding by its ID.
        """

        for index in range(
            self.findings_list.count()
        ):

            item = self.findings_list.item(
                index
            )

            if item.data(
                Qt.UserRole
            ) == finding_id:

                self.findings_list.setCurrentItem(
                    item
                )

                self._select_finding(
                    item
                )

                self.title_edit.setFocus()

                return

    def _select_finding(
        self,
        item: QListWidgetItem,
    ):
        """
        Load the selected finding.
        """

        finding_id = item.data(
            Qt.UserRole
        )

        self.finding = self.finding_service.get_finding(
            finding_id
        )

        if self.finding is None:
            return

        self.title_edit.blockSignals(True)
        self.severity_combo.blockSignals(True)
        self.status_combo.blockSignals(True)
        self.description_edit.blockSignals(True)

        self.title_edit.setText(
            self.finding.title
        )

        self.severity_combo.setCurrentText(
            self.finding.severity
        )

        self.status_combo.setCurrentText(
            self.finding.status
        )

        self.description_edit.setPlainText(
            self.finding.description
        )

        self.title_edit.blockSignals(False)
        self.severity_combo.blockSignals(False)
        self.status_combo.blockSignals(False)
        self.description_edit.blockSignals(False)

    def _save_finding(
        self,
    ):
        """
        Save the selected finding.
        """

        if self.finding is None:
            return

        title = self.title_edit.text().strip()

        severity = self.severity_combo.currentText().strip()

        status = self.status_combo.currentText().strip()

        description = self.description_edit.toPlainText().strip()

        if (
            title == self.finding.title
            and
            severity == self.finding.severity
            and
            status == self.finding.status
            and
            description == self.finding.description
        ):
            return

        self.finding_service.save_finding(
            finding=self.finding,
            title=title,
            severity=severity,
            status=status,
            description=description,
        )

        # Keep the in-memory object synchronized.

        self.finding.title = title
        self.finding.severity = severity
        self.finding.status = status
        self.finding.description = description

        item = self.findings_list.currentItem()

        if item is not None:

            item.setText(
                f"[{severity}] {title}"
            )

    def _delete_finding(
        self,
    ):
        """
        Delete the selected finding.
        """

        if self.finding is None:
            return

        self.finding_service.delete_finding(
            self.finding
        )

        self.finding = None

        self.title_edit.clear()

        self.severity_combo.setCurrentText(
            "Info"
        )

        self.status_combo.setCurrentText(
            "Open"
        )

        self.description_edit.clear()

        self._load_findings()