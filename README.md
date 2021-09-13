# TextAdventure
This is a simple text adventure framework to help kids learn python and simple game design.  You extend the game by adding more content to the default.json file or by 
to handle new scenarios and actions.

The main program is adventure.py, so you can run the program by typing "python adventure.py".

The basic commands are "move" and "look".  For example to move north you type "move north" or "move n".  To look you can type "look" to see the room, or "look n" to look north.

The file music_room.py provides an example of changing a room's behavior for a specific room.  You can follow this pattern to make a room behave differently than other rooms,
or you can change room.py to change how all rooms behave.  In general it's better to think about how you want all rooms to behave and then represent that behavior
in the description of a room in default.JSON


