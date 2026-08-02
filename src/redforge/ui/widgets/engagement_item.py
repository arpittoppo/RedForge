from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
)


class EngagementItemWidget(QWidget):
    def __init__(
    self,
    program_name: str,
    platform: str,
    target: str,
    status: str,
    last_opened: str,
):
        super().__init__()