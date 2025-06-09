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
    LockDate: System.DateTime
    """
            The freeze date for the license, after which the license cannot be attached to WorkspaceObject
            business objects. A NULL date specifies the license is not locked.
            """
    LicenseReason: str
    """
            A reason for the license to exist. This parameter can be a maximum of 128 bytes.
            This is an optional parameter and may have value as a blank string
            """
    QualifyingCfr: str
    """
            The qualifying Code of Federal Regulations (CFR) for ITAR licenses. This is not applicable
            for IP and Exclude licenses. This parameter can be a maxiumum of 80 bytes. This is
            an optional parameter and  may have value as a blank string.
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

class LicenseInput:
    """
    
LicenseInput represents a list of license
            IDs of ADA licenses, associated WorkspaceObject business objects, and applicable
            authorizing paragraph information (valid for ITAR licenses only).
            
    """
    def __init__(self, ) -> None: ...
    SelectedLicenses: list[str]
    """
            List of license IDs of ADA licenses. These are strings with a maximum of 128 bytes
            size.
            """
    Objects: list[Teamcenter.Soa.Client.Model.ModelObject]
    """
            List of WorkspaceObject business objects associated with the selectedLicenses.
            """
    EadParagraph: list[str]
    """
            List of authorizing paragraphs for the licenses being attached to WorkspaceObject
            business objects. These are strings with a maximum of 80 bytes size. The size of
            eadParagraph vector should match the size
            of the selectedLicenses (each entry in eadParagraph maps to corresponding entry in selectedLicenses). If a paragraph entry is not
            applicable for a specific license (paragraph entries are applicable only for licenses
            of ITAR type), then that entry can be left blank. System will ignore any paragraph
            entry if it is not applicable for a license to be attached. This is an optional parameter
            """

class LicenseManagement:
    """
    Interface LicenseManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def AttachLicenses(self, AttachLicense: list[LicenseInput]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation attaches ADA_License business objects to WorkspaceObject
             business objects such as Item, ItemRevision, Dataset, etc. as
             specified in each LicenseInput. Optionally,
             this operation can set/update authorizing paragraph information for the ITAR
             licenses being attached. Users performing this operation will need IP_ADMIN
             privilege to both the workspace objects and the licenses being attached, if the licenses
             are of type IP or Exclude, while ITAR_ADMIN privilege
             is needed to both the workspace objects and the licenses being attached, if the licenses
             are of ITAR license type. If the user does not have necessary privilege to
             attach any licenses, or if there is any other error while attaching licenses, the
             errors are returned as partial errors in ServiceData.
             

Use Cases:

             Use case 1: Attach ADA licenses to WorkspaceObject
             business objects

             You can attach ADA_License business objects of ITAR/IP/Exclude
             type to classified WorkspaceObject business objects using attachLicenses operation to grant access for users and/or groups
             listed on the licenses. Optionally, authorizing paragraph information can be specified
             for the ITAR licenses being attached through LicenseInput
             structure.
             

             Use Case 2: Modify authorizing paragraph for an attached ITAR license

             You can modify the authorizing paragraph information associated with an ITAR
             license already attached to a WorkspaceObject business object by passing in
             the license ID of the ITAR license, the WorkspaceObject business object
             and the modified authorizing paragraph information in LicenseInput
             structure using attachLicenses operation.
             


Teamcenter Component:

             Authorized Data Access - Authorized Data Access (ADA) is a security solution that
             complements Access Manager rules to control access to sensitive data through the
             use of data classification, user clearance, and time bound authorizing documents
             (ADA Licenses).
             
        :param AttachLicense: 
                         Structures containing information on licenses to attach, workspace objects to attach
                         to, and associated authorizing paragraph information (applicable for <b>ITAR</b>
                         licenses).
             
        :return: 
        """
        ...
    def GetLicenseDetails2(self, LicenseIds: list[str]) -> GetLicenseDetailsResponse:
        """    
             This operation gets the properties for each ADA_License business object specified
             in licenseIds and returns them in LicenseDetails structures as part of GetLicenseDetailsResponse.
             The LicenseDetails contains information for
             properties such as license type, license ID, expiry date, lock date, reason, in accordance
             with, and associated users and groups, for a given license. If there is no matching
             license for a given license ID, LicenseDetails structure for that license will contain
             Not_found as the value for license ID, while
             the rest of the parameters will contain NULL values. However, if the user does not
             have READ privilege to any license or if there is any unexpected error while getting
             property information, the errors are returned in the ServiceData
             of GetLicenseDetailsResponse.
             

Use Cases:

             Use Case 1: Get properties of an ADA License

             You can get properties of an ADA_License business object of type ITAR/IP/Exclude
             using getLicenseDetails2 operation by providing
             license ID for the license.
             

             Use Case 2: Check the existence of an ADA License

             You can check if an ADA_License businesses object with given license ID exists
             using getLicenseDetails2 operation.
             


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
    def SetLicenseDetails(self, LicenseInfo: list[LicenseDetails]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation creates or modifies an ADA_License business object for each
             LicenseDetails supplied. The LicenseDetails contains information for properties such as license
             type, license ID, expiry date, lock date, reason, in accordance with, and associated
             users and groups, for a given license. If a specified license ID already exists,
             the rest of the property values are updated on that license. However, if the license
             ID does not exist, then a new license of the specified type and ID will be created,
             and the rest of the properties are set on the created license. The user performing
             the operation will need the privilege specified in the ADA_license_administration_privilege
             site preference to create/modify an ADA License. If a user does not have the necessary
             privilege or if there is a validation error, the operation would fail and the error
             is returned in the ServiceData.
             

Use Cases:

Use Case 1: Create an ADA license

             You can create a new ADA license of type ITAR/IP/Exclude using setLicenseDetails operation by providing a unique license ID for
             the license using LicenseDetails structure.
             


             Use Case 2: Modify an ADA License

             The following types of modifications can be done on existing ADA licenses using setLicenseDetails operation. Other than the license
             ID and license type, all other parameters of the ADA licenses can be modified using
             this operation.
             

Set an expiry or lock date on a license
             
Unlock licenses by specifying a NULL date or a future date for lockDate
             parameter
             
Add new users and/or groups to a license
             
Remove users and/or groups from a license
             
Specify value for qualifying code of federal regulations for ITAR
             licenses
             
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

