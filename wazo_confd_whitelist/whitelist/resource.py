from flask import url_for

from xivo_dao.alchemy.whitelist import WhitelistModel

from wazo_confd.auth import required_acl
from wazo_confd.helpers.restful import ListResource, ItemResource

from .schema import WhitelistSchema


class WhitelistList(ListResource):
    model = WhitelistModel
    schema = WhitelistSchema

    def build_headers(self, whitelist):
        return {'Location': url_for('whitelists', id=whitelist.id, _external=True)}

    @required_acl('confd.whitelists.create')
    def post(self):
        return super().post()

    @required_acl('confd.whitelists.read')
    def get(self):
        return super().get()


class WhitelistItem(ItemResource):
    schema = WhitelistSchema
    has_tenant_uuid = True

    @required_acl('confd.whitelists.{id}.read')
    def get(self, id):
        return super().get(id)

    @required_acl('confd.whitelists.{id}.update')
    def put(self, id):
        return super().put(id)

    @required_acl('confd.whitelists.{id}.delete')
    def delete(self, id):
        return super().delete(id)
