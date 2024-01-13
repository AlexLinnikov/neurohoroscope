from datetime import datetime
import uuid
from typing import Optional

from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import relationship
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import Date
from sqlalchemy import DateTime
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class Base(DeclarativeBase):
    __DB_STRING = "sqlite://user:password@127.0.0.1/neurohoroscope"

    @classmethod
    def get_engine(cls) -> Engine:
        """Returns Engine instance"""

        return create_engine(
            cls.__DB_STRING,
            echo=True)

    @classmethod
    def init_db(cls) -> None:
        """Creating all Tables inherited by Base class if not exists"""

        cls.metadata.create_all(cls.get_engine())

    @classmethod
    def get_session(cls) -> Session:
        session = sessionmaker(cls.get_engine())
        return session()

    @classmethod
    def drop_db(cls) -> None:
        cls.metadata.drop_all(bind=cls.get_engine())


class Zodiacs(Base):
    __tablename__ = "zodiacs"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(32))
    description: Mapped[str] = mapped_column(Text)
    date_start: Mapped[str] = mapped_column(String(6))
    date_end: Mapped[str] = mapped_column(String(6))

    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now, onupdate=datetime.now)


class Years(Base):
    __tablename__ = "years"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(32))
    description: Mapped[str] = mapped_column(Text)
    value: Mapped[int]
    years_system_id = relationship("years_system.id")

    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now, onupdate=datetime.now)


class YearsSystem(Base):
    __tablename__ = "years_system"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(32))
    description: Mapped[str] = mapped_column(Text)

    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now, onupdate=datetime.now)


class Predictions(Base):
    __tablename__ = "predictions"

    id: Mapped[int] = mapped_column(primary_key=True)
    uuid: Mapped[str] = mapped_column(String(36), default=uuid.uuid4)

    name: Mapped[str] = mapped_column(String(64))
    birthday: Mapped[datetime] = mapped_column(Date)
    text: Mapped[Optional[str]] = mapped_column(Text)
    status: Mapped[str] = mapped_column(String(32), default="processing")
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now)
