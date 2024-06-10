from marshmallow import fields
from wazo_confd.helpers.mallow import BaseSchema


class WhitelistSchema(BaseSchema):
    id = fields.Integer(dump_only=True)
    tenant_uuid = fields.String(dump_only=True)
    ip_addresses = fields.List(fields.String(), required=False)
    domains = fields.List(fields.String(), required=False)
    created_at = fields.Date(required=True)
    expire_at = fields.Date(required=True)
    renew = fields.Boolean(required=True)
