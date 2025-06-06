from typing import Optional
from dataclasses import dataclass

@dataclass
class CreatePassword:
    name: str
    description: str
    login: str
    password: str
    time_to_change: int
    profile_id: int


@dataclass
class CreateProfile:
    title: str
    description: str
    service_name: str
    email: str
    phone: str
    email_password: str
