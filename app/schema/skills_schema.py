import marshmallow as ma


class SkillsTitleInputSchema(ma.Schema):
    skill_title = ma.fields.String()


class SkillsReverseTitleOutputSchema(ma.Schema):
    skill_title = ma.fields.String()
    reversed_skill_title = ma.fields.String()