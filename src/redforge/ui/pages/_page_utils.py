"""
Shared layout helpers for RedForge workspace pages.
"""

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QSplitter,
    QVBoxLayout,
    QWidget,
)


def make_page_header(title: str) -> tuple[QLabel, QVBoxLayout, QWidget]:
    """
    Return (title_label, content_layout, root_widget) for a standard page.
    """
    root = QWidget()
    layout = QVBoxLayout(root)
    layout.setContentsMargins(0, 0, 0, 0)
    layout.setSpacing(0)

    title_label = QLabel(title)
    title_label.setObjectName("PageTitle")

    return title_label, layout, root


def section_label(text: str) -> QLabel:
    lbl = QLabel(text.upper())
    lbl.setObjectName("SectionLabel")
    return lbl


def hline() -> QFrame:
    f = QFrame()
    f.setFrameShape(QFrame.Shape.HLine)
    return f


def action_button(text: str, primary: bool = False, danger: bool = False) -> QPushButton:
    btn = QPushButton(text)
    if primary:
        btn.setObjectName("PrimaryButton")
    elif danger:
        btn.setObjectName("DangerButton")
    btn.setCursor(Qt.CursorShape.PointingHandCursor)
    btn.setFixedHeight(30)
    return btn
