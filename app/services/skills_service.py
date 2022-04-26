def reverse_skill_title(external_skill_title: str) -> dict:
    """ Reverse and lowercase the skill title string """
    reversed_skill_title = external_skill_title[::-1].lower()
    output = {
        "skill_title": external_skill_title,
        "reversed_skill_title": reversed_skill_title,
    }
    return output