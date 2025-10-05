class Bottle:
    def __init__(self, capacity_in_liters: float):
        if not isinstance(capacity_in_liters, (int, float)):
            raise TypeError("Capacity must be a number (int or float).")
        if capacity_in_liters <= 0:
            raise ValueError("Capacity must be positive.")
        self.capacity: float = float(capacity_in_liters)
        self.volume: float = 0.0
        self.is_open: bool = False  # closed

    def open(self) -> None:
        self.is_open = True

    def close(self) -> None:
        self.is_open = False

    def set_volume(self, volume: float) -> None:
        if not isinstance(volume, (int, float)):
            raise TypeError("Volume must be a number (int or float).")
        if volume < 0:
            raise ValueError("Volume cannot be negative.")
        if self.is_open:
            if volume <= self.capacity:
                self.volume = float(volume)
            else:
                self.volume = self.capacity

    def get_volume(self) -> float:
        return self.volume

    def empty(self) -> None:
        if self.is_open:
            self.volume = 0.0

    def set_volume_in_milliliters(self, ml: float) -> None:
        if not isinstance(ml, (int, float)):
            raise TypeError("Volume in ml must be a number (int or float).")
        if ml < 0:
            raise ValueError("Volume in ml cannot be negative.")
        volume_in_liters = ml / 1000
        self.set_volume(volume_in_liters)

    def get_volume_in_milliliters(self) -> float:
        return self.get_volume() * 1000
