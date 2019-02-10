from tastypie.resources import ModelResource
from accounts.models import Beneficiary
class FullAccess(ModelResource):
    class Meta:
        queryset= Beneficiary.objects.all()
        resource_name="full"
        
