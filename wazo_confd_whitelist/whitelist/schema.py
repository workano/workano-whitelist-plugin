# schema.py
from marshmallow import fields
from wazo_confd.helpers.mallow import BaseSchema


class WhitelistSchema(BaseSchema):
    uuid = fields.UUID(dump_only=True)
    unique_id = fields.String(dump_only=True)
    url = fields.String(required=True)
    customer_name = fields.String(required=True)
