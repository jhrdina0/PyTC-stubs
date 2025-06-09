import typing

class Classification:
    """
    Interface Classification
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def SearchClassificationObjects(self, JsonRequest: str) -> str: ...

