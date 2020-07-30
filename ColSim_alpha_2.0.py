# Game Project: Culture Simulator
# June 26, 2020

#Version 1.1. update: now with basic UI, thank you Wisly, see menus for details
#version 1.11: finalized ui for prototype, mostly. I think it's playable, as long as you build houses and assign them to clans
#wisly: search "!!" for places where I have notes for you

import random #importing random: random.randint(1, 6)


total_unit_counter = 0 #counts total units created
units = {} #!
total_clan_counter = 0 #counts total clans created
clans = {} #!
base_stat = 3 #adjust this to adjust starting stats
dice = 0

def roll(x, y):
    global dice
    dice = random.randint(x, y)
    return dice

    #Global variable: Resource Supplies

wood = 20
gold = 50
techpt = 0
puzzlenut = 0
ore = 0
metal = 0
jade = 0
crystal = 0
hide = 0
oil = 0
food = 0

buildings = {}
total_building_counter = 0

date = 1
hour = 9


#Wisly's Ux stuff

import tkinter as tk
# Create GUI window
root = tk.Tk()
root.geometry("800x600")

#Frames
event = tk.Frame(root, bd=1)
event.place(relx=0.1, rely=0.45, relwidth=0.75, relheight=0.45)


    
#Class: Unit (citizen)

def find_location(u):
    loc = "None"
    for i in list(buildings.values()):
        if u in i.inside:
            loc = i
    

class unit:
    def __init__(self, number, clan, culture):
        self.number = number
        self.clan = clan
        self.culture = culture
        self.religion = religion
        self.firstname = random_f_name(self.culture, self.clan) 
        self.name = (str(self.firstname) + " " + str(self.clan.name))
        self.str = roll(1, base_stat) #strength- for manual labor
        self.cre = roll(1, base_stat) #creativity- for making crafts and art
        self.com = roll(1, base_stat) #combat- for battle
        self.int = roll(1, base_stat) #intellegence- for research, literacy, and certain other things
        self.cha = roll(1, base_stat) #charisma- ability to make friends and sway them
        self.prestige = 0 #prestige- how important this person is
        self.wallet = 0 #the amount of money they have
        self.items = []
        self.age = random.randint(1, 20)
        self.sleep = 0
        self.job = nojob
        self.hunger = 0
        self.happy = 50
        self.location = find_location(self)
        self.project = 0 #a progress meter for a work of literature they are writing
        
        self.status = []
        self.gender = "Pupae"
        #List of beliefs kept here
        self.beliefs = []
        modify_belief(self, clan.relig.faith, reason("Homeland Belief", roll(1, 40), 100))
        #some age modifiers
        
        if self.age > 12:
            x = roll(0, 4)
            if x == 0 or x == 1:
                self.gender = "Hatcher"
                self.com += roll(4,7)
            if x == 2 or x == 3:
                self.gender = "Gatherer"
                y = roll(0, 1)
                if y == 0:
                    self.cre += roll(4, 7)
                if y == 1:
                    self.str += roll(4, 7)
            if x == 4:
                self.gender = "Cerebral"
                y = roll(0, 1)
                if y == 0:
                    self.int += roll(5, 8)
                if y == 1:
                    self.cha += roll (5, 8)
        if self.age > 15:
            x = roll(1, 5)
            if x == 1:
                self.str += 3
            if x == 2:
                self.cre += 3
            if x == 3:
                self.com += 3
            if x == 4:
                self.int += 3
            if x == 5:
                self.cha += 3
        self.hpcap = 5 + self.com
        self.hp = self.hpcap
        

def find_highest_stat(unit):
    x = unit.str
    y = "Strength"
    if unit.cre > x:
        x= unit.cre
        y = "Creativity"
    if unit.com > x:
        x = unit.com
        y = "Combat"
    if unit.int > x:
        x = unit.int
        y = "Intelligence"
    if unit.cha > x:
        x = unit.cha
        y = "Charisma"
    ans = str(y + ": " + str(x))
    return ans

#Class: Clan

def generate_clan_member(clan):
    global total_unit_counter
    number = (total_unit_counter + 1)
    total_unit_counter = total_unit_counter + 1
    x = unit(number, clan, clan.culture) #&&&
    clan.size = clan.size + 1
    units.update({total_unit_counter : x})
    return x

def generate_clan(culture, size):
    global total_clan_counter
    size = size
    number = (total_clan_counter + 1)
    total_clan_counter = total_clan_counter + 1
    x = clan(number, culture, size) #&&&
    clans.update({x.name : x})
    x.elder = choose_elder(x.name)
    return x




clan_list = [1]
        
class clan:
    def __init__(self, number, culture, start_size):
        global clan_list
        self.number = number
        self.culture = culture
        self.name = str(random_name(self.culture))
        clan_list.append(self.name)
        self.size = 0
        self.start_size = start_size
        self.relig = out_of(culture.likely_religions)
        count = 0 #generates first clan members
        while count < self.start_size:
            generate_clan_member(self)
            count = count + 1

      

def choose_elder(sclan):
    thing = clans[sclan]
    oldestage = 0
    oldest = None
    for i in units:
        it = units[i]
        if it.clan == thing:
            if it.age > oldestage:
                oldest = it
                oldestage = it.age
    oldest.status.append("Elder")
    oldest.prestige += 10
    return oldest

#Class: Culture

class culture:
    def __init__(self, name):
        self.name = str(name)
        self.f_names = []
        self.l_names = []
        self.r_names = []
        self.likely_religions = {}
        self.craftnames = []

def random_culture():
    x = roll(1, 2)
    if x == 1:
        return knani
    else:
        return huxley

#adding new names to culture
def add_random_l_names(culture, names):
    for i in names:
        culture.l_names.append(i)

def add_random_f_names(culture, names):
    for i in names:
        culture.f_names.append(i)

def add_random_r_names(culture, names):
    for i in names:
        culture.r_names.append(i)

def random_name(culture):
    global total_unit_counter
    x = (0-1)
    for i in culture.l_names:
        x = x + 1
    choose = random.randint(0, x)
    ans = culture.l_names[choose]
    a = 0
    for i in clans.keys():
        a = a + 1
        if a == x:
            ans = str(culture.l_names[choose] + "2")
        elif i == ans:
            ans = random_name(culture)
    return ans

def random_f_name(culture, tclan):
    x = (0-1)
    for i in culture.f_names:
        x = x + 1
    choose = random.randint(0, x)
    ans = culture.f_names[choose]
    for i in units:
        it = units[i]
        if it.clan == tclan and ans == it.firstname:
            ans = random_f_name(culture, tclan)
    return ans

#Class: Belief


class belieftype: #type of beliefs- the archtype, instead of a specific instance within a unit. Ex: rebellion
    def __init__(self, name, description):
        
        self.description = str(description)
        self.name = str(name)
        self.triggers = {} #When an event is triggered, something will happen that will modify this belief. The key is the trigger event, and the lock is the value it's modified by
        self.restrictedfrom = [] #list of things that can't exist with this belief &&&&&&
        self.events = {}
        self.is_religion = False

class belief: #Ex: rebellion belief within George, +20
    def __init__(self, belieftype):
        self.belieftype = belieftype
        self.description = belieftype.description
        self.name = belieftype.name
        self.triggers = belieftype.triggers
        self.score = 0
        self.reasons = []

class reason(belief): #Didn't get to eat, +20 to rebellion
    def __init__(self, description, scoremod, length):
        self.description = description
        self.scoremod = scoremod
        global date
        self.length = length
        self.expiration = date+length

def check_for_belief(unit, z): #checks if the unit has this belief, and returns either the belief or false
    x = 0
    for i in unit.beliefs:
        if i.belieftype == z:
            x = i
    if x != 0:
        return x
    elif x == 0:

        return False

def modify_belief(unit, belieftype, reason):
    x = check_for_belief(unit, belieftype) #Is this belief in the unit's mind?
    if unit.culture == knani and belieftype == prej_knani:
        unit.happy -= 20
    elif unit.culture == huxley and belieftype == prej_huxley:
        unit.happy -= 20
    elif unit.culture == uul and belieftype == prej_uul:
        unit.happy -= 20
    else:
        if x == False: #if not
            x = belief(belieftype) #makes a new belief instance
            unit.beliefs.append(x) #adds it to the unit's mind
        x.reasons.append(reason) #adds a new reason to the list of reasons
        x.score += reason.scoremod #modifies the belief's score
    

    
def b_score(belief):
    return belief.score

def rank_unit_belief(unit): #sorts a units beliefs by score
    unit.beliefs.sort(reverse = True, key = b_score)

def display_beliefs(unit):
    num = 1
    for i in unit.beliefs:
        text(i.name)
        text("Rank: "+ str(num))
        num += 1
        text(str(i.score))
        space()
        
    
    
        

#Menu stuff

def list_members(sclan):
    tclan = clans[sclan]
    text("Clan " + tclan.name)
    text("")
    text("Elder: " + tclan.elder.name)
    text("Culture: " + str(tclan.culture.name))
    text("")
    for i in units:
        it = units[i]
        if it.clan == tclan:
            space()
            text("Name: " + it.name)
            text(find_highest_stat(it))
        



def list_clans():
    x = clans.keys()
    for i in x:
        space()
        text("Clan " + i)
        text("Culture: " + clans[i].culture.name)
        text("Elder: " + clans[i].elder.name)
        text("Size: " + str(clans[i].size))


#Game, menus, inputs
    #menus
        
def space():
    text(" ")


gamestate = False

def game():
    text("Game Start")
    global gamestate
    gamestate = True
    space()
    space()
    space()
    space()
    text("Instructions: type 'clans' to see a list of your clans, and then type a unit's name to see more details on it. Type 'go' to advance the game one hour. Village lets you build buildings.")
    text("Job will take you to the job menu. Typing 'select job' will allow you to select a building. Farms give food, and goldmines give gold. Once a building is selected, go back into job menu")
    text("and type the number of a unit. That unit will be assigned to that building, and will work at the correct hour.")
    text("You lose if you run out of gold. Hungry units will slowly lose hp. Units go to the market and buy food with wallet earned from jobs when they are running out. Price is (kinda) supply and demand.")
    text("Right now strength is the only score that matters, and affects output of goldmines, farms, and sawmills. Use sawmills to get wood, use wood to build more buildings. Buildings cost 5.")
    text("Also every clan needs a house if they want to sleep and eat. You can assign a clan a house by choosing a clan in the clan menu, then typing in assign. 1 clan per house!")
    text("Your food stockpile spoils every 3 days (good for raising prices!) and you get a new clan every week. Good luck!")
    space()
    while gamestate == True:
        main_menu()


def clan_menu():
    menu = tk.Frame(root, bg="black", bd=1) #main menu frame and buttons
    menu.place(relx=0.1, rely=0.3, relwidth=0.75, relheight=0.1)
    event = tk.Frame(root, bd=1)
    event.place(relx=0.1, rely=0.45, relwidth=0.75, relheight=0.45)
    btn_back = tk.Button(menu, text="Back", command=main_menu)
    btn_back.place(relx=0.5, rely=0.3)
    lbl_clanm = tk.Label(event, text = "Select Clan name:")
    lbl_clanm.place(relx = 0.3, rely=0.05)
    lst_clans = tk.Listbox(event)
    lst_clans.place(relx=0.5, rely=0.1)
    x= 1 #!! this bit is one ex of how I plug in the game data into the UX- the "middle end" if you will. I think I got the middle end handled for now :)
    for i in list(clans.keys()): 
        lst_clans.insert(x, clans[i].name)
        x += 1
    btn_mem = tk.Button(event, text = "List Members", command = lambda: member_menu(clans[lst_clans.get(lst_clans.curselection()[0], last = None)])) #!! this is how to return the text of the highlighed thing: list.get(list.curselection()[0], last = None)
    btn_mem.place(relx=0.75, rely=0.9)
    btn_assign = tk.Button(event, text = "Assign Clan to House", command = lambda: assign_menu(clans[lst_clans.get(lst_clans.curselection()[0], last = None)]))
    btn_assign.place(relx=0.25, rely=0.9)


def member_menu(tclan):
    menu = tk.Frame(root, bg="black", bd=1) #main menu frame and buttons
    menu.place(relx=0.1, rely=0.3, relwidth=0.75, relheight=0.1)
    event = tk.Frame(root, bd=1)
    event.place(relx=0.1, rely=0.45, relwidth=0.75, relheight=0.45)
    btn_back = tk.Button(menu, text="Back", command=clan_menu)
    btn_back.place(relx=0.5, rely=0.3)
    lbl_memm = tk.Label(event, text = "Select Member name:")
    lbl_memm.place(relx = 0.3, rely=0.05)
    lst_clans = tk.Listbox(event)
    lst_clans.place(relx=0.5, rely=0.1)
    x = 1
    for i in units:
        it = units[i]
        if it.clan.name == tclan.name:
            lst_clans.insert(x, it.name)
            x +=1
    btn_show = tk.Button(event, text = "Show Member's stats", command = lambda: show_stats(find_unit(lst_clans.get(lst_clans.curselection()[0], last = None))))
    btn_show.place(relx=0.5, rely=0.9)




def show_stats(unit): #!! edited this by adding extra labels. Once you get the event prompt working, we can change this or make it nicer
    menu = tk.Frame(root, bg="black", bd=1) #main menu frame and buttons
    menu.place(relx=0.1, rely=0.3, relwidth=0.75, relheight=0.1)
    event = tk.Frame(root, bd=1)
    event.place(relx=0.1, rely=0.45, relwidth=0.75, relheight=0.45)
    btn_back = tk.Button(menu, text="Back", command=clan_menu)
    btn_back.place(relx=0.5, rely=0.3)
    a = tk.Label(event, text = unit.name)
    a.place(relx = 0.3, rely=0.05)
    b = tk.Label(event, text = ("Age: " + str(unit.age)))
    b.place(relx = 0.3, rely=0.13)
    c = tk.Label(event, text = (("Gender: " + unit.gender)))
    c.place(relx = 0.3, rely=0.21)
    d = tk.Label(event, text = (("Status: " + str(unit.status))))
    d.place(relx = 0.3, rely=0.29)
    e = tk.Label(event, text = (("Prestige: " + str(unit.prestige))))
    e.place(relx = 0.3, rely=0.37)
    f = tk.Label(event, text = (("Strength: " + str(unit.str))))
    f.place(relx = 0.3, rely=0.45)
    g = tk.Label(event, text = (("Creativity: " + str(unit.cre))))
    g.place(relx = 0.3, rely=0.53)
    h = tk.Label(event, text = (("Combat: " + str(unit.com))))
    h.place(relx = 0.3, rely=0.61)
    i = tk.Label(event, text = (("Intelligence: " + str(unit.int))))
    i.place(relx = 0.3, rely=0.69)
    j = tk.Label(event, text = (("Charisma: " + str(unit.cha))))
    j.place(relx = 0.3, rely=0.77)
    k = tk.Label(event, text = (("Wallet: " + str(unit.wallet))))
    k.place(relx = 0.3, rely=0.85)
    l = tk.Label(event, text = "Hunger: " + str(unit.hunger))
    l.place(relx = 0.6, rely=0.05)
    m= tk.Label(event, text = "Happiness: " + str(unit.happy))
    m.place(relx = 0.6, rely=0.13)
    n= tk.Label(event, text = (("Job: " + str(unit.job.name))))
    n.place(relx = 0.6, rely=0.21)
    o= tk.Listbox(event)
    o.place(relx=0.6, rely=0.29)
    x= 1
    for i in unit.beliefs:
        o.insert(x, (i.name))
        x += 1
    
    btn_show = tk.Button(event, text = "Show Belief", command = lambda: show_belief(unit, find_belief(unit, o.get(o.curselection()[0], last = None))))
    btn_show.place(relx=0.5, rely=0.9)
    btn_back = tk.Button(menu, text="Back", command= lambda: member_menu(unit.clan))
    btn_back.place(relx=0.5, rely=0.3)

def find_belief(unit, beliefname): #gives belief object from name and unit
    ans = None
    for i in unit.beliefs:
        if i.name == beliefname:
            ans = i
    return ans

def show_belief(unit, belief): #screen for showing selected belief and reasons

    menu = tk.Frame(root, bg="black", bd=1) #main menu frame and buttons
    menu.place(relx=0.1, rely=0.3, relwidth=0.75, relheight=0.1)
    event = tk.Frame(root, bd=1)
    event.place(relx=0.1, rely=0.45, relwidth=0.75, relheight=0.45)
    btn_back = tk.Button(menu, text="Back", command=clan_menu)
    btn_back.place(relx=0.5, rely=0.3)
    
    ttxt_event = tk.Text(event, height=150, width=600)

    ttxt_event.insert(tk.END, str(belief.name + ": " + str(belief.score) + "\n"))
    if belief.belieftype.is_religion == True:
        ttxt_event.insert(tk.END, str("A religion" + "\n"))
    ttxt_event.insert(tk.END, str("\n"))
    r = []
    for i in belief.reasons:
        r.append(str(i.scoremod) + "- " + i.description + "\n")
    for i in r:
        ttxt_event.insert(tk.END, str(i))
    ttxt_event.configure(state='disabled')
    scroll = tk.Scrollbar(event, orient = 'vertical', command=ttxt_event.yview)
    scroll.pack(side="right", expand=True, fill='y')
    ttxt_event.configure(yscrollcommand=scroll.set)
    ttxt_event.pack(side="right")

    
    btn_back = tk.Button(menu, text="Back", command= lambda: show_stats(unit))
    btn_back.place(relx=0.5, rely=0.3)





##Assign House Menu
def assign_menu(tclan):
    menu = tk.Frame(root, bg="black", bd=1) #main menu frame and buttons
    menu.place(relx=0.1, rely=0.3, relwidth=0.75, relheight=0.1)
    event = tk.Frame(root, bd=1)
    event.place(relx=0.1, rely=0.45, relwidth=0.75, relheight=0.45)
    btn_back = tk.Button(menu, text="Back", command=clan_menu)
    btn_back.place(relx=0.5, rely=0.3)
    lbl_memm = tk.Label(event, text = "Select house:")
    lbl_memm.place(relx = 0.3, rely=0.05)
    lst_house = tk.Listbox(event)
    lst_house.place(relx=0.5, rely=0.1)
    x = 1
    for i in list(buildings.keys()):
            if buildings[i].btype == "house":
                lst_house.insert(x, buildings[i].name)
                x = x +1
        
    btn_ass = tk.Button(event, text = "Assign to Selected House",command = lambda: assign_house(tclan, buildings[(lst_house.get(lst_house.curselection()[0], last = None))]))
    btn_ass.place(relx=0.5, rely=0.9)

def sort_str(x):
    return x.str

#Job Menu
def job_menu(): 
    menu = tk.Frame(root, bg="black", bd=1) #main menu frame and buttons
    menu.place(relx=0.1, rely=0.3, relwidth=0.75, relheight=0.1)
    event = tk.Frame(root, bd=1)
    event.place(relx=0.1, rely=0.45, relwidth=0.75, relheight=0.45)
    btn_back = tk.Button(menu, text="Back", command=main_menu)
    btn_back.place(relx=0.5, rely=0.3)
    lbl_memm = tk.Label(event, text = "Select Member name:")
    lbl_memm.place(relx = 0.3, rely=0.03)
    lst_clans = tk.Listbox(event)
    lst_clans.place(relx=0.3, rely=0.1)
    btn_s = tk.Label(event, text = "Strength:")
    btn_s.place(relx = 0.6, rely=0.03)
    s = tk.Listbox(event)
    s.place(relx=0.6, rely=0.1)
    x = 1
    y = list(units.values())
    y.sort(reverse = True, key = sort_str)
    for i in y:
        it = i
        lst_clans.insert(x, it.name)
        s.insert(x, str(it.str))
        x +=1
    btn_show = tk.Button(event, text = "Assign Job", command = lambda: job_assign(find_unit(lst_clans.get(lst_clans.curselection()[0], last = None))))
    btn_show.place(relx=0.5, rely=0.9)

###Job Assignment Menu
def job_assign(unit):
    menu = tk.Frame(root, bg="black", bd=1) #main menu frame and buttons
    menu.place(relx=0.1, rely=0.3, relwidth=0.75, relheight=0.1)
    event = tk.Frame(root, bd=1)
    event.place(relx=0.1, rely=0.45, relwidth=0.75, relheight=0.45)
    btn_back = tk.Button(menu, text="Back", command=job_menu)
    btn_back.place(relx=0.5, rely=0.3)
    a = tk.Label(event, text = unit.name)
    a.place(relx = 0.3, rely=0.05)
    b = tk.Label(event, text = ("Age: " + str(unit.age)))
    b.place(relx = 0.3, rely=0.13)
    c = tk.Label(event, text = (("Gender: " + unit.gender)))
    c.place(relx = 0.3, rely=0.21)
    d = tk.Label(event, text = (("Status: " + str(unit.status))))
    d.place(relx = 0.3, rely=0.29)
    e = tk.Label(event, text = (("Prestige: " + str(unit.prestige))))
    e.place(relx = 0.3, rely=0.37)
    f = tk.Label(event, text = (("Strength: " + str(unit.str))))
    f.place(relx = 0.3, rely=0.45)
    g = tk.Label(event, text = (("Creativity: " + str(unit.cre))))
    g.place(relx = 0.3, rely=0.53)
    h = tk.Label(event, text = (("Combat: " + str(unit.com))))
    h.place(relx = 0.3, rely=0.61)
    i = tk.Label(event, text = (("Intelligence: " + str(unit.int))))
    i.place(relx = 0.3, rely=0.69)
    j = tk.Label(event, text = (("Charisma: " + str(unit.cha))))
    j.place(relx = 0.3, rely=0.77)
    k = tk.Label(event, text = (("Wallet: " + str(unit.wallet))))
    k.place(relx = 0.3, rely=0.85)
    lbl_builds = tk.Label(event, text="Select Building to Assign Unit to:")
    lbl_builds.place(relx=0.6, rely=0.05)
    lst_builds = tk.Listbox(event)
    lst_builds.place(relx=0.6, rely=0.15)
    x = 1
    for i in buildings:
        it = buildings[i]
        lst_builds.insert(x, it.name)
        x +=1

    btn_ass = tk.Button(event, text = "Assign to Selected Building", command = lambda: hire(unit, buildings[(lst_builds.get(lst_builds.curselection()[0], last = None))]))
    btn_ass.place(relx=0.75, rely=0.9)

#Village Menu
def build_menu():
    global wood
    menu = tk.Frame(root, bg="black", bd=1) #main menu frame and buttons
    menu.place(relx=0.1, rely=0.3, relwidth=0.75, relheight=0.1)
    event = tk.Frame(root, bd=1)
    event.place(relx=0.1, rely=0.45, relwidth=0.75, relheight=0.45)
    btn_back = tk.Button(menu, text="Back", command=main_menu)
    btn_back.place(relx=0.5, rely=0.3)
    lbl_wood = tk.Label(event, text="Wood available: "+ str(wood))
    lbl_wood.place(relx=0.4, rely=0.01)
    lbl_stats = tk.Label(event, text = "Building List:")
    lbl_stats.place(relx=0.1, rely=0.1)
    op_builds = tk.Listbox(event)
    op_builds.place(relx=0.1, rely=0.2)
    op_builds.insert(1, "sawmill")
    op_builds.insert(2, "goldmine")
    op_builds.insert(3, "farm")
    op_builds.insert(4, "house")
    op_builds.insert(5, "market")
    op_builds.insert(6, "craftshop")
    op_builds.insert(7, "library")
    lbl_builds = tk.Label(event, text="Your Buildings")
    lbl_builds.place(relx=0.6, rely=0.1)
    lst_builds = tk.Listbox(event)
    lst_builds.place(relx=0.6, rely=0.2)
    x = 1
    for i in buildings:
        it = buildings[i]
        lst_builds.insert(x, it.name)
        x +=1
    

    btn_ass = tk.Button(event, text = "Build Selected Building", command = lambda: build_building_from_options(op_builds.get(op_builds.curselection()[0], last = None)))
    btn_ass.place(relx=0.1, rely=0.9)
    btn_view = tk.Button(event, text = "View", command = lambda: show_b_stats(buildings[lst_builds.get(lst_builds.curselection()[0], last = None)]))
    btn_view.place(relx=0.6, rely=0.9)

def build_building_from_options(name):
    if name == "sawmill":
        build(woodworking, name)
    if name == "goldmine":
        build(goldmine, name)
    if name == "farm":
        build(farm, name)
    if name == "house":
        build(house, name)
    if name == "craftshop":
        build(craftshop, name)
    if name == "market":
        build(foodmarket, name)
    if name =="library":
        build(library, name)
    
    build_menu()

def show_b_stats(b):
    menu = tk.Frame(root, bg="black", bd=1) #main menu frame and buttons
    menu.place(relx=0.1, rely=0.3, relwidth=0.75, relheight=0.1)
    event = tk.Frame(root, bd=1)
    event.place(relx=0.1, rely=0.45, relwidth=0.75, relheight=0.45)
    btn_back = tk.Button(menu, text="Back", command= build_menu)
    btn_back.place(relx=0.5, rely=0.3)
    workers = tk.Listbox(event)
    workers.place(relx=0.1, rely=0.2)
    g = show_job(b)
    a = 1
    for i in g:
        workers.insert(a, i.name)
        a += 1
    if b.btype == "house":
        lbl_food = tk.Label(event, text = "Foodstore: " + str(b.foodstore))
        lbl_food.place(relx=0.1, rely=0.1)
        lbl_owned = tk.Label(event, text = "Clan: " + b.clan.name)
        lbl_owned.place(relx=0.1, rely=0.03)
    elif b.btype == "craft shop":
        x = b.store
        g = []
        for i in x:
            g.append(i.name)
        lbl_crafts = tk.Label(event, text = "Crafts in Store:" + str(g))
        lbl_crafts.place(relx=0.1, rely=0.1)

def show_job(building): #returns a list of the units that work in the building
    ans = []
    for i in units:
        it = units[i]
        if it.job == building:
            ans.append(it)
    return ans
            
#Data menu- useful for Playtesting
def data_menu():
    
    menu = tk.Frame(root, bg="black", bd=1) #main menu frame and buttons
    menu.place(relx=0.1, rely=0.3, relwidth=0.75, relheight=0.1)
    event = tk.Frame(root, bd=1)
    event.place(relx=0.1, rely=0.45, relwidth=0.75, relheight=0.45)
    btn_back = tk.Button(menu, text="Back", command=main_menu)
    btn_back.place(relx=0.5, rely=0.3)
    ttxt_event = tk.Text(event, height=100, width=200)
    global datafocus
    x = list(units.values())
    if datafocus == "Strength":
        x.sort(reverse = True, key = sort_str)
        for i in x:
            ttxt_event.insert(tk.END, str(i.name + "- " + str(i.str)+ "\n"))
    elif datafocus == "Creativity":
        x.sort(reverse = True, key = sort_cre)
        for i in x:
            ttxt_event.insert(tk.END, str(i.name + "- " + str(i.cre)+ "\n"))
    elif datafocus == "Combat":
        x.sort(reverse = True, key = sort_com)
        for i in x:
            ttxt_event.insert(tk.END, str(i.name + "- "+ str(i.com)+ "\n"))
    elif datafocus == "Beliefs":
        x.sort(reverse = True, key = sort_beliefs)
        for i in x:
            ttxt_event.insert(tk.END, str(i.name + "- "+ str(sort_beliefs(i))+ " " + str(find_highest_belief(i).name) + "\n"))
    elif datafocus == "Happy":
        x.sort(reverse = True, key = sort_happy)
        for i in x:
            ttxt_event.insert(tk.END, str(i.name + "- "+ str(i.happy) + "\n"))
   
    btn_data1 = tk.Button(menu, text="Strength", command = lambda: focus_data("Strength"))
    btn_data1.place(relx=0.3, rely=0.3)
    btn_data2 = tk.Button(menu, text="Creativity", command = lambda: focus_data("Creativity"))
    btn_data2.place(relx=0.7, rely=0.3)
    btn_data3 = tk.Button(menu, text="Combat", command = lambda: focus_data("Combat"))
    btn_data3.place(relx=0.9, rely=0.3)
    btn_data4 = tk.Button(menu, text="Beliefs", command = lambda: focus_data("Beliefs"))
    btn_data4.place(relx=0.1, rely=0.5)
    btn_data5 = tk.Button(menu, text="Happiness", command = lambda: focus_data("Happy"))
    btn_data5.place(relx=0.1, rely= 0)    
    ttxt_event.configure(state='disabled')
    scroll = tk.Scrollbar(event, orient = 'vertical', command=ttxt_event.yview)
    scroll.pack(side="right", expand=True, fill='y')
    ttxt_event.configure(yscrollcommand=scroll.set)
    ttxt_event.pack(side="right")

datafocus = "Beliefs"
def focus_data(data):
    global datafocus
    datafocus = data
    data_menu()

def sort_cre(x):
    return x.cre

def sort_com(x):
    return x.com

def sort_happy(x):
    return x.happy

def sort_beliefs(x):
    ans = 0
    for i in x.beliefs:
        if i.score > ans:
            ans = i.score
    return ans
        
def find_highest_belief(x):
    ans = x.beliefs[0]
    for i in x.beliefs:
        if i.score > ans.score:
            ans = i
    return ans

#Resources and Buildings



#Buildings and their events

class building:
    def __init__(self, num): #serial number. Location will be added later. &&&&
        self.num = num

class nothing: #placeholder job
    def __init__(self):
        self.name = "Nothing"

nojob = nothing()

def price_check(building):
        global wood
        buildings[building.name] = building
        if building.cost > wood:
            x = buildings.pop(building.name)
            text("Not enough wood")
        else:
            wood -= building.cost
            text("Built " + building.name)

class woodworking(building):
    def __init__(self, num, name):
        super().__init__(num)
        self.name = name
        self.event = {"nothing" : [1, 60], "conversation" : [61, 80], "argument" : [81, 97], "accident" : [98, 100]}
        self.eventlist = ["nothing", "conversation", "argument", "accident"]
        self.production = wood
        self.stat = "Strength"
        self.prodmod = 1
        self.hoursworked = 0
        self.hourwage = 1
        self.cost = 5
        self.inside=[] #this will be a constantly-changing variable to see who is "inside
        self.btype = "sawmill"
        self.capacity = 3
        self.gcost = 0
        self.mcost = 0
        price_check(self)


    def produce(self):
            totalstr = 0
            guys = ("")
            global gold
            for i in self.inside:
                totalstr += i.str
                i.wallet += self.hourwage*self.hoursworked
                gold -= self.hourwage*self.hoursworked
                text("Paid "+ i.name+ " " + str(self.hourwage*self.hoursworked) + " gold.")
                guys += (i.name + ", ")
            global wood
            x = round(totalstr*self.prodmod*self.hoursworked/5)
            text(guys + "produced " + str(x) +" wood at " + self.name+".")
            wood += x
            self.hoursworked = 0
            totalstr = 0

class farm(building):
    def __init__(self, num, name):
        super().__init__(num)#&&
        self.name = name
        self.event = {"nothing" : [1, 60], "conversation" : [61, 80], "argument" : [81, 97], "accident" : [98, 100]}
        self.eventlist = ["nothing", "conversation", "argument", "accident"]
        self.production = food
        self.stat = "Strength"
        self.prodmod = 1
        self.hoursworked = 0
        self.hourwage = 1
        self.cost = 5
        self.inside=[] #this will be a constantly-changing variable to see who is "inside
        self.btype = "farm"
        self.capacity = 3
        self.gcost = 0
        self.mcost = 0
        price_check(self)

    def produce(self):
        totalstr = 0
        guys = ("")
        global gold
        for i in self.inside:
            totalstr += i.str
            i.wallet += self.hourwage*self.hoursworked
            gold -= self.hourwage*self.hoursworked
            text("Paid "+ i.name+ " " + str(self.hourwage*self.hoursworked) + " gold.")
            guys += (i.name + ", ")
        global food
        x = round(totalstr*self.prodmod*self.hoursworked/2.5)
        text(guys + "produced " + str(x) +" food at " + self.name+".")
        food += x
        self.hoursworked = 0
        

class goldmine(building):
    def __init__(self, num, name):
        super().__init__(num)#&&
        self.name = name
        self.event = {"nothing" : [1, 60], "conversation" : [61, 80], "argument" : [81, 97], "accident" : [98, 100]}
        self.eventlist = ["nothing", "conversation", "argument", "accident"]
        self.production = gold
        self.stat = "Strength"
        self.prodmod = 1
        self.hoursworked = 0
        self.hourwage = 1
        self.cost = 5
        self.inside=[] 
        self.btype = "gold mine"
        self.capacity = 3
        self.gcost = 0
        self.mcost = 0
        price_check(self)

    def produce(self):
        totalstr = 0
        guys = ("")
        global gold
        for i in self.inside:
            totalstr += i.str
            i.wallet += self.hourwage*self.hoursworked
            gold -= self.hourwage*self.hoursworked
            text("Paid "+ i.name+ " " + str(self.hourwage*self.hoursworked) + " gold.")
            guys += (i.name + ", ")
        x = round(totalstr*self.prodmod*self.hoursworked/2.5)
        text(guys + "produced " + str(x) +" gold at " + self.name+".")
        gold += x
        self.hoursworked = 0
        totalstr = 0


workevents = {"nothing" : [1, 60], "conversation" : [61, 80], "argument" : [81, 100]}
workeventslist = ["nothing", "conversation", "argument"]

class craftshop(building):
    def __init__(self, num, name):
        super().__init__(num)#&&
        self.name = name
        self.event = workevents
        self.eventlist = workeventslist
        self.production = "crafts"
        self.stat = "Creativity"
        self.prodmod = 1
        self.hoursworked = 0
        self.hourwage = 2
        self.cost = 15
        self.inside=[] 
        self.btype = "craft shop"
        self.progress = 0
        self.store = []
        self.capacity = 3
        self.gcost = 0
        self.mcost = 0
        price_check(self)


    def produce(self): #produce craft
        totalcre = 0
        guys = ("")
        totalint = 0
        global gold
        for i in self.inside:
            totalint += i.int #intelligence makes more things
            i.wallet += round(self.hourwage*self.hoursworked)
            gold -= round(self.hourwage*self.hoursworked)
            text("Paid "+ i.name+ " " + (str(round(self.hourwage*self.hoursworked))) + " gold.")
            guys += (i.name + " ")
        self.progress += self.prodmod*self.hoursworked*totalint/10
        text(guys + "worked on crafts")
        while self.progress >= 5:
            creator = random.choice(self.inside)
            craft = generate_craft(creator)
            self.progress -= 5
            text(creator.name + " produced a " + craft.name + " with help from others.")
            self.store.append(craft)
        self.hoursworked = 0
        totalcre = 0
        totalint = 0

    def sell(self): #sell craft to people in store
        global gold
        text("Items in store: ")
        for x in self.store:
            text(x.ctype + ", quality: " + str(x.quality) + ", price:" + str(x.quality*2))
        for i in self.inside: #each buyer in the store
            guy = i
            for item in self.store: #looks at each item in the store
                if item.culture == guy.culture and item.quality*2 <= guy.wallet: #if item quality (price) is less than their wallet
                    text(guy.name + " purchased a " + item.name + " for " + str(2*item.quality) + " gold.")
                    guy.items.append(item) #guy takes item
                    gold += item.quality*2 #pays
                    guy.wallet -= item.quality*2
                    guy.happy += item.quality*5 #is happy
                    guy.prestige += 1 #is more fashionable
                    self.store.remove(item) #takes from the store
                    modify_belief(guy, capitalism, reason("Bought a fancy new item", item.quality*2, 20)) #wants to be a capitalist


class house(building):
    def __init__(self, num, name):
        super().__init__(num)
        self.name = name
        self.btype = "house"
        self.eventlist = ["nothing", "conversation", "elder tells stories"]
        self.event = {"nothing": [1, 50], "conversation" : [51, 80], "elder tells stories" : [81, 100]}
        self.cost = 10
        self.clan = "None"
        self.foodstore = 0
        self.unitlist= [] #a list of the serial numbers of its residents
        self.inside=[]
        self.hoursworked = 0
        self.capacity = 15
        self.gcost = 0
        self.mcost = 0
        price_check(self)

    def meal(self):
        if self.clan != "None" and self.foodstore >= self.clan.size and self.inside != []:
            for i in self.inside:
                i.hunger -= 20
            self.foodstore -= self.clan.size
            text("Clan " + self.clan.name + " ate a meal.")
        elif self.foodstore < len(self.inside) and self.inside != []: 
            text("Clan " + self.clan.name + " went hungry.")
            for i in self.inside:
                i.hunger += 10

                
    def sleep(self):
        if self.inside != []:
            for i in self.inside:
                if i.hunger == 0:
                    if i.hp < i.hpcap:
                        i.hp += 1
                        text(i.name + " healed 1 hp through rest.")
                if i.hunger < 0:
                    i.hunger = 0
                i.sleep = 1
       

class foodmarket(building):
    def __init__(self, num, name):
        super().__init__(num)
        self.name = name
        self.btype = "food market"
        self.eventlist = ["nothing","conversation"]
        self.event = {"nothing": [1,50], "conversation" : [51, 100]}
        self.cost = 10
        self.clan = "None"
        self.foodstore = 0
        self.inside=[]
        self.hoursworked = 0
        self.price = 1
        self.capacity = 3
        self.gcost = 0
        self.mcost = 0
        price_check(self)
        
    def set_price(self):
        global food
        demand = 0
        for i in self.inside:
            demand += i.clan.size
        supply = food
        if food == 0:
            supply = 1
        self.price = round(15*demand/(supply))#Important equation - not exactly supply and demand but close enough
        if self.price == 0:
            self.price = 1
        text("Food Prices: "+ str(self.price))
        space()


    def sell(self):
        global food
        global gold
        done = 0
        insidenum = 0
        for i in self.inside:
            insidenum += 1
 
        while done < insidenum:
            for i in self.inside:
                if i.wallet >= self.price and food > 0:
                    gold += self.price
                    i.wallet -= self.price
                    x = find_clans_house(i.clan)
                    i.items.append("food")
                    x.foodstore += 1
                    food -= 1
                else:
                    bought = 0
                    for thing in i.items:
                        if thing == "food":
                            bought += 1
                            i.items.remove(thing)
                    text(i.name + " bought " + str(bought) + " food for their clan")
                    rolled = roll(0, bought)
                    if rolled > 5:
                        modify_belief(i, capitalism, reason("realized the importance of buying food", bought, 7)) #capitalism
                        text("Though about Capitalism")
                    self.inside.remove(i)
                    done +=1
            

class library(building):
    def __init__(self, num, name):
        super().__init__(num)
        self.name = name
        self.btype = "library"
        self.eventlist = ["nothing", "learn"]
        self.event = {"nothing": [1,98], "learn": [99,100]}
        self.cost = 20
        self.gcost = 0
        self.mcost = 0
        self.inside=[]
        self.hoursworked = 0
        self.hourwage = 2
        self.capacity = 1 #amount of workers
        price_check(self)
        
    def produce(self):
        totalint = 0
        guys = ("")
        global techpt
        for i in self.inside:
            totalint += i.int
            i.wallet += self.hourwage*self.hoursworked
            gold -= self.hourwage*self.hoursworked
            text("Paid "+ i.name+ " " + str(self.hourwage*self.hoursworked) + " gold.")
            guys += (i.name + " ")
        x = totalint*self.prodmod*self.hoursworked/10
        rolled = roll(1, 3)
        if rolled < 3:
            text(guys + "produced " + str(round(x)) +" tech at " + self.name+".")
            techpt += round(x)
        else:
            text(guys + "worked on literature at " + self.name+".")
            for i in self.inside:
                i.project += x
                if i.project >= 10:
                    e_produce_literature(i)
                
            
        self.hoursworked = 0

palace_exists = False #checks to see if palace exists

    #advanced tech level 2 and 3 buildings
        
class palace(building):
    def __init__(self, num, name):
        super().__init__(num)
        self.name = name
        self.btype = "palace"
        self.eventlist = ["nothing", "good impression"]
        self.event = {"nothing": [1,95], "good impression": [96,100]}
        self.cost = 35
        self.m = "crystal"
        self.mcost = 10
        self.gcost = 200
        self.inside=[]
        self.hoursworked = 0
        self.hourwage = 5
        self.capacity = 20
        price_check(self)
        global palaceexists
        palace_exists = True
        
class fancy_house(building):
    def __init__(self, num, name):
        super().__init__(num)
        self.name = name
        self.btype = "fancy house"
        self.eventlist = ["nothing", "conversation", "elder tells stories"]
        self.event = {"nothing": [1, 50], "conversation" : [51, 80], "elder tells stories" : [81, 100]}
        self.cost = 10
        self.clan = "None"
        self.foodstore = 0
        self.unitlist= [] #a list of the serial numbers of its residents
        self.inside=[]
        self.hoursworked = 0
        self.capacity = 15
        self.gcost = 0
        self.mcost = 0
        price_check(self)
        

    def meal(self):
        if self.clan != "None" and self.foodstore >= self.clan.size and self.inside != []:
            for i in self.inside:
                i.hunger -= 20
            self.foodstore -= self.clan.size
            text("Clan " + self.clan.name + " ate a meal.")
        elif self.foodstore < len(self.inside) and self.inside != []: 
            text("Clan " + self.clan.name + " went hungry.")
            for i in self.inside:
                i.hunger += 10

                
    def sleep(self):
        if self.inside != []:
            for i in self.inside:
                if i.hunger == 0:
                    if i.hp < i.hpcap:
                        i.hp += 1
                        text(i.name + " healed 1 hp through rest.")
                if i.hunger < 0:
                    i.hunger = 0
                i.sleep = 1

hardworkevents = {"nothing" : [1, 60], "conversation" : [61, 80], "argument" : [81, 97], "accident" : [98, 100]}
hardworkeventslist = ["nothing", "conversation", "argument", "accident"]

class metal_mine(building):
    def __init__(self, num, name):
        super().__init__(num)
        self.name = name
        self.btype = "metal mine"
        self.event = {"nothing" : [1, 60], "conversation" : [61, 80], "argument" : [81, 97], "accident" : [98, 100]}
        self.eventlist = ["nothing", "conversation", "argument", "accident"]
        self.cost = 10
        self.gcost = 100 #gold cost- remember to add this in
        self.inside=[]
        self.hoursworked = 0
        self.hourwage = 1
        self.capacity = 3
        price_check(self)

    def produce(self):
        totalstr = 0
        guys = ("")
        global gold
        for i in self.inside:
            totalstr += i.str
            i.wallet += self.hourwage*self.hoursworked
            gold -= self.hourwage*self.hoursworked
            text("Paid "+ i.name+ " " + str(self.hourwage*self.hoursworked) + " gold.")
            guys += (i.name + ", ")
        global ore
        global metal
        x = round(totalstr*self.prodmod*self.hoursworked/2.5)

        text(guys + "produced " + str(x) +" ore at " + self.name+".")
        ore += x
        self.hoursworked = 0


class metal_processor(building):
    def __init__(self, num, name):
        super().__init__(num)
        self.name = name
        self.btype = "metal processor"
        self.event = {"nothing" : [1, 63], "conversation" : [64, 83], "argument" : [84, 100]}
        self.eventlist = ["nothing", "conversation", "argument", "accident"]
        self.cost = 10
        self.gcost = 100 
        self.inside=[]
        self.hoursworked = 0
        self.hourwage = 1
        self.capacity = 3
        price_check(self)

    def produce(self):
        totalstr = 0
        guys = ("")
        global gold
        for i in self.inside:
            totalstr += i.str
            i.wallet += self.hourwage*self.hoursworked
            gold -= self.hourwage*self.hoursworked
            text("Paid "+ i.name+ " " + str(self.hourwage*self.hoursworked) + " gold.")
            guys += (i.name + ", ")
        global ore
        global metal
        y = round(totalstr*self.prodmod*self.hoursworked/2.5)
        x = 0
        if y < ore:
            x = y
        else:
            x = ore
        text(guys + "produced " + str(x) +" metal at " + self.name+".")
        metal += x
        ore -= x
        self.hoursworked = 0
        


        
class smith(building):
    def __init__(self, num, name):
        super().__init__(num)#&&
        self.name = name
        self.event = {"nothing" : [1, 60], "conversation" : [61, 80], "argument" : [81, 100]}
        self.eventlist = ["nothing", "conversation", "argument"]
        self.prodmod = 1
        self.hoursworked = 0
        self.hourwage = 2
        self.cost = 20
        self.inside=[] 
        self.btype = "smith"
        self.progress = 0
        self.store = []
        self.capacity = 3
        self.gcost = 0
        self.mcost = 10
        self.m = "metal"
        price_check(self)


    def produce(self): #produce weapons
        totalcre = 0
        totalstr = 0
        guys = ("")
        global gold
        for i in self.inside:
            totalstr += i.str #str makes more things
            i.wallet += round(self.hourwage*self.hoursworked)
            gold -= round(self.hourwage*self.hoursworked)
            text("Paid "+ i.name+ " " + (str(round(self.hourwage*self.hoursworked))) + " gold.")
            guys += (i.name + " ")
        self.progress += self.prodmod*self.hoursworked*totalint/10
        text(guys + "worked on weapons")
        while self.progress >= 10:
            creator = random.choice(self.inside)
            weapon = generate_weapon(creator) #&& need to make a generate weapon 
            self.progress -= 10
            text(creator.name + " produced a " + weapon.name + " with help from others.")
            self.store.append(craft)
        self.hoursworked = 0
        totalcre = 0
        totalstr = 0

    def sell(self): #sell weapons to people in store
        global gold
        text("Items in store: ")
        text("")
        for x in self.store:
            text(x.ctype + ", quality: " + str(x.quality) + ", price: " + str(x.quality*2))
        for i in self.inside: #each buyer in the store
            guy = i
            for item in self.store: #looks at each item in the store
                if item.culture == guy.culture and item.quality*2 <= guy.wallet: #if item quality (price) is less than their wallet
                    text(guy.name + " purchased a " + item.name + " for " + str(2*item.quality) + " gold.")
                    guy.items.append(item) #guy takes item
                    gold += item.quality*2 #pays
                    guy.wallet -= item.quality*2
                    guy.happy += item.quality*5 #is happy
                    guy.prestige += 1 #is more fashionable
                    self.store.remove(item) #takes from the store
                    modify_belief(guy, capitalism, reason("Bought a fancy new weapon", item.quality*2, 20)) #wants to be a capitalist


class tavern(building): #serves liquor for happiness, uses creativity
    def __init__(self, num, name):
        super().__init__(num)#&&
        self.name = name
        self.event = workevents
        self.eventlist = workeventslist
        self.tevent = {"drink" : [1, 45], "conversation" : [46, 65], "argument" : [66, 70], "song" : [71, 100]}
        self.teventlist = ["drink", "conversation", "argument", "song"]
        self.prodmod = 1
        self.hoursworked = 0
        self.hourwage = 2
        self.cost = 20
        self.inside=[] #workers inside during the work day, visitors inside during the evening
        self.btype = "tavern"
        self.progress = 0
        self.capacity = 30
        self.gcost = 100
        self.foodtake = 20
        self.foodstore = 0
        self.drinkstore = 0
        self.culture = "None" #figure out a way to set culture for this one
        price_check(self)

    def produce(self): #produce beer
        totalcre = 0
        guys = ("")
        global gold
        for i in self.inside:
            totalcre += i.cre #str makes more things
            i.wallet += round(self.hourwage*self.hoursworked)
            gold -= round(self.hourwage*self.hoursworked)
            text("Paid "+ i.name+ " " + (str(round(self.hourwage*self.hoursworked))) + " gold.")
            guys += (i.name + " ")
        self.progress += self.prodmod*self.hoursworked*totalcre/10
        amount = 0
        while self.progress >= 2 and self.foodstore != 0: #2 progress and 4 food make a drink
            self.foodstore -= 4
            self.progress -= 2
            self.drinkstore += 1
            amount += 1
        text(guys + "distilled " + amount + "liquor")
        self.hoursworked = 0
        totalcre = 0

    def foodtake(self): #take food
        global food
        if self.foodstore < self.foodtake:
            if food > self.foodtake:
                self.foodstore += self.foodtake
                food -= self.foodtake
                text("Took " + self.foodtake + " food for " + self.name)
            else:
                text("Took " + food + " food for " + self.name)
                self.foodstore += food
                food = 0
               

    #instead of sell, they will buy as an event, e_drink

class construction_center(building):
    def __init__(self, num, name):
        super().__init__(num)#&&
        self.name = name
        self.event = hardworkevents
        self.eventlist = hardworkeventslist
        self.prodmod = 1
        self.hoursworked = 0
        self.hourwage = 1
        self.cost = 20
        self.inside=[] 
        self.btype = "construction center"
        self.progress = 0
        self.capacity = 3
        self.gcost = 100
        self.construction_store = 0
        price_check(self)

    def produce(self):
        totalstr = 0
        guys = ("")
        global gold
        for i in self.inside:
            totalstr += i.str
            i.wallet += self.hourwage*self.hoursworked
            gold -= self.hourwage*self.hoursworked
            text("Paid "+ i.name+ " " + str(self.hourwage*self.hoursworked) + " gold.")
            guys += (i.name + ", ")
        global jarble
        y = round(totalstr*self.prodmod*self.hoursworked/2.5)
        x = 0
        if y < jarble:
            x = y
        else:
            x = jarble
        text(guys + "produced " + str(x) +" construction matierials at " + self.name+".")
        self.construction_store += x
        jarble -= x
        self.hoursworked = 0

class school(building):
    def __init__(self, num, name):
        super().__init__(num)#&&
        self.name = name
        self.event = workevents #add an event for intelligence growing
        self.eventlist = workeventslist
        self.prodmod = 1
        self.hoursworked = 0
        self.hourwage = 3
        self.cost = 20
        self.inside=[]
        self.btype = "school"
        self.progress = 0
        self.capacity = 11
        self.gcost = 100
        self.belieffocus = loyalty #loyalty by default
        price_check(self)

    def teach(self):
        teacher = None
        for i in list(units.values()):
            if i.job == self:
                teacher = i
        if teacher != None:
            want = take_action(teacher)
            will = teacher.happy
            chance = roll(0, 30)
            persuasiveness = (teacher.cha*roll(1, 5)) #longer lasting if charisma is high
            impact = (teacher.int*self.hoursworked) #bigger number if hoursworked and intelligence is high
            if (chance + will) > 30: #a teacher with happiness 100 will certainly teach well, while a teacher with happiness 20 will go off and teach whatever they want
                for student in self.inside:
                    if student != teacher:
                        modify_belief(student, self.belieffocus, reason(("Taught in school by " + teacher.name)), impact, persuasiveness)
            else:
                for student in self.inside:
                    if student != teacher:
                        modify_belief(student, want, reason(("Taught in school by " + teacher.name)), impact, persuasiveness)
        global gold
        teacher.wallet += self.hourwage*self.hoursworked
        gold -= self.hourwage*self.hoursworked
        text("Paid "+ teacher.name+ " " + str(self.hourwage*self.hoursworked) + " gold.")
        hoursworked = 0

class ampitheter(building):
    def __init__(self, num, name):
        super().__init__(num)#&&
        self.name = name
        self.event = workevents
        self.eventlist = workeventslist
        self.prodmod = 1
        self.hoursworked = 0
        self.hourwage = 15
        self.cost = 50
        self.inside=[]
        self.actors = []
        self.btype = "ampitheter"
        self.progress = 0
        self.capacity = 25
        self.gcost = 300
        self.production = None #play that they are playing
        price_check(self)

    def practice(self):
        playlist = []
        for i in literatures:
            if i.form == "play":
                playlist.append(i)
        if self.production == None: #choosing a play to put on
            self.production = random.choice(playlist)
        for i in list(units.values()): #define actors
            if i in self.inside and i not in self.actors:
                self.actors.append(i)
        global gold
        guys = ("")
        guys += (i.name + ", ")
        for i in actors:
            progress += i.cha*self.hoursworked #progress is the amount of charisma for each actor, times hours worked
            i.wallet += self.hourwage*self.hoursworked
            gold -= self.hourwage*self.hoursworked
            text("Paid "+ i.name+ " " + str(self.hourwage*self.hoursworked) + " gold.")
        text(guys + " practiced for a production of " + self.production.name + " at " + self.name)
        self.hoursworked = 0
            
        

    def perform(self):
        for i in self.inside:
            if i not in self.actors:
                modify_belief(i, self.production.subject, reason("Saw a play", round(self.progress * self.production.quality / 10), 21))
        
        self.production = None
                

### I still need to do barracks, armory, and storage buildings

def generate_building(btype, name):
    global total_building_counter
    number = (total_building_counter + 1)
    total_building_counter += 1
    x = btype(number, name)
    return x

def generate_craft(creator):
    x = craft(creator)
    return x

def place(unit, building): #affects "inside" variable of building; takes unit object and building object as inputs and adds unit object to "inside" list.
    building.inside.append(unit)#changed this from unit.num. Make sure that "inside" lists are altered
    text(unit.name + " went to " + building.name+".")
    unit.location = find_location(unit)
     
def clear(building):
    for unit in building.inside:
        text(unit.name + " went to the town square")
        unit.location = "None"
    building.inside = []
    

def build(btype, model):
    y = generate_b_name(model)
    generate_building(btype, y)
    build_menu()

def generate_b_name(b):
    x = len(list(buildings.keys()))
    y = (b + " " + str(x))
    return y

#Crafts


crafts = []

class craft:

    def __init__(self, creator): #takes unit object
        self.creator = creator
        self.culture = creator.culture
        self.quality = (roll(1, 3))*self.creator.cre
        self.ctype = random.choice(self.culture.craftnames)
        self.name = str("Quality "+ str(self.quality) +" " + self.ctype + ", made by "+ self.creator.name )


#Some finding objects functions

        
    
def find_unit(name): #if the input matches the name of the unit, it returns the unit. Otherwise, it returns "None"
    ans = "None"
    for i in units:
        it = units[i]
        if name == it.name:
            ans = it
    return ans

def find_b_num(num): #if the input matches the number of the building, it returns the building. Otherwise, it returns "None"
    ans = "None"
    for i in buildings.keys():
        it = buildings[i]
        if num == it.num:
            ans = it
    return ans

def find_u_num(num): #if the input matches the number of the unit, it returns the unit. Otherwise, it returns "None"
    ans = "None"
    for i in units:
        it = units[i]
        if it.number == num:
            ans =  it
    return ans

def find_clans_house(clan): #takes a clan object, returns the last house object that belongs to the clan
    ans = 0
    for i in buildings.keys():
        it = buildings[i]
        if it.btype == "house" and clan == it.clan:
            ans = it
    return ans

def send_to_work(b): #input is building object, puts all people who have that as their job inside
    for i in units:
        it = units[i]
     
        if it.job == b:
            g = take_action(it)
            if g == rebellion:
                itext(it.name + " is striking!")
            else:
                place(it, b)

def send_to_home(b):
    it = b.clan
    for i in units:
        guy = units[i]
        if guy.clan == it:
            place(guy, b)

#Workday
    """
    this will be a substitute for the real-time activity of the final game.
    On the menu, you can click enter to move from one hour to the next.
    At every hour, the game will check for, and then trigger, appropriate events.
    The workday will be: sleep (hours 0-9), work (9-13), eat (13-14), work (14-17), free (17-20), eat(20-21), home (21-24)
    """



def pass_time():
    global hour
    global date
    global gold
    global gamestate
    global food
    if gold < 1:
        text("You're out of gold! GAME OVER")
        gamestate = False
    else:
        hour += 1
        if hour == 24:
            hour = 0
            date +=1
            for u in list(units.values()): #deletes expired reasons
                for b in u.beliefs:
                    for r in b.reasons:
                        if r.expiration == date:
                            b.reasons.remove(r)
        event_checker(hour)
        if date%3 == 0 and hour == 0:
            food = 0
            text("The food spoiled!")
        if date%7 == 0 and hour == 0:
            generate_clan(random_culture(), immigration_size)
            text("A new clan has arrived!")
        for i in units:
            if units[i].hp <= 0:
                die(i)#&&& make a dedicated function for this!
            if units[i].happy < 1:
                modify_belief(units[i], rebellion, reason("Unhappy with the way things are", 15, 7))
                units[i].happy = 50
            if units[i].happy > 99:
                modify_belief(units[i], loyalty, reason("Happy with the way things are", 15, 7))
                units[i].happy = 50
        main_menu()

    #assigning units to jobs

def hire(unit, building):
    guy = unit
    workers = 0
    for i in units:
        it = units[i]
        if it.job == building:
            workers += 1
    if workers < building.capacity:
        guy.job = building
        text("Hired " + unit.name + " to " + building.name)
        if building.btype == "library":
            unit.status.append("researcher")
            unit.prestige += 5
    else:
        text("Too many workers in the buildng, build another")

def assign_house(clan, building):
    if building.btype == "house":
        building.clan = clan
    if building.btype == "fancy house":
        building.clan = clan
        for i in list(units.values()):
            if i.clan ==clan:
                i.prestige += 5 #adds 5 prestige to units living in the house
    text("Assigned house")

    #Master event runner

def event_checker(hour):
    time = "none"
    if hour == 9 or hour == 10 or hour == 11 or hour == 12 or hour == 14 or hour == 15 or hour == 16:
        
        for i in list(buildings.keys()):
            b = buildings[i]
            if hour == 9 or hour == 14:
                send_to_work(b)
                
            if b.btype == "sawmill" or buildings[i].btype == "gold mine" or buildings[i].btype == "farm" or buildings[i].btype == "craft shop":
                if b.inside != []:
                    buildings[i].hoursworked += 1
                    event_decider(b)
               
            if hour == 12 or hour == 16:
                if b.btype == "sawmill" or buildings[i].btype == "gold mine" or buildings[i].btype == "farm" or buildings[i].btype == "craft shop":
                    if b.inside != []:

                        b.produce()
                        clear(b)
        
    elif hour == 13 or hour == 20:
        if hour == 13 or hour == 20:
            for i in list(buildings.keys()):
                if buildings[i].btype == "house":
                    send_to_home(buildings[i])
                    buildings[i].meal()
                    event_decider(buildings[i])
                    
                    
    elif hour == 17 or hour == 18 or hour == 19:
        time = "free"
        if hour == 17:
            for m in units: 
                free_time_ai(units[m])
                #units look for things to do on hour 17
        if hour == 19: #markets work on hour 19
            for i in buildings.keys():
                it = buildings[i]
                if it.btype == "food market":
                    it.set_price()
                    event_decider(buildings[i])
                    it.sell()
                    
                elif it.btype == "craft shop": 
                    event_decider(buildings[i])
                    it.sell()
                    
    elif hour == 21 or hour == 22 or hour == 23:
        for i in list(buildings.keys()):
            if buildings[i].btype == "house":
               event_decider(buildings[i])
    elif hour == 8:
        time = "sleepdone"
        sleep_event()
        for i in list(buildings.keys()):
            clear(buildings[i])


def building_event(building):
    x = building.eventlist
    y = roll(1, 100)
    ans = None
    for i in x:
        a = building.event[i][0]
        b = building.event[i][1]
        if a <= y <= b:
            ans = i
    return ans

def choose_two(L):
    ans = random.sample(L, 2)
    return ans

def event_decider(building): #this randomly chooses people inside, and triggers the event
    if building.inside != []:
        event= building_event(building)

        if event == "conversation":
       
            h = building.inside 
            j = []
            print(building.name)
            print("Amoung of people inside: " + str(len(building.inside)))
            if len(h) > 1: #this should choose two people from the list of units inside the building, and make them have a conversation
                r = choose_two(building.inside)
                print(str(r))
                e_conversation(r[0], r[1])
                print(str(building.inside))
                print("Amoung of people inside: " + str(len(building.inside)))
        elif event== "argument":

            print(building.name)
            h = building.inside
            j = []
            if len(h) > 1: #this should choose two people from the list of units inside the building, and make them have a conversation
   
                r = choose_two(building.inside)
                e_argument(r[0], r[1]) #I think this is taking units out of the inside thing- I need to rethink this "choose two" function
            
        elif event == "accident":
            q = random.choice(building.inside)
            e_accident(q)
        elif event == "elder tells stories":
            e_elder_tells_stories(random.choice(building.inside))
#AI


#Decision-maker for free time! This is important to continously update in this build

def free_time_ai(u): #takes a unit object as input, figures out where they want to go, and then places them there
    if find_clans_house(u.clan).foodstore < u.clan.size*2 and "Elder" not in u.status  and u.wallet != 0: #gives money to the elder to purchase food if foodstores are low
        u.clan.elder.wallet += u.wallet
        text(u.name + " gave their elder " + str(u.wallet) + " gold to buy food.")
        u.wallet = 0
    elif find_clans_house(u.clan).foodstore < u.clan.size*2 and "Elder" in u.status: #places elder in market if foodstores are low
        
        for i in buildings.keys():
            it = buildings[i]
            if it.btype == "food market":
                place(u, it)
    elif u.wallet > 10:
        text("buying test")
        for i in buildings.keys():
            it = buildings[i]
            if it.btype == "craft shop":
                place(u, it)
    else: #decision-based beliefs. I need to figure out a way to edit these
        x = take_action(u)
        
        z = list(x.events.keys())
        y = roll(1, 100)
        ans = None
        for i in z:
            a = x.events[i][0]
            b = x.events[i][1]
            if a <= y <= b:
                ans = i

        if ans == "nothing":
            pass

        elif ans == "insult knani":
            guy = find_random_culture_unit(u, knani)
            if guy != None:
                text(u.name + " insulted knanis")
                e_argument(u, guy)

        elif ans == "attack knani":
            guy = find_random_culture_unit(u, knani)
            if guy != None:
                text(u.name + " looked to fight a knani")
                #guard_check(u)
                e_brawl(u, guy)

        elif ans == "insult huxley":
            guy = find_random_culture_unit(u, huxley)
            if guy != None:
                text(u.name + " insulted huxleys")
                e_argument(u, guy)

        elif ans == "attack huxley":
            guy = find_random_culture_unit(u, huxley)
            if guy != None:
                text(u.name + " looked to fight a huxley")
                #guard_check(u)
                e_brawl(u, guy)
            

        elif ans == "insult uul":
            guy = find_random_culture_unit(u, uul)
            if guy != None:
                text(u.name + " insulted uuls")
                e_argument(u, guy)

        elif ans == "attack uul":
            guy = find_random_culture_unit(u, uul)
            if guy != None:
                text(u.name + " looked to fight an uul")
                #guard_check(u)
                e_brawl(u, guy)

            

        elif ans == "pray":
            text(u.name + " prayed according to the old ways")

        elif ans == "grumble":
            text(u.name + " grumbled about the government")

        elif ans == "insult": #doesn't check for location yet &&&&
            x = None
            while x == None or x == u:
                x = random.choice(list(units.values()))
            text(u.name + " yelled at random people")
            e_argument(u, x)

        elif ans == "convince": #find a random person and try to convince them, doesn't check for location yet &&&&
            f = None
            while f == None or f == u:
                f = random.choice(list(units.values()))
            e_convince(u, f, x)

        else:
            text("no event for " + ans)
        



def find_random_culture_unit(u, c):
    x = []
    for i in units:
        if units[i].culture == c and units[i].location == u.location:
            x.append(units[i])
    if x != []:
        g = random.choice(x)
        if g != []:
            return g

def take_action(u): #Function for deciding on a belieftype, based on score as percentage
    if u.beliefs != []:
        x = u.beliefs #test to make sure this works properly !!! &&&&&
        outof = 0
        possibilities = {}
        for i in x:
            outof += i.score
            possibilities.update({outof : i.belieftype})
        y = roll(1, outof)

        z = list(possibilities.keys())
        ans = possibilities[z[0]]
        g = 0
        for i in z:
            if y > i:
                g += 1
                ans = possibilities[z[g]]
                

        return ans
            
def out_of(thing):
    #takes a dictionary with a thing as key, and an integer as a value. It makes a pie chart of each key according to its value, and chooses one answer based on the pi chart percentage
    outof = 0
    p = {}
    if thing != {}:
        for i in list(thing.keys()):
            outof += thing[i]
            p.update({outof : i})
    y = roll(1, outof)
  
    ans = list(p.values())[0] #answer is the first value of p
    g  = 0

    for i in list(p.keys()):
        if y > i:
            g += 1
            ans = list(p.values())[g]
    return ans
        

    
#Events

def sleep_event():
    for i in list(buildings.keys()): #activating sleep event for all units inside buildings
        if buildings[i].btype == "house":
            buildings[i].sleep() #sleep effects happen, sleeping people's sleep becomes 1
    for i in list(units.keys()): #Making units without sleep unhappy
        if units[i].sleep == 0:
            text(units[i].name + " did not get any sleep, causing distress.")
            units[i].happy -= 50 #no sleep = -30 to happiness, right this down somewhere
        else:
            text(units[i].name + " got some sleep")
        units[i].sleep = 0 #everyone's sleep level goes back to 0
        if units[i].hunger > 50: #hungry people lose hp
                units[i].hp -= 1
                units[i].happy -= 15
                text(units[i].name + " took 1 damage from being hungry.")
                if units[i].hp < 1:
                    text(units[i].name + " died of hunger!")
                    units[i].clan.size -= 1
                    units.remove(i)
        elif units[i].hunger < 0:
            units[i].hunger = 0


def e_convince (unit, target, belieftype):
    text(unit.name + " tried to convince " + target.name + " of " + belieftype.name)
    modify_belief(target, belieftype, reason(str("lecture from " + unit.name), unit.cha * (unit.prestige + 1), (unit.prestige+1)*3)) #prestige effects time and amount

def e_argument(a, b): #takes two units as inputs
    a.happy -= 10
    b.happy -= 10
    text(a.name + " and " + b.name + " had an argument.")
    if a.culture != b.culture:
        if a.culture == huxley:
            modify_belief(b, prej_huxley, reason(("Had an argument with " + a.name), 5, 3))
        if b.culture == huxley:
            modify_belief(a, prej_huxley, reason(("Had an argument with " + b.name), 5, 3))
        if a.culture == uul:
            modify_belief(b, prej_uul, reason(("Had an argument with " + a.name), 5, 3))
        if b.culture == uul:
            modify_belief(a, prej_uul, reason(("Had an argument with " + b.name), 5, 3))
        if a.culture == knani:
            modify_belief(b, prej_knani, reason(("Had an argument with " + a.name), 5, 3))
        if b.culture == knani:
            modify_belief(a, prej_knani, reason(("Had an argument with " + b.name), 5, 3))
            

def e_conversation(a, b): #test this to see if it works
    x = roll(0, 1)
    talker = None
    listner = None
    if x == 0:
        talker = a
        listner = b
    else:
        talker = b
        listner = a

    prop1 = take_action(talker)
    prop2 = take_action(listner)
    modify_belief(listner, prop1, reason(("Discussion with "+ talker.name), talker.cha*3, 7)) #still don't know what to do in cases of discussing racism
    
    modify_belief(talker, prop1, reason(("Discussion with " + listner.name), listner.cha*2, 7))
    if prop1 == prop2:
        text(a.name + " and " + b.name + " agreed on " + prop2.name+".")
    else:
        text(a.name + " and " + b.name + " had a nice discussion about " + prop1.name + " and " + prop2.name+".")
    if (a.wallet > (b.wallet + 10)) and (a.culture != b.culture):
        if a.culture.name == "Knani":
            modify_belief(b, prej_knani, reason(("Income inequality"), a.prestige*2, 15))
        elif a.culture.name == "Uul":
            modify_belief(b, prej_uul, reason(("Income inequality"), a.prestige*2, 15))
        elif a.culture.name == "Huxley":
            modify_belief(b, prej_huxley, reason(("Income inequality"), a.prestige*2, 15))
    if (b.wallet > (a.wallet + 10)) and (a.culture != b.culture):
        if b.culture.name == "Knani":
            modify_belief(a, prej_knani, reason(("Income inequality"), b.prestige*2, 15))
        elif b.culture.name == "Uul":
            modify_belief(a, prej_uul, reason(("Income inequality"), b.prestige*2, 15))
        elif b.culture.name == "Huxley":
            modify_belief(a, prej_huxley, reason(("Income inequality"), b.prestige*2, 15))

    a.happy += 5
    b.happy += 5



        

def e_accident(u):
    text(u.name + " had a bad accident at work!")
    x = roll(2, 3)
    u.hp -= x
    text(u.name + " took " + str(x) + " damage.")
    u.happy -= 50
    if u.hp < 1:
        text(u.name + " died!")
        u.clan.size -= 1
        del units[u.number]

def e_elder_tells_stories(u):
    x = u.clan.elder
    propoganda = take_action(x) #should return a belieftype
    modify_belief(u, propoganda, reason("Convinced by elder", x.cha*5, x.cha*5))
    text(u.name + "'s elder, " + x.name + ", told them about " + propoganda.name)

#literature


class literature:
    def __init__(self, author):
        self.subject = take_action(author)
        self.form = random.choice(forms)
        self.name = str("a " + form + " about " + self.subject.name + " by " + author.name)
        self.quality = 0
        if form == "book": #quality is intelligence, length should be very long
            self.quality = author.int*6 
        elif form == "play": #quality is creativity and charisma, length should be medium
            self.quality = author.cre*3 + author.cha*3
        elif form == "poem": #quality is intelligence and creativity, length should be medium
            self.quality = author.int*3 + author.cre*3
        elif form == "song": #quality is creativity, length should be short
            self.quality = author.cre*6
            
            

forms= ["book", "play", "poem", "song"]
literatures = []

def e_produce_literature(u): 
    x = literature(u)
    literatures.append(x)
    itext(u.name + " has finished: " + x.name)
    u.status.append("author")
    u.prestige = round(x.quality/2)


#religion

    #archtype generation

class religion_archtype:
    def __init__(self, name):
        self.name = name
        self.leader_title = ""
        self.high_leader_title = ""
        self.b1 = ""
        self.b2 = ""
        self.name_start = []
        

        #religions basically work as a belief right now. The difference is that there will be special "take_religious_action" moments where they will choose what to do based on highest religious belief
        #I still need to design and implement an institution system for religions, so it's not just a behavior decider but also an institution


        #traditional religion
        
traditional = religion_archtype("tradition")

traditional.leader_title = "Shaman"

traditional.high_leader_title = "Prophet"

traditional.b1 = "shrine"

traditional.b2 = "altar"

        #scholar religion

scholar = religion_archtype("scholar")

scholar.leader_title = "Sage"

scholar.high_leader_title = "Grand Sage"

scholar.b1 = "prayer hall"

scholar.b2 = "seminary"

scholar.name_start = ["Book", "Word", "Wisdom", "Truth"]

        #priest religion

priest = religion_archtype("priest")

priest.leader_title = "Cleric"

priest.high_leader_title = "Bishop"

priest.b1 = "temple"

priest.b2 = "office" #might change later- gotta think this through

priest.name_start = ["Love", "Heart", "Tears", "Mercy"]

        #mystic religion

mystic = religion_archtype("mystic")

mystic.leader_title = "Disciple"

mystic.high_leader_title = "Master"

mystic.b1 = "court"

mystic.b2 = "grave"

mystic.name_start = ["Dream", "Transcendence", "Star", "Sleep"]


#list of archtypes
archtypelist = (scholar, priest, mystic)


    #specific religions

class religion:
    def __init__(self, culture, archtype, based_on):
        self.archtype = archtype
        self.culture = culture
        self.deity = random.choice(self.culture.r_names) #need to make a system to not choose the same one twice
        self.name = ""
        self.based_on = based_on #is this derivative from an existing religion?
        if self.archtype == traditional:
            self.name = self.culture.name + " Ancestor Worship"
            self.deity = "Ancestors"
        else:
            self.name = str("The " + random.choice(self.archtype.name_start) + " of " + self.deity)
        self.traits = []
        if based_on == False:
            for i in random.sample(r_traits, 3): #choose 3 random traits
                self.traits.append(i)
            if archtype == traditional and "culture-specific" not in self.traits:
                self.traits[0] = "culture-specific"
        else:
            for i in random.sample(based_on.traits, 2):
                self.traits.append(i)
            self.traits.append(random.choice(r_traits))
        self.faith = belieftype(self.name, str("Belief in " + self.name))
        self.faith.is_religion = True
        self.faith.events = {"pray" : [1, 50], "convince": [51, 80] , "donate":[81, 93], "trait_special": [94, 100]} #need a way to more complexly generate these, based on traits
        


    #list of traits can include: culture-specific, sacrificial, apolitical
r_traits= ["sacrificial", "culture-specific", "apolitical", "intense", "warrior"]

def generate_religion(culture):
    x = religion(culture, random.choice(archtypelist), False)


#tech tree

techs = []

class tech:
    def __init__(self, name):
        techs.append(self)
        self.unlocked = False
        self.description = "No Description"
        self.name = name
        self.tcost = 0
        self.required = None #techs required before

def tech_check(tech):
    return tech.unlocked

def unlock_tech(tech):
    global techpt
    if tech.unlocked == True:
        text("This has already been unlocked!")
    elif tech.required.unlocked == False:
        text("Required: " + tech.required.name)
    elif techpt >= tech.tcost:
        tech.unlocked = True
        itext("Unlocked " + tech.name + ": " + tech.description)
    else:
        text("Not enough tech progress to unlock")

basic = tech("Basic")
basic.unlocked = True

east1 = tech("Metal")
east1.description = "Build a metal mine and processor"
east1.tcost = 5
east1.required = basic

east2= tech("Smith")
east2.description = "Build a Smith that can make weapons"
east2.tcost = 10
east2.required = east1

east3= tech("Farm 2") #this should be a specific type of animal, once I add different types of food
east2.description = "Farm that produces more food per unit, of a new type of food"
east2.tcost = 10
east2.required = east1

east4= tech("Mystic Buildings")
east4.description = "Buildings for Mystic Religions"
east4.tcost = 10
east4.required = east1

north1= tech("Crystals")
north1.description = "Build a crystal producer"
north1.tcost = 5
north1.required = basic

north2= tech("Palace")
north2.description = "Build a place to lead your city"
north2.tcost = 10
north2.required = north1

north3= tech("Fancy House")
north3.description = "Build a nicer, more prestigious house"
north3.tcost = 10
north3.required = north1

north4= tech("Craftshop 2")
north4.description = "Build a craftshop that can work with luxary matierials"
north4.tcost = 10
north4.required = north1

west1= tech("Jarble")
west1.description = "Build a jarble quarry"
west1.tcost = 5
west1.required = basic

west2= tech("Construction")
west2.description = "Build a construction center, to make roads and walls"
west2.tcost = 10
west2.required = west1

west3= tech("Ampitheter")
west3.description = "Build an ampitheter, to entertain and inform citizens"
west3.tcost = 10
west3.required = west1

west4= tech("Priestly Buildings")
west4.description = "Build buildings for Priestly Religions"
west4.tcost = 10
west4.required = west1

south1= tech("Gizard")
south1.description = "Build a gizard ranch"
south1.tcost = 5
south1.required = basic

south2= tech("Farm 3")#this should be a specific type of animal, once I add different types of food
south2.description = "Build a farm that produces more types of food, more efficiently"
south2.tcost = 10
south2.required = south1

south3= tech("Traditional Buildings")
south3.description = "Build buildings for Traditional Religions"
south3.tcost = 10
south3.required = south1

south4= tech("Tavern")
south4.description = "Build a tavern for your citizens to gather"
south4.tcost = 10
south4.required = south1

south5= tech("Armory")
south5.description = "Build an armory to give your troops and citizens armor"
south5.tcost = 10
south5.required = south2 #not sure where to put this one... I need to reorganize the tech tree to make more sense


se1 = tech("Puzzlenut Dye")
se1.description = "Build a Puzzlenut Processery"
se1.tcost = 5
se1.required = basic

se2 = tech("School")
se2.description = "Train and inform your citizens"
se2.tcost = 10
se2.required = se1

se3 = tech("Scholarly Buildings")
se3.description = "Build buildings for Scholarly Religions"
se3.tcost = 10
se3.required = se1

se4 = tech("Muskoil")
se4.description = "Build a Muskoil Prospectery"
se4.tcost = 10
se4.required = se1

se5 = tech("Healer")
se5.description = "Heal wounded citizens"
se5.tcost = 15
se5.required = se4


#combat

def attack(a, b):
    x = roll(0, 20) + a.com #roll d20, add combat
    if x > 10: #if result is over 20
        d = round(((a.str + a.com)/5 + 1)) #damage = str and com / 5 + 1 
        text(a.name + " hit " + b.name+ " for " + str(d) + " hp")
        b.hp -= d #deal the damage
        return "hit"
    else:
        return "miss"

def e_brawl(a, b):
    text("A brawl has begun between " + a.name + " and " + b.name)
    done = False
    battle_count = []
    battle = roll(3, 6) #how many misses in battle
    miss_count = 0
    gg = b.hp
    ff = a.hp 
    g = ""
    f = ""
    while done == False:
        battle_count.append(attack(a, b))#attacks
        g = dead_check(b, a)
        battle_count.append(attack(b, a))
        f = dead_check(a, b)
        
        for i in battle_count: #adds to miss counter
            if i == "miss":
                miss_count += 1

        if miss_count > battle or f == "dead" or g == "dead":  #checks if misses hit max
            done = True
    if f == "alive":
        text(a.name + " went from " + str(ff) + " to " + str(a.hp))
    if g == "alive":
        text(b.name + " went from " + str(gg) + " to " + str(b.hp))
        if b.culture != a.culture:
            if a.culture == knani:
                modify_belief(b, prej_knani, reason("Attacked by Knani", 50, 30))
            if a.culture == uul:
                modify_belief(b, prej_uul, reason("Attacked by Uul", 50, 30))
            if a.culture == huxley:
                modify_belief(b, prej_huxley, reason("Attacked by Huxley", 50, 30))

    

def dead_check(u, a): #unit, killer
    if u.hp < 1:
        u.clan.size -= 1
        v = units.pop(u.number)
        itext(u.name+ " has died!")
        for i in list(buildings.values()):
            if u in i.inside:
                i.inside.remove(u)
        choose_elder(u.clan.name)
        for i in units:
            if units[i].clan == u.clan:
                units[i].happy -= 30
                if units[i].culture != a.culture:
                    if a.culture == knani:
                        modify_belief(units[i], prej_knani, reason("Kin killed by Knani", 50, 30))
                    if a.culture == uul:
                        modify_belief(units[i], prej_uul, reason("Kin killed by Uul", 50, 30))
                    if a.culture == huxley:
                        modify_belief(units[i], prej_huxley, reason("Kin killed by Huxley", 50, 30))
        return "dead"
    else:
        return "alive"



#wisly's main menu

def main_menu():
    global gold
    lbl_gold = tk.Label(root, text = "Gold: " + str(gold) + " ")#extra space because brakets keep popping up
    lbl_gold.place(relx=0.4, rely=0.25)
    lbl_units = tk.Label(root, text = "Population: " + str(len(list(units.keys()))))
    lbl_units.place(relx=0.7, rely=0.25)
    global food
    lbl_food = tk.Label(root, text = "Food: " + str(food))
    lbl_food.place(relx=0.6, rely=0.25)
    global hour
    global date
    lbl_time = tk.Label(root, text="Day: " + str(date)+ "   Hour: " + str(hour))
    lbl_time.place(relx=0.2, rely=0.25)

    menu = tk.Frame(root, bg="black", bd=1) #main menu frame and buttons
    menu.place(relx=0.1, rely=0.3, relwidth=0.75, relheight=0.1)
    event = tk.Frame(root, bd=1)
    event.place(relx=0.1, rely=0.45, relwidth=0.75, relheight=0.45)
    btn_go = tk.Button(menu, text="Go", fg="green", command= pass_time)
    btn_go.place(relx=0.1, rely=0.3)
    btn_clans = tk.Button(menu, text="Clans", command = clan_menu)
    btn_clans.place(relx=0.3, rely=0.3)
    btn_job = tk.Button(menu, text="Jobs", command = job_menu)
    btn_job.place(relx=0.5, rely=0.3)
    btn_vill = tk.Button(menu, text="Village", command = build_menu)
    btn_vill.place(relx=0.7, rely=0.3)
    btn_data = tk.Button(menu, text="Data", command = data_menu)
    btn_data.place(relx=0.9, rely=0.3)
    btn_end = tk.Button(root, text="End", bg="red", command=root.quit)
    btn_end.place(relx=0.9, rely=0.1)
    lbl_event = tk.Label(event, text="Welcome to Colonizer Simulator!")
    lbl_event.place(relx=0.1, rely=0.1)
    for i in units:
        if units[i].happy < 0:
            text(units[i].name + " is unhappy")
            unit[i].happy = 0
    global txt_event
    global prompter
    txt_event = tk.Text(event, height=300, width=600)
    update_txt()
    prompter = [] #clears prompter
    txt_event.configure(state='disabled')
    scroll = tk.Scrollbar(event, orient = 'vertical', command=txt_event.yview)
    scroll.pack(side="right", expand=True, fill='y')
    txt_event.configure(yscrollcommand=scroll.set)
    txt_event.pack(side="right")



prompter = []

    
def text(quote):
    global prompter
    prompter.append(str(str(quote) + "\n"))

def itext(quote): #for important stuff
    text("----------")
    text(quote)
    text("----------")


def update_txt():
    global prompter
    global txt_event
    for i in prompter:
        txt_event.insert(tk.END, i)
    
    
#Initial Main menu
    
lbl_gold = tk.Label(root, text = "Gold: " + str(gold))
lbl_gold.place(relx=0.4, rely=0.25)
lbl_food = tk.Label(root, text = "Food: " + str(food))
lbl_food.place(relx=0.6, rely=0.25)

intro = "Welcome to Colonizer Simulator, alpha 1.11! Your goal is to get as much gold as possible, by manipulating your citizens. Give each clan a house to sleep and eat in, and assign units to different jobs. Goldmines get you gold, farms get you food, sawmills get you wood to build more buildings."
intro2 = " All those buildings use the strength stat. Craft shops use creativity, and allow units to build items that their cultural brothers will like."
intro3= " You pay units 1 gold per hour to work in these places. You earn the money back when units buy food (to survive) or crafts of their culture (for fun)."
intro4 = " Units go to buy food (price is kinda supply/demand) in the evenings, and crafts if they've got too much money on hand. Start by building two homes, a farm, and a goldmine"
intro5 = " Make sure there's enough food so no-one starves, and that everyone is spending it back to you. Run out of gold and you lose. Your food supply spoils after 4 days, every 7 you  get a new clan. Oh, and watch out for 'beliefs' (for now). Good luck!"
intro6= " Oh yeah and lmk if you see any errors pop up on the command prompt."
menu = tk.Frame(root, bg="black", bd=1) #main menu frame and buttons
menu.place(relx=0.1, rely=0.3, relwidth=0.75, relheight=0.1)
btn_go = tk.Button(menu, text="Go", fg="green", command= pass_time)
btn_go.place(relx=0.1, rely=0.3)
btn_clans = tk.Button(menu, text="Clans", command = clan_menu)
btn_clans.place(relx=0.3, rely=0.3)
btn_job = tk.Button(menu, text="Jobs", command = job_menu)
btn_job.place(relx=0.5, rely=0.3)
btn_vill = tk.Button(menu, text="Village", command = build_menu)
btn_vill.place(relx=0.7, rely=0.3)
btn_data = tk.Button(menu, text="Data", command = data_menu)
btn_data.place(relx=0.9, rely=0.3)
btn_end = tk.Button(root, text="End", bg="red", command=root.quit)
btn_end.place(relx=0.9, rely=0.1)
txt_event = tk.Text(event, height=300, width=600)
quote= intro + intro2 + intro3 +intro4 + intro5+intro6 #Insert event text here
txt_event.insert(tk.END, quote)
txt_event.configure(state='disabled')
scroll = tk.Scrollbar(event, orient = 'vertical', command=txt_event.yview)
scroll.pack(side="right", expand=True, fill='y')
txt_event.configure(yscrollcommand=scroll.set)
txt_event.pack(side="right")


        

#testing
        
    # culture settings
knani = culture("Knani")
knani.craftnames = ["Clay Mask", "Bead String", "Carving of a Figurine", "Ceramic Bowl", "Ceramic Jug", "Wax Seal"]
add_random_l_names(knani, ["Shorah", "Hita", "Zahav", "Gefen", "Tana", "Zayit", "Dvash", "Rimon", "Hamam", "Aviyonah", "Kosht", "Karbos", "Shevet", "Gufnan", "Ezov", "Lulav", "Etrog", "Pilpel", "Og"])
add_random_f_names(knani, ["Avshalom", "Yeshayahu", "Rechavam", "Yaravam", "Nadav", "Baasha", "Elah", "Zimri", "Omri", "Achaziah", "Yehoram", "Elitsur", "Amminadav", "Zurishaddai", "Zuar", "Helon", "Gamaliel", "Pedahzur", "Enan", "Korach"])
add_random_r_names(knani, ["Enki", "Enlil", "Utu", "Nergal", "Nabu", "Marduk", "Ninurta", "Ki", "Geshtinanna", "Ereshkigal", "Aruru", "Emesh", "Ennugi", "Hahanu", "Imdugud", "Lamashtu"])
knani.likely_religions = {religion(knani, traditional, False) : 60, religion(knani, random.choice(archtypelist), False) : roll(10, 40), religion(knani, random.choice(archtypelist), False) : roll(10, 40) }


huxley = culture("Huxley")
huxley.craftnames = ["Belt Buckle", "Neck Band", "Ceremonial Sword", "Goblet", "Tin Hat", "Bejewled Box"]
add_random_f_names(huxley, ["Guthmaer", "Gladwin", "Edmund", "Elfrith", "Peohtred", "Wulfhere", "Swidbert", "Sighere", "Caedmon", "Orped", "Wynbald", "Turgiua", "Wynflead", "Begild", "Hiltrude", "Elfswitha", "Sunnild", "Burchwen"])
add_random_l_names(huxley, ["Newham", "Wolfpine", "Swinford", "Eastcliff", "Skystead", "Colkirk", "Dewhurst", "Armskirk", "Cullfield", "Nantwich", "Keld", "Sudbury", "Aynor", "Lockinge", "Merton"])
add_random_r_names(huxley, ["Abhean", "Amergin Gluingel", "Bodb Dearg", "Conand", "Ecne", "Lir", "Luchtaine", "Mac Cecht", "Seonaidh", "Airmed", "Blathnat", "Brigid", "Cethlenn", "Flidais", "The Morrigan"])
huxley.likely_religions = {religion(huxley, traditional, False) : 60, religion(huxley, random.choice(archtypelist), False) : roll(10, 40), religion(huxley, random.choice(archtypelist), False) : roll(10, 40) }


uul = culture("Uul")
uul.craftnames = ["Bone Necklace", "Dragon Pendant", "Embroidered Boots", "Jade Scabard", "Stenciled Plate"]
add_random_f_names(uul, ["Jebke", "Ligdan", "Sokhor", "Tomorbaatar", "Kamala", "Khagatai", "Menggulig", "Jungshoi", "Kus", "Geugi", "Khenbish", "Samga", "Solongo", "Maa", "Altun", "Oyuunchimeg", "Ergene", "Terbish"])
add_random_l_names(uul, ["Ganbold", "Ganbaatar", "Batbayar", "Ganbat", "Dorj", "Jargalsaikhan", "Battulga", "Hu", "Ganzorig", "Gantulga", "Nergui", "Purev", "Myagmar", "Banzragch", "Ochirbat", "Byambajav", "Chinbat"])
add_random_r_names(uul, ["Kayra", "Mergen", "Kyzaghan", "Kubai", "Yel Ana", "Aisyt", "Etugen", "Hurmuz", "Baianai", "Akbugha", "Qovaq", "Izıh", "Khyrtyq", "Yaryond", "Uylak", "Erbuke"])
uul.likely_religions = {religion(uul, traditional, False) : 60, religion(uul, random.choice(archtypelist), False) : roll(10, 40), religion(uul, random.choice(archtypelist), False) : roll(10, 40) }
        #cultures might start out with powerful religions, or almost entirely traditions, at their homeland

    # sample beliefs

rebellion = belieftype("Rebellion", "This person dislikes your rule")
rebellion.events = {"nothing": [1, 50], "grumble": [51, 75], "convince": [76, 100]}
prej_huxley = belieftype("Huxley Prejudice", "This person dislikes Huxleys")
prej_huxley.events = {"nothing" : [1, 50], "insult huxley": [51, 80] , "convince":[81, 93], "attack huxley": [94, 100]}
prej_knani = belieftype("Knani Prejudice", "This person dislikes Knanis")
prej_knani.events = {"nothing" : [1, 50], "insult knani": [51, 80] , "convince":[81, 93], "attack knani": [94, 100]}
prej_uul = belieftype("Uul Prejudice", "This person dislikes Uuls")
prej_uul.events = {"nothing" : [1, 50], "insult uul": [51, 80] , "convince":[81, 93], "attack uul": [94, 100]}
trad = belieftype("Traditonal Values", "This person belives in tradition")
trad.events = {"nothing": [1, 50], "pray": [51, 100]}
capitalism = belieftype("Wealth", "This person wants riches")
capitalism.events = {"nothing": [1, 50], "go to store": [51, 100]}
loyalty = belieftype("Loyalty", "Loyalty to you")
loyalty.events = {"nothing": [1, 50], "donate wallet": [51, 100]}

                
immigration_size = random.randint(3, 8) #starting clan size upon arrival



generate_clan(knani, roll(3, 6))
generate_clan(uul, roll(3, 6))




all_unit_nums = list(units.keys())



generate_building(foodmarket, "market 0")

hour = 0

root.mainloop()


