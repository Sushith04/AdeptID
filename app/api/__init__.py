from app.api.skills_resource import skills_bp


def init_app(app):
    app.register_blueprint(blp=skills_bp)
