#from django.views.generic import ListView
from django.db import connection
from user_app.models import Expert

def run():
    # Fetch all experts
    experts = Expert.objects.all()

    # Display usernames
    print("Usernames of Experts:")
    for expert in experts:
        print(expert.user.username)

#how to make sure the script is run directly
if __name__ == "__main__":
    run()