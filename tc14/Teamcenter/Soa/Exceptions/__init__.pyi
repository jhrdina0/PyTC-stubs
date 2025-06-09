import System
import System.IO
import typing

class CanceledOperationException(System.Exception):
    """
    
Throws when operation fails  in a middle due to some reason.
    """
    @typing.overload
    def __init__(self, message: str) -> None: ...
    @typing.overload
    def __init__(self, ) -> None: ...
    @typing.overload
    def __init__(self, message: str, inner: System.Exception) -> None: ...

class ExceptionMapper:
    """
    
Maps the perticular exception.
    """
    def __init__(self, ) -> None: ...
    def ThrowSoaException(self, ex: System.Exception) -> None:
        """    
            Maps the JETI level exceptions to the equivalent Web Service level exception.
            After mapping the exception, the Web Service equivalent is thrown. If an
            equivalent excpetion does not exist a InternalServerException is thrown. This
            method will always thrown an exception vs. a normal return.
            
        :param ex: The exception to map
        :return: 
        """
        ...
    def WriteSoaException(self, ex: System.Exception, outStream: System.IO.Stream) -> None:
        """    
            Serialize (XML Document) the given excpetion.
            The exception is mapped using the throwWebServiceExcetpion
            
        :param ex: The exception to serialize
        :param outStream: Writer to write the XML document to
        :return: 
        """
        ...
    def ParseExceptionString(self, xmlString: str) -> None:
        """    
            Parse an XML string to an exception.
            The appropriate exception is constructed and populated from the XML document
            and thrown. This is potentailly used on client to map the XML Response Exception
            to appropraite objects
            
        :param xmlString: Source XML document representing an exception
        :return: 
        """
        ...
    @staticmethod
    def IsException(xml: str) -> bool:
        """    
            Check if the xml document contains an exception
            
        :param xml: xml document
        :return: True, if document contains ex
        """
        ...

class NotLoadedException(System.Exception):
    """
    
Throws when loading operation fails. For e.g. expected properties/object not get
loaded.
    """
    @typing.overload
    def __init__(self, message: str) -> None: ...
    @typing.overload
    def __init__(self, ) -> None: ...
    @typing.overload
    def __init__(self, message: str, inner: System.Exception) -> None: ...

