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


class PollutionType(BaseSqlModel):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True)

    # rel
    pollutions_near_place_list: Mapped[list["PollutionsNearPlace"]] = relationship(
        "PollutionsNearPlace", back_populates="pollution_type"
    )


class PollutionsNearPlace(BaseSqlModel):
    address_id: Mapped[int] = mapped_column(Integer, ForeignKey(Address.id))
    pollution_id: Mapped[int] = mapped_column(Integer, ForeignKey(PollutionType.id))

    # rel
    address: Mapped["Address"] = relationship(
        "Address", back_populates="pollutions_near_place_list"
    )
    pollution_type: Mapped["PollutionType"] = relationship(
        "PollutionType", back_populates="pollutions_near_place_list"
    )
