import pandas as pd

table = pd.read_excel("data\periodic_table.xlsx")
reactivity = pd.read_excel('data\\reactivity_series.xlsx')
electromotive = pd.read_excel('data\electromotive_potentials.xlsx')

def menu():
    print("\n----------------------------------------------------")
    print("------------------------MENU------------------------")
    print("1 - Periodic Table")
    print("2 - Reactivity Series")
    print("3 - Electromotive Potential")
    print("----------------------------------------------------")
    print("----------------------------------------------------")

def show_table(i):
    number = table["number"][i]
    name = table["name"][i]
    sym = table["symbol"][i]
    appearance = table["appearance"][i]
    group = table["group_block"][i]
    period = table["period"][i]
    category = table["element_category"][i]
    atomic_weight = table["atomic_weight"][i]
    elec_config = table["electron_configuration"][i]
    electronegativity = table["electronegativity"][i]
    phase = table["phase"][i]
    melting = table["melting_point"][i]
    boiling = table["boiling_point"][i]
    density = table["density_at_stp"][i]
    oxidation = table["oxidation_states"][i]
    discovery = table["discovery"][i]

    print("\n==========================================")
    print(f"ATOMIC NUMBER: {number}")
    print(f"SYMBOL: {sym}")
    print(f"NAME: {name}")
    print(f"ELECTRONIC CONFIGURATION: {elec_config}")
    print(f"ELECTRONEGATIVITY: {electronegativity}")
    print(f"PERIOD: {period}")
    print(f"CATEGORY: {category}")
    print(f"PHASE: {phase}")
    print(f"ATOMIC WEIGHT: {atomic_weight}")
    print(f"MELTING POINT: {melting}")
    print(f"BOILING POINT: {boiling}")
    print(f"DENSITY: {density}")
    print(f"OXIDATION: {oxidation}")
    print(f"GROUP: {group}")
    print(f"APPEARANCE: {appearance}")
    print(f"DISCOVER: {discovery}")
    print("==========================================")

def title(x):
    print("\n----------------------------------------------------")
    print("{:^50}".format(x))
    print("----------------------------------------------------")

def reactivity_series(sym, aux):
    for i in range(len(reactivity)):
        if sym == reactivity['symbol'][i]:
            name = reactivity['name'][i]
            ion = reactivity['ion'][i]

            print("\n==========================================")
            print(f"SYMBOL: {sym}")
            print(f"NAME: {name}")
            print(f"ION: {ion}")
            print("==========================================")
            aux += 1
    if aux == 0:
                print("No elements found.")

def electromotive_potentials(element):
    print(f"\nHere's all matches with '{element}'")
    print("Format: oxidant | reductant | potential")
    for i in range(0, len(electromotive)):
        oxidant = electromotive['oxidant'][i]
        if element in oxidant:
            reductant = electromotive['reductant'][i]
            potential = electromotive['potential'][i]
            print(f"\n{oxidant} | {reductant} | {potential}")
