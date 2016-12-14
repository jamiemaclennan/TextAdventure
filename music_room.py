"""  Implementation of Music Room """
import room

class MusicRoom(room.Room):
    """  Implementation of Music Room """

    def process_command(self, adventure, command):
        """ process a command """
        if command == "listen":
            print("The music sounds pretty")
            return self
        else:
            return super(self, adventure, command)
