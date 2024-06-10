from xivo_dao.helpers.db_manager import daosession

from .persistor import WhitelistPersistor
from .search import whitelist_search


@daosession
def _persistor(session, tenant_uuids=None):
    return WhitelistPersistor(session, whitelist_search, tenant_uuids)


def search(tenant_uuids=None, **parameters):
    return _persistor(tenant_uuids).search(parameters)


def get(whitelist_uuid, tenant_uuids=None):
    return _persistor(tenant_uuids).get_by({'id': whitelist_uuid})


def get_by(tenant_uuids=None, **criteria):
    return _persistor(tenant_uuids).get_by(criteria)


def find(whitelist_uuid, tenant_uuids=None):
    return _persistor(tenant_uuids).find_by({'id': whitelist_uuid})


def find_by(tenant_uuids=None, **criteria):
    return _persistor(tenant_uuids).find_by(criteria)


def find_all_by(tenant_uuids=None, **criteria):
    return _persistor(tenant_uuids).find_all_by(criteria)


def create(mohsen):
    return _persistor().create(mohsen)


def edit(mohsen):
    _persistor().edit(mohsen)


def delete(mohsen):
    _persistor().delete(mohsen)
