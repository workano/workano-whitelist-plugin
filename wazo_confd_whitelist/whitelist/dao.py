# dao.py
from xivo_dao.helpers.db_manager import daosession

from .persistor import WhitelistPersistor
from .search import whitelist_search


@daosession
def _persistor(session, tenant_uuids=None):
    return WhitelistPersistor(session, whitelist_search, tenant_uuids)


def search(tenant_uuids=None, **parameters):
    return _persistor(tenant_uuids).search(parameters)


def get(whitelist_uuid, tenant_uuids=None):
    return _persistor(tenant_uuids).get_by({'uuid': whitelist_uuid})


def get_by(tenant_uuids=None, **criteria):
    return _persistor(tenant_uuids).get_by(criteria)


def find(whitelist_uuid, tenant_uuids=None):
    return _persistor(tenant_uuids).find_by({'uuid': whitelist_uuid})


def find_by(tenant_uuids=None, **criteria):
    return _persistor(tenant_uuids).find_by(criteria)


def find_all_by(tenant_uuids=None, **criteria):
    return _persistor(tenant_uuids).find_all_by(criteria)


def create(whitelist):
    return _persistor().create(whitelist)


def edit(whitelist):
    _persistor().edit(whitelist)


def delete(whitelist):
    _persistor().delete(whitelist)


def get_by_url(url, tenant_uuids=None):
    return _persistor(tenant_uuids).get_by({'url': url})


def get_url_by_unique_id(unique_id, tenant_uuids=None):
    whitelist = _persistor(tenant_uuids).get_by({'unique_id': unique_id})
    return whitelist.url if whitelist else None
