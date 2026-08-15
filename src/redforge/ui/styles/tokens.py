"""
RedForge Design Tokens
======================

Single source of truth for RedForge's visual language.

Design Goals
------------
• Modern professional desktop application
• Neutral charcoal surfaces (no blue tint)
• RedForge red accent
• High contrast
• Soft elevation
• Comfortable spacing
"""

from __future__ import annotations


class Color:
    # ==========================================================
    # Base Surfaces
    # ==========================================================

    WINDOW = "#0D0D0F"            # Main application background
    VOID = WINDOW

    SURFACE = "#151517"           # Cards / Sidebar / Panels
    SURFACE_1 = "#1B1B1E"         # Inputs
    SURFACE_2 = "#222226"         # Hover
    SURFACE_3 = "#2A2A2F"         # Active / Raised

    OVERLAY = "#242429"           # Menus / Dialogs / Combo Popup

    # ==========================================================
    # Borders
    # ==========================================================

    BORDER = "#2A2A2D"
    BORDER_LIGHT = "#35353A"
    BORDER_STRONG = "#404046"

    BORDER_FOCUS = "#EF4655"

    # ==========================================================
    # Text
    # ==========================================================

    TEXT_PRIMARY = "#F4F4F5"

    TEXT_SECONDARY = "#B2B2B7"

    TEXT_TERTIARY = "#8C8C91"

    TEXT_DISABLED = "#5E5E63"

    TEXT_ON_ACCENT = "#FFFFFF"

    # ==========================================================
    # Accent
    # ==========================================================

    SIGNAL = "#EF4655"

    SIGNAL_HOVER = "#FF5A69"

    SIGNAL_PRESSED = "#D63A49"

    SIGNAL_MUTED = "#35171B"

    SIGNAL_BORDER = "#EF4655"

    # ==========================================================
    # Buttons
    # ==========================================================

    BUTTON = SURFACE_1

    BUTTON_HOVER = SURFACE_2

    BUTTON_PRESSED = SURFACE_3

    # ==========================================================
    # Inputs
    # ==========================================================

    INPUT = "#121214"

    INPUT_HOVER = "#1B1B1F"

    INPUT_FOCUS = "#18181B"

    # ==========================================================
    # Severity
    # ==========================================================

    SEV_CRITICAL = "#EF4655"
    SEV_CRITICAL_BG = "#351419"

    SEV_HIGH = "#FF8A4C"
    SEV_HIGH_BG = "#392315"

    SEV_MEDIUM = "#E6B84A"
    SEV_MEDIUM_BG = "#342B16"

    SEV_LOW = "#6FCF7C"
    SEV_LOW_BG = "#17321F"

    SEV_INFO = "#9A9AA1"
    SEV_INFO_BG = "#252528"

    SEVERITY_MAP = {
        "Critical": SEV_CRITICAL,
        "High": SEV_HIGH,
        "Medium": SEV_MEDIUM,
        "Low": SEV_LOW,
        "Info": SEV_INFO,
    }

    # ==========================================================
    # Status
    # ==========================================================

    STATUS_OPEN = "#EF4655"

    STATUS_VERIFIED = "#6FCF7C"

    STATUS_REPORTED = "#C79DFF"

    STATUS_CLOSED = "#9A9AA1"

    STATUS_MAP = {
        "Open": STATUS_OPEN,
        "Verified": STATUS_VERIFIED,
        "Reported": STATUS_REPORTED,
        "Closed": STATUS_CLOSED,
    }

    # ==========================================================
    # Misc
    # ==========================================================

    SUCCESS = "#6FCF7C"

    WARNING = "#E6B84A"

    ERROR = "#EF4655"

    LINK = "#FF707D"

    SELECTION = SIGNAL_MUTED

    SHADOW = "#000000"


class Font:
    UI_FAMILY = (
        "Inter, 'Segoe UI', 'SF Pro Display', "
        "-apple-system, sans-serif"
    )

    MONO_FAMILY = (
        "'JetBrains Mono', "
        "'Cascadia Code', "
        "'Consolas', monospace"
    )

    SIZE_XS = 11

    SIZE_SM = 12

    SIZE_MD = 13

    SIZE_LG = 15

    SIZE_XL = 18

    SIZE_XXL = 24

    WEIGHT_NORMAL = 400

    WEIGHT_MEDIUM = 500

    WEIGHT_SEMIBOLD = 600

    WEIGHT_BOLD = 700


class Space:
    XS = 4

    SM = 8

    MD = 12

    LG = 16

    XL = 24

    XXL = 32

    XXXL = 40


class Radius:
    XS = 4

    SM = 6

    MD = 8

    LG = 10

    XL = 14

    PILL = 999


class Shadow:
    NONE = 0

    SM = 2

    MD = 4

    LG = 8


# ==============================================================
# Layout Constants
# ==============================================================

SIDEBAR_WIDTH = 240

TOPBAR_HEIGHT = 58

STATUSBAR_HEIGHT = 28

CONTENT_MAX_WIDTH = 1600