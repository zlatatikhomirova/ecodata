from typing import TYPE_CHECKING
from datetime import date

from uuid import UUID as PyUUID, uuid4
from sqlalchemy.dialects.postgresql import UUID

from sqlalchemy import (
    ForeignKey,
    String,
    Date,
    Integer,
    func,
    ForeignKeyConstraint,
)

from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import BaseSqlModel

if TYPE_CHECKING:
    from .job_rel_models import Job
    from .user_research_assoc_rel_models import UserResearchAssociation

class User(BaseSqlModel):
    id: Mapped[PyUUID] = mapped_column(
        UUID, primary_key=True, default=uuid4, server_default=func.gen_random_uuid()
    )
    name: Mapped[str] = mapped_column(String)
    surname: Mapped[str] = mapped_column(String)
    patronymic: Mapped[str] = mapped_column(String)
    job_id: Mapped[int] = mapped_column(Integer, ForeignKey(Job.id))
    phone: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String, unique=True)
    orcid_link: Mapped[str] = mapped_column(String, nullable=True)
    orcid_id: Mapped[str] = mapped_column(String, nullable=True)
    birthday: Mapped[date] = mapped_column(Date)
    username: Mapped[str] = mapped_column(String, unique=True)
    password_hash: Mapped[str] = mapped_column(String)

    # rel
    # m2one
    job: Mapped["Job"] = relationship(back_populates="users")
    # one2m
    user_research_associations: Mapped[list["UserResearchAssociation"]] = relationship(back_populates="user")