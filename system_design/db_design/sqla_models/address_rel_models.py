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


from .base_model import BaseSqlModel


class HouseNumber(BaseSqlModel):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    number: Mapped[str] = mapped_column(String)


class Street(BaseSqlModel):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)


class Country(BaseSqlModel):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)


class Region(BaseSqlModel):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    country_id: Mapped[int] = mapped_column(
        Integer, ForeignKey(Country.id), primary_key=True
    )


class District(BaseSqlModel):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    region_id: Mapped[int] = mapped_column(
        Integer, ForeignKey(Region.id), primary_key=True
    )


class SettlementType(BaseSqlModel):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)


class SettlementName(BaseSqlModel):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    district_id: Mapped[int] = mapped_column(
        Integer, ForeignKey(District.id), primary_key=True
    )
    settlement_type_id: Mapped[int] = mapped_column(
        Integer, ForeignKey(SettlementType.id), primary_key=True
    )


class StreetSettlementAssociation(BaseSqlModel):
    street_id: Mapped[int] = mapped_column(
        Integer, ForeignKey(Street.id), primary_key=True
    )
    settlement_name_id: Mapped[int] = mapped_column(
        Integer, ForeignKey(SettlementName.id), primary_key=True
    )


class Address(BaseSqlModel):
    house_number_id: Mapped[int] = mapped_column(
        Integer, ForeignKey(HouseNumber.id), primary_key=True
    )
    street_settlement_association_id: Mapped[int] = mapped_column(
        Integer, ForeignKey(StreetSettlementAssociation.id), primary_key=True
    )
