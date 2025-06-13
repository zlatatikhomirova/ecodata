import re

from sqlalchemy import MetaData, Integer, String
from sqlalchemy.orm import declared_attr, Mapped, mapped_column
from sqlalchemy.ext.declarative import as_declarative

from sqlalchemy import DateTime, func
from sqlalchemy.orm import Mapped, mapped_column
from typing import Annotated

import datetime

@as_declarative()
class BaseSqlModel:

    @declared_attr
    def __tablename__(cls) -> str:
        return re.sub(r"(?<!^)(?=[A-Z])", "_", cls.__name__).lower()

    metadata = MetaData(
        naming_convention={
            "ix": "ix_%(column_0_label)s",
            "uq": "uq_%(table_name)s_%(column_0_name)s",
            "ck": "ck_%(table_name)s_`%(constraint_name)s`",
            "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
            "pk": "pk_%(table_name)s",
        }
    )

class NameCategory(BaseSqlModel):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True)

intpk = Annotated[int, mapped_column(primary_key=True)]

created_at_utc = Annotated[datetime, mapped_column(
    DateTime(timezone=True),
    default=lambda: datetime.utcnow(),
    server_default=func.timezone("utc", func.now())
)]
updated_at_utc = Annotated[datetime, mapped_column(
    DateTime(timezone=True),
    default=lambda: datetime.utcnow(),
    server_default=func.timezone("utc", func.now()),
    onupdate=lambda: datetime.utcnow(),
    server_onupdate=func.timezone("utc", func.now())
)]

