from typing import TYPE_CHECKING

from sqlalchemy import (
    ForeignKey,
    String,
    Integer,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import BaseSqlModel

if TYPE_CHECKING:
    from .leaves_template_photo_rel_models import LeavesTemplatePhoto
    from .morph_features_rel_models import MorphologicalFeatureLeafAssociation

class LocationOnPlant(BaseSqlModel):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True)
    
    # rel 
    # one2m
    leaves: Mapped[list["Leaf"]] = relationship(back_populates="location_on_plant")

class SideOfTheWorld(BaseSqlModel):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True)

    # rel
    # one2m
    leaves: Mapped[list["Leaf"]] = relationship(back_populates="side_of_the_world")


class Leaf(BaseSqlModel):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    side_of_the_world_id: Mapped[int] = mapped_column(Integer, ForeignKey(SideOfTheWorld.id))
    location_on_plant_id: Mapped[int] = mapped_column(Integer, ForeignKey(LocationOnPlant.id))
    s3_key_leaf_info: Mapped[str] = mapped_column(String, unique=True)
    s3_key_leaf_mask: Mapped[str] = mapped_column(String, unique=True)

    # rel
    # m2one
    leaves_template_photo: Mapped["LeavesTemplatePhoto"] = relationship(back_populates="leaves")
    location_on_plant: Mapped["LocationOnPlant"] = relationship(back_populates="leaves")
    side_of_the_world: Mapped["SideOfTheWorld"] = relationship(back_populates="leaves")

    # one2m
    morphological_features_leaf_associations: Mapped[list["MorphologicalFeatureLeafAssociation"]] = relationship(back_populates="leaf")