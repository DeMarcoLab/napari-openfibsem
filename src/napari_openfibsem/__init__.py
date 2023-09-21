
try:
    from ._version import version as __version__
except ImportError:
    __version__ = "unknown"

from .app import autolamella_ui, autoliftout_ui

__all__ = (
    "autolamella_ui",
    "autoliftout_ui",
)
