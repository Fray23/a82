from typing import Optional
from dataclasses import dataclass


@dataclass
class PasswordModel:
    id: int
    name: str
    description: str
    login: str
    password: str
    time_to_change: int
    extra: dict
    profile_id: Optional[int]


@dataclass
class ProfileModel:
    id: int
    title: str
    description: str
    service_name: str
    email: str
    phone: str
    email_password: str
