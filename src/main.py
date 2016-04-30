def generate_regex(samples):
    characters_list = []
    for sample in samples:
        characters_list = extend_characters_list(characters_list, len(sample))
        for i, character in enumerate(sample):
            characters_list[i].add(character)
    return "".join(display_group(characters) for characters in characters_list)


def display_group(characters):
    if len(characters) == 1:
        template = "{}"
    else:
        template = "[{}]"
    return template.format("".join(sorted(characters)))


def extend_characters_list(characters_list, length):
    extension_length = max(length - len(characters_list), 0)
    return characters_list + [set() for i in range(extension_length)]
