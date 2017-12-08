from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
	String
)

from .meta import Base


class TblPatient(Base):
	__tablename__ = 'tbl_patient'
	patient_id = Column(Integer(), primary_key=True, nullable=False)
	patient_name = Column(String(70), nullable=False)
	patient_age = Column(Integer, nullable=False)
	patient_race = Column(String(70), nullable=False)
	
	def __init__(self, patient_name, patient_age, patient_race):
		self.patient_name = patient_name
		self.patient_age = patient_age
		self.patient_race = patient_race


# Index('my_index', MyModel.name, unique=True, mysql_length=255)
