from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QComboBox, QListView, QWidget


def fix_combo(combo: QComboBox) -> None:
    """
    Replace the native popup with a QListView so Qt stylesheet rules
    apply correctly. The native popup ignores background-color on
    QAbstractItemView when a global QWidget rule is present.
    """
    view = QListView()
    view.setStyleSheet("""
        QListView {
            background-color: #2B2B31;
            color: #E4E4E8;
            border: 1px solid #4A4A50;
            border-radius: 0px;
            padding: 4px;
            outline: none;
        }

        QListView::item {
            min-height: 34px;
            padding: 6px 14px;
            color: #E4E4E8;
            background-color: #2B2B31;
            border: none;
        }

        QListView::item:hover {
            background-color: #35353B;
            color: #E4E4E8;
        }

        QListView::item:selected {
            background-color: #2A2A3A;
            color: #E4E4E8;
            border-left: 3px solid #6C6CF0;
        }
    """)
    combo.setView(view)

    # Prevent the popup from going behind the window on some platforms
    combo.view().window().setWindowFlags(
        Qt.WindowType.Popup |
        Qt.WindowType.FramelessWindowHint |
        Qt.WindowType.NoDropShadowWindowHint
    )


def fix_all_combos(root: QWidget) -> None:
    """Call this after your UI is built to patch every QComboBox in the tree."""
    for combo in root.findChildren(QComboBox):
        fix_combo(combo)