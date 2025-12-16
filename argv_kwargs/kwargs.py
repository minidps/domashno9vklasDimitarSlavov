import json
def user_profile(**kwargs):
    profile={}
    for key,value in kwargs.items():
        profile[key]=value
    with open("profile.json","w",encoding="utf-8") as f:
        json.dump(profile, f)
user_profile(name="Dinka", age=69, city="Chernobyl")