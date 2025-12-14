# models.py
from dataclasses import dataclass
from typing import Optional


@dataclass
class User:
username: str
role: str
password_hash: Optional[str] = None


@dataclass
class SecurityIncident:
incident_id: str
timestamp: str
campaign: str
severity: str
assigned_to: str
status: str
resolution_time_hours: float
raw_details: str


@dataclass
class DatasetMeta:
dataset_name: str
owner: str
rows: int
size_mb: float
last_accessed: str
source: str
lineage: str


@dataclass
class ITTicket:
ticket_id: str
opened_at: str
closed_at: Optional[str]
status: str
owner: str
assigned_to: str
queue_stage: str
resolution_hours: Optional[float]
notes: Optional[str]