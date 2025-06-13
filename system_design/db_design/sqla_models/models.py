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


class JobTitle(BaseSqlModel):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)

    # relationships
    organization_details_list: Mapped[list["Organization"]] = relationship(
        back_populates="job_title",
    )


class OrganizationDetails(BaseSqlModel):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String)
    phone: Mapped[str] = mapped_column(String)

    # relationships
    job_titles: Mapped[list["Organization"]] = relationship(
        back_populates="organization_details",
    )


class Organization(BaseSqlModel):
    id: Mapped[PyUUID] = mapped_column(
        UUID, primary_key=True, default=uuid4, server_default=func.gen_random_uuid()
    )
    address_id: Mapped[int] = mapped_column(
        Integer, ForeignKey(Address.id), primary_key=True
    )
    organization_details_id: Mapped[int] = mapped_column(
        Integer, ForeignKey(OrganizationDetails.id), primary_key=True
    )

    # relationships
    job_title: Mapped["JobTitle"] = relationship(
        back_populates="organization_details_list"
    )
    organization_details: Mapped["OrganizationDetails"] = relationship(
        back_populates="job_titles"
    )


class Job(BaseSqlModel):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    job_title_id: Mapped[int] = mapped_column(
        Integer, ForeignKey(JobTitle.id), primary_key=True
    )


class User(BaseSqlModel):
    id: Mapped[PyUUID] = mapped_column(
        UUID, primary_key=True, default=uuid4, server_default=func.gen_random_uuid()
    )
    name: Mapped[str] = mapped_column(String)
    surname: Mapped[str] = mapped_column(String)
    patronymic: Mapped[str] = mapped_column(String)
    job_id: Mapped[int] = mapped_column(Integer, ForeignKey(Job.id))
    phone: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String, unique=True)
    orcid_link: Mapped[str] = mapped_column(String, unique=True)
    orcid_id: Mapped[str] = mapped_column(String, unique=True)
    birthday: Mapped[date] = mapped_column(Date)
    username: Mapped[str] = mapped_column(String, unique=True)
    password_hash: Mapped[str] = mapped_column(String)


class Role(BaseSqlModel):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True)


class Status(BaseSqlModel):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True)


class Research(BaseSqlModel):
    id: Mapped[PyUUID] = mapped_column(
        UUID, primary_key=True, default=uuid4, server_default=func.gen_random_uuid()
    )
    title: Mapped[str] = mapped_column(String, unique=True)
    goal: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(String)
    dates: ...
    status_id: Mapped[int] = mapped_column(Integer, ForeignKey(Status.id))


class UserResearchAssociation(BaseSqlModel):
    research_id: Mapped[PyUUID] = mapped_column(
        UUID, ForeignKey(Research.id), primary_key=True
    )
    user_id: Mapped[PyUUID] = mapped_column(UUID, ForeignKey(User.id), primary_key=True)
    role_id: Mapped[int] = mapped_column(Integer, ForeignKey(Role.id))


class LeafType(BaseSqlModel):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True)


class Genus(BaseSqlModel):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True)


class Species(BaseSqlModel):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True)


class LifeForm(BaseSqlModel):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True)


class PlantDescription(BaseSqlModel):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    life_form_id: Mapped[int] = mapped_column(Integer, ForeignKey(LifeForm.id))
    leaf_type_id: Mapped[int] = mapped_column(Integer, ForeignKey(LeafType.id))
    genus_id: Mapped[int] = mapped_column(Integer, ForeignKey(Genus.id))
    species_id: Mapped[int] = mapped_column(Integer, ForeignKey(Species.id))


class Pollution(BaseSqlModel):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True)


class PollutionsNearPlace(BaseSqlModel):
    address_id: Mapped[int] = mapped_column(Integer, ForeignKey(Address.id))
    pollution_id: Mapped[int] = mapped_column(Integer, ForeignKey(Pollution.id))

class Plant(BaseSqlModel):
    id: Mapped[PyUUID] = mapped_column(
        UUID, primary_key=True, default=uuid4, server_default=func.gen_random_uuid()
    )
    address_id: Mapped[int] = mapped_column(
        Integer, ForeignKey(Address.id)
    )
    plant_description_id: Mapped[int] = mapped_column(
        Integer, ForeignKey(PlantDescription.id)
    )

class ResearchPlantAssociation(BaseSqlModel):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    research_id: Mapped[PyUUID] = mapped_column(
        UUID, ForeignKey(Research.id), primary_key=True
    )
    plant_id: Mapped[PyUUID] = mapped_column(
        UUID, ForeignKey(Research.id), primary_key=True
    )
    s3_key_final_morphological_result: Mapped[str] = mapped_column(String, unique=True)


class PhotoDir(BaseSqlModel):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    research_plant_association_id:  Mapped[int] = mapped_column(Integer, ForeignKey(ResearchPlantAssociation.id))
    name: Mapped[str] = mapped_column(String, unique=True)
    s3_key_joined_result_csv: Mapped[str] = mapped_column(String, unique=True)


class LeavesTemplatePhoto(BaseSqlModel):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    photo_dir_id: Mapped[int] = mapped_column(Integer, ForeignKey(PhotoDir.id))
    s3_key_template: Mapped[str] = mapped_column(String, unique=True)
    s3_key_result_csv: Mapped[str] = mapped_column(String, unique=True)
    uploaded_at: Mapped[created_at_utc] # type: ignore

class MeasurementUnit(BaseSqlModel):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True)

class BiochemAnalysis(BaseSqlModel):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    date: Mapped[date] = mapped_column(Date) # type: ignore
    additional_info: Mapped[str] = mapped_column(String)
    research_plant_association_id: Mapped[int] = mapped_column(Integer, ForeignKey(ResearchPlantAssociation.id))
    organization_id: Mapped[int] = mapped_column(Integer, ForeignKey(Organization.id))
    s3_key: Mapped[str] = mapped_column(String, unique=True)

class BiochemFeature(BaseSqlModel):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True)
    measurement_unit_id: Mapped[int] = mapped_column(Integer, ForeignKey(MeasurementUnit.id))

class BiochemAnalysisFeatureAssociation(BaseSqlModel):
    biochem_analysis_id: Mapped[int] = mapped_column(Integer, ForeignKey(BiochemAnalysis.id))
    biochem_feature_id: Mapped[int] = mapped_column(Integer, ForeignKey(BiochemFeature.id))
    value: Mapped[int] = mapped_column(Integer)

class MorphologicalFeature(BaseSqlModel):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True)
    measurement_unit_id: Mapped[int] = mapped_column(Integer, ForeignKey(MeasurementUnit.id))

class LocationOnPlant(BaseSqlModel):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True)

class SideOfTheWorld(BaseSqlModel):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True)

class Leaf(BaseSqlModel):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    side_of_the_world_id: Mapped[int] = mapped_column(Integer, ForeignKey(SideOfTheWorld.id), primary_key=True)
    location_on_plant_id: Mapped[int] = mapped_column(Integer, ForeignKey(LocationOnPlant.id), primary_key=True)
    s3_key_leaf_info: Mapped[str] = mapped_column(String, unique=True)
    s3_key_leaf_mask: Mapped[str] = mapped_column(String, unique=True)

class MorphologicalFeatureLeafAssociation(BaseSqlModel):
    morphological_feature_id: Mapped[int] = mapped_column(Integer, ForeignKey(MorphologicalFeature.id), primary_key=True)
    leaf_id: Mapped[int] = mapped_column(Integer, ForeignKey(Leaf.id), primary_key=True)
    value: Mapped[int] = mapped_column(Integer)