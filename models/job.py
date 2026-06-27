from sqlalchemy import Column,Integer,String,ForeignKey,relationship
from models.company import Company
from database import Base,engine,sessionLocal


class Job(Base):
    _tablename_="companies"
    id=Column(Integer,primary_key=True,index=True)
    title=Column(String,nullabel=False,description=Column(String))
    salary=Column(Integer)
    company_id=Column(Integer,ForeignKey("companied.id"))
    company=relationship("company",back_populates="jobs")