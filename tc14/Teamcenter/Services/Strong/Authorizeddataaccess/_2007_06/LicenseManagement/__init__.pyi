import System
import Teamcenter.Soa.Client.Model
import typing

class GetLicenseDetailsResponse:
    """
    
GetLicenseDetailsResponse represents the
            details of ADA_License business objects.
            
    """
    def __init__(self, ) -> None: ...
    LicDetails: list[LicenseDetails]
    """Structures containing the properties of ADA_License business objects."""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """
            Contains partial errors encountered while fetching properties for ADA_License
            business objects. The ADA_License business objects for which properties are
            fetched successfully are added to the Plain list.
            """

class LicenseDetails:
    """
    
LicenseDetails structure represents all the
            details of an ADA License object.
            
    """
    def __init__(self, ) -> None: ...
    LicenseType: str
    """
            The type of ADA License object. The type can be ITAR_License, Exclude_License,
            or IP_License.
            """
    LicenseId: str
    """The unique ID of the license. This is string with a maximum of 128 bytes."""
    ExpiryDate: System.DateTime
    """
            The expiry date for the license, after which the license cannot be attached to WorkspaceObject
            business objects and ceases to grant the access to users/groups listed on the license.
            A NULL date specifies the license will never expire.
            """
    LicenseReason: str
    """
            A reason for the license to exist. This parameter can be a maximum of 128 bytes.
            This is an optional parameter and may have value as a blank string.
            """
    Users: list[str]
    """
            The list of users associated with a license identified by licenseId.
            When the license is attached to a classified WorkspaceObject, the users listed
            on the license will get access to the WorkspaceObject, based on the access
            rules.
            """
    Groups: list[str]
    """
            List of names of groups associated with the license identified by licenseId. For subgroups, the full names should be specified.
            When the license is attached to a classified WorkspaceObject, the users from
            the groups/subgroups listed on the license will get access to the workspace object,
            based on the access rules. This parameter represents an array of group name strings
            of upto 256 bytes in size.
            """

class LicenseIdAndType:
    """
    
LicenseIdAndType structure Represents license
            Type and license ID of an ADA License object.
            
    """
    def __init__(self, ) -> None: ...
    LicenseType: str
    """The type of a license object.  This is string with a maximum of 32 bytes."""
    LicenseId: str
    """The unique ID of the license object. This is string with a maximum of 128 bytes."""

class LicenseIdsAndTypesResponse:
    """
    
LicenseIdsAndTypesResponse Represents the
            license IDs and types of ADA_License business objects.
            
    """
    def __init__(self, ) -> None: ...
    LicIdType: list[LicenseIdAndType]
    """
            Structures containing the license Type and license ID of fetched ADA_License business
            objects
            """
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """Contains partial errors encountered while fetching ADA_License business objects."""

class LicenseInput:
    """
    
LicenseInput represents a list of license
            IDs of ADA licenses and the associated WorkspaceObject business objects.
            
    """
    def __init__(self, ) -> None: ...
    SelectedLicenses: list[str]
    """
            List of license IDs of ADA licenses. These are strings of each with a maximum of
            128 bytes size.
            """
    Objects: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            List of WorkspaceObject business objects associated with the selectedLicenses.
            """

class LicenseTypeAndStatusFilter:
    """
    
LicenseTypeAndStatusFilter structure Represents
            type and status of ADA License objects.
            
    """
    def __init__(self, ) -> None: ...
    LicType: str
    """
            The type of ADA License objects. The type can be specified as ITAR_License,
            ExcludeE_License, IP_License, or, ALL. The value of ALL indicates that
            licenses of all types need to be fetched.
            """
    LicStatus: str
    """
            The status of ADA License objects. The value should be set to ALL for returning all licenses. Any other value for licStatus returns only unlocked and unexpired licenses.
            """

class LicenseManagement:
    """
    Interface LicenseManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def AttachLicenses(self, AttachLicense: list[LicenseInput]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation attaches ADA Licenses to WorkspaceObject business objects such
             as Item, ItemRevision, Dataset, etc. as specified in each LicenseInput. LicenseInput
             provides details on the licenses to be attached, and the WorkspaceObject business
             objects to attach the licenses to. Users performing this operation will need IP_ADMIN
             privilege to both the workspace objects and the licenses being attached, if the licenses
             are of type IP or Exclude, while ITAR_ADMIN privilege
             is needed to both the workspace objects and the licenses being attached if the licenses
             are of ITAR license type. If the user does not have necessary privilege to
             attach any licenses, or if there is any other error while attaching licenses, the
             errors are returned as partial errors in ServiceData.
             

Use Cases:

             You can attach ADA_License business objects to classified WorkspaceObject
             business objects to grant access for users and/or groups listed on the licenses.
             

Teamcenter Component:

             Authorized Data Access - Authorized Data Access (ADA) is a security solution that
             complements Access Manager rules to control access to sensitive data through the
             use of data classification, user clearance, and time bound authorizing documents
             (ADA Licenses).
             
        :param AttachLicense: 
                         Structures containing information of licenses to attach, and the workspace objects
                         to attach to.
             
        :return: 
        """
        ...
    def DeleteLicense(self, LicenseIds: list[str]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation deletes all ADA_License business objects specified in
             licenseIds parameter. Users performing this
             operation will need privilege specified in ADA_license_administration_privilege
             site preference to delete the licenses. If the user does not have necessary privilege
             to delete the licenses, or if any license is attached to workspace objects, or, if
             there is any other error while deleting the licenses, the errors are returned as
             partial errors in ServiceData.
             

Use Cases:

             You can delete ADA_License business objects of type ITAR/IP/Exclude
             by providing license IDs for the licenses.
             

Teamcenter Component:

             Authorized Data Access - Authorized Data Access (ADA) is a security solution that
             complements Access Manager rules to control access to sensitive data through the
             use of data classification, user clearance, and time bound authorizing documents
             (ADA Licenses).
             
        :param LicenseIds: 
                         License IDs of the ADA licenses to delete.
             
        :return: 
        """
        ...
    def GetLicenseDetails(self, LicenseIds: list[str]) -> GetLicenseDetailsResponse:
        """    
             This operation gets the properties for each ADA_License business object specified
             in licenseIds and returns them in LicenseDetails structures as part of GetLicenseDetailsResponse.
             The LicenseDetails contains information for
             properties such as license type, license ID,  expiry date, reason, and associated
             users and groups, for a given license. If there is no matching license for a given
             license ID, LicenseDetails structure for
             that license will contain Not_found as the
             value for license ID, while the rest of the parameters will contain NULL values.
             However, if the user does not have READ privilege to any license or if there is any
             unexpected error while getting property information, the errors are returned in the
             ServiceData of GetLicenseDetailsResponse.
             

Use Cases:


             Use Case 1: Get properties of an ADA License

             You can get properties of an ADA_License business object of type ITAR/IP/Exclude
             using getLicenseDetails operation by providing
             license ID for the license.
             

             Use Case 2: Check the existence of an ADA License

             You can check if an ADA_License businesses object with given license ID exists
             using getLicenseDetails operation.
             


Teamcenter Component:

             Authorized Data Access - Authorized Data Access (ADA) is a security solution that
             complements Access Manager rules to control access to sensitive data through the
             use of data classification, user clearance, and time bound authorizing documents
             (ADA Licenses).
             
        :param LicenseIds: 
                         License IDs of the licenses to get properties for.
             
        :return: 
        """
        ...
    def GetLicenseIdsAndTypes(self, LicenseFilterInput: list[LicenseTypeAndStatusFilter]) -> LicenseIdsAndTypesResponse:
        """    
             This operation gets all the ADA_License business objects based on license
             type and license status specified in licenseFilterInput
             parameter. Licenses of a specific type can be queried for by specifying the license
             type as ITAR_License, IP_License or Exclude_License.
             A value of  ALL for the license type returns
             all types of ADA licenses. If the license status specified is ALL, all ADA licenses are returned, else only unlocked and unexpired
             licenses are returned. For the ADA_License business objects found, details
             like license IDs and license types are returned in LicenseIdAndType
             structures as part of LicenseIdsAndTypesResponse.
             If there is any unexpected error while getting licenses, the errors are returned
             in the serviceData of LicenseIdsAndTypesResponse.
             

Use Cases:

             Use Case 1: Get ADA Licenses based on type and status

             You can get ADA_License business objects using getLicenseIdsAndTypes
             operation based on specified license type and license status.
             

Teamcenter Component:

             Authorized Data Access - Authorized Data Access (ADA) is a security solution that
             complements Access Manager rules to control access to sensitive data through the
             use of data classification, user clearance, and time bound authorizing documents
             (ADA Licenses).
             
        :param LicenseFilterInput: 
                         Specifies the  type and  status of ADA licenses to get.
             
        :return: .
        """
        ...
    def RemoveLicenses(self, RemoveLicense: list[LicenseInput]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation removes/detaches ADA Licenses from WorkspaceObject business
             objects such as Item, ItemRevision, Dataset, etc. as specified
             in each LicenseInput. LicenseInput provides details of the licenses
             to be removed, and the WorkspaceObject business objects to remove the licenses
             from. Users performing this operation will need IP_ADMIN privilege to both
             the workspace objects and the licenses being removed, if the licenses are of type
             IP or Exclude, while the privilege specified in ADA_license_administration_privilege
             site preference is needed to both the workspace objects and the licenses being removed
             if the licenses are of ITAR license type. If the user does not have necessary
             privilege to remove any licenses, or if there is any other error while removing licenses,
             the errors are returned as partial errors in ServiceData.
             

Use Cases:

             Use case:
             
             You can remove ADA_License business objects from classified WorkspaceObject
             business objects to revoke access for users and/or groups listed on the licenses.
             

Teamcenter Component:

             Authorized Data Access - Authorized Data Access (ADA) is a security solution that
             complements Access Manager rules to control access to sensitive data through the
             use of data classification, user clearance, and time bound authorizing documents
             (ADA Licenses).
             
        :param RemoveLicense: 
                         Structures containing information of licenses to remove, and workspace objects from
                         which to remove.
             
        :return: 
        """
        ...
    def SetLicenseDetails(self, LicenseInfo: list[LicenseDetails]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation creates or modifies an ADA_License business object for each
             LicenseDetails supplied. The LicenseDetails contains information for properties such as license
             type, license ID, expiry date, reason, and associated users and groups, for a given
             license. If a specified license ID already exists, the rest of the property values
             are updated on that license. However, if the license ID does not exist, then a new
             license of the specified type and ID will be created, and the rest of the properties
             are set on the created license. The user performing the operation will need the privilege
             specified in the ADA_license_administration_privilege site preference
             to create/modify an ADA License. If a user does not have the necessary privilege
             or if there is a validation error, the operation would fail and the error is returned
             in the ServiceData.
             

Use Cases:

Use Case 1: Create an ADA license

             You can create a new ADA license of type ITAR/IP/Exclude using setLicenseDetails operation by providing a unique license ID for
             the license using LicenseDetails structure.
             

Use Case 2: Modify an ADA License

             The following types of modifications can be done on existing ADA licenses using setLicenseDetails operation. Other than the license
             ID and license type, all other parameters of the ADA licenses can be modified using
             this operation.
             

Set an expiry date on a license
             
Add new users and/or groups to a license
             
Remove users and/or groups from a license
             
Set reason for a license
             



Teamcenter Component:

             Authorized Data Access - Authorized Data Access (ADA) is a security solution that
             complements Access Manager rules to control access to sensitive data through the
             use of data classification, user clearance, and time bound authorizing documents
             (ADA Licenses).
             
        :param LicenseInfo: 
                         Structures containing the details of the licenses to be created/modified.
             
        :return: 
        """
        ...

