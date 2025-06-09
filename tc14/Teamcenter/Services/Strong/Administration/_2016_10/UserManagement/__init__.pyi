import System.Collections
import Teamcenter.Soa.Client.Model
import typing

class GetCurrentCountryPageInfoResponse:
    """
    The information used to populate the current country selection page.
    """
    def __init__(self, ) -> None: ...
    DisplayCountries: System.Collections.Hashtable
    """
            Map of key/value pairs (string, string) representing the selectable countries the
            user may choose when filling out the current country selection page.
            

Key is the ISO 3166-1 alpha-2 two letter country codes.
            
Value is the full country name.
            


            Examples: US - United States of America, GB - United Kingdom, and IN - India.
            """
    ExtraInfoOut: System.Collections.Hashtable
    """
            Map of key/value pairs (string, string).
            

Key: initialCountry. The initial value displayed in the current
            country pick list. The format is ISO 3166-1 alpha-2 two letter country. This is optional.
            The value may be the empty string.
            
Key: confidentialityStatement. The agreement that the user
            must read when filling out the current country page.
            

"""
    ServiceData: Teamcenter.Soa.Client.Model.ServiceData
    """ServiceData."""

class UserManagement:
    """
    Interface UserManagement
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def GetCurrentCountryPageInfo(self) -> GetCurrentCountryPageInfoResponse:
        """    
             This operation retrieves current configuration of country selection. The configuration
             is a list of selectable countries, the initial country to be displayed, and a customer
             configurable confidentiality statement.
             

Use Cases:

             This will be used for both RAC and AW to populate their current country selection
             pages.
             

Teamcenter Component:

             Organization Management - It maps Organization Management services documentation
             to BMIDE
             
        :return: 
        """
        ...
    def SaveAndValidateCurrentCountry(self, Selectedcountry: str) -> Teamcenter.Soa.Client.Model.ServiceData: ...

