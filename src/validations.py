import uuid


def is_valid_uuid(value):
    """
    Validate if the given value is a valid UUID.
    :param value: The string to validate.
    :return: True if valid UUID, False otherwise.
    """
    try:
        uuid_obj = uuid.UUID(str(value), version=4)
    except ValueError:
        return False
    return str(uuid_obj) == value
