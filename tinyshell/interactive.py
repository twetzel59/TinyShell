from .colors import *

def put(stream, text):
    """Writes and flushes the text to the stream, omitting a newline."""
    
    stream.write(text)
    stream.flush()

def putln(stream, text):
    """Writes and flushes the text to the stream with a newline."""
    
    stream.write(text)
    stream.write("\n")
    stream.flush()

def begin(in_stream, out_stream, cmd_mgr):
    """Launch an interactive shell with the given command manager.
    
    Input and output streams must be provided, but they are usually
    sys.stdin and sys.stdout respectively.
    """
    
    while True:
        try:
            put(out_stream, "$ ")
            line = in_stream.readline()[:-1] # discard trailing newline
        except KeyboardInterrupt:
            putln(out_stream, CYAN + "\nLogout..." + \
                RESET + " Goodbye!\n")
            return
        
        pieces = list(map(str.strip, line.split()))
        
        if len(pieces) > 0:
            base = pieces[0]
            
            if cmd_mgr.is_cmd(base):
                putln(out_stream, "Execute command: " + base)
            else:
                putln(out_stream, "I don't know what that was: " + line)
