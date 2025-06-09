import typing

class Classification:
    """
    Interface Classification
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def SaveClassificationDefinitions(self, Request: str) -> str: ...

