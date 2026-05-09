import warnings

# pylint: disable=wrong-import-position
warnings.warn(
    "fild-compare is deprecated and will no longer be maintained. "
    "Migrate to surety-diff: pip install surety-diff. "
    "Replace 'from fild_compare import compare' with 'from surety.diff import compare'. "
    "See https://github.com/elenakulgavaya/surety-diff for details.",
    DeprecationWarning,
    stacklevel=2,
)

from .compare import compare
from .rule_decorator import compare_rule
