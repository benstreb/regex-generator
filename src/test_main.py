from . import main


def test_generate_regex():
    assert main.generate_regex(["a"]) == "a"
