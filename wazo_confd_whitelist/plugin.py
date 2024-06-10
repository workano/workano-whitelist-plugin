import logging

from .whitelist.resource import WhitelistListResource, WhitelistItemResource, WhitelistInquiryResource
from .services import build_whitelist_service
from .db import init_db

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

class Plugin:
    def load(self, dependencies):
        logger.info('Whitelist plugin loading')
        try:
            init_db('postgresql://asterisk:proformatique@localhost/asterisk?application_name=wazo-whitelist-plugin')
            api = dependencies['api']
            whitelist_service = build_whitelist_service()

            # Register API resources
            api.add_resource(
                WhitelistListResource,
                '/whitelists',
                resource_class_args=(whitelist_service,)
            )
            api.add_resource(
                WhitelistItemResource,
                '/whitelists/<int:id>',
                endpoint='whitelists',
                resource_class_args=(whitelist_service,)
            )

            logger.info('Whitelist plugin loaded successfully')
        except Exception as e:
            logger.error(f'Error loading whitelist plugin: {e}', exc_info=True)
