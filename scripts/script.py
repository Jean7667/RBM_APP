from user_app.models import Skill

def run ():
    print("hello from runscript OK")


def run ():
    inst = Skill ()
    Skill.name = 'Java'
    Skill.category = 'Programming'
    Skill.level = 1
    inst.save()
    

