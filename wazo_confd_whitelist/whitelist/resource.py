import logging

from flask import url_for, request, make_response
from flask_restful import Resource
from wazo_confd.auth import required_acl
from wazo_confd.helpers.restful import ItemResource, ListResource

from .model import WhitelistModel
from .schema import WhitelistSchema

logger = logging.getLogger(__name__)


class WhitelistListResource(ListResource):
    schema = WhitelistSchema
    model = WhitelistModel

    def build_headers(self, model):
        return {'Location': url_for('whitelists', uuid=model.id, _external=True)}

    @required_acl('confd.whitelists.create')
    def post(self):
        return super().post()

    @required_acl('confd.whitelists.read')
    def get(self):
        return super().get()


class WhitelistItemResource(ItemResource):
    schema = WhitelistSchema
    model = WhitelistModel

    @required_acl('confd.whitelists.read')
    def get(self, uuid):
        return super().get(uuid)

    @required_acl('confd.whitelists.update')
    def put(self, uuid):
        return super().put(uuid)

    @required_acl('confd.whitelists.delete')
    def delete(self, uuid):
        return super().delete(uuid)


class WhitelistInquiryResource(Resource):
    def __init__(self, service):
        """
        :type service: WhitelistService
        """
        self._service = service

    def get(self):
        tenant_uuid = request.headers.get('Wazo-Tenant')
        from_num = request.args.get('from_num')
        to_num = request.args.get('to_num')
        is_block = self._service.is_blocked_num(tenant_uuid, to_num, from_num)
        logger.info(f"Whitelist Inquiry {tenant_uuid} : {from_num} => {to_num} : {is_block}")

        response = "BLOCKED" if is_block else "NOT_BLOCKED"
        return make_response(response)
