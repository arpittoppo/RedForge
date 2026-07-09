"""
RedForge

Application entry point.
"""

from redforge.app.bootstrap import bootstrap


def main() -> None:
    """
    Start the RedForge application.
    """
    bootstrap()


if __name__ == "__main__":
    main()