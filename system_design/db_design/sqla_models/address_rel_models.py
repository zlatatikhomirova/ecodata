from datetime import datetime, date
import re
from uuid import uuid4

from sqlalchemy import (
    UUID,
    Column,
    DateTime,
    ForeignKey,
    MetaData,
    Numeric,
    String,
    Table,
    Date,
    Integer,
)
from sqlalchemy.orm import declared_attr, Mapped, mapped_column, relationship


from .base import BaseSqlModel
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .pollutions_rel_models import PollutionsNearPlace
    from .plant_rel_models import Plant

class HouseNumber(BaseSqlModel):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    number: Mapped[str] = mapped_column(String, nullable=False)

    # rel
    addresses: Mapped[list["Address"]] = relationship("Address", back_populates="house_number")


class Street(BaseSqlModel):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)

    # rel
    street_settlement_association: Mapped[list["StreetSettlementAssociation"]] = relationship("StreetSettlementAssociation",
                                                                                        back_populates="street")


class Country(BaseSqlModel):
    __tablename__ = 'countries'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)

    # Отношение один-ко-многим: страна → регионы
    regions: Mapped[list["Region"]] = relationship("Region", back_populates="country")

class Region(BaseSqlModel):
    __tablename__ = 'regions'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)

    country_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("countries.id"), nullable=False
    )

    # Отношение к Country
    country: Mapped["Country"] = relationship("Country", back_populates="regions")
    # Отношение: один Region -> много District
    districts: Mapped[list["District"]] = relationship("District", back_populates="region")


class District(BaseSqlModel):
    __tablename__ = 'districts'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)

    region_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("regions.id"), nullable=False
    )

    # Обратная связь к Region
    region: Mapped["Region"] = relationship("Region", back_populates="districts")
    settlements: Mapped[list["Settlement"]] = relationship("Settlement", back_populates="district")


class SettlementType(BaseSqlModel):
    __tablename__ = 'settlement_types'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)

    # Отношение один-ко-многим: тип → имена
    settlements: Mapped[list["Settlement"]] = relationship("Settlement", back_populates="settlement_type")

class Settlement(BaseSqlModel):
    __tablename__ = 'settlement_names'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)

    district_id: Mapped[int] = mapped_column(
        Integer, ForeignKey(District.id), nullable=False
    )
    settlement_type_id: Mapped[int] = mapped_column(
        Integer, ForeignKey(SettlementType.id), nullable=False
    )

    # Обратная связь к SettlementType
    settlement_type: Mapped["SettlementType"] = relationship("SettlementType", back_populates="settlements")
    district: Mapped["District"] = relationship("District", back_populates="settlements")
    street_settlement_association: Mapped[list["StreetSettlementAssociation"]] = relationship("StreetSettlementAssociation",
                                                                                        back_populates="settlement")


class StreetSettlementAssociation(BaseSqlModel):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    street_id: Mapped[int] = mapped_column(
        Integer, ForeignKey(Street.id), primary_key=True
    )
    settlement_name_id: Mapped[int] = mapped_column(
        Integer, ForeignKey(Settlement.id), primary_key=True
    )

    street: Mapped["Street"] = relationship("Street", back_populates="street_settlement_association")
    settlement: Mapped["Settlement"] = relationship("Settlement", back_populates="street_settlement_association")
    addresses: Mapped[list["Address"]] = relationship("Address", back_populates="street_settlement_association")

class Address(BaseSqlModel):
    house_number_id: Mapped[int] = mapped_column(
        Integer, ForeignKey(HouseNumber.id), primary_key=True
    )
    street_settlement_association_id: Mapped[int] = mapped_column(
        Integer, ForeignKey(StreetSettlementAssociation.id), primary_key=True
    )

    # rel
    street_settlement_association: Mapped["StreetSettlementAssociation"] = relationship("StreetSettlementAssociation",
                                                                                        back_populates="addresses",
                                                                                        )
    house_number: Mapped["HouseNumber"] = relationship("HouseNumber", back_populates="addresses")
    pollutions_near_place_list: Mapped[list["PollutionsNearPlace"]] = relationship(back_populates="address")

    plants: Mapped[list["Plant"]] = relationship(back_populates="address")

