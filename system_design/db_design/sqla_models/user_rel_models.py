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
    __table_args__ = (
        ForeignKeyConstraint(
            ['par_job_title_id', 'par_organization_id'],
            ['Job.job_title_id', 'Job.organization_id']
        ),
    )

    id: Mapped[PyUUID] = mapped_column(
        UUID, primary_key=True, default=uuid4, server_default=func.gen_random_uuid()
    )
    name: Mapped[str] = mapped_column(String)
    surname: Mapped[str] = mapped_column(String)
    patronymic: Mapped[str] = mapped_column(String)

    # parent keys
    par_job_title_id: Mapped[int] = mapped_column(Integer)
    par_organization_id: Mapped[int] = mapped_column(Integer)

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