"""
Settings page for RedForge.
"""

from PySide6.QtCore import Signal

from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QComboBox,
    QVBoxLayout,
)


class SettingsPage(QWidget):
    """
    Application settings page.
    """

    font_scale_changed = Signal(float)

    def __init__(
        self,
        parent=None,
    ):
        super().__init__(parent)

        # ==================================================
        # Build UI
        # ==================================================

        self._build_ui()

    # ==================================================
    # UI
    # ==================================================

    def _build_ui(self):
        """
        Build the settings UI.
        """

        # ==================================================
        # Main Layout
        # ==================================================

        self.main_layout = QVBoxLayout(
            self
        )

        self.main_layout.setContentsMargins(
            32,
            28,
            32,
            28,
        )

        self.main_layout.setSpacing(
            12
        )

        # ==================================================
        # Page Header
        # ==================================================

        self.title_label = QLabel(
            "Settings"
        )

        self.title_label.setObjectName(
            "pageTitle"
        )

        self.subtitle_label = QLabel(
            "Workspace preferences and configuration."
        )

        self.subtitle_label.setObjectName(
            "caption"
        )

        self.main_layout.addWidget(
            self.title_label
        )

        self.main_layout.addWidget(
            self.subtitle_label
        )

        # ==================================================
        # Appearance
        # ==================================================

        self.appearance_label = QLabel(
            "Appearance"
        )

        self.appearance_label.setObjectName(
            "eyebrow"
        )

        self.main_layout.addSpacing(
            16
        )

        self.main_layout.addWidget(
            self.appearance_label
        )

        # ==================================================
        # Font Size
        # ==================================================

        self.font_size_label = QLabel(
            "Font Size"
        )

        self.font_size_label.setObjectName(
            "caption"
        )

        self.font_size_combo = QComboBox()

        self.font_size_combo.addItems(
            [
                "Small (90%)",
                "Default (100%)",
                "Large (115%)",
                "Extra Large (130%)",
            ]
        )

        self.font_size_combo.setCurrentText(
            "Default (100%)"
        )

        self.main_layout.addWidget(
            self.font_size_label
        )

        self.main_layout.addWidget(
            self.font_size_combo
        )

        # ==================================================
        # Font Size Description
        # ==================================================

        self.font_size_description = QLabel(
            "Adjust the interface text size to improve readability."
        )

        self.font_size_description.setObjectName(
            "caption"
        )

        self.font_size_description.setWordWrap(
            True
        )

        self.main_layout.addWidget(
            self.font_size_description
        )

        # ==================================================
        # Signals
        # ==================================================

        self.font_size_combo.currentIndexChanged.connect(
            self._font_size_changed
        )

        # ==================================================
        # Stretch
        # ==================================================

        self.main_layout.addStretch()

    # ==================================================
    # Private Methods
    # ==================================================

    def _font_size_changed(
        self,
        index: int,
    ):
        """
        Emit the selected font scale.
        """

        scales = [
            0.90,
            1.00,
            1.15,
            1.30,
        ]

        self.font_scale_changed.emit(
            scales[index]
        )