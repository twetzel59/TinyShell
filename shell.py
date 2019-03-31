import sys
from tinyshell.colors import *
from tinyshell.commands import *
from tinyshell import interactive

def tests():
    PASS = "[ {}PASS{} ]".format(GREEN, RESET)
    FAIL = "[ {}FAIL{} ]".format(RED, RESET)
    
    def cmd_manager():
        # The following should all be equivalent.
        mgr0 = CommandManager()
        mgr0.register(Command("gcc", {"-o": ArgType.FILENAME}))
        mgr0.register(Command("test"))
        mgr0.register(Command("cat", {"-n": ArgType.NATURAL}))
        #
        mgr1 = CommandManager()
        mgr1["gcc"] = [{"-o": ArgType.FILENAME}]
        mgr1["test"] = []
        mgr1["cat"] = [{"-n": ArgType.NATURAL}]
        #
        mgr2 = CommandManager(
            ("gcc", [{"-o": ArgType.FILENAME}]),
            ("test", []),
            ("cat", [{"-n": ArgType.NATURAL}])
        )

        # Check that the shorthands work.
        assert(mgr0.cmds == mgr1.cmds == mgr2.cmds)
    
    class TestError(Exception):
        """Raised when a test fails."""
        
        def __init__(self, msg):
            pass
    
    def should_not_throw(fn, *args):
        name = fn.__name__
        
        try:
            fn(*args)
        except:
            print(FAIL, name)
            raise TestError("Test \"" + name + "\" did not succeed.")
        
        print(PASS, name)

    should_not_throw(cmd_manager)

def create_cmd_mgr():
    return CommandManager(
        ("g++", [{"-o": ArgType.FILENAME}]),
        ("cat", [{"-n": ArgType.NATURAL}])
    )

def run():
    bar = "--------------------------------------------"
    
    print(CYAN + "\nSelf-checking:" + RESET + \
        " running routine unit tests...\n", bar, sep = "")
    
    try:
        tests()
        print(GREEN + "\nNo error reported!" + RESET + \
            " Starting shell...")
    except Exception as e:
        print(RED + "\nError during testing:" + RESET, e)
        sys.exit(-1)
    
    print(bar, end = "\n\n")
    
    interactive.begin(sys.stdin, sys.stdout, create_cmd_mgr())

if __name__ == "__main__":
    run()
