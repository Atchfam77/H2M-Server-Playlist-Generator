import string
import random
# Define your lists # "gametype hp map ",
mode = ["gametype dom map ", "gametype dm map ", "gametype war map ", "gametype conf map ", "gametype gun map "]
aw = ["mp_venus", "mp_urban", "mp_torqued", "mp_terrace", "mp_spark", "mp_solar", "mp_sector17", "mp_refraction",
      "mp_recovery", "mp_prison", "mp_perplex_1", "mp_lost", "mp_liberty", "mp_levity", "mp_laser2", "mp_lair",
      "mp_lab2", "mp_kremlin", "mp_instinct", "mp_highrise2", "mp_greenband", "mp_fracture", "mp_detroit", "mp_dam",
      "mp_comeback", "mp_clowntown3", "mp_climate_3", "mp_bigben2"] #  "mp_blackbox",
mw2 = ["mp_afghan", "mp_complex", "mp_abandon", "mp_derail", "mp_estate", "mp_favela", "mp_fuel2", "mp_highrise",
       "mp_invasion", "mp_checkpoint", "mp_quarry", "mp_rundown", "mp_rust", "mp_compact", "mp_boneyard",
       "mp_nightshift", "mp_storm", "mp_subbase", "mp_terminal", "mp_trailerpark", "mp_underpass", "mp_brecourt"]
cod4 = ["mp_convoy", "mp_backlot", "mp_bloc", "mp_bog", "mp_countdown", "mp_crash", "mp_crossfire", "mp_citystreets",
        "mp_farm", "mp_overgrown", "mp_pipeline", "mp_shipment", "mp_showdown", "mp_strike", "mp_vacant", "mp_wet",
        "mp_bog_summer", "mp_farm_spring", "mp_crash_snow"]
mw2cr = ["airport", "boneyard", "cliffhanger", "contingency", "dc_whitehouse", "dcburning", "estate", "gulag", "oil rig"]

# Shuffle maps to ensure randomness
random.shuffle(mw2)
random.shuffle(aw)
random.shuffle(cod4)
random.shuffle(mw2cr)

# Set up the config command with this string
pastestring="set sv_maprotation \""
# Generate the combined list
mw2list = []
for item in mw2:
    mw2list.append(f"{random.choice(mode)}{item}")
# append random list into 1 string
mw2playlist = " ".join(mw2list)
# print the final command
print(pastestring+mw2playlist+"\"")

# Generate the combined list
awlist = []
for item in aw:
    awlist.append(f"{random.choice(mode)}{item}")
# append random list into 1 string
awplaylist = " ".join(awlist)
# print the final command
print(pastestring+awplaylist+"\"")

# Generate the combined list
cod4list = []
for item in cod4:
    cod4list.append(f"{random.choice(mode)}{item}")
# append random list into 1 string
cod4playlist = " ".join(cod4list)
# print the final command
print(pastestring+cod4playlist+"\"")

# Generate the combined list
mw2crlist = []
for item in mw2cr:
    mw2crlist.append(f"{random.choice(mode)}{item}")
# append random list into 1 string
mw2crplaylist = " ".join(mw2crlist)
# print the final command
print(pastestring+mw2crplaylist+"\"")