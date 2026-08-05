from services.enquiry_service import EnquiryService

class EnquiryModel:
    @classmethod
    def create(cls, data):
        return EnquiryService.create(data)

    @classmethod
    def find_all(cls, status=None, page=1, limit=20):
        return EnquiryService.get_all(status=status, page=page, limit=limit)

    @classmethod
    def update_status(cls, enquiry_id, status, notes=None):
        return EnquiryService.update_status(enquiry_id, status, notes=notes)

    @classmethod
    def get_stats(cls):
        return EnquiryService.get_stats()
