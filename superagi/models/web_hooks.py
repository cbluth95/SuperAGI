from sqlalchemy import Column, Integer, Text, String, Boolean, ForeignKey,JSON
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import JSONB
from superagi.models.base_model import DBBaseModel
from superagi.models.agent_execution import AgentExecution

class WebHooks(DBBaseModel):
    """

    Attributes:
        

    Methods:
    """
    __tablename__ = 'web_hooks'

    id = Column(Integer, primary_key=True)
    name=Column(String)
    org_id = Column(Integer)
    url = Column(String)
    headers=Column(JSON)
    isDeleted=Column(Boolean)