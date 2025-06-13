from datetime import datetime, date

from uuid import UUID as PyUUID, uuid4

from sqlalchemy.dialects.postgresql import UUID, DATERANGE
from psycopg2.extras import DateRange

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
    from .user_research_assoc_rel_models import UserResearchAssociation
    from .research_plant_assoc_rel_models import ResearchPlantAssociation

class Status(BaseSqlModel):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True)

    # rel
    researches: Mapped[list["Research"]] = relationship(back_populates="status")


class Research(BaseSqlModel):
    id: Mapped[PyUUID] = mapped_column(
        UUID, primary_key=True, default=uuid4, server_default=func.gen_random_uuid()
    )
    title: Mapped[str] = mapped_column(String, unique=True)
    goal: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(String)
    period: Mapped[DateRange] = mapped_column(DATERANGE())
    status_id: Mapped[int] = mapped_column(Integer, ForeignKey(Status.id))

    # rel
    user_research_associations: Mapped[list["UserResearchAssociation"]] = relationship(back_populates="research")
    status: Mapped["Status"] = relationship(back_populates="researches")
    research_plant_associations: Mapped[list["ResearchPlantAssociation"]] = relationship(back_populates="research")