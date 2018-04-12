from sqlalchemy.orm import relationship, backref, joinedload
from sqlalchemy import Column, DateTime, String, Integer, Float, ForeignKey, func
from base import Base, inverse_relationship, create_tables

class Candidate(Base):
    __tablename__ = 'candidate'
    id = Column(Integer, primary_key=True)
    fec_id = Column(String, unique=True)
    name = Column(String)
    party = Column(String)
    relative_uri = Column(String)
    committee = Column(String)
    district = Column(String)
    state = Column(String)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    def parse_candidate(self, json_data):
        self.fec_id = json_data['candidate']['id']
        self.name = json_data['candidate']['name']
        self.party = json_data['candidate']['party']
        self.relative_uri = json_data['candidate']['relative_uri']
        self.committee = json_data['committee']
        self.district = json_data['district']
        self.state = json_data['state']
