import System
import Teamcenter.Soa.Client.Model
import typing

class IPAManagementGenerateSearchScopeResponse:
    """
    Return structure for IPAManagementGenerateSearchScope operation
    """
    def __init__(self, ) -> None: ...
    Bomlines: list[Teamcenter.Soa.Client.Model.ModelObject]
    """A vectoer of all the bomlines that are the search scope."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            This is a common data strucuture used to return sets of Teamcenter  Data Model object
            from a service request. This also holds services exceptions.
            """

class IPAManagementGetFilteredIPAResponse:
    """
    Return structure for IPAManagementGetFilteredIPA operation
    """
    def __init__(self, ) -> None: ...
    FilteredIPAs: list[Teamcenter.Soa.Client.Model.ModelObject]
    """A vectoer of all the filteredIPAs found."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            This is a common data strucuture used to return sets of Teamcenter  Data Model object
            from a service request. This also holds services exceptions.
            """

class IPAManagementSaveSearchResultInput:
    """
    Input structure for IPAManagementSaveSearchResult operation
    """
    def __init__(self, ) -> None: ...
    Process: Teamcenter.Soa.Client.Model.ModelObject
    """The process from which we want to filter the IPA."""
    SearchResultList: list[Teamcenter.Soa.Client.Model.ModelObject]
    """The bomlines result from the search."""
    Name: str
    """The name of the new filtered structure."""

class IPAManagementSaveSearchResultResponse:
    """
    Return structure for IPAManagementSaveSearchResult operation
    """
    def __init__(self, ) -> None: ...
    FilteredIPA: Teamcenter.Soa.Client.Model.ModelObject
    """This is the new filteredIPA structure."""
    FilteredIPARoot: Teamcenter.Soa.Client.Model.ModelObject
    """The flat list of all filteredIPA structures."""
    RejectedList: list[Teamcenter.Soa.Client.Model.ModelObject]
    """A list of all the bomlines that were not found in the IPA structure."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            This is a common data strucuture used to return sets of Teamcenter  Data Model object
            from a service request. This also holds services exceptions.
            """

class IPAManagement:
    """
    Interface IPAManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def DeletefilteredIPA(self, Processes: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    Deletes the filteredIPA structure from the process.
        :param Processes: 
                         Input Vector of process lines, from which we want to delete the filteredIPA.
             
        :return: serviceData This is a common data strucuture used to return sets of Teamcenter Data
             Model object from a service request. This also holds services exceptions.
        """
        ...
    def GenerateSearchScope(self, Processes: list[Teamcenter.Soa.Client.Model.ModelObject]) -> IPAManagementGenerateSearchScopeResponse:
        """    
             find the IPA under the given process (for each process) and retrives the bomlines
             from under it.
             
        :param Processes: 
                         processes Vector of process lines, that we would like to get all the search scope
                         from.
             
        :return: IPAManagementGenerateSearchScopeResponse Return Structure see discription in structure
             definition file.
        """
        ...
    def GetFilteredIPA(self, Processes: list[Teamcenter.Soa.Client.Model.ModelObject]) -> IPAManagementGetFilteredIPAResponse:
        """    Return the filteredIPA structure from the process.
        :param Processes: 
                         Input Vector of process lines, from which we want to find the filteredIPA.
             
        :return: IPAManagementGetFilteredIPAResponse Return Structure see discription in structure
             definition file.
        """
        ...
    def SaveSearchResult(self, Input: list[IPAManagementSaveSearchResultInput]) -> IPAManagementSaveSearchResultResponse:
        """    Saves the search result in a new/updated structure.
        :param Input: 
                         Input Vector of IPAManagementSaveSearchResultInput Structures see discription in
                         structure definition file.
             
        :return: IPAManagementSaveSearchResultResponse Return Structure see discription in structure
             definition file.
        """
        ...

