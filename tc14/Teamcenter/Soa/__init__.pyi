

class SoaConstants:
    """
    
Used to assign SOA constants.
    """
    def __init__(self, ) -> None: ...
    HTTP: str
    """Protocols for communication between client and server"""
    IIOP: str
    """Protocols for communication between client and server"""
    REST: str
    """Bindings for communication between client and server"""
    SOAP: str
    """Bindings for communication between client and server"""
    TCCS: str
    """Bindings for communication between client and server"""
    REST_SERVICES: str
    """Misc. SOA"""
    CLIENT_CREDENTIAL_TYPE_SSO: int
    """Client Credential Type SSO."""
    CLIENT_CREDENTIAL_TYPE_STD: int
    """Client Credentail Type STD."""
    CLIENT_CREDENTIAL_TYPE_SPONSORED: int
    """Client Credential Type SSO."""
    CLIENT_CREDENTIAL_TYPE_SPONSORED_SSO: int
    """Client Credentail Type STD."""

