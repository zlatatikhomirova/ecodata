from typing import TYPE_CHECKING
from uuid import UUID as PyUUID

from sqlalchemy.dialects.postgresql import UUID

from sqlalchemy import (
    ForeignKey,
    String,
    Integer,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import BaseSqlModel

if TYPE_CHECKING:
    from .research_rel_models import Research
    from .plant_rel_models import Plant
    from .photo_dir_rel_models import PhotoDir
    from .biochem_analysis_rel_models import BiochemAnalysis

class ResearchPlantAssociation(BaseSqlModel):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    research_id: Mapped[PyUUID] = mapped_column(
        UUID, ForeignKey(Research.id), primary_key=True
    )
    plant_id: Mapped[PyUUID] = mapped_column(
        UUID, ForeignKey(Plant.id), primary_key=True
    )
    s3_key_final_morphological_result: Mapped[str] = mapped_column(String, unique=True)

    # rel
    # m2one
    research: Mapped["Research"] = relationship(back_populates="research_plant_associations")
    plant: Mapped["Plant"] = relationship(back_populates="research_plant_associations")

    # one2m
    photo_dirs: Mapped[list["PhotoDir"]] = relationship(back_populates="research_plant_association")
    biochem_analysis_list: Mapped[list["BiochemAnalysis"]] = relationship(back_populates="research_plant_association")