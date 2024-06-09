from xivo_dao.helpers.db_manager import Session
from xivo_dao.resources.whitelist import dao as whitelist_dao

from wazo_confd.helpers.resource import CRUDService

from .notifier import build_whitelist_notifier
from .validator import build_whitelist_validator


class WhitelistService(CRUDService):
    def create(self, whitelist):
        self.validator.validate_create(whitelist, tenant_uuids=[whitelist.tenant_uuid])
        created_whitelist = self.dao.create(whitelist)
        self.notifier.created(created_whitelist)
        return created_whitelist

    def edit(self, whitelist, updated_fields=None):
        with Session.no_autoflush:
            self.validator.validate_edit(whitelist, tenant_uuids=[whitelist.tenant_uuid])
        self.dao.edit(whitelist)
        self.notifier.edited(whitelist)


def build_whitelist_service():
    return WhitelistService(whitelist_dao, build_whitelist_validator(), build_whitelist_notifier())
