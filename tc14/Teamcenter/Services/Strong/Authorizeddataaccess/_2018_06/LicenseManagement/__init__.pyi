import System
import Teamcenter.Soa.Client.Model
import typing

class LicenseDetails:
    """
    LicenseDetails structure represents all the details of an ADA License object.
    """
    def __init__(self, ) -> None: ...
    LicenseType: str
    """
            The type of ADA License object. Supported types are  &lt;i&gt;ITAR_License&lt;/i&gt;,
            &lt;i&gt;Exclude_License&lt;/i&gt;, or &lt;i&gt;IP_License&lt;/i&gt;.
            """
    LicenseId: str
    """The unique ID of the license. This is string with a maximum of 128 characters."""
    NewLicenseId: str
    """
            The unique ID of the license. This is string with a maximum of 128 characters. A
            non-empty value indicates the licenseId will be replaced by newLicenseId.
            """
    LicenseCategory: str
    """
            The category property of an ADA license. This is an optional parameter of string
            type 128 characters in size. The value specified for licenseCategory parameter must
            match one of the values in the LOV associated with Category property on the specifc
            ADA license type.This is an optional parameter and may be left as a blank string
            (&quot;&quot;).
            """
    UserCitizenships: list[str]
    """
            A list of user citizenships property values of an ADA license. This is an optional
            parameter. The value specified for userCitizenships parameter is an ISO-3166 two-letter
            country code. If a valid country code is not specified, partial error code 10219
            will be returned.
            """
    ExpiryDate: System.DateTime
    """
            The expiry date for the license, after which the license cannot be attached to a
            WorkspaceObject and ceases to grant the access to users or groups listed on
            the license. The value specified for expiryDate should be greater than or equal to
            current date, unless the value is same as current value on an existing license. A
            NULL date specifies the license will never expire.
            """
    LockDate: System.DateTime
    """
            The freeze date for the license, after which the license cannot be attached to a
            WorkspaceObject. The value specified for this parameter should be greater
            than the current date and should be less than the value specified for expiryDate
            parameter, unless the value is same as current value on an existing license. A NULL
            date specifies the license is not locked.
            """
    LicenseReason: str
    """
            A reason for the license to exist. This parameter can be a maximum of 128 characters.
            This is an optional parameter and and  may be left as a blank string (&quot;&quot;).
            """
    QualifyingCfr: str
    """
            The qualifying Code of Federal Regulations (CFR) for ITAR licenses. This is not applicable
            for IP and Exclude licenses. This parameter can be a maxiumum of 80 characters. This
            is an optional parameter and  may have value as a blank string (&quot;&quot;).
            """
    Users: list[str]
    """
            A list of users associated with a license identified by &lt;font face=&amp;quot;courier&amp;quot;
            height=&amp;quot;10&amp;quot;&gt;licenseId&lt;/font&gt;. When
            the license is attached to a classified WorkspaceObject, the users listed
            on the license will get access to the WorkspaceObject, based on the access
            rules.
            """
    Groups: list[str]
    """
            A list of names of groups associated with the license identified by &lt;font
            face=&amp;quot;courier&amp;quot; height=&amp;quot;10&amp;quot;&gt;licenseId&lt;/font&gt;.
            For subgroups, the full names should be specified. When the license is attached to
            a classified WorkspaceObject;, the users from the groups or subgroups listed
            on the license will get access to the workspace objects, based on the access rules.
            This parameter represents an array of group name strings of upto 256 characters in
            size.
            """

class LicenseManagement:
    """
    Interface LicenseManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CreateOrUpdateLicense(self, LicenseInfo: list[LicenseDetails]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation creates or modifies an ADA_License business object for each LicenseDetails
             supplied. The LicenseDetails contains information for properties such as license
             type, license ID, category, citizenship, expiry date, lock date, reason, in accordance
             with, and associated users and groups, for a given license. If a specified license
             ID already exists, the rest of the property values are updated on that license. However,
             if the license ID does not exist, then a new license of the specified type and ID
             will be created, and the rest of the properties are set on the created license. The
             user performing the operation will need the privilege specified in the ADA_license_administration_privilege
             site preference to create or modify an ADA License. If a user does not have the necessary
             privilege or if there is a validation error, the operation would fail and the error
             is returned in the ServiceData.
             

Teamcenter Component:

             Authorized Data Access - Authorized Data Access (ADA) is a security solution that
             complements Access Manager rules to control access to sensitive data through the
             use of data classification, user clearance, and time bound authorizing documents
             (ADA Licenses).
             
        :param LicenseInfo: 
                         Structures containing the details of the licenses to be created or modified
             
        :return: 
        """
        ...

