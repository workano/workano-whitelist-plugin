from sqlalchemy import (
    Column,
    Integer,
    String,
    ARRAY,
    Date,
    Boolean
)
from xivo_dao.helpers.db_manager import UUIDAsString

from ..db import Base


class WhitelistModel(Base):
    __tablename__ = 'plugin_whitelist'

    id = Column(Integer, primary_key=True)
    tenant_uuid = Column(UUIDAsString(36), nullable=False)
    ip_addresses = Column(ARRAY(String), nullable=True)  # List of IP addresses
    domains = Column(ARRAY(String), nullable=True)       # List of domains
    created_at = Column(Date, nullable=False)            # Creation date
    expire_at = Column(Date, nullable=False)             # Expiration date
    renew = Column(Boolean, nullable=False, default=False)  # Renewal status
