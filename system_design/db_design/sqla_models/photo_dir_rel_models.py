from typing import TYPE_CHECKING
from uuid import UUID as PyUUID, uuid4

from sqlalchemy.dialects.postgresql import UUID

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
    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    research_plant_association_id: Mapped[PyUUID] = mapped_column(
        UUID, ForeignKey(ResearchPlantAssociation.id)
    )

    name: Mapped[str] = mapped_column(String, unique=True)
    s3_key_joined_result_csv: Mapped[str] = mapped_column(String, unique=True)

    # rel
    # m2one
    research_plant_association: Mapped["ResearchPlantAssociation"] = relationship(back_populates="photo_dirs")

    # one2m
    leaves_template_photos: Mapped[list["LeavesTemplatePhoto"]] = relationship(back_populates="photo_dir")
