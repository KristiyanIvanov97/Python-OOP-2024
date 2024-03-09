from typing import List

from project.room import Room


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms: List[Room] = []
        self.guests: int = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people: int) -> None:
        try:
            room = next(filter(lambda r: r.number == room_number, self.rooms))
        except StopIteration:
            return

        if not room.is_taken and room.capacity >= people:
            self.guests += people
            room.is_taken = True
            room.guests += people

    def free_room(self, room_number) -> None:
        try:
            room = next(filter(lambda r: r.number == room_number, self.rooms))
        except StopIteration:
            return

        room_guests = room.guests
        if room.is_taken:
            room.is_taken = False
            room.guests = 0
            self.guests -= room_guests

    def status(self) -> str:
        return f"Hotel {self.name} has {self.guests} total guests\n" \
               f"Free rooms: {', '.join(str(room.number) for room in self.rooms if not room.is_taken)}\n" \
               f"Taken rooms: {', '.join(str(room.number) for room in self.rooms if room.is_taken)}"
