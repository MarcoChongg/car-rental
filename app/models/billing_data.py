
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, CheckConstraint
from sqlalchemy.orm import relationship

from db.db_setup import Base
from .mixins import Timestamp

#from .user import User

class BillingData(Timestamp, Base):
    __tablename__ = "billing_data"

    id = Column(Integer, primary_key=True, index=True)
    rfc = Column(String(20), nullable=False)
    full_name = Column(String(50), nullable=True)
    company_name = Column(String(50), nullable=True)
    #postal_code = Column(String(7), null=False)
    is_active = Column(Boolean, default=True)
    tax_regimen = Column(String(50), nullable=False)

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    user = relationship("User", back_populates="billing_data", cascade="all,delete")

    __table_args__ = (
        CheckConstraint(
            '(full_name IS NOT NULL AND company_name IS NULL) OR (full_name IS NULL AND company_name IS NOT NULL)',
            name='one_column_null_constraint'
        ),
    )