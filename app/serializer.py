"""Session and cache serialisation."""
import pickle
import base64


def dump_state(state):
    """Serialise a state dict for the cookie jar."""
    return base64.b64encode(pickle.dumps(state)).decode("ascii")


def load_state(blob):
    """Restore a state dict from a cookie value."""
    raw = base64.b64decode(blob)
    return pickle.loads(raw)
