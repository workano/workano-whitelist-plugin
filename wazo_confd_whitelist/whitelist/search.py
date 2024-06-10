from xivo_dao.resources.utils.search import SearchConfig
from xivo_dao.resources.utils.search import SearchSystem

from .model import WhitelistModel

whitelist_config = SearchConfig(
    table=WhitelistModel,
    columns={
        'id': WhitelistModel.id,
        'tenant_uuid': WhitelistModel.tenant_uuid,
        'ip_addresses': WhitelistModel.ip_addresses,
        'domains': WhitelistModel.domains,
        'created_at': WhitelistModel.created_at,
        'expire_at': WhitelistModel.expire_at,
        'renew': WhitelistModel.renew,
    },
    default_sort='id',
)

whitelist_search = SearchSystem(whitelist_config)
