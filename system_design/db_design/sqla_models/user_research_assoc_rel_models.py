from datetime import datetime, date

from uuid import UUID as PyUUID, uuid4

from sqlalchemy.dialects.postgresql import UUID

from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    MetaData,
    Numeric,
    String,
    Table,
    Date,
    Integer,
    types,
    func,
)
from sqlalchemy.orm import declared_attr, Mapped, mapped_column, relationship

from .base import BaseSqlModel, NameCategory, created_at_utc
from .address_rel_models import Address

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .organization_rel_models import Organization

class Role(BaseSqlModel):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True)

class UserResearchAssociation(BaseSqlModel):
    research_id: Mapped[PyUUID] = mapped_column(
        UUID, ForeignKey(Research.id), primary_key=True
    )
    user_id: Mapped[PyUUID] = mapped_column(UUID, ForeignKey(User.id), primary_key=True)
    role_id: Mapped[int] = mapped_column(Integer, ForeignKey(Role.id))
