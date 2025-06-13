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
    from .organization_rel_models import Organization
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
    
