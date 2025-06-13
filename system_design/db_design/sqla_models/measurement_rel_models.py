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
    from .morph_features_rel_models import MorphologicalFeature
    from .biochem_analysis_rel_models import BiochemFeature


class MeasurementUnit(BaseSqlModel):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True)
    
    # rel
    # one2m
    morphological_features: Mapped[list["MorphologicalFeature"]] = relationship(back_populates="measurement_unit")
    biochem_features: Mapped[list["BiochemFeature"]] = relationship(back_populates="measurement_unit")