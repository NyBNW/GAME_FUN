class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}

    def add_exit(self, direction, room):
        self.exits[direction] = room

    def get_exit(self, direction):
        return self.exits.get(direction)

class Game:
    def __init__(self):
        self.current_room = None
        self.create_rooms()

    def create_rooms(self):
        room1 = Room("Room 1", "You are in a dark room.")
        room2 = Room("Room 2", "You are in a bright room.")

        room1.add_exit("north", room2)
        room2.add_exit("south", room1)

        self.current_room = room1

    def play(self):
        print(self.current_room.description)
        while True:
            direction = input("Enter a direction (north, south, east, west): ")
            next_room = self.current_room.get_exit(direction)
            if next_room:
                self.current_room = next_room
                print(self.current_room.description)
            else:
                print("Invalid direction. Try again.")

game = Game()
game.play()
