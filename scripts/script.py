#from django.views.generic import ListView
from django.db import connection
from user_app.models import Expert, Skill
import time

""" def run():
    # Fetch all experts
    experts = Expert.objects.all()

    # Display usernames
    print("Usernames of Experts:")
    for expert in experts:
        print(expert.user.username)

#how to make sure the script is run directly
if __name__ == "__main__":
    run() """
    
""" def run():
 # get skills from the table with user input filter
    all_skills = Skill.objects.all()

#  skills per category
    skills = {}
    for skill in all_skills:
        category = skill.category  
        if category not in skills:
            skills[category] = []
        skills[category].append(skill.name)

    print("list of category:")
    for category in skills:
        print(category)
    
    chose_category = input("Choose a category: ")    
    
    if chose_category in skills:
        print(f"Skills in {chose_category}:")
        for skill in skills[chose_category]:
            print(skill)
    else:
        print("not a category.")
    
    if __name__ == "__main__":
        run() """