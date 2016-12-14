""" This is the main module for the adventure text adventure program """

import json
import sys
import room


# Load adventure definition
class AdventureProgram:
    """ main program class """
    map = None
    test = None
    rooms = dict()

    def __init__(self):
        """ Initalize the adventure """
        self.map = None
        self.test = None
        self.rooms = dict()
        mapfile = "default.json"
        if len(sys.argv) > 1:
            params = sys.argv[1]
            params = params.split(" ")
            index = 0
            while len(params) > index:
                if  params[index] == "-m":
                    mapfile = params[index + 1]
                    index = index + 1
                if params[index] == "-t":
                    self.test = open(params[index + 1])
                    index = index + 1
                index = index + 1
        f__ = open(mapfile)
        self.map = json.load(f__)

    def get_class(self, kls):
        """ Load a class dynamically """
        parts = kls.split('.')
        modulename = ".".join(parts[:-1])
        mm_ = __import__(modulename)
        for comp in parts[1:]:
            mm_ = getattr(mm_, comp)
        return mm_

    def get_room(self, room_name):
        """ Get the room by the room name, create a new one if needed. """
        if room_name not in self.rooms:
            room_desc = self.map["rooms"][room_name]
            if "class" in room_desc:
                self.rooms[room_name] = self.get_class(room_desc["class"])(room_desc)
            else:
                self.rooms[room_name] = room.Room(room_desc)
        return self.rooms[room_name]

    def run(self):
        """ Run the adventure """
        current_room = self.get_room(self.map["init"]["startingRoom"])
        command = ""
        while command != "quit":
            print("\n" + current_room["caption"])
            if self.test is None:
                command = input("# ")
            else:
                command = self.test.readline()
                print("# " + command)
            command = command.strip()
            if command != "quit":
                current_room = current_room.process_command(self, command)


if __name__ == "__main__":
    ADVENTURE = AdventureProgram()
    ADVENTURE.run()

