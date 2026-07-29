import ulid

def generate_id() -> str:
    """Genera un identificador único en formato ULID."""
    return str(ulid.new())
