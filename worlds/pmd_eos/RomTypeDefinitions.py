from typing import List, NamedTuple


class SubXBitfield (NamedTuple):
    bitfield_bit_number: int
    subX_area: int
    subX_byte: int
    subX_bit_number: int
    flag_definition: str  # name
    prerequisites: List[str]
    default_item: str  # what item is normally there?

subX_table = [
SubXBitfield(0, 1, 0, 0, "Bag Upgrade 0", ["Clear Beach Cave"], "Bag Upgrade"),
SubXBitfield(1, 1, 0, 1, "Bag Upgrade 1", ["Mt. Bristle"], "Bag Upgrade"),
SubXBitfield(2, 1, 0, 2, "Bag Upgrade 2", ["Apple Woods"], "Bag Upgrade"),
SubXBitfield(3, 1, 0, 3, "Bag Upgrade 3", ["Steam Cave"], "Bag Upgrade"),
SubXBitfield(4, 1, 0, 4, "Bag Upgrade 4", ["Mystifying Forest"], "Bag Upgrade"),
SubXBitfield(5, 1, 0, 5, "Bidoof's SE Location", ["None"], "Bidoof's SE"),
SubXBitfield(6, 1, 0, 6, "Igglybuff's SE Location", ["None"], "Igglybuff's SE"),
SubXBitfield(7, 1, 0, 7, "Sunflora's SE Location", ["None"], "Sunflora's SE"),
SubXBitfield(8, 1, 1, 0, "Team Charm SE Location", ["None"], "Team Charm SE"),
SubXBitfield(9, 1, 1, 1, "Grovyle + Dusknoir SE location", ["Hidden Land"], "Grovyle + Dusknoir SE"),
SubXBitfield(10, 1, 1, 2, "Shop Item #1", ["Have money"], "Filler"),
SubXBitfield(11, 1, 1, 3, "Shop Item #2", ["Have money"], "Filler"),
SubXBitfield(12, 1, 1, 4, "Shop Item #3", ["Have money"], "Filler"),
SubXBitfield(13, 1, 1, 5, "Shop Item #4", ["Have money"], "Filler"),
SubXBitfield(14, 1, 1, 6, "Shop Item #5", ["Have money"], "Filler"),
SubXBitfield(15, 1, 1, 7, "Shop Item #6", ["Have money"], "Filler"),
SubXBitfield(16, 2, 0, 0, "Shop Item #7", ["Have money"], "Filler"),
SubXBitfield(17, 2, 0, 1, "Shop Item #8", ["Have money"], "Filler"),
SubXBitfield(18, 2, 0, 2, "Shop Item #9", ["Have money"], "Filler"),
SubXBitfield(19, 2, 0, 3, "Shop Item #10", ["Have money"], "Filler"),
SubXBitfield(20, 2, 0, 4, "Blue Goomi #1", ["Surrounded Sea ", " Manaphy Egg"], "Filler"),
SubXBitfield(21, 2, 0, 5, "Blue Goomi #2", ["Surrounded Sea"], "Filler"),
SubXBitfield(22, 2, 0, 6, "Manaphy Healed", ["Surrounded Sea ", " Miracle Sea"], "Filler"),
SubXBitfield(23, 2, 0, 7, "Manaphy's Gift", ["Defeat Dialga ", " Surrounded Sea"], "Manaphy"),
SubXBitfield(24, 2, 1, 0, "Manaphy's Discovery", ["Recruit Manaphy"], "Marine Resort"),
SubXBitfield(25, 2, 1, 1, "Uxie's Gift", ["Defeat Dialga ", " Steam Cave"], "Uxie"),
SubXBitfield(26, 2, 1, 2, "Mesprit's Gift", ["Defeat Dialga ", " Quicksand Cave"], "Mesprit"),
SubXBitfield(27, 2, 1, 3, "Azelf's Gift", ["Defeat Dialga ", " Crystal Crossing"], "Azelf"),
SubXBitfield(28, 2, 1, 4, "Dialga's Gift", ["Defeat Dialga ", " Temporal Tower"], "Dialga"),
SubXBitfield(29, 2, 1, 5, "Phione's Gift", ["Defeat Dialga ", " Manaphy Healed ", " Miracle Sea"], "Phione"),
SubXBitfield(30, 2, 1, 6, "Palkia's Gift", ["Defeat Dialga ", " Spacial Rift"], "Dialga"),
SubXBitfield(31, 2, 1, 7, "Aqua-Monica Location", ["Defeat Dialga ", " Secret Rank ", " Bottomless Sea"], "Instrument"),
SubXBitfield(32, 3, 0, 0, "Kyogre's Gift", ["Defeat Dialga ", " Secret Rank ", " Bottomless Sea"], "Kyogre"),
SubXBitfield(33, 3, 0, 1, "Terra Cymbal Location", ["Defeat Dialga ", " Secret Rank ", " Shimmer Desert"], "Instrument"),
SubXBitfield(34, 3, 0, 2, "Groudon's Gift", ["Defeat Dialga ", " Secret Rank ", " Shimmer Desert"], "Groudon"),
SubXBitfield(35, 3, 0, 3, "Icy Flute Location", ["Defeat Dialga ", " Secret Rank ", " Mt. Avalanche"], "Instrument"),
SubXBitfield(36, 3, 0, 4, "Articuno's Gift", ["Defeat Dialga ", " Secret Rank ", " Mt. Avalanche"], "Articuno"),
SubXBitfield(37, 3, 0, 5, "Fiery Drum Location", ["Defeat Dialga ", " Secret Rank ", " Giant Volcano"], "Instrument"),
SubXBitfield(38, 3, 0, 6, "Heatran's Gift", ["Defeat Dialga ", " Secret Rank ", " Giant Volcano"], "Heatran"),
SubXBitfield(39, 3, 0, 7, "Rock Horn Location", ["Defeat Dialga ", " Secret Rank ", " World Abyss"], "Instrument"),
SubXBitfield(40, 3, 1, 0, "Giratina's Gift", ["Defeat Dialga ", " Secret Rank ", " World Abyss"], "Giratina"),
SubXBitfield(41, 3, 1, 1, "Sky Melodica Location", ["Defeat Dialga ", " Secret Rank ", " Sky Stairway"], "Instrument"),
SubXBitfield(42, 3, 1, 2, "Rayquaza's Gift", ["Defeat Dialga ", " Secret Rank ", " Sky Stairway"], "Rayquaza"),
SubXBitfield(43, 3, 1, 3, "Grass Cornet Location", ["Defeat Dialga ", " Secret Rank ", " Mystery Jungle"], "Instrument"),
SubXBitfield(44, 3, 1, 4, "Mew's Gift", ["Defeat Dialga ", " Secret Rank ", " Mystery Jungle"], "Mew"),
SubXBitfield(45, 3, 1, 5, "Cresselia's Gift", ["Defeat Dialga"], "Cresselia"),
SubXBitfield(46, 3, 1, 6, "Shaymin's Gift", ["Defeat Dialga ", " Sky Peak Summit Cleared"], "Shaymin"),
SubXBitfield(47, 3, 1, 7, "Scizor's Gift", ["Crevice Cave"], "Secret Rank"),
SubXBitfield(48, 4, 0, 0, "Aqua-Monica Mission", ["Secret Rank"], "Bottomless Sea"),
SubXBitfield(49, 4, 0, 1, "Terra Cymbal Mission", ["Secret Rank"], "Shimmer Desert"),
SubXBitfield(50, 4, 0, 2, "Icy Flute Mission", ["Secret Rank"], "Mt. Avalanche"),
SubXBitfield(51, 4, 0, 3, "Fiery Drum Mission", ["Secret Rank"], "Giant Volcano"),
SubXBitfield(52, 4, 0, 4, "Rock Horn Mission", ["Secret Rank"], "World Abyss"),
SubXBitfield(53, 4, 0, 5, "Sky Melodica Mission", ["Secret Rank"], "Sky Stairway"),
SubXBitfield(54, 4, 0, 6, "Grass Cornet Mission", ["Secret Rank"], "Mystery Jungle"),
SubXBitfield(55, 4, 0, 7, "Unused", ["-"], "-"),
SubXBitfield(56, 4, 1, 0, "Unused", ["-"], "-"),
SubXBitfield(57, 4, 1, 1, "Unused", ["-"], "-"),
SubXBitfield(58, 4, 1, 2, "Unused", ["-"], "-"),
SubXBitfield(59, 4, 1, 3, "Unused", ["-"], "-"),
SubXBitfield(60, 4, 1, 4, "Unused", ["-"], "-"),
SubXBitfield(61, 4, 1, 5, "Unused", ["-"], "-"),
SubXBitfield(62, 4, 1, 6, "Unused", ["-"], "-"),
SubXBitfield(63, 4, 1, 7, "Unused", ["-"], "-"),
SubXBitfield(64, 5, 0, 0, "Unused", ["-"], "-"),
SubXBitfield(65, 5, 0, 1, "Unused", ["-"], "-"),
SubXBitfield(66, 5, 0, 2, "Unused", ["-"], "-"),
SubXBitfield(67, 5, 0, 3, "Unused", ["-"], "-"),
SubXBitfield(68, 5, 0, 4, "Unused", ["-"], "-"),
SubXBitfield(69, 5, 0, 5, "Unused", ["-"], "-"),
SubXBitfield(70, 5, 0, 6, "Unused", ["-"], "-"),
SubXBitfield(71, 5, 0, 7, "Unused", ["-"], "-"),
SubXBitfield(72, 5, 1, 0, "Unused", ["-"], "-"),
SubXBitfield(73, 5, 1, 1, "Unused", ["-"], "-"),
SubXBitfield(74, 5, 1, 2, "Unused", ["-"], "-"),
SubXBitfield(75, 5, 1, 3, "Unused", ["-"], "-"),
SubXBitfield(76, 5, 1, 4, "Unused", ["-"], "-"),
SubXBitfield(77, 5, 1, 5, "Unused", ["-"], "-"),
SubXBitfield(78, 5, 1, 6, "Unused", ["-"], "-"),
SubXBitfield(79, 5, 1, 7, "Unused", ["-"], "-"),
SubXBitfield(80, 6, 0, 0, "Unused", ["-"], "-"),
SubXBitfield(81, 6, 0, 1, "Unused", ["-"], "-"),
SubXBitfield(82, 6, 0, 2, "Unused", ["-"], "-"),
SubXBitfield(83, 6, 0, 3, "Unused", ["-"], "-"),
SubXBitfield(84, 6, 0, 4, "Unused", ["-"], "-"),
SubXBitfield(85, 6, 0, 5, "Unused", ["-"], "-"),
SubXBitfield(86, 6, 0, 6, "Unused", ["-"], "-"),
SubXBitfield(87, 6, 0, 7, "Unused", ["-"], "-"),
SubXBitfield(88, 6, 1, 0, "Unused", ["-"], "-"),
SubXBitfield(89, 6, 1, 1, "Unused", ["-"], "-"),
SubXBitfield(90, 6, 1, 2, "Unused", ["-"], "-"),
SubXBitfield(91, 6, 1, 3, "Unused", ["-"], "-"),
SubXBitfield(92, 6, 1, 4, "Unused", ["-"], "-"),
SubXBitfield(93, 6, 1, 5, "Unused", ["-"], "-"),
SubXBitfield(94, 6, 1, 6, "Unused", ["-"], "-"),
SubXBitfield(95, 6, 1, 7, "Unused", ["-"], "-"),
SubXBitfield(96, 7, 0, 0, "Unused", ["-"], "-"),
SubXBitfield(97, 7, 0, 1, "Unused", ["-"], "-"),
SubXBitfield(98, 7, 0, 2, "Unused", ["-"], "-"),
SubXBitfield(99, 7, 0, 3, "Unused", ["-"], "-"),
SubXBitfield(100, 7, 0, 4, "Unused", ["-"], "-"),
SubXBitfield(101, 7, 0, 5, "Unused", ["-"], "-"),
SubXBitfield(102, 7, 0, 6, "Unused", ["-"], "-"),
SubXBitfield(103, 7, 0, 7, "Unused", ["-"], "-"),
SubXBitfield(104, 7, 1, 0, "Unused", ["-"], "-"),
SubXBitfield(105, 7, 1, 1, "Unused", ["-"], "-"),
SubXBitfield(106, 7, 1, 2, "Unused", ["-"], "-"),
SubXBitfield(107, 7, 1, 3, "Unused", ["-"], "-"),
SubXBitfield(108, 7, 1, 4, "Unused", ["-"], "-"),
SubXBitfield(109, 7, 1, 5, "Unused", ["-"], "-"),
SubXBitfield(110, 7, 1, 6, "Unused", ["-"], "-"),
SubXBitfield(111, 7, 1, 7, "Unused", ["-"], "-"),
SubXBitfield(112, 8, 0, 0, "Unused", ["-"], "-"),
SubXBitfield(113, 8, 0, 1, "Unused", ["-"], "-"),
SubXBitfield(114, 8, 0, 2, "Unused", ["-"], "-"),
SubXBitfield(115, 8, 0, 3, "Unused", ["-"], "-"),
SubXBitfield(116, 8, 0, 4, "Unused", ["-"], "-"),
SubXBitfield(117, 8, 0, 5, "Unused", ["-"], "-"),
SubXBitfield(118, 8, 0, 6, "Unused", ["-"], "-"),
SubXBitfield(119, 8, 0, 7, "Unused", ["-"], "-"),
SubXBitfield(120, 8, 1, 0, "Unused", ["-"], "-"),
SubXBitfield(121, 8, 1, 1, "Unused", ["-"], "-"),
SubXBitfield(122, 8, 1, 2, "Unused", ["-"], "-"),
SubXBitfield(123, 8, 1, 3, "Unused", ["-"], "-"),
SubXBitfield(124, 8, 1, 4, "Unused", ["-"], "-"),
SubXBitfield(125, 8, 1, 5, "Unused", ["-"], "-"),
SubXBitfield(126, 8, 1, 6, "Unused", ["-"], "-"),
SubXBitfield(127, 8, 1, 7, "Team Name Location", ["Clear Beach Cave"], "Team Name Trap")
]
