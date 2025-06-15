from typing import TYPE_CHECKING

from sqlalchemy import (
    ForeignKey,
    String,
    Integer,
    UniqueConstraint,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import BaseSqlModel

if TYPE_CHECKING:
    from .organization_rel_models import Organization
    from .user_rel_models import User


class JobTitle(BaseSqlModel):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)

    # rel
    # one2m
    jobs: Mapped[list["Job"]] = relationship(back_populates="job_title")

class Job(BaseSqlModel):
    __table_args__ = (
        UniqueConstraint("job_title_id", "organization_id"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    job_title_id: Mapped[int] = mapped_column(
        Integer, ForeignKey(JobTitle.id),
    )
    organization_id: Mapped[int] = mapped_column(
        Integer, ForeignKey(Organization.id),
    )

    # rel
    # m2one
    organization: Mapped["Organization"] = relationship(back_populates="jobs")
    job_title: Mapped["JobTitle"] = relationship(back_populates="jobs")
    
    # one2m
    users: Mapped[list["User"]] = relationship(back_populates="job")