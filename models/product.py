from services.product_service import ProductService

class ProductModel:
    @classmethod
    def find_all(cls, filter_query=None, sort_field='created_at', sort_order=-1, page=1, limit=12):
        s_order = 'desc' if sort_order in (-1, 'desc', 'DESC') else 'asc'
        return ProductService.get_all(filter_query=filter_query, sort_field=sort_field, sort_order=s_order, page=page, limit=limit)

    @classmethod
    def find_by_slug(cls, subcategory_slug, product_slug):
        return ProductService.get_by_slug(subcategory_slug, product_slug)

    @classmethod
    def find_by_id(cls, product_id):
        return ProductService.get_by_id(product_id)

    @classmethod
    def find_featured(cls, limit=8):
        return ProductService.get_featured(limit=limit)

    @classmethod
    def create(cls, data):
        return ProductService.create(data)

    @classmethod
    def update(cls, product_id, data):
        return ProductService.update(product_id, data)

    @classmethod
    def delete(cls, product_id):
        return ProductService.delete(product_id)
