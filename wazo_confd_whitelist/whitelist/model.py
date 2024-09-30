# model.py
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from xivo_dao.helpers.db_manager import UUIDAsString
from ..db import Base
import uuid


class WhitelistModel(Base):
    __tablename__ = 'plugin_whitelist'

    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    unique_id = Column(String, unique=True, nullable=False, default=lambda: str(uuid.uuid4()))
    url = Column(String, nullable=False)
    customer_name = Column(String, nullable=False)
