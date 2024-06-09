import logging

from .whitelist.resource import WhitelistList, WhitelistItem
from .services import build_whitelist_service
from .db import init_db

logger = logging.getLogger(__name__)

class Plugin:
    def load(self, dependencies):
        logger.info('Whitelist plugin loading')
        init_db('postgresql://asterisk:proformatique@localhost/asterisk?application_name=wazo-whitelist-plugin')
        api = dependencies['api']
        whitelist_service = build_whitelist_service()

        # Whitelists
        api.add_resource(
            WhitelistList,
            '/whitelists',
            resource_class_args=(whitelist_service,)
        )
        api.add_resource(
            WhitelistItem,
            '/whitelists/<int:id>',
            endpoint='whitelists',
            resource_class_args=(whitelist_service,)
        )

        logger.info('Whitelist plugin loaded')
