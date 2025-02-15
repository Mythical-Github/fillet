from enum import Enum


class Games(Enum):
    CALL_OF_DUTY_WORLD_AT_WAR = 'Call of Duty World at War'
    CALL_OF_DUTY_BLACK_OPS_I = 'Call of Duty Black Ops I'
    CALL_OF_DUTY_BLACK_OPS_II = 'Call of Duty Black Ops II'


def get_enum_from_val(enum: Enum, value: str) -> Enum:
    for member in enum:
        if member.value == value:
            return member
    return None


def get_enum_strings_from_enum(enum: Enum) -> list[str]:
    strings = []
    for entry in enum:
        strings.append(entry.value)
    return strings
