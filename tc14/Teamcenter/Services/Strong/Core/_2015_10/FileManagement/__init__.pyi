import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class DatasetDigestInfoResponse:
    """
    
            this structure contains the details about the digest information for the ImanFile
            objects in the Dataset objects.
            
    """
    def __init__(self, ) -> None: ...
    DatasetDigestInfo: System.Collections.Hashtable
    """
            A list of DatasetDigestInfos objects. It contains the digest information for each
            file referenced by each of the input dataset object.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The ServiceData response that can contain the partial errors."""

class DigestInfo:
    """
    Structure containing information about an individual digest for an ImanFile object.
    """
    def __init__(self, ) -> None: ...
    DigestAlgorithm: str
    """
            The digest algorithm used to the compute the digest for this file. This can be one
            of:
            

None
            
MD5
            
SHA-1
            
SHA-256
            

"""
    Digest: str
    """
            The digest for the file. Message digest algorithms ("digests") are widely used cryptographic
            hash functions.  Digests are utilized in a wide variety of cryptographic applications,
            and are also commonly used to verify data integrity.  FMS uses digest algorithms
            to produce a hash value of the contents of whole binary files, and expresses the
            hash value in text format as a hexadecimal number. An empty string is returned if
            no digest was available for the file.
            """
    Certainty: int
    """
            The certainty of the digest stored. The possible values are:
            

0 - default for unknown or unparsable certainty values.
            
1 - absolute certainty, a digest generated on the first generation
            of a file (before an FMS network transport)
            
2 - high level of certainty, a digest generated as a file is stored
            in the volume (after an FMS network transport)
            
3 - medium level of certainty, a digest generated on an existing
            file in a volume (sometime after the initial write to the server)
            
4 - lowest level of certainty, a digest generated on the fly.
            

"""

class FileDigestInfoResponse:
    """
    
            This structure contains the details about the digest information for the ImanFile
            objects.
            
    """
    def __init__(self, ) -> None: ...
    FileDigestInfo: System.Collections.Hashtable
    """
            A map (ImanFile, list of DigestInfo) of input ImanFile objects to the
            digest informationa for the file.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """The ServiceData response that can contain the partial errors."""

class FileDigestInfoSet:
    """
    
            This structure contains the digest information available for each of the files in
            the map.
            
    """
    def __init__(self, ) -> None: ...
    Map: System.Collections.Hashtable
    """
            A map of ImanFile objects to a list of DigestInfo objects for each digest
            available for the file.
            """

class FileManagement:
    """
    Interface FileManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetDigestInfoForDatasets(self, Datasets: list[Teamcenter.Soa.Client.Model.Strong.Dataset]) -> DatasetDigestInfoResponse:
        """    
             Gets the file digest information for the ImanFile objects contained in the
             Dataset objects. These digests can be used by clients to check for file integrity.
             Clients must use the same digest algorithm (as returned by this operation) to compute
             the digest on their end and compare with the digest returned by this operation.
             
             The Teamcenter File Management System (FMS) computes and stores the file digests
             on the volume if the content verification feature is turned on.
             
             This operation returns digests for binary files only.
             

Teamcenter Component:

             FMS Tc Integration - The integration of the FMS with the Tc Server.
             
        :param Datasets: 
                         the <b>Dataset</b> objects for which the digest information is to be obtained for
                         each of the <b>ImanFile</b> objects in them.
             
        :return: 
        """
        ...
    def GetDigestInfoForFiles(self, Files: list[Teamcenter.Soa.Client.Model.Strong.ImanFile]) -> FileDigestInfoResponse:
        """    
             Gets the file digest information for all the ImanFile objects specified using
             files. These digests can be used by clients to check for file integrity. Clients
             must use the same digest algorithm (as returned by this operation) to compute the
             digest on their end and compare with the digest returned by this operation.
             
             The Teamcenter File Management System (FMS) computes and stores the file digests
             on the volume if the content verification feature is turned on.
             
             This operation returns digests for binary files only.
             

Teamcenter Component:

             FMS Tc Integration - The integration of the FMS with the Tc Server.
             
        :param Files: 
                         The <b>ImanFile</b> objects for which the digest information is to be obtained.
             
        :return: 
        """
        ...

