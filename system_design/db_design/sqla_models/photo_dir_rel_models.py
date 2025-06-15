from typing import TYPE_CHECKING

from sqlalchemy import (
    ForeignKey,
    String,
    Integer,
    ForeignKeyConstraint,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import BaseSqlModel

if TYPE_CHECKING:
    from .research_plant_assoc_rel_models import ResearchPlantAssociation
    from .leaves_template_photo_rel_models import LeavesTemplatePhoto


class PhotoDir(BaseSqlModel):
    __table_args__ = (
        ForeignKeyConstraint(
            ['par_research_id', 'par_plant_id'],
            ['ResearchPlantAssociation.research_id', 'ResearchPlantAssociation.plant_id']
        ),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    # parent keys
    # research_plant_association_id
    par_research_id: Mapped[int] = mapped_column(Integer)
    par_plant_id: Mapped[int] = mapped_column(Integer)

    name: Mapped[str] = mapped_column(String, unique=True)
    s3_key_joined_result_csv: Mapped[str] = mapped_column(String, unique=True)

    # rel
    # m2one
    research_plant_association: Mapped["ResearchPlantAssociation"] = relationship(back_populates="photo_dirs")

    # one2m
    leaves_template_photos: Mapped[list["LeavesTemplatePhoto"]] = relationship(back_populates="photo_dir")
