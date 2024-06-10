from wazo_confd.helpers.resource import CRUDService

from . import dao
from .notifier import build_whitelist_notifier
from .validator import build_whitelist_validator


class WhitelistService(CRUDService):
    def is_blocked_num(self, tenant_uuid, exten, blocked_num):
        """
        :rtype: bool
        """
        return self.dao.is_blocked_num(tenant_uuid, exten, blocked_num)


def build_whitelist_service():
    return WhitelistService(dao, build_whitelist_validator(), build_whitelist_notifier())