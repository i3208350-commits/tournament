from email.charset import add_alias
from shlex import split

team = {
    "id": 1,
    "name":0,
    "played":0,
    "wins":0,
    "draws":0,
    "losses":0,
    "goals_for":0,
    "goals_againts":0,
    "ponits":0}
itams=[]

matches={
    "home_team_id":0,
    "away_team_id":0,
    "home_goals":0}
def menu():

    print("1. Add team")
    print("2. Show all teams")
    print("3. Add match result")
    print("4. Show standings")
    print("5. Show leading team")
    print("6. Show best attacking team")
    print("7. Show team success rate")
    print("8. Show teams without wins")
    print("9. Show tournament summary")
    print("10.Check championship potential")
    print("0. Exit Choose an option:")

    choice=input("Tap your choice")
    if choice==1:
        add_team(itams)
    if choice==2:
        show_all_teams(itams)
    # if choice==3:



def add_team():
    a_test_that_is_filled()
    team = {
        "id": 1,
        "name": 0,
        "played": 0,
        "wins": 0,
        "draws": 0,
        "losses": 0,
        "goals_for": 0,
        "goals_againts": 0,
        "ponits": 0}

    add_1=input("הכנס את שם הקבוצה")
    for i in itams:
        if i["name"]==add_1:
            print("השם קיים במערכת")

    team["name"]=add_1
    for i in itams:
         team["id"]=i["id"]+1
    itams.append(team)

def show_all_teams():
    for i in itams:
        print(f"The group name is {i["name"]}")

def add_match_result():
    match=input("הכנס תוצאת משחק")
    match=split(match,":",)


add_team()
add_team()
print(itams)
add_team()
print(itams)
show_all_teams()


def a_test_that_is_filled(x):
    if len(x)==0:
         menu()



if __name__=="__main__":
       menu()
