from typing import TYPE_CHECKING

from sqlalchemy import (
    ForeignKey,
    String,
    Integer,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import BaseSqlModel, created_at_utc

if TYPE_CHECKING:
    from .photo_dir_rel_models import PhotoDir
    from .leaf_rel_models import Leaf

class LeavesTemplatePhoto(BaseSqlModel):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    photo_dir_id: Mapped[int] = mapped_column(Integer, ForeignKey(PhotoDir.id))
    s3_key_template: Mapped[str] = mapped_column(String, unique=True)
    s3_key_result_csv: Mapped[str] = mapped_column(String, unique=True)
    uploaded_at: Mapped[created_at_utc] # type: ignore

    # rel    
    # m2one
    photo_dir: Mapped["PhotoDir"] = relationship(back_populates="leaves_template_photos")

    # one2m
    leaves: Mapped[list["Leaf"]] = relationship(back_populates="leaves_template_photo")
    
