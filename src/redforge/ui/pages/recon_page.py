"""
Recon page.
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
    QVBoxLayout,
    QHBoxLayout,
)

from redforge.services.recon_service import ReconService
from redforge.ui.styles.combo_fix import fix_combo


class ReconPage(QWidget):
    """
    Workspace page for managing recon entries.
    """

    def __init__(
        self,
        recon_service: ReconService,
        parent=None,
    ):
        super().__init__(parent)

        self.recon_service = recon_service
        self.engagement = None
        self.recon = None

        # ==================================================
        # Widgets
        # ==================================================

        self.new_entry_button = QPushButton("+ New Entry")
        self.new_entry_button.setObjectName("primaryButton")

        self.delete_entry_button = QPushButton("Delete")
        self.delete_entry_button.setObjectName("dangerButton")

        self.recon_entries_label = QLabel("RECON ENTRIES")
        self.recon_entries_label.setObjectName("eyebrow")

        self.recon_list = QListWidget()

        self.type_label = QLabel("Type")
        self.type_label.setObjectName("caption")

        self.type_combo = QComboBox()
        self.type_combo.setEditable(True)
        self.type_combo.addItems(
            [
                "Subdomain",
                "URL",
                "JS File",
                "API",
                "GraphQL",
                "Directory",
                "Parameter",
                "Technology",
                "IP Address",
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

        self.target_label = QLabel("Target")
        self.target_label.setObjectName("caption")

        self.target_edit = QLineEdit()
        self.target_edit.setObjectName("mono")
        self.target_edit.setPlaceholderText("e.g. api.acme.com")

        # ==================================================
        # Layout
        # ==================================================

        layout = QVBoxLayout(self)
        layout.setContentsMargins(32, 28, 32, 28)
        layout.setSpacing(10)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.new_entry_button)
        button_layout.addWidget(self.delete_entry_button)
        button_layout.addStretch()

        type_layout = QHBoxLayout()
        type_layout.setSpacing(4)
        type_layout.addWidget(self.type_combo, stretch=1)
        type_layout.addWidget(self.type_dropdown_btn)

        layout.addLayout(button_layout)
        layout.addWidget(self.recon_entries_label)
        layout.addWidget(self.recon_list)
        layout.addWidget(self.type_label)
        layout.addLayout(type_layout)
        layout.addWidget(self.target_label)
        layout.addWidget(self.target_edit)

        # ==================================================
        # Signals
        # ==================================================

        self.new_entry_button.clicked.connect(self._create_recon)
        self.delete_entry_button.clicked.connect(self._delete_recon)
        self.recon_list.itemClicked.connect(self._select_recon)
        self.type_combo.currentTextChanged.connect(self._save_recon)
        self.target_edit.textChanged.connect(self._save_recon)

        # ==================================================
        # Combo fix — after all widgets are built
        # ==================================================

        fix_combo(self.type_combo)

    # ==================================================
    # Public Methods
    # ==================================================

    def load_engagement(self, engagement):
        self.engagement = engagement
        self.recon = None
        self.type_combo.setCurrentText("Other")
        self.target_edit.clear()
        self._load_recons()

    # ==================================================
    # Private Methods
    # ==================================================

    def _load_recons(self):
        self.recon_list.clear()
        if self.engagement is None:
            return
        recons = self.recon_service.get_recons(self.engagement.id)
        for recon in recons:
            item = QListWidgetItem(f"[{recon.recon_type}]  {recon.value}")
            item.setData(Qt.UserRole, recon.id)
            self.recon_list.addItem(item)

    def _create_recon(self):
        if self.engagement is None:
            return
        recon = self.recon_service.create_recon(self.engagement.id)
        self._load_recons()
        self._select_recon_by_id(recon.id)

    def _delete_recon(self):
        if self.recon is None:
            return
        self.recon_service.delete_recon(self.recon)
        self.recon = None
        self._load_recons()
        if self.recon_list.count() > 0:
            item = self.recon_list.item(0)
            self.recon_list.setCurrentItem(item)
            self._select_recon(item)
        else:
            self.type_combo.blockSignals(True)
            self.target_edit.blockSignals(True)
            self.type_combo.setCurrentText("Other")
            self.target_edit.clear()
            self.type_combo.blockSignals(False)
            self.target_edit.blockSignals(False)

    def _select_recon_by_id(self, recon_id: int):
        for index in range(self.recon_list.count()):
            item = self.recon_list.item(index)
            if item.data(Qt.UserRole) == recon_id:
                self.recon_list.setCurrentItem(item)
                self._select_recon(item)
                self.target_edit.setFocus()
                return

    def _select_recon(self, item: QListWidgetItem):
        recon_id = item.data(Qt.UserRole)
        self.recon = self.recon_service.get_recon(recon_id)
        if self.recon is None:
            return
        self.type_combo.blockSignals(True)
        self.target_edit.blockSignals(True)
        self.type_combo.setCurrentText(self.recon.recon_type)
        self.target_edit.setText(self.recon.value)
        self.type_combo.blockSignals(False)
        self.target_edit.blockSignals(False)

    def _save_recon(self):
        if self.recon is None:
            return
        recon_type = self.type_combo.currentText().strip()
        value = self.target_edit.text().strip()
        if recon_type == self.recon.recon_type and value == self.recon.value:
            return
        self.recon_service.save_recon(
            recon=self.recon,
            recon_type=recon_type,
            value=value,
        )
        self.recon.recon_type = recon_type
        self.recon.value = value
        item = self.recon_list.currentItem()
        if item is not None:
            item.setText(f"[{recon_type}]  {value}")