import typing

class LinkedDataRequest:
    def __init__(self , *args: typing.Any) -> None: ...
    def GetOAuthRequestToken(self, UidServiceProvider: str) -> str: ...
    def RequestServerToFetchAccessToken(self, UidServiceProvider: str) -> bool: ...
    def SignURLForOAuth(self, UrlString: str, UidServiceProvider: str) -> str: ...

