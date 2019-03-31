from enum import Enum, auto, unique

@unique
class ArgType(Enum):
    NATURAL = auto()
    FILENAME = auto()

class CommandManager:
    """A CommandManager handles the storage of valid commands."""

    def __init__(self, *commands):
        """Create a new CommandManager with the specified commands.
        
        Each argument is a pair containing the name, attrib pairs,
        as the __setitem__ method is called on each element.
        """
        
        self.cmds = dict()
        
        for nm, attr in commands:
            self[nm] = attr

    def __setitem__(self, name, attribs):
        """Create and register a command with the name item.
        
        This is a shortcut for constructing a Command and
        registering it with the register method.
        
        attribs is a list containing arguments to be sent
        to Command's constructor.
        
        Raises TypeError if attribs is not a list.
        """
        
        assert(type(attribs) is list)
        
        self.register(Command(*([name] + attribs)))

    def register(self, cmd):
        """Establish a command with a given name as a valid command.
        
        The command's name must not already be registered.
        Raises AssertionError if a command of the same name already
        has been registered or if the command's switches are not
        expressed by a dictionary type.
        """

        assert(cmd.name not in self.cmds)
        
        data = cmd.data
        assert(type(data.switches) is dict)
        
        self.cmds[cmd.name] = data
    
    def is_cmd(self, name):
        """Return a boolean indicating if the name is registered."""
        
        return name in self.cmds

class CmdData:
    """Stores a command's argument data."""
    
    def __init__(self):
        self.switches = None
    
    def __eq__(self, other):
        if self is other:
            return True
        
        return self.switches == other.switches

class Command:
    """Describes a command's arguments."""

    def __init__(self, name, switches = dict()):
        """Create a new command description.

        name is the name of the command that the user must
        type at the prompt.

        switches is a dictionary that maps from the allowed
        command line switch keys to the type of their values.
        """

        self.name = name

        self.data = CmdData()
        self.data.switches = switches
