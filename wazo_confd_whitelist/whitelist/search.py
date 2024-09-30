# search.py
from xivo_dao.resources.utils.search import SearchConfig, SearchSystem

from .model import WhitelistModel

whitelist_config = SearchConfig(
    table=WhitelistModel,
    columns={
        'uuid': WhitelistModel.uuid,
        'unique_id': WhitelistModel.unique_id,
        'url': WhitelistModel.url,
        'customer_name': WhitelistModel.customer_name,
    },
    default_sort='uuid',
)

whitelist_search = SearchSystem(whitelist_config)
