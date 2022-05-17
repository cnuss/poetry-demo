from poetry_demo import __version__, whoismylib


def test_version():
    assert __version__ == '0.0.1'


def test_lib_works():
    assert whoismylib() == "i am mylib"
