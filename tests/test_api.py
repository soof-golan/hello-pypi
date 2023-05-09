import sys

import pytest

import sg_identity

PY38 = (3, 8) <= sys.version_info < (3, 9)


def test_sometimes_identity():
    args = (1, 2, 3)
    if PY38:
        with pytest.raises(RuntimeError):
            sg_identity.sometimes_identity(*args)
    else:
        assert args == sg_identity.sometimes_identity(*args)
        assert isinstance(sg_identity.sometimes_identity(*args), tuple)


def test_identity_gives_back_args():
    args = (1, 2, 3)
    assert args == sg_identity.identity(*args)
