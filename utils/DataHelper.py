def get_gear_name(gear: int) -> str:
    match gear:
        case 0:
            return 'R'
        case -1:
            return 'N'
        case _:
            return '%d' % gear

def get_speed_kph(speed: float, integer=True) -> int | float:
    kph = speed * 3.6
    return int(kph) if integer else kph

def get_speed_mph(speed: float,  integer=True) -> int | float:
    mph = speed * 2.23694
    return int(mph) if integer else mph