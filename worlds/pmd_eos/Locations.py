import typing

import typing_extensions

from BaseClasses import Location


class LocationData:
    name: str = ""
    classification: str = ""
    dungeon_length: int = 1
    id: int = -1
    dungeon_start_id: int = -1

    def __init__(self,  classification, dungeon_length, name, id, dungeon_start_id):
        self.name = name
        self.classification = classification
        self.dungeon_length = dungeon_length
        self.id = id
        self.dungeon_start_id = dungeon_start_id


class EOSLocation(Location):
    game: str = "Pokemon Mystery Dungeon Explorers of Sky"


EOS_location_table: typing.List[LocationData] = [
    # "Test Dungeon", 0,  # Should be unused
    LocationData("EarlyDungeonComplete", 2,  "Beach Cave", 2,  1),
    LocationData("EarlyDungeonComplete", 1, "Drenched Bluff", 3, 3),
    LocationData("EarlyDungeonComplete", 2, "Mt. Bristle", 5, 4),  # 2 subareas
    LocationData("EarlyDungeonComplete", 1, "Waterfall Cave", 6, 6),
    LocationData("EarlyDungeonComplete", 1, "Apple Woods", 7, 7),
    LocationData("EarlyDungeonComplete", 1, "Craggy Coast", 8, 8),
    LocationData("EarlyDungeonComplete", 1, "Side Path", 9, 9),
    LocationData("EarlyDungeonComplete", 1, "Mt. Horn", 10, 10),
    LocationData("EarlyDungeonComplete", 1, "Rock Path", 11, 11),
    LocationData("EarlyDungeonComplete", 1, "Foggy Forest", 12, 12),
    LocationData("EarlyDungeonComplete", 1, "Forest Path", 13, 13),
    LocationData("EarlyDungeonComplete", 3, "Steam Cave", 16, 14),  # 3 subareas
    LocationData("EarlyDungeonComplete", 3, "Amp Plains", 19, 17),  # 3 subareas
    LocationData("EarlyDungeonComplete", 1, "Northern Desert", 20, 20),
    LocationData("EarlyDungeonComplete", 3, "Quicksand Cave", 23, 21),  # 3 subareas
    LocationData("EarlyDungeonComplete", 1, "Crystal Cave", 24, 24),
    LocationData("EarlyDungeonComplete", 2, "Crystal Crossing", 26, 25),  # 2 subareas
    LocationData("EarlyDungeonComplete", 1, "Chasm Cave", 27, 27),
    LocationData("EarlyDungeonComplete", 1, "Dark Hill", 28, 28),
    LocationData("EarlyDungeonComplete", 3, "Sealed Ruin", 31, 29),  # 3 subareas
    LocationData("EarlyDungeonComplete", 1, "Dusk Forest", 32, 32),
    LocationData("EarlyDungeonComplete", 1, "Deep Dusk Forest", 33, 33),
    LocationData("EarlyDungeonComplete", 1, "Treeshroud Forest", 34, 34),
    LocationData("EarlyDungeonComplete", 3, "Brine Cave", 37, 35),  # 3 subareas
    LocationData("BossDungeonComplete", 3, "Hidden Land", 40, 38),  # 3 subareas
    LocationData("BossDungeonComplete", 3, "Temporal Tower", 43, 41),  # 3 subareas
    LocationData("LateDungeonComplete", 2, "Mystifying Forest", 45, 44),  # start of extra levels
    LocationData("LateDungeonComplete", 1, "Blizzard Island", 46, 46),
    LocationData("LateDungeonComplete", 3, "Crevice Cave", 49, 47),  # 3 subareas
    LocationData("LateDungeonComplete", 1, "Surrounded Sea", 50, 50),
    LocationData("LateDungeonComplete", 3, "Miracle Sea", 53, 51),  # 3 subareas
    # LocationData("DungeonComplete", 8,  "Ice Aegis Cave", 60,  54),   # 8 subareas             we hate aegis cave. also it's kinda broken rn so we're gonna remove it for now
    LocationData("LateDungeonComplete", 1, "Mt. Travail", 62, 62),
    LocationData("LateDungeonComplete", 1, "The Nightmare", 63, 63),
    LocationData("LateDungeonComplete", 3, "Spacial Rift", 66, 64),  # 3 subareas
    LocationData("LateDungeonComplete", 3, "Dark Crater", 69, 67),  # 3 subareas
    LocationData("LateDungeonComplete", 2, "Concealed Ruins", 71, 70),  # 2 subareas
    LocationData("LateDungeonComplete", 1, "Marine Resort", 72, 72),
    LocationData("LateDungeonComplete", 2, "Bottomless Sea", 74, 73),  # 2 subareas
    LocationData("LateDungeonComplete", 2, "Shimmer Desert", 76, 75),  # 2 subareas
    LocationData("LateDungeonComplete", 2, "Mt. Avalanche", 78, 77),  # 2 subareas
    LocationData("LateDungeonComplete", 2, "Giant Volcano", 80, 79),  # 2 subareas
    LocationData("LateDungeonComplete", 2, "World Abyss", 82, 81),  # 2 subareas
    LocationData("LateDungeonComplete", 2, "Sky Stairway", 84, 83),  # 2 subareas
    LocationData("LateDungeonComplete", 2, "Mystery Jungle", 86, 85),  # 2 subareas
    LocationData("LateDungeonComplete", 1, "Serenity River", 87, 87),
    LocationData("LateDungeonComplete", 1, "Landslide Cave", 88, 88),
    LocationData("LateDungeonComplete", 1, "Lush Prairie", 89, 89),
    LocationData("LateDungeonComplete", 1, "Tiny Meadow", 90, 90),
    LocationData("LateDungeonComplete", 1, "Labyrinth Cave", 91, 91),
    LocationData("LateDungeonComplete", 1, "Oran Forest", 92, 92),
    LocationData("LateDungeonComplete", 1, "Lake Afar", 93, 93),
    LocationData("LateDungeonComplete", 1, "Happy Outlook", 94, 94),
    LocationData("LateDungeonComplete", 1, "Mt. Mistral", 95, 95),
    LocationData("LateDungeonComplete", 1, "Shimmer Hill", 96, 96),
    LocationData("LateDungeonComplete", 1, "Lost Wilderness", 97, 97),
    LocationData("LateDungeonComplete", 1, "Midnight Forest", 98, 98),
    LocationData("RuleDungeonComplete", 1, "Zero Isle North", 99, 99),
    LocationData("RuleDungeonComplete", 1, "Zero Isle East", 100, 100),
    LocationData("RuleDungeonComplete", 1, "Zero Isle West", 101, 101),
    LocationData("RuleDungeonComplete", 1, "Zero Isle South", 102, 102),
    LocationData("RuleDungeonComplete", 1, "Zero Isle Center", 103, 103),
    LocationData("RuleDungeonComplete", 1, "Destiny Tower", 104, 104),
    LocationData("RuleDungeonComplete", 1, "Oblivion Forest", 107, 107),
    LocationData("RuleDungeonComplete", 1, "Treacherous Waters", 108, 108),
    LocationData("RuleDungeonComplete", 1, "Southeastern Islands", 109, 109),
    LocationData("RuleDungeonComplete", 1, "Inferno Cave", 110, 110),
    LocationData("LateDungeonComplete", 12, "1st Station Pass", 122, 111),  # 12 subareas
    # Special Episode Dungeons
    LocationData("SpecialDungeonComplete", 5, "SE Star Cave", 127, 123),
    LocationData("SpecialDungeonComplete", 1,  "SE Murky Forest", 128,  128),
    LocationData("SpecialDungeonComplete", 1,  "SE Eastern Cave", 129,  129),
    LocationData("SpecialDungeonComplete", 3,  "SE Fortune Ravine", 132,  130),   # 3 subareas
    LocationData("SpecialDungeonComplete", 3,  "SE Barren Valley", 135,  133),   # 3 subareas
    LocationData("SpecialDungeonComplete", 1,  "SE Dark Wasteland", 136,  136),
    LocationData("SpecialDungeonComplete", 2,  "SE Temporal Tower", 138,  137),   # 2 subareas
    LocationData("SpecialDungeonComplete", 2,  "SE Dusk Forest", 140,  139),   # 2 subareas
    LocationData("SpecialDungeonComplete", 1,  "SE Spacial Cliffs", 141,  141),
    LocationData("SpecialDungeonComplete", 3,  "SE Dark Ice Mountain", 144,  142),   # 3 subareas
    LocationData("SpecialDungeonComplete", 1,  "SE Icicle Forest", 145,  145),
    LocationData("SpecialDungeonComplete", 3,  "SE Vast Ice Mountain", 148,  146),   # 3 subareas
    LocationData("SpecialDungeonComplete", 1,  "SE Southern Jungle", 149,  149),
    LocationData("SpecialDungeonComplete", 3,  "SE Boulder Quarry", 152,  150),   # 3 subareas
    LocationData("SpecialDungeonComplete", 1,  "SE Right Cave Path", 153,  153),
    LocationData("SpecialDungeonComplete", 1,  "SE Left Cave Path", 154,  154),
    LocationData("SpecialDungeonComplete", 3,  "SE Limestone Cavern", 157,  155),   # 3 subareas
    LocationData("SpecialDungeonComplete", 7,  "SE Spring Cave", 164,  158),   # 7 subareas
    LocationData("LateDungeonComplete", 1, "Star Cave", 174,  174),
    # Dojo Dungeons
    LocationData("DojoDungeonComplete", 1, "Dojo Normal/Fly Maze", 180, 180),  # 7 subareas
    LocationData("DojoDungeonComplete", 1, "Dojo Dark/Fire Maze", 181, 181),  # 7 subareas
    LocationData("DojoDungeonComplete", 1, "Dojo Rock/Water Maze", 182, 182),  # 7 subareas
    LocationData("DojoDungeonComplete", 1, "Dojo Grass Maze", 183, 183),  # 7 subareas
    LocationData("DojoDungeonComplete", 1, "Dojo Elec/Steel Maze", 184, 184),  # 7 subareas
    LocationData("DojoDungeonComplete", 1, "Dojo Ice/Ground Maze", 185, 185),  # 7 subareas
    LocationData("DojoDungeonComplete", 1, "Dojo Fight/Psych Maze", 186, 186),  # 7 subareas
    LocationData("DojoDungeonComplete", 1, "Dojo Poison/Bug Maze", 187, 187),  # 7 subareas
    LocationData("DojoDungeonComplete", 1, "Dojo Dragon Maze", 188, 188),  # 7 subareas
    LocationData("DojoDungeonComplete", 1, "Dojo Ghost Maze", 189, 189),  # 7 subareas
    #LocationData("RuleDungeonComplete", 1, "Dojo Final Maze", 191, 191),  # 7 subareas

    LocationData("Event", 0,  "Final Boss", 700, 0),
    # generic checks, right now just bag upgrades
    LocationData("ProgressiveBagUpgrade", 0, "Progressive Bag loc 1", 300, 0),
    LocationData("ProgressiveBagUpgrade", 0, "Progressive Bag loc 2", 301, 0),
    LocationData("ProgressiveBagUpgrade", 0, "Progressive Bag loc 3", 302, 0),
    LocationData("ProgressiveBagUpgrade", 0, "Progressive Bag loc 4", 303, 0),
    LocationData("ProgressiveBagUpgrade", 0, "Progressive Bag loc 5", 304, 0),

    LocationData("SEDungeonUnlock", 0, "Bidoof SE Location", 305, 0),
    LocationData("SEDungeonUnlock", 0, "Igglybuff SE Location", 306, 0),
    LocationData("SEDungeonUnlock", 0, "Sunflora SE Location", 307, 0),
    LocationData("SEDungeonUnlock", 0, "Team Charm SE Location", 308, 0),
    LocationData("SEDungeonUnlock", 0, "Grovyle + DusknoirSE Location", 309, 0),

    LocationData("ShopItem", 0, "Shop Item 1", 310, 0),
    LocationData("ShopItem", 0, "Shop Item 2", 311, 0),
    LocationData("ShopItem", 0, "Shop Item 3", 312, 0),
    LocationData("ShopItem", 0, "Shop Item 4", 313, 0),
    LocationData("ShopItem", 0, "Shop Item 5", 314, 0),
    LocationData("ShopItem", 0, "Shop Item 6", 315, 0),
    LocationData("ShopItem", 0, "Shop Item 7", 316, 0),
    LocationData("ShopItem", 0, "Shop Item 8", 317, 0),
    LocationData("ShopItem", 0, "Shop Item 9", 318, 0),
    LocationData("ShopItem", 0, "Shop Item 10", 319, 0),
    LocationData("SEDungeonUnlock", 0, "Team Name", 427, 0),


]

location_Dict_by_id: typing.Dict[int, LocationData] = {location.id: location for location in EOS_location_table}
