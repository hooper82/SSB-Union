import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

# Story Names
HumanMusic = "We Play Human Music"
CatGone = "A Cat That Really Was Gone"
Duelist = "The Duelist in Purple Armor"
Horok = "The Adventures of Horok Ra"
CitySlickers = "City Slickers and Hayseeds"
DeniedOps = "Denied Operations"
SemperShil = "Semper Shil'vati"
ChaosAndMayhem = "Chaos and Mayhem"
DependentSpouse = "Dependent Spouse"
JustOneDrop = "Just One Drop"
FireWithin = "Fire Within"
TopLasgun = "Top Lasgun"
AlienNation = "Alien Nation"
BlueBlood = "The Blue Blood"
GoingNative = "Going Native"
StreetFighter = "Streetfighter"
FarAway = "Far Away"
Loyalist = "Loyalist"
PianoMan = "The Piano Man"
Lifeguards = "Lifeguards and Amazons"
CulturalExchange = "Cultural Exchange"
ClawsOfFate = "Claws of Fate"
InForPenny = "In for a Penny"
NoSeparatePeace = "No Separate Peace"
Insurgent = "Insurgent"
Untitled = "Untitled"
Marauder = "The Marauder"
HumanStudies = "Human Studies"
TourDownUnder = "A Tour Down Under"
WesternInsurgency = "The Western Insurgency"
SocialEngineering = "Social Engineering"
TheCook = "The Cook"
Shadows = "Shadows in the Berkshires"
DearJournal = "Dear Journal"
OfferYouCantRefuse = "An offer they can't refuse"
OnceRebel = "Once a Rebel"
RunningWithThePack = "Running with the Pack"
Astray = "Astray"
Pizzaman = "Tales of a Post Invasion Pizzaman"
UnwelcomeGuests = "The Unwelcome Guests"
IndependenciaFilipina = "La Independencia Filipina"
NoGoodDeed = "No Good Deed"
FireTeamFloofy = "Fire Team Floofy"
HuntingMaus = "Hunting a Maus"
DivedeAndConquer = "Divede and Conquer"
HellFury = "Hell Hath No Fury"
Refractor = "Refractor"
Stray = "Stray"
PaxImperia = "Pax Imperia"
AppalachiaCalling = "Appalachia Calling"
ImperiumsHeart = "The way to an imperium's heart"
SonsOfThunder = "Sons of Thunder"
TuroxAndLeopard = "The Turox and the Leopard"
SalvagedPast = "Salvaged Past"
BloodForParadise = "Blood for Paradise"
ToxicSands = "Toxic Sands"
EagleSprings = "Eagle Springs"
LlanosMestanas = "Llanos Mestanas"
LegionOfMonsters = "Legion of monsters: the last king"


# Crossover/alt timeline story names
Unbreakable = "Unbreakable"
FireteamProvidence = "Fireteam Providence"

# Create nodes
G.add_node(DependentSpouse)
G.add_node(ChaosAndMayhem)
G.add_node(TopLasgun)
G.add_node(SemperShil)
G.add_node(InForPenny)
G.add_node(CitySlickers)
G.add_node(StreetFighter)
G.add_node(ClawsOfFate)
G.add_node(GoingNative)
G.add_node(CulturalExchange)
G.add_node(DeniedOps)
G.add_node(Duelist)
G.add_node(Horok)
G.add_node(JustOneDrop)
G.add_node(HumanMusic)
G.add_node(PianoMan)
G.add_node(FireWithin)
G.add_node(FarAway)
G.add_node(Lifeguards)
G.add_node(Loyalist)
G.add_node(Insurgent)
G.add_node(Shadows)
G.add_node(BlueBlood)
G.add_node(AlienNation)
G.add_node(CatGone)
G.add_node(NoSeparatePeace)
G.add_node(RunningWithThePack)
G.add_node(Astray)
G.add_node(BloodForParadise)
G.add_node(ToxicSands)
G.add_node(EagleSprings)
G.add_node(LegionOfMonsters)

# All of the references, attempted to kinda group them by story
G.add_edge(SemperShil, FarAway)
G.add_edge(SemperShil, DependentSpouse)
G.add_edge(SemperShil, FireWithin)
G.add_edge(SemperShil, TopLasgun)
G.add_edge(SemperShil, CatGone)

G.add_edge(FireWithin, StreetFighter)
G.add_edge(FireWithin, GoingNative)

G.add_edge(GoingNative, InForPenny)
G.add_edge(GoingNative, TopLasgun)

G.add_edge(InForPenny, ClawsOfFate)

G.add_edge(JustOneDrop, GoingNative)
G.add_edge(JustOneDrop, CitySlickers)
G.add_edge(JustOneDrop, PianoMan)
G.add_edge(JustOneDrop, CulturalExchange)
G.add_edge(JustOneDrop, HumanMusic)
G.add_edge(JustOneDrop, DeniedOps)

G.add_edge(DeniedOps, Horok)
G.add_edge(DeniedOps, ClawsOfFate)
G.add_edge(DeniedOps, ChaosAndMayhem)
G.add_edge(DeniedOps, HumanMusic)
G.add_edge(DeniedOps, CulturalExchange)

G.add_edge(Horok, Duelist)
G.add_edge(Horok, ClawsOfFate)
G.add_edge(Horok, BloodForParadise)
G.add_edge(Horok, RunningWithThePack)
G.add_edge(Astray, RunningWithThePack)

G.add_edge(CitySlickers, PianoMan)
G.add_edge(CitySlickers, ChaosAndMayhem)

G.add_edge(ChaosAndMayhem, Lifeguards)
G.add_edge(ChaosAndMayhem, DependentSpouse)
G.add_edge(ChaosAndMayhem, InForPenny)
G.add_edge(ChaosAndMayhem, PianoMan)
G.add_edge(ChaosAndMayhem, BlueBlood)
G.add_edge(ChaosAndMayhem, AlienNation)

G.add_edge(FarAway, TopLasgun)
G.add_edge(HumanMusic, TopLasgun)
G.add_edge(Loyalist, DependentSpouse)

G.add_edge(AlienNation, CatGone)
G.add_edge(AlienNation, SemperShil)
G.add_edge(AlienNation, BlueBlood)
G.add_edge(AlienNation, Shadows)

G.add_edge(Insurgent, BlueBlood)

G.add_edge(NoSeparatePeace, TopLasgun)
G.add_edge(NoSeparatePeace, HumanMusic)

G.add_edge(JustOneDrop, TopLasgun)
G.add_edge(JustOneDrop, Loyalist)

G.add_edge(DeniedOps, ToxicSands)
G.add_edge(DeniedOps, EagleSprings)

G.add_edge(FarAway, EagleSprings)
G.add_edge(FarAway, DeniedOps)
G.add_edge(FarAway, ChaosAndMayhem)

G.add_edge(Untitled, AlienNation)

G.add_edge(SemperShil, Untitled)
G.add_edge(SemperShil, ChaosAndMayhem)

G.add_edge(ClawsOfFate, FireWithin)

G.add_edge(LegionOfMonsters, ChaosAndMayhem)

# Create a colormap for recoloring nodes
color_map = []
for node in G:
    if node == "insert name variable here" or node == "or here":
        color_map.append('#1f76b4')  # Switch story colors if listed in if
    else:
        color_map.append('#1f76b4')  # Else stay blue

# Bump up figure size if text starts overlapping (width, height)
plt.figure(3, figsize=(16, 16))
# Add labels and the color map
nx.draw_shell(G, with_labels=True, node_color=color_map)
plt.axis('off')
axis = plt.gca()

# A bit of spacing around the edge so labels won't overflow
# Current settings give the current amount of stories a circular shape
axis.set_xlim([1.8 * x for x in axis.get_xlim()])
axis.set_ylim([1.2 * y for y in axis.get_ylim()])
# plt.tight_layout() - commented out, just throws a warning
plt.show()


# TODO: Get the universe crossover/alt timeline version up-to-date

# Alt version nodes
G.add_node(FireteamProvidence)

# Alt version connections
G.add_edge(FireteamProvidence, FarAway)
G.add_edge(FireteamProvidence, EagleSprings)

# Yes, this is kind of awful, no I don't care
# (at least yet, I might when I add more colored nodes)
color_map = []
for node in G:
    if node == FireteamProvidence or node == "or here":
        color_map.append('#eb0000')  # Switch story colors if listed in if
    else:
        color_map.append('#1f76b4')  # Else stay blue

# Bump up figure size if text starts overlapping (width, height)
plt.figure(3, figsize=(16, 16))
# Add labels and the color map
nx.draw_shell(G, with_labels=True, node_color=color_map)
plt.axis('off')
axis = plt.gca()

# A bit of spacing around the edge so labels won't overflow
# Current settings give the current amount of stories a circular shape
axis.set_xlim([1.7 * x for x in axis.get_xlim()])
axis.set_ylim([1.2 * y for y in axis.get_ylim()])
# plt.tight_layout() - commented out, just throws a warning
plt.show()
