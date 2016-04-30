import main


def test_generate_regex():
    assert main.generate_regex(["a"]) == "a"
    assert main.generate_regex(["a", "b"]) == "[ab]"
    assert main.generate_regex(["a", "bb"]) == "[ab]b"


def test_display_group():
    assert main.display_group(set("a")) == "a"
    assert main.display_group(set("ab")) == "[ab]"


def test_extend_characters_list():
    assert main.extend_characters_list([], 5) == [set() for i in range(5)]
    assert main.extend_characters_list([{"a"}], 3) == [{"a"}, set(), set()]
