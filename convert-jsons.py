#!/usr/bin/env python

import json

l18n_english = './data/locale/en/cardinal.en.ucs'

units = [{
    "id": "spearman",
    "customName": "Spearman",
    "ageId": "1",
    "civs": ["ab", "ch", "de", "fr", "hr", "mo", "ru"],
    "weapon_file": "./data/attrib/attrib/weapon/races/common/melee/weapon_spearman_1.json",
    "unit_ebps_file": "./data/attrib/attrib/ebps/races/core/units/unit_spearman_1.json",
    "unit_sbps_file": "./data/attrib/attrib/sbps/races/core/unit_spearman_1.json"
},
    {
    "id": "hardened-spearman",
    "customName": "Hardened Spearman",
    "ageId": "2",
    "civs": ["ab", "ch", "de", "en", "fr", "hr", "mo", "ru"],
    "weapon_file": "./data/attrib/attrib/weapon/races/common/melee/weapon_spearman_2.json",
    "unit_ebps_file": "./data/attrib/attrib/ebps/races/core/units/unit_spearman_2.json",
    "unit_sbps_file": "./data/attrib/attrib/sbps/races/core/unit_spearman_2.json"
},
    {
    "id": "veteran-spearman",
    "customName": "Veteran Spearman",
    "ageId": "3",
    "civs": ["ab", "ch", "de", "en", "fr", "hr", "mo", "ru"],
    "weapon_file": "./data/attrib/attrib/weapon/races/common/melee/weapon_spearman_3.json",
    "unit_ebps_file": "./data/attrib/attrib/ebps/races/core/units/unit_spearman_3.json",
    "unit_sbps_file": "./data/attrib/attrib/sbps/races/core/unit_spearman_3.json"
},
    {
    "id": "elite-spearman",
    "customName": "Elite Spearman",
    "ageId": "4",
    "civs": ["ab", "ch", "de", "en", "fr", "hr", "mo", "ru"],
    "weapon_file": "./data/attrib/attrib/weapon/races/common/melee/weapon_spearman_4.json",
    "unit_ebps_file": "./data/attrib/attrib/ebps/races/core/units/unit_spearman_4.json",
    "unit_sbps_file": "./data/attrib/attrib/sbps/races/core/unit_spearman_4.json"
},
    {
    "id": "vanguard-man-at-arms",
    "customName": "Man-at-Arms (Vanguard)",
    "ageId": "1",
    "civs": ["en"],
    "weapon_file": "./data/attrib/attrib/weapon/races/common/melee/weapon_manatarms_1.json",
    "unit_ebps_file": "./data/attrib/attrib/ebps/races/core/units/unit_manatarms_1.json",
    "unit_sbps_file": "./data/attrib/attrib/sbps/races/core/unit_manatarms_1.json"
},
    {
    "id": "early-man-at-arms",
    "customName": "Man-at-Arms (Early)",
    "ageId": "2",
    "civs": ["en", "hr"],
    "weapon_file": "./data/attrib/attrib/weapon/races/common/melee/weapon_manatarms_2.json",
    "unit_ebps_file": "./data/attrib/attrib/ebps/races/core/units/unit_manatarms_2.json",
    "unit_sbps_file": "./data/attrib/attrib/sbps/races/core/unit_manatarms_2.json"
},
    {
    "id": "man-at-arms",
    "customName": "Man-at-Arms",
    "ageId": "3",
    "civs": ["ab", "de", "en", "fr", "mo", "ru", "hr"],
    "weapon_file": "./data/attrib/attrib/weapon/races/common/melee/weapon_manatarms_3.json",
    "unit_ebps_file": "./data/attrib/attrib/ebps/races/core/units/unit_manatarms_3.json",
    "unit_sbps_file": "./data/attrib/attrib/sbps/races/core/unit_manatarms_3.json"
},
    {
    "id": "elite-man-at-arms",
    "customName": "Elite Man-at-Arms",
    "ageId": "4",
    "civs": ["ab", "de", "en", "fr", "mo", "ru", "hr"],
    "weapon_file": "./data/attrib/attrib/weapon/races/common/melee/weapon_manatarms_4.json",
    "unit_ebps_file": "./data/attrib/attrib/ebps/races/core/units/unit_manatarms_4.json",
    "unit_sbps_file": "./data/attrib/attrib/sbps/races/core/unit_manatarms_4.json"
},
    {
    "id": "landsknecht",
    "customName": "Landsknecht",
    "ageId": "3",
    "civs": ["hr"],
    "weapon_file": "./data/attrib/attrib/weapon/races/hre/melee/weapon_landsknecht_3_hre.json",
    "unit_ebps_file": "./data/attrib/attrib/ebps/races/hre/units/unit_landsknecht_3_hre.json",
    "unit_sbps_file": "./data/attrib/attrib/sbps/races/hre/unit_landsknecht_3_hre.json"
},
    {
    "id": "elite-landsknecht",
    "customName": "Elite Landsknecht",
    "ageId": "4",
    "civs": ["hr"],
    "weapon_file": "./data/attrib/attrib/weapon/races/hre/melee/weapon_landsknecht_4_hre.json",
    "unit_ebps_file": "./data/attrib/attrib/ebps/races/hre/units/unit_landsknecht_4_hre.json",
    "unit_sbps_file": "./data/attrib/attrib/sbps/races/hre/unit_landsknecht_4_hre.json"
},
    {
    "id": "villager",
    "customName": "Villager",
    "ageId": "1",
    "civs": ["ab", "ch", "de", "hr", "mo", "ru"],
    "weapon_file": "./data/attrib/attrib/weapon/races/common/melee/weapon_villager_1.json",
    "unit_ebps_file": "./data/attrib/attrib/ebps/races/core/units/unit_villager_1.json",
    "unit_sbps_file": "./data/attrib/attrib/sbps/races/core/unit_villager_1.json"
},
    {
    "id": "villager",
    "customName": "Villager",
    "ageId": "1",
    "civs": ["en"],
    "weapon_file": "./data/attrib/attrib/weapon/races/english/ranged/weapon_villager_militarized_2_eng.json",
    "unit_ebps_file": "./data/attrib/attrib/ebps/races/english/units/unit_villager_1_eng.json",
    "unit_sbps_file": "./data/attrib/attrib/sbps/races/english/unit_villager_1_eng.json"
},
    {
    "id": "villager",
    "customName": "Villager",
    "ageId": "1",
    "civs": ["fr"],
    "weapon_file": "./data/attrib/attrib/weapon/races/common/melee/weapon_villager_1.json",
    "unit_ebps_file": "./data/attrib/attrib/ebps/races/french/units/unit_villager_1_fre.json",
    "unit_sbps_file": "./data/attrib/attrib/sbps/races/french/unit_villager_1_fre.json"
},
    {
    "id": "scout",
    "customName": "Scout",
    "ageId": "1",
    "civs": ["ab", "ch", "de", "en", "fr", "hr", "mo", "ru"],
    "weapon_file": "./data/attrib/attrib/weapon/races/common/melee/weapon_scout_1.json",
    "unit_ebps_file": "./data/attrib/attrib/ebps/races/core/units/unit_scout_1.json",
    "unit_sbps_file": "./data/attrib/attrib/sbps/races/core/unit_scout_1.json"
},
    {
    "id": "fishing-boat",
    "customName": "Fishing Boat",
    "ageId": "1",
    "civs": ["ab", "ch", "en", "fr", "hr", "mo"],
    "weapon_file": "",
    "unit_ebps_file": "./data/attrib/attrib/ebps/races/core/units/unit_naval_fishing_boat_2.json",
    "unit_sbps_file": "./data/attrib/attrib/sbps/races/core/unit_naval_fishing_boat_2.json"
},
    {
    "id": "fishing-boat",
    "customName": "Fishing Boat",
    "ageId": "1",
    "civs": ["de"],
    "weapon_file": "",
    "unit_ebps_file": "./data/attrib/attrib/ebps/races/sultanate/units/unit_naval_fishing_boat_2_sul.json",
    "unit_sbps_file": "./data/attrib/attrib/sbps/races/sultanate/unit_naval_fishing_boat_2_sul.json"
},
]


def get_damage_type(data):
    try:
        damage_type = data['weapon_bag']['damage']['damage_type']

        return damage_type
    except:
        return ""


def get_weapon(data):
    try:
        damage_type = data['weapon_bag']['weapon_class']

        return damage_type
    except:
        return ""


def get_damage(data):
    try:
        damage_min = data['weapon_bag']['damage']['min']
        damage_max = data['weapon_bag']['damage']['max']
        if (damage_min != damage_max):
            return f"{damage_min} - {damage_max}"
        else:
            return damage_min
    except:
        return ""


def get_bonus_damage(data):
    try:
        bonus_list = []
        bonus_damages = data['weapon_bag']['target_type_table']['list']
        for bonus_info in bonus_damages:
            bonus = {}
            bonus['damage'] = bonus_info['target_unit_type_multipliers']['base_damage_modifier']
            bonus['vs'] = bonus_info['target_unit_type_multipliers']['unit_type']
            bonus_list.append(bonus)
        return bonus_list
    except:
        return ""


def get_range(data):
    try:
        range = {}
        range_max = data['weapon_bag']['range']['max']
        range_min = data['weapon_bag']['range']['min']
        range['min'] = range_min
        range['max'] = range_max
        return range
    except:
        return ""


def get_speed(data):
    try:
        speed = data['moving_ext']['speed_scaling_table']['default_speed']
        speed_tiles_per_second = speed * 0.25
        return speed_tiles_per_second
    except:
        return ""


def get_melee_armor(data):
    try:
        melee_armor = data['health_ext']['armor_scaler_by_damage_type']['Melee']
        return melee_armor
    except:
        return ""


def get_fire_armor(data):
    try:
        fire_armor = data['health_ext']['armor_scaler_by_damage_type']['Fire']
        return fire_armor
    except:
        return ""


def get_ranged_armor(data):
    try:
        ranged_armor = data['health_ext']['armor_scaler_by_damage_type']['Ranged']
        return ranged_armor
    except:
        return ""


def get_true_armor(data):
    try:
        true_armor = data['health_ext']['armor_scaler_by_damage_type']['True Damage']
        return true_armor
    except:
        return ""


def get_hp(data):
    try:
        hp = data['health_ext']['hitpoints']
        return hp
    except:
        return ""


def get_cost(data):
    try:
        cost = {}
        time = data['cost_ext']['time_cost']['time_seconds']
        food = data['cost_ext']['time_cost']['cost']['food']
        wood = data['cost_ext']['time_cost']['cost']['wood']
        gold = data['cost_ext']['time_cost']['cost']['gold']
        stone = data['cost_ext']['time_cost']['cost']['stone']
        population_personnel = data['population_ext']['personnel_pop']
        population_vehicle = data['population_ext']['vehicle_pop']
        population = population_personnel + population_vehicle

        cost['time'] = time
        cost['food'] = food
        cost['wood'] = wood
        cost['gold'] = gold
        cost['stone'] = stone
        cost['population'] = population

        return cost
    except Exception as e:
        return ""


def get_translation(id):
    with open(l18n_english, encoding='utf-16-le') as l18n_file:
        Lines = l18n_file.readlines()
        for line in Lines:
            if line.find(f"{id}	") >= 0:
                return line.replace(f"{id}	", "").strip()

    return ""


def get_classification(data):
    classification_id = data['squad_ui_ext']['race_list']['list'][0]['race_data']['info']['extra_text']
    classification = get_translation(classification_id)
    return classification


def get_description(data):
    classification_id = data['squad_ui_ext']['race_list']['list'][0]['race_data']['info']['help_text']
    classification = get_translation(classification_id)
    return classification


units_info = []

for unit in units:
    unit_info = {}
    unit_info['id'] = unit['id']
    unit_info['customName'] = unit['customName']
    unit_info['ageId'] = unit['ageId']
    unit_info['civs'] = unit['civs']

    if unit['weapon_file']:
        with open(unit['weapon_file']) as json_file:
            json_data = json.load(json_file)
            damage_type = get_damage_type(json_data)
            weapon = get_weapon(json_data)
            damage = get_damage(json_data)
            bonus = get_bonus_damage(json_data)
            range = get_range(json_data)

            unit_info['damageType'] = damage_type
            unit_info['weapon'] = weapon
            unit_info['damage'] = damage
            unit_info['bonus'] = bonus
            unit_info['range'] = range
    else:
        print(f"Weapon file for unit {unit['id']} doesn't exist")

    if unit['unit_sbps_file']:
        with open(unit['unit_sbps_file']) as json_file:
            json_data = json.load(json_file)
            classification = get_classification(json_data)
            description = get_description(json_data)

            unit_info['classification'] = classification
            unit_info['description'] = description
    else:
        print(f"Sbps file for unit {unit['id']} doesn't exist")

    if unit['unit_ebps_file']:
        with open(unit['unit_ebps_file']) as json_file:
            json_data = json.load(json_file)
            speed = get_speed(json_data)
            melee_armor = get_melee_armor(json_data)
            fire_armor = get_fire_armor(json_data)
            ranged_armor = get_ranged_armor(json_data)
            true_armor = get_true_armor(json_data)
            hp = get_hp(json_data)
            cost = get_cost(json_data)

            unit_info['speed'] = speed
            armor = {}
            armor['meleeArmor'] = melee_armor
            armor['fireArmor'] = fire_armor
            armor['rangedArmor'] = ranged_armor
            armor['trueArmor'] = true_armor
            unit_info['armor'] = armor
            unit_info['hp'] = hp
            unit_info['cost'] = cost
    else:
        print(f"Ebps file for unit {unit['id']} doesn't exist")

    units_info.append(unit_info)


print(json.dumps(units_info, indent=4, sort_keys=True))
