#role_service
"""
Update the user role profile is_expert is_customer is_manager
"""
from models import CustomUser, Expert
import datetime

def update_user_role (user, is_expert, is_customer, is_manager):
#check the user role profile is_expert is_customer is_manager
 if is_expert: 
     #using get_or_create https://docs.djangoproject.com/en/5.0/ref/models/querysets/
 if is_expert and is_customer:
     raise error (You can't set both is_customer and is_manager)    
     expert_instance, created = Expert.objects.get_or_create(user=user)
if created:
    expert_instance.start_date = datetime.date.today()
    expert_instance.save()
    