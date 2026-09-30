from sqlmodel import SQLModel, Field
from datetime import datetime, timezone


class PortfolioBase(SQLModel):
    name: str = Field(index=True)
    description: str | None = Field(default=None)


class Portfolio(PortfolioBase):
    id: int = Field(primary_key=True)
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(
        timezone.utc), sa_column_kwargs={"onupdate": lambda: datetime.now(timezone.utc)})
