from sqlalchemy import String,Text,Float,Boolean,ForeignKey
from sqlalchemy.orm import Mapped,mapped_column
from .db import Base
class User(Base):
 __tablename__='users'
 id:Mapped[int]=mapped_column(primary_key=True)
 email:Mapped[str]=mapped_column(String(255),unique=True,index=True)
 hashed_password:Mapped[str]=mapped_column(String(255))
 role:Mapped[str]=mapped_column(String(30),default='student')
class Concept(Base):
 __tablename__='concepts'
 id:Mapped[int]=mapped_column(primary_key=True)
 title:Mapped[str]=mapped_column(String(200))
 content:Mapped[str]=mapped_column(Text,default='')
class LearningProgress(Base):
 __tablename__='learning_progress'
 id:Mapped[int]=mapped_column(primary_key=True)
 user_id:Mapped[int]=mapped_column(ForeignKey('users.id'))
 concept_id:Mapped[int]=mapped_column(ForeignKey('concepts.id'))
 mastery:Mapped[float]=mapped_column(Float,default=0)
