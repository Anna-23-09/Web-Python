import pytest
from test_task_1 import test_check_text


def test_milk(word):
    # test1
    assert word[0] in test_check_text(word[1])


if __name__ == '__main__':
    pytest.main(["-vv"])
