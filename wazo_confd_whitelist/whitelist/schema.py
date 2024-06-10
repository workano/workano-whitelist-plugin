from marshmallow import fields
from wazo_confd.helpers.mallow import BaseSchema


class WhitelistSchema(BaseSchema):
    id = fields.Integer(dump_only=True)
    tenant_uuid = fields.String(dump_only=True)
    exten = fields.Str(required=False)
    blocked_num = fields.Str(required=True)