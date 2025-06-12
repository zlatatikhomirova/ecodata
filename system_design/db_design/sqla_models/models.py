from datetime import datetime, date

from uuid import uuid4

from sqlalchemy import UUID, Column, DateTime, ForeignKey, MetaData, Numeric, String, Table, Date, Integer
from sqlalchemy.orm import declared_attr, Mapped, mapped_column, relationship

from .base_model import BaseSqlModel
from .address_rel_models import Address

class JobTitle(BaseSqlModel):
    id: ...
    name: ...

class OrganizationDetails(BaseSqlModel):
    id: ...
    name: ...
    email: ...
    phone: ...

class Organization(BaseSqlModel):
    address_id: ...
    oranization_details_id: ...

class Job(BaseSqlModel):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    job_title_id: ...

class User(BaseSqlModel):
    id: Mapped[UUID] = mapped_column(UUID, primary_key=True, default=uuid4)
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
    name: ...

class Research(BaseSqlModel):
    id: Mapped[UUID] = mapped_column(UUID, primary_key=True, default=uuid4)
    title: ...
    goal: ...
    description: ...
    dates: ...
    status_id: ...

class UserResearchAssociation(BaseSqlModel):
    research_id : ...
    user_id: ...
    role_id: Mapped[int] = mapped_column(Integer, ForeignKey(Role.id))

class LeafType(BaseSqlModel):
    id: ...
    name: ...

class Genus(BaseSqlModel):
    id: ...
    name: ...

class Spesies(BaseSqlModel):
    id: ...
    name: ...

class PlantDescription(BaseSqlModel):
    id: ...
    life_form: ...
    leaf_type_id: ...
    genus_id: ...
    species_id: ...

class PollutionsNearPlace(BaseSqlModel):
    address_id: ...
    pollution_id: ...

class Pollution(BaseSqlModel):
    id: ...
    name: ...

class Plant(BaseSqlModel):
    address_id: ...
    plant_description_id: ...


class ResearchPlantAssociation(BaseSqlModel):
    research_id: ...
    plant_id: ...
    s3_key_final_morphological_result: ...

class PhotoDir(BaseSqlModel):
    id: ...
    research_plant_association_id: ...
    name: ...
    s3_key_joined_result_csv: ...

class LeavesTemplatePhoto(BaseSqlModel):
    id: ...
    photo_dir_id: ...
    s3_key_template: ...
    s3_key_result_csv: ...
    file_size: ...
    uploaded_at: ...

class BiochemAnalysis(BaseSqlModel):
    id: ...
    date: ...
    additional_info: ...
    research_plant_association_id: ...
    organization_id: ...
    s3_key: ...


class BiochemAnalysisFeatureAssociation(BaseSqlModel):
    biochem_analysis_id: ...
    biochem_feature_id: ...
    value: ...

class BiochemFeature(BaseSqlModel):
    id: ...
    name: ...
    measurement_unit_id: ...

class MeasurementUnit(BaseSqlModel):
    id: ...
    name: ...

class MorphologicalFeature(BaseSqlModel):
    id: ...
    name: ...
    measurement_unit_id: ...

class MorphologicalFeatureLeafAssociation(BaseSqlModel):
    morphological_feature_id: ...
    leaf_id: ...
    value: ...

class Leaf(BaseSqlModel):
    id: ...
    side_of_the_world: ...
    location_on_plant: ...
    s3_key_leaf_info: ...
    s3_key_leaf_mask: ...







    


class Place(BaseSqlModel):
    country: Mapped[str] = mapped_column(String)
    region: Mapped[str] = mapped_column(String)
    city: Mapped[str] = mapped_column(String)
    district: Mapped[str] = mapped_column(String)
    type_of_settlement: Mapped[str] = mapped_column(String)
    
    plants: Mapped[list["Plant"]] = relationship(back_populates="place")





class Plant(BaseSqlModel):
    form: Mapped[str] = mapped_column(String)
    sheet_type: Mapped[str] = mapped_column(String)
    family: Mapped[str] = mapped_column(String)
    type: Mapped[str] = mapped_column(String)
    place_id = mapped_column(ForeignKey(Place.id))
    
    place: Mapped[Place] = relationship(back_populates="plants")
    researches: Mapped[list["Research"]] = relationship(back_populates="plant")


class Research(BaseSqlModel):
    name: Mapped[str] = mapped_column(String, nullable=False)
    target: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    start_date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    end_date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    status: Mapped[str] = mapped_column(String)
    plant_id = mapped_column(ForeignKey(Plant.id))
    
    plant: Mapped[Plant] = relationship(back_populates="researches")


class Article(BaseSqlModel):
    name: Mapped[str] = mapped_column(String, nullable=False)
    plant_id = mapped_column(ForeignKey(Plant.id))
    journal_name: Mapped[str] = mapped_column(String)
    link: Mapped[str] = mapped_column(String)
    file: Mapped[str] = mapped_column(String)


class Laboratory(BaseSqlModel):
    name: Mapped[str] = mapped_column(String, nullable=False)
    address: Mapped[str] = mapped_column(String, nullable=False)
    phone: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False)
    
    
class Leaf(BaseSqlModel):
    plant_id = mapped_column(ForeignKey(Plant.id))
    date_of_measurement: Mapped[datetime] = mapped_column(DateTime)
    side_of_the_world: Mapped[str] = mapped_column(String)
    unit: Mapped[str] = mapped_column(String, nullable=False)
    photo: Mapped[str] = mapped_column(String, nullable=False)
    location_on_the_plant: Mapped[str] = mapped_column(String, nullable=False)
    
    
class BioChem(BaseSqlModel):
    chlorophyll_a: Mapped[float] = mapped_column(Numeric)
    chlorophyll_b: Mapped[float] = mapped_column(Numeric)
    carotenoids: Mapped[float] = mapped_column(Numeric)
    phenols: Mapped[float] = mapped_column(Numeric)
    anthocyanins: Mapped[float] = mapped_column(Numeric)
    peroxidase: Mapped[float] = mapped_column(Numeric)
    vitamin_c: Mapped[float] = mapped_column(Numeric)
    unit: Mapped[str] = mapped_column(String, nullable=False)
    note: Mapped[str] = mapped_column(String, nullable=False)
    analysis_date: Mapped[datetime] = mapped_column(DateTime)
    laboratory_id = mapped_column(ForeignKey(Laboratory.id))
    plant_id = mapped_column(ForeignKey(Plant.id))
    
    
class MorphologicalFeature(BaseSqlModel):
    area: Mapped[float] = mapped_column(Numeric)
    length: Mapped[float] = mapped_column(Numeric)
    left_second_vein_length: Mapped[float] = mapped_column(Numeric)
    right_second_vein_length: Mapped[float] = mapped_column(Numeric)
    left_btw_first_n_second_veins_ends_dist: Mapped[float] = mapped_column(Numeric)
    right_btw_first_n_second_veins_ends_dist: Mapped[float] = mapped_column(Numeric)
    left_btw_first_n_second_veins_begins_dist: Mapped[float] = mapped_column(Numeric)
    right_btw_first_n_second_veins_begins_dist: Mapped[float] = mapped_column(Numeric)
    left_btw_second_n_central_veins_angle: Mapped[float] = mapped_column(Numeric)
    right_btw_second_n_central_veins_angle: Mapped[float] = mapped_column(Numeric)
    left_halfs_width: Mapped[float] = mapped_column(Numeric)
    right_halfs_width: Mapped[float] = mapped_column(Numeric)
    leaf_id = mapped_column(ForeignKey(Leaf.id))

    
order_mtm_product_table = Table(
    'specialist_in_research',
    BaseSqlModel.metadata,
    Column('research_id', ForeignKey('research.id')),
    Column('specialist_id', ForeignKey('specialist.id')),
)

    