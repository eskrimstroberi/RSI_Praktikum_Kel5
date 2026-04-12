from enum import Enum


class RoleName(str, Enum):
    SUPER_ADMIN = "SuperAdmin"
    ADMIN = "Admin"
    USER = "User"

    @classmethod
    def get_hierarchy(cls, role: "RoleName"):
        levels = {
            cls.SUPER_ADMIN: [cls.SUPER_ADMIN],
            cls.ADMIN: [cls.ADMIN, cls.SUPER_ADMIN],
            cls.USER: [cls.USER, cls.ADMIN, cls.SUPER_ADMIN],
        }
        return levels.get(role, [])
