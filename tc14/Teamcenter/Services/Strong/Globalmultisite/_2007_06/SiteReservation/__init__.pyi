import System
import Teamcenter.Soa.Client.Model
import typing

class SiteReservation:
    """
    Interface SiteReservation
    """
    def __init__(self , *args: typing.Any) -> None: ...
    def CancelSiteCheckOut(self, Objects: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation is used in offline GMS. It is used to cancel site check out objects
             which has been site checked out to another site and removes the reservation objects.
             If errors occur, they are returned in the ServiceData structure.
             

Use Cases:

             User can pass a list of objects which have been in site checked out status to do
             cancel site check in.
             

Dependencies:

             siteCheckOut
             

Teamcenter Component:

             Briefcase - Offline GMS capabilitiy tailored to support the disconnected supplier
             use case for data transfer and synchronization.
             
        :param Objects: 
<ul>
<li type="disc"><b>Item</b>
</li>
<li type="disc"><b>ItemRevision</b>
</li>
<li type="disc"><b>PSBOMView</b>
</li>
<li type="disc"><b>PSBOMViewRevision</b>
</li>
<li type="disc"><b>Form</b>
</li>
<li type="disc"><b>Dataset</b>
</li>
</ul>

        :return: 
        """
        ...
    def SiteCheckIn(self, Objects: list[Teamcenter.Soa.Client.Model.ModelObject]) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation is used in offline GMS. It is used to check in objects that were checked
             out to another site and removes the reservation objects. If errors occur, they are
             returned in the ServiceData structure.
             

Use Cases:

             User can pass a list of objects which have been in site checked out status to do
             site check in. A series of related objects will be site checked in along with the
             input objects Item, ItemRevision or Dataset:
             

Item        Related Master
             Form(s)
             
ItemRevision    Related Master Form(s)
             
Dataset        All namedReference
             objects which are WorkspaceObject




Dependencies:

             siteCheckOut
             

Teamcenter Component:

             Briefcase - Offline GMS capabilitiy tailored to support the disconnected supplier
             use case for data transfer and synchronization.
             
        :param Objects: 
<ul>
<li type="disc"><b>Item</b>
</li>
<li type="disc"><b>ItemRevision</b>
</li>
<li type="disc"><b>PSBOMView</b>
</li>
<li type="disc"><b>PSBOMViewRevision</b>
</li>
<li type="disc"><b>Form</b>
</li>
<li type="disc"><b>Dataset</b>
</li>
</ul>

        :return: 
        """
        ...
    def SiteCheckOut(self, Objects: list[Teamcenter.Soa.Client.Model.ModelObject], SiteId: int, Comment: str, ChangeId: str) -> Teamcenter.Soa.Client.Model.ServiceData:
        """    
             This operation is used in offline GMS. It is used to checkout objects to another
             site, so that after the objects are imported into that site, they are modifiable.
             If errors occur, they are returned in the ServiceData structure.
             

Use Cases:

             User can pass a list of objects (only these six types and their sub types are supported:
             Item, ItemRevision, Form, Dataset, BOMView, BOMViewRevision)
             to do site check out. A series of related objects will be site checked out along
             with the input objects Item, ItemRevision or Dataset:
             

Item        Related Master
             Form(s)
             
ItemRevision    Related Master Form(s)
             
Dataset        All namedReference
             objects which are WorkspaceObject




Teamcenter Component:

             Briefcase - Offline GMS capabilitiy tailored to support the disconnected supplier
             use case for data transfer and synchronization.
             
        :param Objects: 
<ul>
<li type="disc"><b>Item</b>
</li>
<li type="disc"><b>ItemRevision</b>
</li>
<li type="disc"><b>PSBOMView</b>
</li>
<li type="disc"><b>PSBOMViewRevision</b>
</li>
<li type="disc"><b>Form</b>
</li>
<li type="disc"><b>Dataset</b>
</li>
</ul>

        :param SiteId: 
                         Id of the site that the objects are to be checked out to.
             
        :param Comment: 
                         Check out comment, the reason for the site check out.
             
        :param ChangeId: 
                         The mark for this site check out process.
             
        :return: 
        """
        ...

