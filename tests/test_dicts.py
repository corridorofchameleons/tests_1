import pytest

from utils.dicts import get_val


@pytest.fixture
def get_coll():
    return {1: '1', 2: '2'}


def test_get_val(get_coll):
    assert get_val(get_coll, 1, '') == '1'
    assert get_val(get_coll, 1) == '1'
    assert get_val(get_coll, 3, 'i_use_arch_btw') == 'i_use_arch_btw'
