from typing import TYPE_CHECKING
from uuid import UUID as PyUUID, uuid4

from sqlalchemy.dialects.postgresql import UUID

from sqlalchemy import (
    ForeignKey,
    String,
    Integer,
    func,
    UniqueConstraint,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import BaseSqlModel

if TYPE_CHECKING:
    from .address_rel_models import Address
    from .job_rel_models import Job
    from .biochem_analysis_rel_models import BiochemAnalysis

class OrganizationDetails(BaseSqlModel):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String)
    phone: Mapped[str] = mapped_column(String)

    # rel
    # one2m
    organizations: Mapped[list["Organization"]] = mapped_column(back_populates="organization_details")

class OrganizationType(BaseSqlModel):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)

    # rel
    # one2m
    organizations: Mapped[list["Organization"]] = relationship(back_populates="organization_type")


class Organization(BaseSqlModel):
    __table_args__ = (
        UniqueConstraint("address_id", "organization_details_id"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    address_id: Mapped[PyUUID] = mapped_column(
        UUID, ForeignKey(Address.id)
    )

    organization_details_id: Mapped[int] = mapped_column(
        Integer, ForeignKey(OrganizationDetails.id)
    )

    organization_type_id: Mapped[int] = mapped_column(
        Integer, ForeignKey(OrganizationType.id)
    )
    # rel
    # m2one
    organization_details: Mapped["OrganizationDetails"] = mapped_column(back_populates="organizations")
    organization_type: Mapped["OrganizationType"] = relationship(back_populates="organizations")
    address: Mapped["Address"] = relationship(back_populates="organizations")
    
    # one2m
    jobs: Mapped[list["Job"]] = relationship(back_populates="organization")
    biochem_analysis_list: Mapped[list["BiochemAnalysis"]] = relationship(back_populates="organization")
    
