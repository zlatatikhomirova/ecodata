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
    from .address_rel_models import Address
    from .job_rel_models import Job
    from .biochem_analysis_rel_models import BiochemAnalysis

class OrganizationDetails(BaseSqlModel):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String)
    phone: Mapped[str] = mapped_column(String)

    # rel
    organizations: Mapped[list["Organization"]] = mapped_column(back_populates="organization_details")

class OrganizationType(BaseSqlModel):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)

    # rel
    organizations: Mapped[list["Organization"]] = relationship(back_populates="organization_type")


class Organization(BaseSqlModel):
    id: Mapped[PyUUID] = mapped_column(
        UUID, primary_key=True, default=uuid4, server_default=func.gen_random_uuid()
    )
    address_id: Mapped[int] = mapped_column(
        Integer, ForeignKey(Address.id), primary_key=True
    )
    organization_details_id: Mapped[int] = mapped_column(
        Integer, ForeignKey(OrganizationDetails.id), primary_key=True
    )

    organization_type: Mapped[int] = mapped_column(
        Integer, ForeignKey(OrganizationType.id), primary_key=True
    )
    # rel
    organization_details: Mapped["OrganizationDetails"] = mapped_column(back_populates="organizations")
    jobs: Mapped[list["Job"]] = relationship(back_populates="organization")
    # one2m
    biochem_analysis_list: Mapped[list["BiochemAnalysis"]] = relationship(back_populates="organization")
    organization_type: Mapped["OrganizationType"] = relationship(back_populates="organizations")
