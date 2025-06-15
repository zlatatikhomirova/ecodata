from typing import TYPE_CHECKING

from sqlalchemy import (
    ForeignKey,
    String,
    Integer,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import BaseSqlModel

if TYPE_CHECKING:
    from .leaf_rel_models import Leaf
    from.measurement_rel_models import MeasurementUnit
    
class MorphologicalFeature(BaseSqlModel):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True)
    measurement_unit_id: Mapped[int] = mapped_column(Integer, ForeignKey(MeasurementUnit.id))

    # rel
    # m2one
    measurement_unit: Mapped["MeasurementUnit"] = relationship(back_populates="morphological_features")
    # one2m
    morphological_features_leaf_associations: Mapped[list["MorphologicalFeatureLeafAssociation"]] = relationship(
        back_populates="morphological_feature",
    )

class MorphologicalFeatureLeafAssociation(BaseSqlModel):
    morphological_feature_id: Mapped[int] = mapped_column(Integer, ForeignKey(MorphologicalFeature.id), primary_key=True)
    leaf_id: Mapped[int] = mapped_column(Integer, ForeignKey(Leaf.id), primary_key=True)
    value: Mapped[int] = mapped_column(Integer)

    # rel
    # m2one
    leaf: Mapped["Leaf"] = relationship(back_populates="morphological_features_leaf_associations")
    morphological_feature: Mapped["MorphologicalFeature"] = relationship(back_populates="morphological_features_leaf_associations")