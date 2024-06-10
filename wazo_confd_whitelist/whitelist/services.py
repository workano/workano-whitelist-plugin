from wazo_confd.helpers.resource import CRUDService

from . import dao
from .notifier import build_whitelist_notifier
from .validator import build_whitelist_validator


class WhitelistService(CRUDService):
    pass


def build_whitelist_service():
    return WhitelistService(dao, build_whitelist_validator(), build_whitelist_notifier())
