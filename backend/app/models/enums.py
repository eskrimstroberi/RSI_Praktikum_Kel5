from enum import Enum


class RoleName(str, Enum):
    ADMIN = "Admin"
    SUPER_ADMIN = "SuperAdmin"
    USER = "User"
    MODERATOR = "Moderator"
