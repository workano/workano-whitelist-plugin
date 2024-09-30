# plugin.py
import logging

from .whitelist.resources import (
    WhitelistListResource,
    WhitelistItemResource,
    WhitelistInquiryResource,
    WhitelistUniqueIdResource
)
from .whitelist.services import build_whitelist_service
from .db import init_db

logger = logging.getLogger(__name__)


class Plugin:
    def load(self, dependencies):
        logger.info('Whitelist plugin loading')
        init_db('postgresql://asterisk:proformatique@localhost/asterisk?application_name=wazo-whitelist-plugin')
        api = dependencies['api']
        whitelist_service = build_whitelist_service()

        # Register existing resources
        api.add_resource(
            WhitelistListResource,
            '/whitelists',
            resource_class_kwargs={'service': whitelist_service}
        )
        api.add_resource(
            WhitelistItemResource,
            '/whitelists/<string:uuid>',
            endpoint='whitelists',
            resource_class_kwargs={'service': whitelist_service}
        )

        # Register new resources
        api.add_resource(
            WhitelistInquiryResource,
            '/whitelists/check',
            resource_class_kwargs={'service': whitelist_service}
        )
        api.add_resource(
            WhitelistUniqueIdResource,
            '/whitelists/unique/<string:unique_id>',
            resource_class_kwargs={'service': whitelist_service}
        )

        logger.info('Whitelist plugin loaded')
