# resources.py
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
        return {'Location': url_for('whitelists', uuid=model.uuid, _external=True)}

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
        url = request.args.get('url')
        is_whitelisted = self._service.is_url_whitelisted(tenant_uuid, url)
        logger.info(f"Whitelist Inquiry {tenant_uuid} : {url} : {is_whitelisted}")

        response = "ALLOWED" if is_whitelisted else "NOT_ALLOWED"
        return make_response(response)


class WhitelistUniqueIdResource(Resource):
    def __init__(self, service):
        """
        :type service: WhitelistService
        """
        self._service = service

    def get(self, unique_id):
        tenant_uuid = request.headers.get('Wazo-Tenant')
        url = self._service.get_url_by_unique_id(tenant_uuid, unique_id)
        if url:
            return make_response({"url": url}, 200)
        else:
            return make_response({"error": "Not Found"}, 404)
