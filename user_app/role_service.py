#role_service
"""
Update the user role profile is_expert is_customer is_manager
"""
from .models import Expert
import datetime

def update_user_role (user, is_expert, is_customer):
#raise error if both roles are selected.    
    if is_expert and is_customer:
        raise ValueError("You can't set both is_customer and is_manager")
#if user is no longer an expert remove instance
#check the user role profile is_expert is_customer 
    if is_expert: 
        expert_instance, created = Expert.objects.get_or_create(user=user)
        #then if created add the start_date and save
        if created:
            expert_instance.start_date = datetime.date.today()
            expert_instance.save()
    else:
        Expert.objects.filter(user=user).delete()    
     
#using get_or_create https://docs.djangoproject.com/en/5.0/ref/models/querysets/


