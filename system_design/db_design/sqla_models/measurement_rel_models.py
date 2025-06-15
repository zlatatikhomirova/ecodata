from typing import TYPE_CHECKING

from sqlalchemy import (
    String,
    Integer,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import BaseSqlModel

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