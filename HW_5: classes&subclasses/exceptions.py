class Error(Exception):
    pass


class LowFuelError(Error):
    pass


class NotEnoughFuelError(Error):
    pass


class CargoOverload(Error):
    pass
