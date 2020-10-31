import requests
import json
from bs4 import BeautifulSoup
import os
import webbrowser
from sqlToPyton import viewData,insertData,deleteData

#deleteData()#Löscht den gesamten Inhalt in der SQL Datenbank


def json_from_url(url,tag):

    parser = "html.parser"#gibt der print Ausgabe Struktur
    req = requests.get(url)
    soup = BeautifulSoup(req.text, parser)#Greift aus das HTML file zu
    
    all_ld_json=soup.find_all("script", {"type":"application/ld+json"})#findet alle Scripte die ld+json enthalten
    
    ld_json=str(all_ld_json[1]).strip('[]').replace('&quot;', '')#in ld+json umwandeln und die eckigen Klammern entfernen
    
    #Der Inhalt des ld+json wird herraus gefiltert
    start=ld_json.find("ld+json")
    str_ende=ld_json.find("</script>")
    input_json=json.loads(ld_json[start+9:str_ende])
    
    content_json=input_json[tag][:]#nur die Inhalte die unter dem Tag ... abgespeichert sind werden herrausgegeben
    return content_json

os.system("CLS")#Für windows
#os.system('clear')#für Linux

#url='https://www.chefkoch.de/rs/s0/'#nach allem suchen
url='https://www.chefkoch.de/rs/s0t50/'#nach einfachen rezepten suchen

print("Bist du Vegetarier oder Veganer?")

input_vegan=input().lower()

#Je nach dem ob man angegeben hat ob man Veganer, Vegetariere oder nichts der beiden ist wir der URL angepasst
if input_vegan=="ja"or input_vegan=="vegan":
    input_vegan="vegan"
    url='https://www.chefkoch.de/rs/s0g111/'
elif input_vegan=="vegetarisch"or input_vegan=="vegetarier":
    url='https://www.chefkoch.de/rs/s0t32/'
elif input_vegan=="nein":
    url='https://www.chefkoch.de/rs/s0t50/'  
else:
    print("ich habe die Eingabe nicht verstanden und gehe davon aus das du nichts von beiden bist.")


print("Was befindet sich in deinem Kühlschrank?\nWenn sie mehrere Zutaten haben trennen sie diese durch ein + z.B. Nudeln+Tomaten ")
input1=input().replace(' ','+')#falls jemand ein Leerzeichen statt + macht wird das ersetzt durch +
url=url+input1+'/Rezepte.html'

response=requests.get(url)#es wir nach allen Rezepten für die Zutaten gesucht


if str(response)=="<Response [200]>":#abfrage ob die Seite erreichbar ist
    
    all_recipes=json_from_url(url,"itemListElement")#Liste mit allen Rezepten die zur Auswahl stehen
    
    choose_recipe=""
    rec_index=5
    while isinstance(choose_recipe,str) or choose_recipe>=rec_index: #die schleife wird solange wieder holt bis choose_recipe kein String ist oder eine nummer die kleiner als choose_recipe ist
            
        os.system("CLS")#Für windows
        #os.system('clear')#für Linux
        
        for i in range(0,rec_index):#gibt die ersten 5 Rezeptnamen aus die es findet und den dazugeörigen index
            print(i,all_recipes[i]["name"])
            
        choose_recipe=input("\nGeben sie Zahl vor dem jeweiligen Rezept ein das sie wollen oder geben sie Nein ein für mehr Rezepte:\n")
        
       
        if choose_recipe.isdigit():#wenn choose_recipe eine Zahl ist das true
            if int(choose_recipe)<rec_index:#überprüfen ob die Zahl sinn macht
                break;
            elif int(choose_recipe)>=rec_index:
                print("Sie müssen eine der Zahlen an geben die vor den Rezeptnamen steht. Diese Zahl war leider zu groß.")
        rec_index=rec_index+5#index wird um 5 erhöht. Heist die nächsten 5 Rezeptideen werden angezeigt
            
    
    os.system("CLS")#Für windows
    #os.system('clear')#für Linux
    
    print("\nSie haben",all_recipes[int(choose_recipe)]["name"],"ausgewählt")
    
    recipe_name=all_recipes[int(choose_recipe)]["name"]
    recipe_url=all_recipes[int(choose_recipe)]["url"]


    insertData(input1,input_vegan,recipe_name,recipe_url,)#daten in SQL-DatenBank einfügen. SQL-Datenbank ist bei mir der Verlauf 
    
    #print("Daten in SQL Data Base:")
    #viewData()#wenn man die SQL-Datenbank sehen will den Befehl einfügen

    print(recipe_url)#Die URL wir ausgegeben. Sozusagen als Quelle
    
    recipeIngredient=json_from_url(recipe_url,"recipeIngredient")#es werden die Zutaten herrausgefiltert
    print("\nDas sind die Zutaten die du dafür brauchst:")
    print(*recipeIngredient,sep="\n")
    
    recipe_instruction=json_from_url(recipe_url,"recipeInstructions")#es wir die Anleitung herrausgefiltert
    print("\nUnd so Kochst du das Gericht:\n")
    print(recipe_instruction)
    
    
else:
    print("nichts gefunden")
    
    

#such funktion ob Zutaten enthalten sind
# =============================================================================
# recipeIngredient=json_from_url(url,"recipeIngredient")
# print(recipeIngredient)
# 
# 
# 
# input1=input()
# i=0
# for i in range(len(recipeIngredient)):
#     temp=recipeIngredient[i]
#     if input1 in temp:
#         print("ist da")
#     
# =============================================================================

#print(input1 in recipeIngredient)
