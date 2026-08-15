from __future__ import annotations

from PySide6.QtWidgets import QApplication

from redforge.ui.styles.tokens import (
    Color,
    Font,
    Radius,
    Space,
)


def build_stylesheet(font_scale: float = 1.0) -> str:
    c = Color
    f = Font
    r = Radius
    s = Space

    def font_size(size: int) -> int:
        return max(1, round(size * font_scale))

    return f"""

/* ==========================================================
   GLOBAL
   ========================================================== */

/* ----------------------------------------------------------
   DO NOT set background-color on QWidget globally.
   Doing so bleeds into every child widget inside dialogs,
   sidebars, and panels — producing the black-strip effect
   on label cells and title rows.

   Instead: set background only on the root window containers
   (QMainWindow, QDialog) and let everything else be
   transparent by default, inheriting from its painted parent.
   ---------------------------------------------------------- */

QWidget {{
    color: {c.TEXT_PRIMARY};
    font-family: {f.UI_FAMILY};
    font-size: {font_size(f.SIZE_MD)}px;
    selection-background-color: {c.SIGNAL_MUTED};
    selection-color: {c.TEXT_PRIMARY};
}}

/* Root containers get the window background */
QMainWindow {{
    background: {c.WINDOW};
}}

/* Dialogs get a lifted surface so the form grid is visible */
QDialog {{
    background: #2B2B31;
}}

/* All labels inside dialogs must be transparent so they show
   the dialog surface behind them, not the QWidget default black */
QDialog QLabel {{
    background: transparent;
}}

/* General-purpose panels/frames that aren't explicitly styled
   should also be transparent — they paint over their parent */
QFrame {{
    background: transparent;
}}

QToolTip {{
    background: #2B2B31;
    color: {c.TEXT_PRIMARY};
    border: 1px solid #4A4A50;
    border-radius: {r.SM}px;
    padding: 6px 10px;
    font-size: {font_size(f.SIZE_SM)}px;
}}


/* ==========================================================
   TYPOGRAPHY
   ========================================================== */

QLabel#pageTitle {{
    color: {c.TEXT_PRIMARY};
    font-size: {font_size(f.SIZE_XXL)}px;
    font-weight: {f.WEIGHT_BOLD};
    padding-bottom: 2px;
    background: transparent;
}}

QLabel#sectionTitle {{
    color: {c.TEXT_PRIMARY};
    font-size: {font_size(f.SIZE_XL)}px;
    font-weight: {f.WEIGHT_SEMIBOLD};
    background: transparent;
}}

QLabel#eyebrow {{
    color: {c.TEXT_TERTIARY};
    font-size: {font_size(f.SIZE_XS)}px;
    font-weight: {f.WEIGHT_SEMIBOLD};
    letter-spacing: 1px;
    text-transform: uppercase;
    background: transparent;
}}

QLabel#caption {{
    color: {c.TEXT_SECONDARY};
    font-size: {font_size(f.SIZE_SM)}px;
    background: transparent;
}}

QLabel#mono {{
    font-family: {f.MONO_FAMILY};
    color: {c.TEXT_SECONDARY};
    font-size: {font_size(f.SIZE_SM)}px;
    background: transparent;
}}


/* ==========================================================
   PUSH BUTTONS
   ========================================================== */

QPushButton {{
    background: {c.BUTTON};
    color: {c.TEXT_PRIMARY};
    border: 1px solid {c.BORDER};
    border-radius: {r.MD}px;
    padding: 8px 16px;
    min-height: 18px;
    font-weight: {f.WEIGHT_MEDIUM};
}}

QPushButton:hover {{
    background: {c.BUTTON_HOVER};
    border: 1px solid #4A4A50;
}}

QPushButton:pressed {{
    background: {c.BUTTON_PRESSED};
    border: 1px solid {c.SIGNAL_BORDER};
}}

QPushButton:disabled {{
    background: {c.SURFACE};
    color: {c.TEXT_DISABLED};
    border: 1px solid {c.BORDER};
}}


/* ==========================================================
   PRIMARY BUTTON
   ========================================================== */

QPushButton#primaryButton {{
    background: {c.SIGNAL};
    color: {c.TEXT_ON_ACCENT};
    border: 1px solid {c.SIGNAL};
    font-weight: {f.WEIGHT_SEMIBOLD};
}}

QPushButton#primaryButton:hover {{
    background: {c.SIGNAL_HOVER};
    border: 1px solid {c.SIGNAL_HOVER};
}}

QPushButton#primaryButton:pressed {{
    background: {c.SIGNAL_PRESSED};
    border: 1px solid {c.SIGNAL_PRESSED};
}}


/* ==========================================================
   DANGER BUTTON
   ========================================================== */

QPushButton#dangerButton {{
    background: transparent;
    color: {c.ERROR};
    border: 1px solid {c.ERROR};
}}

QPushButton#dangerButton:hover {{
    background: {c.SEV_CRITICAL_BG};
    color: {c.SEV_CRITICAL};
    border: 1px solid {c.SEV_CRITICAL};
}}

QPushButton#dangerButton:pressed {{
    background: {c.ERROR};
    color: white;
}}


/* ==========================================================
   GHOST BUTTON
   ========================================================== */

QPushButton#ghostButton {{
    background: transparent;
    border: none;
    color: {c.TEXT_SECONDARY};
    padding: 6px 10px;
}}

QPushButton#ghostButton:hover {{
    background: #35353B;
    color: {c.TEXT_PRIMARY};
    border-radius: {r.SM}px;
}}

QPushButton#ghostButton:pressed {{
    background: {c.SURFACE_3};
}}


/* ==========================================================
   INPUTS
   ========================================================== */

QLineEdit,
QTextEdit,
QPlainTextEdit,
QComboBox,
QSpinBox,
QDateEdit {{
    background: {c.INPUT};
    color: {c.TEXT_PRIMARY};
    border: 1px solid {c.BORDER};
    border-radius: {r.MD}px;
    padding: 8px 10px;
    selection-background-color: {c.SIGNAL_MUTED};
    selection-color: {c.TEXT_PRIMARY};
}}

QLineEdit:hover,
QTextEdit:hover,
QPlainTextEdit:hover,
QComboBox:hover,
QSpinBox:hover,
QDateEdit:hover {{
    background: {c.INPUT_HOVER};
    border: 1px solid #4A4A50;
}}

QLineEdit:focus,
QTextEdit:focus,
QPlainTextEdit:focus,
QComboBox:focus,
QSpinBox:focus,
QDateEdit:focus {{
    background: {c.INPUT_FOCUS};
    border: 1px solid {c.BORDER_FOCUS};
}}

QLineEdit::placeholder,
QTextEdit::placeholder {{
    color: {c.TEXT_TERTIARY};
}}


/* ==========================================================
   COMBO BOX
   ========================================================== */

QComboBox {{
    min-height: 22px;
    padding-right: 32px;
}}

QComboBox::drop-down {{
    subcontrol-origin: padding;
    subcontrol-position: top right;
    width: 28px;
    border: none;
    background: transparent;
}}

QComboBox::down-arrow {{
    image: none;
    width: 0px;
    height: 0px;
}}

QComboBox:on {{
    border-color: {c.SIGNAL};
}}


/* ==========================================================
   SPIN BOX
   ========================================================== */

QSpinBox::up-button,
QSpinBox::down-button {{
    width: 18px;
    border: none;
    background: transparent;
}}

QSpinBox::up-button:hover,
QSpinBox::down-button:hover {{
    background: #35353B;
}}


/* ==========================================================
   DATE EDIT
   ========================================================== */

QDateEdit::drop-down {{
    width: 24px;
    border: none;
    background: transparent;
}}

QDateEdit::down-arrow {{
    image: none;
}}


/* ==========================================================
   MENU
   ========================================================== */

QMenu {{
    background: #2B2B31;
    color: {c.TEXT_PRIMARY};
    border: 1px solid #4A4A50;
    border-radius: {r.MD}px;
    padding: 6px;
}}

QMenu::item {{
    padding: 8px 28px;
    border-radius: {r.SM}px;
    background: transparent;
}}

QMenu::item:selected {{
    background: {c.SIGNAL_MUTED};
    color: {c.TEXT_PRIMARY};
}}

QMenu::separator {{
    height: 1px;
    margin: 6px 4px;
    background: {c.BORDER};
}}


/* ==========================================================
   LIST WIDGET
   ========================================================== */

QListWidget {{
    background: {c.SURFACE_1};
    border: 1px solid {c.BORDER};
    border-radius: {r.MD}px;
    padding: 4px;
    outline: none;
}}

QListWidget::item {{
    padding: 10px 12px;
    margin: 2px;
    border-radius: {r.SM}px;
    color: {c.TEXT_SECONDARY};
}}

QListWidget::item:hover {{
    background: #35353B;
    color: {c.TEXT_PRIMARY};
}}

QListWidget::item:selected {{
    background: {c.SIGNAL_MUTED};
    color: {c.TEXT_PRIMARY};
    border-left: 3px solid {c.SIGNAL};
}}


/* ==========================================================
   TREE WIDGET
   ========================================================== */

QTreeWidget {{
    background: {c.SURFACE_1};
    border: 1px solid {c.BORDER};
    border-radius: {r.MD}px;
    outline: none;
    alternate-background-color: {c.SURFACE};
}}

QTreeWidget::item {{
    padding: 8px;
    border-radius: {r.SM};
}}

QTreeWidget::item:hover {{
    background: #35353B;
}}

QTreeWidget::item:selected {{
    background: {c.SIGNAL_MUTED};
    color: {c.TEXT_PRIMARY};
    border-left: 3px solid {c.SIGNAL};
}}


/* ==========================================================
   TABLES
   ========================================================== */

QTableWidget,
QTableView {{
    background: {c.SURFACE_1};
    alternate-background-color: {c.SURFACE};
    gridline-color: {c.BORDER};
    color: {c.TEXT_PRIMARY};
    border: 1px solid {c.BORDER};
    border-radius: {r.MD}px;
    selection-background-color: {c.SIGNAL_MUTED};
    selection-color: {c.TEXT_PRIMARY};
    outline: none;
}}

QTableWidget::item,
QTableView::item {{
    padding: 8px;
}}

QTableWidget::item:selected,
QTableView::item:selected {{
    background: {c.SIGNAL_MUTED};
    color: {c.TEXT_PRIMARY};
}}

QTableWidget::item:hover,
QTableView::item:hover {{
    background: #35353B;
}}


/* ==========================================================
   TABLE HEADER
   ========================================================== */

QHeaderView {{
    background: {c.SURFACE};
}}

QHeaderView::section {{
    background: {c.SURFACE};
    color: {c.TEXT_SECONDARY};
    padding: 10px;
    border: none;
    border-bottom: 1px solid {c.BORDER_LIGHT};
    border-right: 1px solid {c.BORDER};
    font-weight: {f.WEIGHT_SEMIBOLD};
}}

QHeaderView::section:hover {{
    background: #35353B;
}}

QTableCornerButton::section {{
    background: {c.SURFACE};
    border: none;
    border-right: 1px solid {c.BORDER};
    border-bottom: 1px solid {c.BORDER};
}}


/* ==========================================================
   CARDS
   ========================================================== */

QFrame#card {{
    background: {c.SURFACE};
    border: 1px solid {c.BORDER};
    border-radius: {r.LG}px;
}}

QFrame#card:hover {{
    background: {c.SURFACE_1};
    border: 1px solid #4A4A50;
}}


/* ==========================================================
   GROUP BOX
   ========================================================== */

QGroupBox {{
    background: {c.SURFACE};
    border: 1px solid {c.BORDER};
    border-radius: {r.LG}px;
    margin-top: 14px;
    padding: 16px;
    font-weight: {f.WEIGHT_SEMIBOLD};
    color: {c.TEXT_PRIMARY};
}}

QGroupBox::title {{
    subcontrol-origin: margin;
    left: 14px;
    padding: 0px 6px;
    color: {c.TEXT_SECONDARY};
}}


/* ==========================================================
   SIDEBAR
   ========================================================== */

QFrame#sidebar {{
    background: {c.SURFACE};
    border-right: 1px solid {c.BORDER};
}}

QPushButton#navButton {{
    background: transparent;
    border: none;
    border-left: 3px solid transparent;
    border-radius: 0px;
    text-align: left;
    padding: 11px 18px;
    color: {c.TEXT_SECONDARY};
    font-weight: {f.WEIGHT_MEDIUM};
}}

QPushButton#navButton:hover {{
    background: #35353B;
    color: {c.TEXT_PRIMARY};
}}

QPushButton#navButton:pressed {{
    background: {c.SURFACE_3};
}}

QPushButton#navButton[active="true"] {{
    background: {c.SIGNAL_MUTED};
    border-left: 3px solid {c.SIGNAL};
    color: {c.TEXT_PRIMARY};
    font-weight: {f.WEIGHT_SEMIBOLD};
}}


/* ==========================================================
   TOP BAR
   ========================================================== */

QWidget#topBar {{
    background: {c.SURFACE};
    border-bottom: 1px solid {c.BORDER};
}}


/* ==========================================================
   STATUS BAR
   ========================================================== */

QWidget#statusBar {{
    background: {c.SURFACE};
    border-top: 1px solid {c.BORDER};
}}

QLabel#statusText {{
    color: {c.TEXT_TERTIARY};
    font-size: {font_size(f.SIZE_XS)}px;
    background: transparent;
}}


/* ==========================================================
   SEPARATORS
   ========================================================== */

QFrame[frameShape="4"] {{
    color: {c.BORDER};
}}

QFrame[frameShape="5"] {{
    color: {c.BORDER};
}}


/* ==========================================================
   TAB WIDGET
   ========================================================== */

QTabWidget::pane {{
    border: 1px solid {c.BORDER};
    border-radius: {r.MD}px;
    background: {c.SURFACE};
    margin-top: 6px;
}}

QTabBar::tab {{
    background: transparent;
    color: {c.TEXT_SECONDARY};
    padding: 10px 18px;
    margin-right: 4px;
    border-bottom: 2px solid transparent;
    font-weight: {f.WEIGHT_MEDIUM};
}}

QTabBar::tab:hover {{
    color: {c.TEXT_PRIMARY};
    background: #35353B;
}}

QTabBar::tab:selected {{
    color: {c.TEXT_PRIMARY};
    border-bottom: 2px solid {c.SIGNAL};
    background: {c.SIGNAL_MUTED};
    font-weight: {f.WEIGHT_SEMIBOLD};
}}


/* ==========================================================
   CHECK BOX
   ========================================================== */

QCheckBox {{
    spacing: 10px;
    color: {c.TEXT_PRIMARY};
    background: transparent;
}}

QCheckBox::indicator {{
    width: 18px;
    height: 18px;
    border-radius: 4px;
    border: 1px solid #4A4A50;
    background: {c.SURFACE_1};
}}

QCheckBox::indicator:hover {{
    border-color: {c.SIGNAL};
}}

QCheckBox::indicator:checked {{
    background: {c.SIGNAL};
    border: 1px solid {c.SIGNAL};
}}


/* ==========================================================
   RADIO BUTTON
   ========================================================== */

QRadioButton {{
    spacing: 10px;
    color: {c.TEXT_PRIMARY};
    background: transparent;
}}

QRadioButton::indicator {{
    width: 18px;
    height: 18px;
    border-radius: 9px;
    border: 1px solid #4A4A50;
    background: {c.SURFACE_1};
}}

QRadioButton::indicator:hover {{
    border-color: {c.SIGNAL};
}}

QRadioButton::indicator:checked {{
    background: {c.SIGNAL};
    border: 1px solid {c.SIGNAL};
}}


/* ==========================================================
   PROGRESS BAR
   ========================================================== */

QProgressBar {{
    background: {c.SURFACE_1};
    border: 1px solid {c.BORDER};
    border-radius: {r.SM}px;
    text-align: center;
    color: {c.TEXT_PRIMARY};
    min-height: 18px;
}}

QProgressBar::chunk {{
    background: {c.SIGNAL};
    border-radius: {r.SM}px;
}}


/* ==========================================================
   SEVERITY CHIPS
   ========================================================== */

QLabel[severity="Critical"] {{
    color: {c.SEV_CRITICAL};
    background: {c.SEV_CRITICAL_BG};
    border: 1px solid {c.SEV_CRITICAL};
    border-radius: {r.PILL}px;
    padding: 3px 10px;
    font-weight: {f.WEIGHT_SEMIBOLD};
}}

QLabel[severity="High"] {{
    color: {c.SEV_HIGH};
    background: {c.SEV_HIGH_BG};
    border: 1px solid {c.SEV_HIGH};
    border-radius: {r.PILL}px;
    padding: 3px 10px;
    font-weight: {f.WEIGHT_SEMIBOLD};
}}

QLabel[severity="Medium"] {{
    color: {c.SEV_MEDIUM};
    background: {c.SEV_MEDIUM_BG};
    border: 1px solid {c.SEV_MEDIUM};
    border-radius: {r.PILL}px;
    padding: 3px 10px;
    font-weight: {f.WEIGHT_SEMIBOLD};
}}

QLabel[severity="Low"] {{
    color: {c.SEV_LOW};
    background: {c.SEV_LOW_BG};
    border: 1px solid {c.SEV_LOW};
    border-radius: {r.PILL}px;
    padding: 3px 10px;
    font-weight: {f.WEIGHT_SEMIBOLD};
}}

QLabel[severity="Info"] {{
    color: {c.SEV_INFO};
    background: {c.SEV_INFO_BG};
    border: 1px solid {c.SEV_INFO};
    border-radius: {r.PILL}px;
    padding: 3px 10px;
    font-weight: {f.WEIGHT_SEMIBOLD};
}}


/* ==========================================================
   STATUS CHIPS
   ========================================================== */

QLabel[status="Open"] {{
    color: {c.STATUS_OPEN};
    background: {c.SEV_CRITICAL_BG};
    border: 1px solid {c.STATUS_OPEN};
    border-radius: {r.PILL}px;
    padding: 3px 10px;
}}

QLabel[status="Verified"] {{
    color: {c.STATUS_VERIFIED};
    background: {c.SEV_LOW_BG};
    border: 1px solid {c.STATUS_VERIFIED};
    border-radius: {r.PILL}px;
    padding: 3px 10px;
}}

QLabel[status="Reported"] {{
    color: {c.STATUS_REPORTED};
    background: #2B2237;
    border: 1px solid {c.STATUS_REPORTED};
    border-radius: {r.PILL}px;
    padding: 3px 10px;
}}

QLabel[status="Closed"] {{
    color: {c.STATUS_CLOSED};
    background: #35353B;
    border: 1px solid {c.STATUS_CLOSED};
    border-radius: {r.PILL}px;
    padding: 3px 10px;
}}


/* ==========================================================
   SCROLL BARS
   ========================================================== */

QScrollBar:vertical {{
    background: transparent;
    width: 12px;
    margin: 4px;
}}

QScrollBar::handle:vertical {{
    background: {c.BORDER_LIGHT};
    border-radius: 6px;
    min-height: 36px;
}}

QScrollBar::handle:vertical:hover {{
    background: {c.SIGNAL};
}}

QScrollBar::handle:vertical:pressed {{
    background: {c.SIGNAL_HOVER};
}}

QScrollBar::add-line:vertical,
QScrollBar::sub-line:vertical {{
    height: 0px;
    background: none;
    border: none;
}}

QScrollBar::add-page:vertical,
QScrollBar::sub-page:vertical {{
    background: transparent;
}}

QScrollBar:horizontal {{
    background: transparent;
    height: 12px;
    margin: 4px;
}}

QScrollBar::handle:horizontal {{
    background: {c.BORDER_LIGHT};
    border-radius: 6px;
    min-width: 36px;
}}

QScrollBar::handle:horizontal:hover {{
    background: {c.SIGNAL};
}}

QScrollBar::handle:horizontal:pressed {{
    background: {c.SIGNAL_HOVER};
}}

QScrollBar::add-line:horizontal,
QScrollBar::sub-line:horizontal {{
    width: 0px;
    background: none;
    border: none;
}}

QScrollBar::add-page:horizontal,
QScrollBar::sub-page:horizontal {{
    background: transparent;
}}


/* ==========================================================
   SPLITTER
   ========================================================== */

QSplitter::handle {{
    background: {c.BORDER};
}}

QSplitter::handle:hover {{
    background: {c.SIGNAL};
}}

QSplitter::handle:horizontal {{
    width: 2px;
}}

QSplitter::handle:vertical {{
    height: 2px;
}}


/* ==========================================================
   MESSAGE BOX
   ========================================================== */

QMessageBox {{
    background: #2B2B31;
    color: {c.TEXT_PRIMARY};
}}

QMessageBox QLabel {{
    background: transparent;
    color: {c.TEXT_PRIMARY};
}}


/* ==========================================================
   DIALOG
   ========================================================== */

QDialog {{
    background: #2B2B31;
    border: 1px solid {c.BORDER};
    border-radius: {r.LG}px;
}}

/* Every direct and nested widget inside a dialog is transparent
   so the dialog surface (#2B2B31) shows through.
   Without this, QWidget {{ background: WINDOW }} bleeds in
   and paints label rows / title bars near-black. */
QDialog QWidget {{
    background: transparent;
}}

QDialog QLabel {{
    background: transparent;
    color: {c.TEXT_PRIMARY};
}}

/* Re-assert opaque backgrounds only for actual input controls
   inside dialogs — they should still look like input wells */
QDialog QLineEdit,
QDialog QTextEdit,
QDialog QPlainTextEdit,
QDialog QComboBox,
QDialog QSpinBox,
QDialog QDateEdit {{
    background: {c.INPUT};
    border: 1px solid {c.BORDER};
}}

/* Buttons inside dialogs keep their own backgrounds */
QDialog QPushButton {{
    background: {c.BUTTON};
}}

QDialog QPushButton#primaryButton {{
    background: {c.SIGNAL};
    color: {c.TEXT_ON_ACCENT};
    border: 1px solid {c.SIGNAL};
}}


/* ==========================================================
   DIALOG BUTTON BOX
   ========================================================== */

QDialogButtonBox QPushButton {{
    min-width: 90px;
    min-height: 34px;
}}


/* ==========================================================
   CALENDAR
   ========================================================== */

QCalendarWidget QWidget {{
    alternate-background-color: {c.SURFACE};
}}

QCalendarWidget QToolButton {{
    background: transparent;
    color: {c.TEXT_PRIMARY};
    border: none;
    padding: 6px;
    font-weight: {f.WEIGHT_MEDIUM};
}}

QCalendarWidget QToolButton:hover {{
    background: #35353B;
}}

QCalendarWidget QMenu {{
    background: #2B2B31;
}}

QCalendarWidget QSpinBox {{
    background: {c.INPUT};
    color: {c.TEXT_PRIMARY};
    border: 1px solid {c.BORDER};
}}

QCalendarWidget QAbstractItemView {{
    background: #2B2B31;
    color: {c.TEXT_PRIMARY};
    selection-background-color: {c.SIGNAL};
    selection-color: white;
}}


/* ==========================================================
   SIZE GRIP
   ========================================================== */

QSizeGrip {{
    background: transparent;
}}
"""


def apply_theme(
    app: QApplication,
    font_scale: float = 1.0,
) -> None:
    """Apply the application theme stylesheet."""
    app.setStyleSheet(build_stylesheet(font_scale=font_scale))