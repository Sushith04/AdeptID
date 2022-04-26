from typing import Dict, List, Any
from flask_restful import Resource
from flask_smorest import Blueprint
from app.schema.skills_schema import (
    SkillsTitleInputSchema,
    SkillsReverseTitleOutputSchema,
)
from app.services import skills_service as skills_svc

skills_bp = Blueprint("Skills", __name__, description="Skills Endpoints")


@skills_bp.route("/skills/reverse-skill-title")
class SkillsReverseTitleResource(Resource):
    @skills_bp.arguments(SkillsTitleInputSchema)
    @skills_bp.response(status_code=200, schema=SkillsReverseTitleOutputSchema)
    def post(self, body: Dict[str, str]):
        """ Reverse and lowercase the skill title word """
        reverse_skill_title_output = skills_svc.reverse_skill_title(
            external_skill_title=body["skill_title"]
        )
        return reverse_skill_title_output
