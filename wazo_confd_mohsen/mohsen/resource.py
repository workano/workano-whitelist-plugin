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
        return {'Location': url_for('mohsens', id=model.id, _external=True)}

    @required_acl('confd.mohsens.create')
    def post(self):
        return super().post()

    @required_acl('confd.mohsens.read')
    def get(self):
        return super().get()

class WhitelistItemResource(ItemResource):
    schema = WhitelistSchema
    model = WhitelistModel

    @required_acl('confd.mohsens.read')
    def get(self, id):
        return super().get(id)

    @required_acl('confd.mohsens.update')
    def put(self, id):
        return super().put(id)

    @required_acl('confd.mohsens.delete')
    def delete(self, id):
        return super().delete(id)



