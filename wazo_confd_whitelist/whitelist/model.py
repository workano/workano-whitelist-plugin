from sqlalchemy import (
    Column,
    Integer,
    String
)
from xivo_dao.helpers.db_manager import UUIDAsString

from ..db import Base


class WhitelistModel(Base):
    __tablename__ = 'plugin_whitelist'

    id = Column(Integer, primary_key=True)
    tenant_uuid = Column(UUIDAsString(36), nullable=False)
    exten = Column(String(50), nullable=True)
    blocked_num = Column(String(50), nullable=False)