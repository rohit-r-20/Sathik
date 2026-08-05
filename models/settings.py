from services.setting_service import SettingService

class SettingModel:
    @classmethod
    def get_all_public(cls):
        return SettingService.get_all_public()

    @classmethod
    def get_all(cls):
        return SettingService.get_all()

    @classmethod
    def get_value(cls, key, default=None):
        return SettingService.get_value(key, default=default)

    @classmethod
    def set_value(cls, key, value, group='general', label='', is_public=True):
        return SettingService.set_value(key, value, group=group, label=label, is_public=is_public)
