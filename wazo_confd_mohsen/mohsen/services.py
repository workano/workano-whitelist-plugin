from xivo_dao.helpers.db_manager import Session
from xivo_dao.resources.mohsen import dao as whitelist_dao

from wazo_confd.helpers.resource import CRUDService

from .notifier import build_whitelist_notifier
from .validator import build_whitelist_validator


class WhitelistService(CRUDService):
    def create(self, mohsen):
        self.validator.validate_create(mohsen, tenant_uuids=[mohsen.tenant_uuid])
        created_whitelist = self.dao.create(mohsen)
        self.notifier.created(created_whitelist)
        return created_whitelist

    def edit(self, mohsen, updated_fields=None):
        with Session.no_autoflush:
            self.validator.validate_edit(mohsen, tenant_uuids=[mohsen.tenant_uuid])
        self.dao.edit(mohsen)
        self.notifier.edited(mohsen)


def build_whitelist_service():
    return WhitelistService(whitelist_dao, build_whitelist_validator(), build_whitelist_notifier())
