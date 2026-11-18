import json
with open("test.json","r",encoding="utf-8") as j :
    donne =json.load(j)

def show_menu(scenarios):
    for i in range (len(scenarios)):
        print(f"{scenarios[i]["id"]}. {scenarios[i]["situation"]}")

def get_response(choix , scenarios):
    dic_choix ={}
    for i in range (len(scenarios)):
        if choix == scenarios[i]["id"]:
            dic_choix["methode"] = scenarios[i]["method"]
            dic_choix["code"] = scenarios[i]["status"]
            dic_choix["message"] = scenarios[i]["message"]
            return dic_choix
    return None
    



show_menu(donne)

choix = input("Choisis une situation enter 1 et 6 ou 0 pour quitter : ")
while True :
    if choix == "0" :
        break
    result = get_response(choix, donne)
    if result == None :
        print("Choix invalide")
    else :
        print(f"la methode :{result["methode"]}")
        print(f"la message :{result["message"]}")
        print(f"le code :{result["code"]}")
        print("////////////////////////////////////////////")
    show_menu(donne)
    choix = input("Choisis une situation enter 1 et 6 ou 0 pour quitter : ")
