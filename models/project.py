from services.project_service import ProjectService

class ProjectModel:
    @classmethod
    def find_all(cls, featured_only=False):
        return ProjectService.get_all(featured_only=featured_only)

    @classmethod
    def find_by_slug(cls, slug):
        return ProjectService.get_by_slug(slug)

    @classmethod
    def create(cls, data):
        return ProjectService.create(data)
