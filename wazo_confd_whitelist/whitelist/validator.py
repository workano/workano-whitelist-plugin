from xivo_dao.resources.whitelist import dao as whitelist_dao

from wazo_confd.helpers.validator import (
    UniqueField,
    UniqueFieldChanged,
    ValidationGroup,
)


def build_whitelist_validator():
    return ValidationGroup(
        create=[
            UniqueField(
                'ip_addresses',
                lambda ip_addresses, tenant_uuids: whitelist_dao.find_by(
                    ip_addresses=ip_addresses, tenant_uuids=tenant_uuids
                ),
                'Whitelist entry with same IP addresses already exists',
            ),
            UniqueField(
                'domains',
                lambda domains, tenant_uuids: whitelist_dao.find_by(
                    domains=domains, tenant_uuids=tenant_uuids
                ),
                'Whitelist entry with same domains already exists',
            )
        ],
        edit=[
            UniqueFieldChanged(
                'ip_addresses', whitelist_dao.find_by, 'Whitelist entry with same IP addresses already exists'
            ),
            UniqueFieldChanged(
                'domains', whitelist_dao.find_by, 'Whitelist entry with same domains already exists'
            )
        ],
    )
