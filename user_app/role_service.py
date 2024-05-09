#role_service
"""
Update the user role profile is_expert is_customer is_manager
"""
from models import CustomUser, Expert
import datetime

def update_user_role (user, is_expert, is_customer, is_manager):
#raise error if both roles are selected.    
#check the user role profile is_expert is_customer is_manager
#using get_or_create https://docs.djangoproject.com/en/5.0/ref/models/querysets/
 if is_expert: 
     expert_instance, created = Expert.objects.get_or_create(user=user)
#then if created add the start_date and save
    if created:
    expert_instance.start_date = datetime.date.today()
    expert_instance.save()
    
 if is_expert and is_customer:
     raise ValueError("You can't set both is_customer and is_manager")
 #if user is no longer an expert remove instance
 else:
     Expert.objects.filter(user=user).delete()    
     
