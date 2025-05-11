from uuid import uuid4

def id_generator() -> str:
    """
    Generate a unique identifier.

    Returns:
        str: A unique identifier.
    """
    return str(uuid4())