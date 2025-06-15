from typing import TYPE_CHECKING

from sqlalchemy import (
    ForeignKey,
    String,
    Integer,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import BaseSqlModel

if TYPE_CHECKING:
    from .address_rel_models import Address


class PollutionType(BaseSqlModel):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True)

    # rel
    # one2m
    pollutions_near_place_list: Mapped[list["PollutionsNearPlace"]] = relationship(
        "PollutionsNearPlace", back_populates="pollution_type"
    )


class PollutionsNearPlace(BaseSqlModel):
    address_id: Mapped[int] = mapped_column(Integer, ForeignKey(Address.id))
    pollution_type_id: Mapped[int] = mapped_column(Integer, ForeignKey(PollutionType.id))

    # rel
    # m2one
    address: Mapped["Address"] = relationship(
        back_populates="pollutions_near_place_list"
    )
    pollution_type: Mapped["PollutionType"] = relationship(
        back_populates="pollutions_near_place_list"
    )
