"""
Reports page.
"""

from PySide6.QtCore import Qt

from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QLineEdit,
    QListWidget,
    QListWidgetItem,
    QTextEdit,
    QHBoxLayout,
    QVBoxLayout,
)

from redforge.services.report_service import (
    ReportService,
)


class ReportsPage(QWidget):
    """
    Workspace page for managing reports.
    """

    def __init__(
        self,
        report_service: ReportService,
        parent=None,
    ):
        super().__init__(parent)

        # ==================================================
        # Services
        # ==================================================

        self.report_service = report_service

        # ==================================================
        # Data
        # ==================================================

        self.engagement = None
        self.report = None

        # ==================================================
        # Widgets
        # ==================================================

        self.new_report_button = QPushButton(
            "New Report"
        )

        self.delete_report_button = QPushButton(
            "Delete"
        )

        self.reports_label = QLabel(
            "Reports"
        )

        self.reports_list = QListWidget()

        self.title_label = QLabel(
            "Title"
        )

        self.title_edit = QLineEdit()

        self.content_label = QLabel(
            "Content"
        )

        self.content_edit = QTextEdit()

        # ==================================================
        # Layouts
        # ==================================================

        button_layout = QHBoxLayout()

        button_layout.addWidget(
            self.new_report_button
        )

        button_layout.addWidget(
            self.delete_report_button
        )

        layout = QVBoxLayout(self)

        layout.addLayout(
            button_layout
        )

        layout.addWidget(
            self.reports_label
        )

        layout.addWidget(
            self.reports_list
        )

        layout.addWidget(
            self.title_label
        )

        layout.addWidget(
            self.title_edit
        )

        layout.addWidget(
            self.content_label
        )

        layout.addWidget(
            self.content_edit
        )

        # ==================================================
        # Signals
        # ==================================================

        self.new_report_button.clicked.connect(
            self._create_report
        )

        self.delete_report_button.clicked.connect(
            self._delete_report
        )

        self.reports_list.itemClicked.connect(
            self._select_report
        )

        self.title_edit.textChanged.connect(
            self._save_report
        )

        self.content_edit.textChanged.connect(
            self._save_report
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

        self.report = None

        self.title_edit.clear()

        self.content_edit.clear()

        self._load_reports()

    def _load_reports(
        self,
    ):
        """
        Load all reports.
        """

        self.reports_list.clear()

        if self.engagement is None:
            return

        reports = self.report_service.get_reports(
            self.engagement.id
        )

        for report in reports:

            item = QListWidgetItem(
                report.title or "Untitled Report"
            )

            item.setData(
                Qt.UserRole,
                report.id,
            )

            self.reports_list.addItem(
                item
            )  
    def _create_report(
        self,
    ):
        """
        Create a new report.
        """

        if self.engagement is None:
            return

        report = self.report_service.create_report(
            self.engagement.id
        )

        self._load_reports()

        self._select_report_by_id(
            report.id
        )

    def _select_report_by_id(
        self,
        report_id: int,
    ):
        """
        Select a report by its ID.
        """

        for index in range(
            self.reports_list.count()
        ):

            item = self.reports_list.item(
                index
            )

            if item.data(
                Qt.UserRole
            ) == report_id:

                self.reports_list.setCurrentItem(
                    item
                )

                self._select_report(
                    item
                )

                self.title_edit.setFocus()

                return

    def _select_report(
        self,
        item: QListWidgetItem,
    ):
        """
        Load the selected report.
        """

        report_id = item.data(
            Qt.UserRole
        )

        self.report = self.report_service.get_report(
            report_id
        )

        if self.report is None:
            return

        self.title_edit.blockSignals(True)
        self.content_edit.blockSignals(True)

        self.title_edit.setText(
            self.report.title
        )

        self.content_edit.setPlainText(
            self.report.content
        )

        self.title_edit.blockSignals(False)
        self.content_edit.blockSignals(False)

    def _save_report(
        self,
    ):
        """
        Save the selected report.
        """

        if self.report is None:
            return

        title = self.title_edit.text().strip()

        content = self.content_edit.toPlainText().strip()

        if (
            title == self.report.title
            and
            content == self.report.content
        ):
            return

        self.report_service.save_report(
            report=self.report,
            title=title,
            content=content,
        )

        self.report.title = title
        self.report.content = content

        item = self.reports_list.currentItem()

        if item is not None:

            item.setText(
                title or "Untitled Report"
            )

    def _delete_report(
        self,
    ):
        """
        Delete the selected report.
        """

        if self.report is None:
            return

        self.report_service.delete_report(
            self.report
        )

        self.report = None

        self.reports_list.clearSelection()

        self.title_edit.clear()

        self.content_edit.clear()

        self._load_reports()                                 