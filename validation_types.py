"""This module contains all project-unique data types"""

from typing import TypedDict


class AddressType(TypedDict):
    """Type for validation addresses"""

    city: str
    district: str
    street: str
    house_number: int

