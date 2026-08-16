"""
Evidence page.
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
    QFileDialog,
    QHBoxLayout,
    QVBoxLayout,
)

from redforge.services.evidence_service import EvidenceService
from redforge.ui.styles.combo_fix import fix_combo


class EvidencePage(QWidget):
    """
    Workspace page for managing evidence.
    """

    def __init__(
        self,
        evidence_service: EvidenceService,
        parent=None,
    ):
        super().__init__(parent)

        self.evidence_service = evidence_service
        self.engagement = None
        self.evidence = None

        # ==================================================
        # Widgets
        # ==================================================

        self.new_evidence_button = QPushButton("+ New Evidence")
        self.new_evidence_button.setObjectName("primaryButton")

        self.delete_evidence_button = QPushButton("Delete")
        self.delete_evidence_button.setObjectName("dangerButton")

        self.evidence_label = QLabel("EVIDENCE")
        self.evidence_label.setObjectName("eyebrow")

        self.evidence_list = QListWidget()

        self.title_label = QLabel("Title")
        self.title_label.setObjectName("caption")

        self.title_edit = QLineEdit()

        self.type_label = QLabel("Type")
        self.type_label.setObjectName("caption")

        self.type_combo = QComboBox()
        self.type_combo.setEditable(True)
        self.type_combo.addItems(
            [
                "Screenshot",
                "Request",
                "Response",
                "HTML",
                "JavaScript",
                "JSON",
                "PDF",
                "Video",
                "Log",
                "Other",
            ]
        )

        # Visible button that opens the dropdown — needed because
        # setEditable(True) intercepts clicks on the combo body,
        # making the native arrow unclickable when it's invisible.
        self.type_dropdown_btn = QPushButton("▾")
        self.type_dropdown_btn.setObjectName("ghostButton")
        self.type_dropdown_btn.setFixedWidth(32)
        self.type_dropdown_btn.setToolTip("Show options")
        self.type_dropdown_btn.clicked.connect(self.type_combo.showPopup)

        self.path_label = QLabel("File Path")
        self.path_label.setObjectName("caption")

        self.path_edit = QLineEdit()
        self.path_edit.setObjectName("mono")

        self.browse_button = QPushButton("Browse")

        self.notes_label = QLabel("Notes")
        self.notes_label.setObjectName("caption")

        self.notes_edit = QTextEdit()

        # ==================================================
        # Layout
        # ==================================================

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.new_evidence_button)
        button_layout.addWidget(self.delete_evidence_button)
        button_layout.addStretch()

        type_layout = QHBoxLayout()
        type_layout.setSpacing(4)
        type_layout.addWidget(self.type_combo, stretch=1)
        type_layout.addWidget(self.type_dropdown_btn)

        path_layout = QHBoxLayout()
        path_layout.addWidget(self.path_edit)
        path_layout.addWidget(self.browse_button)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(32, 28, 32, 28)
        layout.setSpacing(10)

        layout.addLayout(button_layout)
        layout.addWidget(self.evidence_label)
        layout.addWidget(self.evidence_list)
        layout.addWidget(self.title_label)
        layout.addWidget(self.title_edit)
        layout.addWidget(self.type_label)
        layout.addLayout(type_layout)
        layout.addWidget(self.path_label)
        layout.addLayout(path_layout)
        layout.addWidget(self.notes_label)
        layout.addWidget(self.notes_edit)

        # ==================================================
        # Signals
        # ==================================================

        self.new_evidence_button.clicked.connect(self._create_evidence)
        self.delete_evidence_button.clicked.connect(self._delete_evidence)
        self.evidence_list.itemClicked.connect(self._select_evidence)
        self.title_edit.textChanged.connect(self._save_evidence)
        self.type_combo.currentTextChanged.connect(self._save_evidence)
        self.path_edit.textChanged.connect(self._save_evidence)
        self.notes_edit.textChanged.connect(self._save_evidence)
        self.browse_button.clicked.connect(self._browse_file)

        # ==================================================
        # Combo fix — after all widgets are built
        # ==================================================

        fix_combo(self.type_combo)

    # ==================================================
    # Public Methods
    # ==================================================

    def load_engagement(self, engagement):
        self.engagement = engagement
        self.evidence = None
        self.title_edit.clear()
        self.type_combo.setCurrentText("Other")
        self.path_edit.clear()
        self.notes_edit.clear()
        self._load_evidence()

    # ==================================================
    # Private Methods
    # ==================================================

    def _load_evidence(self):
        self.evidence_list.clear()
        if self.engagement is None:
            return
        evidence_items = self.evidence_service.get_evidence(self.engagement.id)
        for evidence in evidence_items:
            item = QListWidgetItem(
                f"[{evidence.evidence_type}]  {evidence.title}"
            )
            item.setData(Qt.UserRole, evidence.id)
            self.evidence_list.addItem(item)

    def _create_evidence(self):
        if self.engagement is None:
            return
        evidence = self.evidence_service.create_evidence(self.engagement.id)
        self._load_evidence()
        self._select_evidence_by_id(evidence.id)

    def _select_evidence_by_id(self, evidence_id: int):
        for index in range(self.evidence_list.count()):
            item = self.evidence_list.item(index)
            if item.data(Qt.UserRole) == evidence_id:
                self.evidence_list.setCurrentItem(item)
                self._select_evidence(item)
                self.title_edit.setFocus()
                return

    def _select_evidence(self, item: QListWidgetItem):
        evidence_id = item.data(Qt.UserRole)
        self.evidence = self.evidence_service.get_evidence_item(evidence_id)
        if self.evidence is None:
            return
        self.title_edit.blockSignals(True)
        self.type_combo.blockSignals(True)
        self.path_edit.blockSignals(True)
        self.notes_edit.blockSignals(True)
        self.title_edit.setText(self.evidence.title)
        self.type_combo.setCurrentText(self.evidence.evidence_type)
        self.path_edit.setText(self.evidence.file_path)
        self.notes_edit.setPlainText(self.evidence.notes)
        self.title_edit.blockSignals(False)
        self.type_combo.blockSignals(False)
        self.path_edit.blockSignals(False)
        self.notes_edit.blockSignals(False)

    def _save_evidence(self):
        if self.evidence is None:
            return
        title = self.title_edit.text().strip()
        evidence_type = self.type_combo.currentText().strip()
        file_path = self.path_edit.text().strip()
        notes = self.notes_edit.toPlainText().strip()
        self.evidence_service.save_evidence(
            evidence=self.evidence,
            title=title,
            evidence_type=evidence_type,
            file_path=file_path,
            notes=notes,
        )
        self.evidence.title = title
        self.evidence.evidence_type = evidence_type
        self.evidence.file_path = file_path
        self.evidence.notes = notes
        item = self.evidence_list.currentItem()
        if item is not None:
            item.setText(f"[{evidence_type}]  {title}")

    def _delete_evidence(self):
        if self.evidence is None:
            return
        self.evidence_service.delete_evidence(self.evidence)
        self.evidence = None
        self._load_evidence()
        if self.evidence_list.count() > 0:
            item = self.evidence_list.item(0)
            self.evidence_list.setCurrentItem(item)
            self._select_evidence(item)
        else:
            self.title_edit.clear()
            self.type_combo.setCurrentText("Other")
            self.path_edit.clear()
            self.notes_edit.clear()

    def _browse_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select Evidence",
        )
        if not file_path:
            return
        self.path_edit.setText(file_path)