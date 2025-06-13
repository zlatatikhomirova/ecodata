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


from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .organization_rel_models import Organization

class JobTitle(BaseSqlModel):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)

class Job(BaseSqlModel):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    job_title_id: Mapped[int] = mapped_column(
        Integer, ForeignKey(JobTitle.id), primary_key=True
    )
    organization_id: ...