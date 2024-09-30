# service.py
from wazo_confd.helpers.resource import CRUDService

from . import dao
from .notifier import build_whitelist_notifier
from .validator import build_whitelist_validator


class WhitelistService(CRUDService):
    def is_url_whitelisted(self, tenant_uuid, url):
        whitelist = self.dao.get_by_url(url, tenant_uuid)
        return whitelist is not None

    def get_url_by_unique_id(self, tenant_uuid, unique_id):
        return self.dao.get_url_by_unique_id(unique_id, tenant_uuid)


def build_whitelist_service():
    return WhitelistService(dao, build_whitelist_validator(), build_whitelist_notifier())
