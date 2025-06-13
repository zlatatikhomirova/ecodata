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
    from .user_rel_models import User


class JobTitle(BaseSqlModel):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)

    # rel
    jobs: Mapped[list["Job"]] = relationship(back_populates="job_title")

class Job(BaseSqlModel):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    job_title_id: Mapped[int] = mapped_column(
        Integer, ForeignKey(JobTitle.id), primary_key=True
    )
    organization_id: Mapped[int] = mapped_column(
        Integer, ForeignKey(Organization.id), primary_key=True
    )

    # rel
    organization: Mapped["Organization"] = relationship(back_populates="jobs")
    job_title: Mapped["JobTitle"] = relationship(back_populates="jobs")
    users: Mapped[list["User"]] = relationship(back_populates="job")