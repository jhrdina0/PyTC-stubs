import Mdl0.Services.Strong.Modelcore._2015_07.GeometricConnectivity
import System
import System.Collections
import Teamcenter.Soa.Client.Model
import Teamcenter.Soa.Client.Model.Strong
import typing

class GroupValidationOutput:
    def __init__(self, ) -> None: ...
    ValidationStatus: str
    """
            Validation status of geometric connectivity group. Valid values are: INVALID, COMPLETE
            and VALID.
            """
    IncompleteElements: list[Teamcenter.Soa.Client.Model.Strong.Mdl0PositionedModelElement]
    """List of positioned model elements where connectivity is incomplete."""
    InvalidElements: list[Teamcenter.Soa.Client.Model.Strong.Mdl0PositionedModelElement]
    """
            List of positioned model elements where connectivity is logically connected, but
            not geometric connected.
            """

class MergeGeomConnGroupsInfo:
    """
    
            Specifies the full set of inputs required to merge list of geometric connectivity
            groups into one.
            
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            This unique ID is used to identify returned merged geometric connection group or
            partial errors associated with this input
            """
    GeomGroups: list[Teamcenter.Soa.Client.Model.Strong.Mdl0GeomConnGroup]
    """List of geometric connectivity groups to be merged"""
    GroupInfo: Mdl0.Services.Strong.Modelcore._2015_07.GeometricConnectivity.GeomConnGroupInfo
    """
            Information needed to create new or specify existing geometric connectivity group
            to which the list of geometric connectivity group will be merged.
            

            If endObject1 is not provided, the default will be set as follows:
            

If mdl0End1 of the first geometric connectivity group in the list
            is not null, it is set to mdl0End1
            
If mdl0End1 of is null and mdl0End2 is not null, it is set to mdl0End2
            
If both mdl0End1 and mdl0End2 are null,  it is set to null
            


            If endObject2 is not provided, the default will be set as follows:
            

If mdl0End2 of the last geometric connecitvity group in the list
            is not null, it is set to mdl0En2
            
If mdl0End2 is null and mdl0End1 is not null, it is set to mdl0End1
            
If both mdl0End1 and mdl0End2 are null,  it is set to null
            

"""
    DeleteInputGroups: bool
    """
            Flag to specify if input list of geometric connectivity groups will be deleted after
            merge.
            
            If it is true, these geometric connectivity groups will be deleted. Otherwise, they
            will not be deleted.
            """

class MergeGeomConnGroupsResponse:
    """
    
            This structure is used to provide the response from the operation. The response contains
            the resultant geometric connectivity groups from the merges as per input.
            
    """
    def __init__(self, ) -> None: ...
    NewGroups: System.Collections.Hashtable
    """
            A map (string/Mdl0GeomConnGroup)  of clientId to the corresponding geometric
            connectivity group.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Contains the resultant geometric connectivity groups and any partial errors within
            the call.
            """

class NewGroupsInfo:
    """
    
            This structure is used to return the newly created geometric connectivity groups
            for each of the input geometric connectivity groups
            
    """
    def __init__(self, ) -> None: ...
    Group1: Teamcenter.Soa.Client.Model.Strong.Mdl0GeomConnGroup
    """
            Business object to the newly created first geometric connectivity group (as per subGroupInfo1 of input)
            """
    Group2: Teamcenter.Soa.Client.Model.Strong.Mdl0GeomConnGroup
    """
            Business object to the newly created first geometric connectivity group (as per subGroupInfo2 of input)
            """

class SplitGeomConnGroupResponse:
    """
    
            This structure is used to provide the response from the operation. The response contains
            the resultant geometric connectivity groups from the splits as per input. The resultant
            geometric connectivity groups can be mapped to the input via clientId.
            
            If there is an error during the processing of merge for any of the inputs, error
            would be returned along with corresponding clientId.
            
    """
    def __init__(self, ) -> None: ...
    NewGroups: System.Collections.Hashtable
    """
            A map of  clientId to the resultant geometric
            connectivity groups afer the split of input geometric connectivity group.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Standard SOA ServiceData structure with groups created or updated. It would also
            contain any partial errors within the call.
            """

class SubGroupInfo:
    """
    
            This structure is used to provide the following inputs:
            

Input needed to identify the positioned model elements to be grouped
            into new geometric connectivity groups
            
Input needed to create new geometric connectivity group with positioned
            model elements identified using the previous input
            



            NOTE: If startLink and endLink inputs in subGroupInfo1
            and subGroupInfo2 result in an overlapping
            path; i.e. they contain one or more positioned model elements in common, an error
            would be returned (284020).
            
    """
    def __init__(self, ) -> None: ...
    StartLink: Teamcenter.Soa.Client.Model.Strong.Mdl0GeomLink
    """
            Geometric link that specifies the position of the positioned model element in input
            geometric connectivity group (geomGroup)
            from where the traversal would start. Note:
            

If startLink is not specified
            in the case of first geometric connectivity group to be created (subGroupInfo1), the geometric link of first end equipment (Mdl0GeomConnGroup.mdl0End1)
            of the input geometric connectivity group will be used.
            
If startLink is not specified
            in the case of second geometric connectivity group to be created (subGroupInfo2), error will be returned (284019)
            

"""
    EndLink: Teamcenter.Soa.Client.Model.Strong.Mdl0GeomLink
    """
            Geometric link that specifies the position of the positioned model element in input
            geometric connectivity group (geomGroup)
            where the traversal will end. Note:
            

If endLink is not specified in the case of first geometric connectivity
            group to be created (subGroupInfo1), error
            will be returned (284018)
            
If endLink is not specified in the case of second geometric connectivity
            group to be created (subGroupInfo2), the
            geometric link second equipment (Mdl0GeomConnGroup.mdl0End2) of the
            input geometric connectivity group will be used
            

"""
    GroupInfo: Mdl0.Services.Strong.Modelcore._2015_07.GeometricConnectivity.GeomConnGroupInfo
    """
            Information needed for creating new geometric connectivity group is provided through
            GeomConnGroupInfo.
            
            The following is specific to the usage of this structure by this operation:
            

            If endObject1 is not provided, the default will be as follows:
            

For the first geometric connectivity group (subGroupInfo1), the first end (mdl0End1) of the input geometric
            connectivity group will be used.
            
For the second geometric connectivity group (subGroupInfo2), there will no default value.
            



            If endObject2 is not provided, the default will be as follows:
            

For the first geometric connectivity group (subGroupInfo1), the second end (mdl0End2) there is no default
            value.
            
For the second geometric connectivity group (subGroupInfo2), the second end (mdl0End2) of the input
            geometric connectivity group will be used.
            

"""

class SplitGeomConnGroupsInfo:
    """
    
            This structure is used to provide the following information:
            

Group to be split
            
Inputs needed for creating new geometric connectivity groups
            


    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            This unique ID is used to identify returned merged geometric connection group or
            partial errors associated with this input structure.
            """
    GeomGroup: Teamcenter.Soa.Client.Model.Strong.Mdl0GeomConnGroup
    """Geometric connectivity group to be split"""
    SubGroupInfo1: SubGroupInfo
    """Inputs to identify contents of first geometric connectivity group to be created"""
    SubGroupInfo2: SubGroupInfo
    """Inputs to identify contents of second geometric connectivity group to be created"""
    DeleteInputGeomGroup: bool
    """
            If true,  the geometric connectivity group (geomGroup)
            should be deleted after split is complete.
            """

class ValidateGeomConnGroupInfo:
    """
    Specifies the group which is to be validated
    """
    def __init__(self, ) -> None: ...
    ClientId: str
    """
            A unique string supplied by the caller. This ID is used to identify returned validation
            status and partial errors associated with this input.
            """
    GeomGroup: Teamcenter.Soa.Client.Model.Strong.Mdl0GeomConnGroup
    """Geometric connecvitiy group to validate."""
    Start: Teamcenter.Soa.Client.Model.Strong.Mdl0GeomLink
    """
            Geometric link where the validation starts. If it is null, validation starts from
            end1 of the geometric connectivity group.
            """
    End: Teamcenter.Soa.Client.Model.Strong.Mdl0GeomLink
    """
            Geometric link where the validation ends. If it is null, validation ends at the end2
            of the geometric connectivity group.
            """

class ValidateGeomConnGroupResponse:
    """
    Response content returned from this SOA call.
    """
    def __init__(self, ) -> None: ...
    ValidationMap: System.Collections.Hashtable
    """
            Map (string/GroupValidationOutput) of clientID
            to validation status.
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Contains list of added, updated, or deleted objects. Also contains list of any errors
            which occurred within the call.
            """

class GeometricConnectivity:
    """
    Interface GeometricConnectivity
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def MergeGeomConnGroups(self, MergeGroupInfos: list[MergeGeomConnGroupsInfo]) -> MergeGeomConnGroupsResponse: ...
    def SplitGeomConnGroups(self, SplitGroupInfos: list[SplitGeomConnGroupsInfo], ConfigContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext) -> SplitGeomConnGroupResponse: ...
    def ValidateGeomConnGroups(self, ValidateGroupInfos: list[ValidateGeomConnGroupInfo], ConfigContext: Teamcenter.Soa.Client.Model.Strong.ConfigurationContext) -> ValidateGeomConnGroupResponse:
        """    
             This operation verifies the geometric connectivity groups and returns their validation
             statuses. If both start and end geometric links are null, the connectivity is verified
             for the whole geometric group and it returns all incomplete or invalid positioned
             model elements. Otherwise, will traverse the group from both, stop at the first positioned
             model element that is incomplete and return these two incomplete positioned model
             elements.
             

Use Cases:

             Validating geometric connectivity group and fixing any invalid connectivity.
             
             This use case is entirely within the domain of CAD tools. Using this SOA, the CAD
             tools can validate the list of geometric connectivity groups, load invalid connectivity
             in CAD tools and fix them.
             

Teamcenter Component:

             Application Model Elements - Defines the basic data management operations(revise,saveAs,deepcopy)
             for Application Model Elements,defines operations to create search expressions and
             execute search on Model Elements in an Application Model.
             
        :param ValidateGroupInfos: 
                         The set of information needed to validate a geometric connectivity group.
             
        :param ConfigContext: 
                         Configuration context to filter routing contents. It is required to validate the
                         geometric connectivity group.
             
        :return: 
        """
        ...

