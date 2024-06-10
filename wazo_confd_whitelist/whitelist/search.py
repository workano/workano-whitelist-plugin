from xivo_dao.resources.utils.search import SearchConfig
from xivo_dao.resources.utils.search import SearchSystem

from .model import WhitelistModel

whitelist_config = SearchConfig(
    table=WhitelistModel,
    columns={
        'id': WhitelistModel.id,
        'exten': WhitelistModel.exten,
        'blocked_num': WhitelistModel.blocked_num,
    },
    default_sort='id',
)

whitelist_search = SearchSystem(whitelist_config)