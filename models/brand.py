from services.brand_service import BrandService

class BrandModel:
    @classmethod
    def find_all(cls, featured_only=False, business_slug=None):
        return BrandService.get_all(featured_only=featured_only, business_slug=business_slug)

    @classmethod
    def find_by_slug(cls, slug):
        return BrandService.get_by_slug(slug)

    @classmethod
    def create(cls, data):
        return BrandService.create(data)
