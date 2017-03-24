""" basic room implementation """

class Room(dict):
    """ basic room implementation """
    """ comment """
    def process_go(self, adventure, words):
        """ process the go command by looking at the next word """
        direction = words[0]
        room = self
        if direction in self["doors"]:
            room = adventure.get_room(self["doors"][direction]["destination"])
            print(room["entryDescription"])
        else:
            print("You can't go that way")
        return room

    def process_look(self, adventure, words):
        """ process the look command by looking at the next word """
        if len(words) == 0:
            print(self["description"])
        elif words[0] in self["doors"]:
            print(self["doors"][words[0]]["description"])
        else:
            print("There's nothing to see")
        return self


    options = {
        "go" : process_go,
        "look" : process_look
    }

    def __init__(self, roomjson):
        super(Room, self).__init__(roomjson)

    def process_command(self, adventure, command):
        """ process a command """
        words = command.split(" ")
        room = self
        if words[0] in self.options:
            room = self.options[words[0]](self, adventure, words[1:])
        else:
            print("I don't know how to do that'")
        return room


if __name__ == "__main__":
    print("This file is not to be run")

