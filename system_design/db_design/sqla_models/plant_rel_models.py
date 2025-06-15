from typing import TYPE_CHECKING
from uuid import UUID as PyUUID, uuid4

from sqlalchemy.dialects.postgresql import UUID

from sqlalchemy import (
    ForeignKey,
    String,
    Integer,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import BaseSqlModel

if TYPE_CHECKING:
    from .address_rel_models import Address
    from .research_plant_assoc_rel_models import ResearchPlantAssociation


class LeafType(BaseSqlModel):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True)

    # rel
    # one2m
    plants_descriptions: Mapped[list["PlantDescription"]] = relationship(back_populates="leaf_type")


class Genus(BaseSqlModel):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True)

    # rel
    # one2m
    plants_descriptions: Mapped[list["PlantDescription"]] = relationship(back_populates="genus")

class Species(BaseSqlModel):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True)

    # rel
    # one2m
    plants_descriptions: Mapped[list["PlantDescription"]] = relationship(back_populates="species")

class LifeForm(BaseSqlModel):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True)

    # rel
    # one2m
    plants_descriptions: Mapped[list["PlantDescription"]] = relationship(back_populates="life_form")

class PlantDescription(BaseSqlModel):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    life_form_id: Mapped[int] = mapped_column(Integer, ForeignKey(LifeForm.id))
    leaf_type_id: Mapped[int] = mapped_column(Integer, ForeignKey(LeafType.id))
    genus_id: Mapped[int] = mapped_column(Integer, ForeignKey(Genus.id))
    species_id: Mapped[int] = mapped_column(Integer, ForeignKey(Species.id))
    description: Mapped[str] = mapped_column(String)

    # rel
    # m2one
    leaf_type: Mapped["LeafType"] = relationship(back_populates="plants_descriptions")
    genus: Mapped["Genus"] = relationship(back_populates="plants_descriptions")
    species: Mapped["Species"] = relationship(back_populates="plants_descriptions")
    life_form: Mapped["LifeForm"] = relationship(back_populates="plants_descriptions")

    # one2m
    plants: Mapped[list["Plant"]] = relationship(back_populates="plant_description")

class Plant(BaseSqlModel):
    id: Mapped[PyUUID] = mapped_column(
        UUID, primary_key=True, default=uuid4, server_default=func.gen_random_uuid()
    )
    address_id: Mapped[PyUUID] = mapped_column(
        UUID, ForeignKey(Address.id)
    )
    plant_description_id: Mapped[int] = mapped_column(
        Integer, ForeignKey(PlantDescription.id)
    )
    additional_info: Mapped[str] = mapped_column(String)

    # rel
    # m2one
    plant_description: Mapped["PlantDescription"] = relationship(back_populates="plants")
    address: Mapped["Address"] = relationship(back_populates="plants")

    # one2m
    research_plant_associations: Mapped[list["ResearchPlantAssociation"]] = relationship(back_populates="plant")

   