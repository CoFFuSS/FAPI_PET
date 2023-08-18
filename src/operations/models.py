import datetime

from sqlalchemy import Integer, String, TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeMeta, declarative_base

Base: DeclarativeMeta = declarative_base()


class Operation(Base):
    __tablename__ = 'operation'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    quantity: Mapped[str] = mapped_column(String)
    figi: Mapped[str] = mapped_column(String)
    instrument_type: Mapped[str] = mapped_column(String, nullable=True)
    date: Mapped[datetime] = mapped_column(TIMESTAMP)
    type: Mapped[str] = mapped_column(String)

    class Config:
        orm_mode = True


# class Operation(BaseModel):
#     id: int
#     quantity: str
#     figi: str
#     instrument_type: str
#     date: datetime.datetime
#     type: str
#
#     class Config:
#         orm_mode = True
