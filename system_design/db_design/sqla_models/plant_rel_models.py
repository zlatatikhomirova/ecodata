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


class LeafType(BaseSqlModel):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True)


class Genus(BaseSqlModel):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True)


class Species(BaseSqlModel):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True)


class LifeForm(BaseSqlModel):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True)


class PlantDescription(BaseSqlModel):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    life_form_id: Mapped[int] = mapped_column(Integer, ForeignKey(LifeForm.id))
    leaf_type_id: Mapped[int] = mapped_column(Integer, ForeignKey(LeafType.id))
    genus_id: Mapped[int] = mapped_column(Integer, ForeignKey(Genus.id))
    species_id: Mapped[int] = mapped_column(Integer, ForeignKey(Species.id))

class Plant(BaseSqlModel):
    id: Mapped[PyUUID] = mapped_column(
        UUID, primary_key=True, default=uuid4, server_default=func.gen_random_uuid()
    )
    address_id: Mapped[int] = mapped_column(
        Integer, ForeignKey(Address.id)
    )
    plant_description_id: Mapped[int] = mapped_column(
        Integer, ForeignKey(PlantDescription.id)
    )