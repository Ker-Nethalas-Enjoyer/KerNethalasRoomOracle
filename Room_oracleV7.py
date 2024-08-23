from random import randint
from random import choice

ker_str = str('⠀⠀             ⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⡀⢰⢀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
'⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⣇⣅⣿⣏⣩⣬⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
'⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀         ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣯⣿⣏⣽⣯⣏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
'⢀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣠⣄⣀⣀⣀⡀⠠⠤⠤⠤⣖⣻⡭⠶⠶⣭⣛⣲⠤⠤⠤⠄⣀⣀⣄⣀⣤⣄⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀\n'
'⠀⠈⠙⠟⠉⠤⢤⡤⣤⣤⢠⣤⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ⠀⠈⠉⠀⠤⢤⡤⣤⢍⣭⣭⠁⠀⠀⠀⠀⠈⠉⠉⠁  ⠤⢤⡄⠀⠀⠉⠁⠀⠀      ⠠⢤⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    ⠉⠿⠋\n'
' ⠀⠀⠀⠀⠀⢰⣇⢸⣿⣿⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   ⠀ ⠀⢰⣇⢸⣿⠊⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⢀⡆⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀    ⠀⠀ ⢹⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
'⠀⠀⠀⠀⠀⠀⢀⣸⣿⣿⣼⣏⠀⠈⣿⡏⢉⣿⠇⠈⣿⣯⠊⡿⠇ ⠀    ⢀⣸⣿ ⢸⣿⠀⠈⣿⡏⢉⣿⠇⠈⣿⡏⠁⣿⡏⢹⣿⠁⠈⢹⠿⠉⣿⡇ ⢸⣿⠈⣿⠏⢹⣿⠁⠈⢹⣿⠉⠿⡇⠀⠀⠀⠀⠀\n'
'⠀⠀⠀⠀⠀⠀⢈⣹⣿⣿ ⢹⣿⠀⠀⣿⡷⠋⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀  ⠀⠀⣨⣹⣿⠀⢸⣿⠀⠀⣿⡷⠋⠀⠀⠀⣿⡇⠀⠀⣿⡇⢸⣿⠀⠀⢠⣴⠊⣿⡇⠀⢸⣿⠀⠀⣤⡖⢹⣿⠀⠀⠘⠿⣶⣦⡀⠀⠀⠀⠀⠀\n'
'⠀⠀⠀⠀⠀⠀⠈⢸⣿⣿ ⢸⣿⠀⠀⣿⣇⠀⣤⡇⠀⣿⣇⠀⢀⠀⠀⠀⠀⠀ ⠀⠈⢸⣿⠀⢸⣿⠀⠀⣿⣇⠀⣤⡇⠀⣿⣇⠀⠀⠿⡇⢸⣿⠀⠀⣸⣿⡀⣿⠇⠀⢸⣿⠀⠀⣿⣇⢸⣿⠀⠀⣰⣶⡀⣿⡇⠀⠀⠀⠀⠀\n'
'⠀⠀⠀⠀⠀⠀⠀⠘⢿⠿ ⣸⢽⠀⠀⠈⡽⠓⠉⠀⠀⠙⠟⢠⠆⡔⠀⠐⠒⠀⠀⠀⠘⢯⠂⠘⣽⢠⠆⠈⢨⠛⠉⠀⠀⡝⠟⠀⠀⡵⠁⠈⡿⠄⠀⠘⠿⢿⠽⣀⣞⠀⠝⠃⠀⠉⠻⠋⠻⠆⠀⠈⠙⠟⠉⠀⠀⠀⠀⠀⠀\n'
)

D4 = str('D4')
D6 = str('D6')
D8 = str('D8')
D10 = str('D10')
D12 = str('D12')
D20 = str('D20')
D66 = str('D66')
D100 = str('D100')
fight = bool
lair_check_bool = False
overseer_bool = False
lair_bool = False
exit_bool = False
lair_count = 5
LX = D12
tension_die = str('?')
tension_bool = False
tension_check_bool = False
curr_tension = 3
TX = D8
tension_str = str('CHECK FOR TENSION DIE:\n'
                          '-----------------------\n'
                          f'{TX:^5} {'|':^6} {tension_die:>4}')
i = 0
j = 0
jj = 0
mod_bool = 0
creature_list = [
        'Abyssal Vexator',
        'Amalgam',
        'Armor Construct',
        'Astral Beast',
        'Bladewings',
        'Blood Stalker',
        'Bone Golem',
        'Bone Spiders',
        'Cavebound Leech',
        'Corpse Ants',
        'Death Sage',
        'Desiccated Cryptguards',
        'Dwerax',
        'Fangvine',
        'Flayed Knight',
        'Fleshmelt Slime',
        'Giant Spider',
        'Hive Larvae',
        'Hive Warrior',
        'Hollow Shambler',
        'Living Moss',
        'Necropede',
        'Netherfiend',
        'Plaguebringer',
        'Pyreborn',
        'Ratkin Marauders',
        'Razorjaw',
        'Reanimated Homunculus',
        'Rotwalkers',
        'Stone Warden',
        'Swarmer',
        'Tomb Crawler',
        'Umbra Fiend',
        'Unfettered Familiar',
        'Vaelorian Magus',
        'Vinekin',
        'Voidweaver',
        'Vorleg',
        'Wraithskull',
        'Wrath Elemental'
    ]
res_table_crea_list = ['Bladewings',
                       'Blightfang Rats',
                       'Bone Spiders',
                       'Death Sage',
                       'Cavebound Leech',
                       'Corpse Ants',
                       'Death Sage',
                       'Fangvine',
                       'Fleshmelt Slime',
                       'Giant Spider',
                       'Hive Larvae',
                       'Living Moss',
                       'Necropede',
                       'Swarmer',
                       'Tomb Crawler',
                       ]

import random
from random import choice
creature_str = str(choice(creature_list))



def res_table_crea_function(die_roll):
    resource_str = str('')
    resource_roll = die_roll(D10)
    if resource_roll <= 2:
        resource_str = str('Nothing')
    elif (resource_roll <= 6 and resource_roll >= 3):
        resource_str = str('1x Cooking Supply')
    elif (resource_roll <= 10 and resource_roll >= 7):
        resoucre_str = str('1x Crafting Supply')
    return resource_str


Hit_table_Arachnid = str('HIT LOCATION - ARACHNID\n'
                         f'{'-' * 20}\n'
                         f'{'1-2':^5} {'|':^3} {'Right Rear Leg':>12}\n'
                         f'{'3-4':^5} {'|':^3} {'Left Rear Leg':>12}\n'
                         f'{'5-6':^5} {'|':^3} {'Mid Right Leg':>12}\n'
                         f'{'7-8':^5} {'|':^3} {'Mid Left Leg':>12}\n'
                         f'{'9-10':^5} {'|':^3} {'Fore Right Leg':>12}\n'
                         f'{'11-12':^5} {'|':^3} {'Fore Left Leg':>12}\n'
                         f'{'13-14':^5} {'|':^3} {'Abdomen':>12}\n'
                         f'{'15-16':^5} {'|':^3} {'Front Right Leg':>12}\n'
                         f'{'17-18':^5} {'|':^3} {'Front Left Leg':>12}\n'
                         f'{'19-20':^5} {'|':^3} {'Cephalothorax':>12}\n')

Hit_table_Humanoid = str('HIT LOCATION - HUMANOID\n'
                         f'{'-' * 20}\n'
                         f'{'1-3':^5} {'|':^3} {'Right Leg':>12}\n'
                         f'{'4-6':^5} {'|':^3} {'Left Leg':>12}\n'
                         f'{'7-9':^5} {'|':^3} {'Abdomen':>12}\n'
                         f'{'10-12':^5} {'|':^3} {'Chest':>12}\n'
                         f'{'13-15':^5} {'|':^3} {'Left Arm':>12}\n'
                         f'{'16-18':^5} {'|':^3} {'Right Arm':>12}\n'
                         f'{'19-20':^5} {'|':^3} {'Head':>12}\n')

Hit_table_Insectoid = str('HIT LOCATION - INSECTOID\n'
                         f'{'-' * 20}\n'
                         f'{'1':^5} {'|':^3} {'Right Rear Leg':>12}\n'
                         f'{'2':^5} {'|':^3} {'Left Rear Leg':>12}\n'
                         f'{'3':^5} {'|':^3} {'Mid Right Leg':>12}\n'
                         f'{'4':^5} {'|':^3} {'Mid Left Leg':>12}\n'
                         f'{'5-9':^5} {'|':^3} {'Abdomen':>12}\n'
                         f'{'10-13':^5} {'|':^3} {'Thorax':>12}\n'
                         f'{'14':^5} {'|':^3} {'Right Front Leg':>12}\n'
                         f'{'15':^5} {'|':^3} {'Left Front Leg':>12}\n'
                         f'{'16-20':^5} {'|':^3} {'Head':>12}\n')

Hit_table_Quadruped = str('HIT LOCATION - QUADRUPED\n'
                         f'{'-' * 20}\n'
                         f'{'1-3':^5} {'|':^3} {'Right Hind Leg':>12}\n'
                         f'{'4-6':^5} {'|':^3} {'Left Hind Leg':>12}\n'
                         f'{'7-9':^5} {'|':^3} {'Hindquarters':>12}\n'
                         f'{'10-12':^5} {'|':^3} {'Forequarters':>12}\n'
                         f'{'13-15':^5} {'|':^3} {'Right Front Leg':>12}\n'
                         f'{'16-18':^5} {'|':^3} {'Left Front Leg':>12}\n'
                         f'{'19-20':^5} {'|':^3} {'Head':>12}\n')

Hit_table_Winged = str('HIT LOCATION - WINGED BEAST\n'
                         f'{'-' * 20}\n'
                         f'{'1':^5} {'|':^3} {'Right Leg':>12}\n'
                         f'{'2':^5} {'|':^3} {'Left Leg':>12}\n'
                         f'{'3':^5} {'|':^3} {'Abdomen':>12}\n'
                         f'{'4':^5} {'|':^3} {'Chest':>12}\n'
                         f'{'5-9':^5} {'|':^3} {'Right Wing':>12}\n'
                         f'{'10-13':^5} {'|':^3} {'Left Wing':>12}\n'
                         f'{'14':^5} {'|':^3} {'Right Arm':>12}\n'
                         f'{'15':^5} {'|':^3} {'Left Arm':>12}\n'
                         f'{'16-20':^5} {'|':^3} {'Head':>12}\n')

Hit_table_Serpentoid = str('HIT LOCATION - SERPENTOID\n'
                           f'{'-' * 16}\n'
                           f'{'1-17':^5} {'|':^3} {'Body':>8}\n'
                           f'{'18-20':^5} {'|':^3} {'Head':>8}\n')




room_desc_list = ['Rusty iron shackles hang from the walls, and the floor is littered with\n'
                  'the remains of those who suffered unspeakable agony.',

                  'This regal hall is filled with shattered marble thrones, a stark\n'
                  "reminder of the empire's fallen rulers and the broken legacy they left\n"
                  'behind.',

                  'Eerie whispers  ill the air in this dimly lit crypt, where the tormented\n'
                  "spirits of the empire's cursed rulers still roam in eternal restlessness.",

                  'The stone altar in the center of the room is covered in dried blood, a\n'
                  'chilling testament to the dark rituals that once took place here.',

                  'A vast network of burial niches houses the remains of countless\n'
                  'forgotten souls, their existence erased from history.',

                  'Chains of all sizes hang from the ceiling, the clinking sound echoing\n'
                  'like a haunting melody in this hall of imprisonment.',

                  'Sculptures of mournful figures adorn the walls, each seemingly\n'
                  'caught in an eternal state of sorrow and despair.',

                  'The room is perpetually shrouded in darkness, where even torches\n'
                  'struggle to dispel the oppressive gloom.',

                  'Tombstones and coffins line the walls, bearing the names of lovers\n'
                  "separated by death, forever longing for each other's embrace.",

                  'Useless trinkets and baubles lie scattered about, remnants of the\n'
                  'once-great Vaelorian Ascendancy now reduced to forgotten relics.',

                  'This room seems to have been blasted by a source of water for\n'
                  'millennia, since all the surfaces are smooth and slippery.',

                  'An opulent throne sits empty in the center of this chamber,\n'
                  "surrounded by dust and decay, a symbol of the empire's fallen glory.",

                  'Echoes of anguished cries reverberate through this room, as if the\n'
                  'walls themselves are weeping for the tragedies that unfolded within.',

                  'Foul, withered plants and skeletal trees twist and reach for sunlight\n'
                  'that will never touch them.',

                  'A pitch-black room that gives the illusion of extending infinitely\n'
                  'downward, leaving those who enter with an overwhelming sense of\n'
                  'dread.',

                  'This crypt room holds the remains of those cursed to eternal\n'
                  'damnation, their souls forever trapped in this unholy place.',

                  'A massive, ominous statue looms over the room, depicting a\n'
                  "malevolent deity once worshiped by the empire's rulers.",

                  'Ghostly apparitions drift through these halls, their faint whispers\n'
                  'offering cryptic warnings and messages.',

                  'An ancient stone altar dominates the room, surrounded by blood\n'
                  'stained grooves where countless offerings met their end.',

                  'This room houses the remains of traitors and turncoats, eternally\n'
                  'damned for their betrayal of the empire.',

                  'Dark, arcane symbols cover the walls, hinting at the dark rituals once\n'
                  'conducted within these unhallowed grounds.',

                  "The bones of the empire's most wicked are piled high in this macabre\n"
                  "display of death's inevitability.",

                  'An eerie ticking fills the air as an ancient, enchanted clock counts\n'
                  'down the minutes to oblivion.',

                  'Any sound uttered within this hall fades into nothingness, as if the\n'
                  'room devours all noise.',

                  'Broken vials, shattered beakers, and rotting experiments reveal an\n'
                  "alchemist's ill - fated pursuit of forbidden knowledge.",

                  'Ancient scrolls and tomes rest on dust-covered shelves. Touching any\n'
                  'of them quickly turns them into piles of dust.',

                  'The stench of death hangs heavy in this room. Judging by some\n'
                  'carvings, the Vaelorians disposed of their enemies in mass graves\n'
                  'right here.',

                  'A morbid altar stands before a statue of a martyr who endured\n'
                  'unimaginable pain in the name of faith.',

                  'The remains of a once-grand spire lie in ruin, a monument to a\n'
                  'forgotten hero of the Vaelorian Ascendancy.',

                  'As you enter this room, haunting visions and terrifying illusions\n'
                  'assault you.',

                  'Dark rituals once performed here have left an indelible mark on the\n'
                  'walls, perpetually tainted by the essence of necromancy.',

                  'The shadows of tormented souls replay their darkest moments in an\n'
                  'eternal loop, forever haunted by their past actions.',

                  'Ancient weapons and armor line the walls, too old and brittle to be of\n'
                  'any use to you.',

                  'The walls bear ghostly imprints of anguished faces, as if the room\n'
                  'captures the final moments of those who met a tragic end.',

                  'Shadows move independently from their sources, dancing across the\n'
                  'walls like malevolent spirits.',

                  "A still, black pool reflects the darkest aspects of one's soul, showing\n"
                  'the horrors hidden within.',

                  'Mirrors shattered into jagged pieces create a disorienting effect,\n'
                  'distorting reality and reflecting haunting images.',

                  'An eerie aura permeates this room, where the empire once sought\n'
                  'answers from a cryptic and enigmatic oracle.',

                  'Statues of macabre figures surround a central platform, where dark\n'
                  'ceremonies once called upon malevolent powers.',

                  'A large crack in the room’s floor reveals a deep, dark abysm.',

                  'This room holds within it an unholy shrine dedicated to dark forces.',

                  'No sound can be heard in this room, not even the slightest whisper,\n'
                  'creating an unsettling atmosphere of absolute quiet.',

                  'This seems to be the final resting place of an emperor who history has\n'
                  'forgotten, his name erased from all records.',

                  'Broken chandeliers hang from the ceiling, and tattered banners once\n'
                  'heralded celebrations now lay in ruin.',

                  'Heat emanates from this room, and you can see the glow of lava in a\n'
                  'corner, the viscous material dripping from a crack on the wall.',

                  'An eerie, dim light filters through an enchanted glass ceiling, casting\n'
                  'an otherworldly twilight over the room.',

                  'Mirrors made from dark, reflective obsidian distort your reflection,\n'
                  'your lightsource casting haunting shadows.',

                  'Shrines to deities long abandoned by worshippers now stand in\n'
                  'silence, their names etched into forgotten prayer tablets.',

                  'Ancient telescopes and stargazing instruments remain untouched,\n'
                  'though the stars they once observed have long changed.',

                  'A once-powerful empress was buried here, her empty sarcophagus\n'
                  'adorned with gilded glyphs.',

                  'The room is plagued by an unnatural, freezing chill that numbs the\n'
                  'bones as soon as you enter.',

                  'Broken vials and failed experiments litter the room, reminders of the\n'
                  'desperate and deadly alchemical pursuits.',

                  'An overgrown courtyard now serves as a graveyard, with tombstones\n'
                  'dotting the landscape where once joyous celebrations took place.',

                  'Twisted and grotesque sculptures rest on pedestals, each\n'
                  "representing the artist's descent into madness.",

                  'The apparitions of those who died seeking revenge are trapped in\n'
                  'this room, their anger seething for eternity.',

                  'Taxidermy displays of long-extinct creatures and monstrous beasts\n'
                  'line the walls, their glass eyes seemingly alive.',

                  'The faint sounds of mournful music fill the air, emanating from\n'
                  'unseen instruments in this haunted room.',

                  'This chamber once housed the living quarters of a family of servants.\n'
                  'Faint children’s drawings can be seen of the walls.',

                  'This room houses a shrine dedicated to a lunar deity. Its worshipers\n'
                  "once performed heinous acts under the cursed moon's glow.",

                  'A large crypt, where the sound of mourning and weeping echoes\n'
                  'endlessly.',

                  'A chamber once dedicated to studying the stars, now abandoned and\n'
                  'covered in dust.',

                  'Phantom weapons float in the air, suspended in an unsettling display\n'
                  'of ethereal power.',

                  'Plans for grand structures, some never built, while others bore\n'
                  'terrible secrets, now rest here with the remains of their creator.',

                  'Statues of once-lovely nymphs are now twisted and grotesque, \n'
                  'surrounded by thorns and brambles.',

                  'This once-imposing chamber is now decayed and crumbling, a\n'
                  "symbol of the empire's decline.",

                  'A series of arcane symbols that you’ve never encountered before\n'
                  'cover the walls of this chamber.',

                  'Phantom wails fill the air, as the spirits of wronged women lament\n'
                  'their tragic fates.',

                  'An ancient, corrupted forge where weapons were crafted from the\n'
                  'souls of the fallen.',

                  'The statues of weeping angels line this hall, their faces eternally\n'
                  'frozen in grief.',

                  'The resting place of an heir to the empire, whose lineage has been\n'
                  'lost to history.',

                  'The walls are adorned with eerie petrified faces that seem to whisper\n'
                  'secrets to those who listen.',

                  'This chamber is made entirely of black stone, and any light that\n'
                  'enters is quickly swallowed by its darkness.',

                  'An ornate stone chalice sits on an altar. It appears to have been fused\n'
                  'to it by some extreme heat.',

                  'This room’s walls are covered with the tattered remains of ancient\n'
                  'heraldic banners.',

                  'At the center of this room, a seemingly bottomless pit drops into the \n'
                  'darkness, its true depth a mystery that strikes fear into your heart.',

                  'An otherworldly mist fills the room, giving glimpses of fleeting,\n'
                  'forgotten dreams from the past.',

                  'A cursed oracle once dwelt here, their prophecies leading to doom\n'
                  'and despair for those who sought answers.',

                  'A dark and foreboding courtyard where twisted shadows play tricks\n'
                  'on the mind.',

                  'The room is filled with the remains of lovers forever entwined in \n'
                  'death, their skeletal hands locked in an eternal embrace.',

                  'An otherworldly chamber where the boundaries between\n'
                  'dimensions blur, allowing glimpses into distant realms.',

                  'Horrifying paintings and sculptures depict scenes of unimaginable\n'
                  'suffering and torment.',

                  'This room has a well on a corner, but the water within it is clearly\n'
                  'tainted with an eerie glow.',

                  'This chamber is completely covered in fungi and mold of all kinds,\n'
                  'making every step feel as if you’re walking on a thick rug.',

                  'Small, empty cells line the walls of this room.',

                  'The walls are adorned with macabre paintings depicting brutal\n'
                  'executions and violent sacrifices.',

                  'Sealed off for centuries, this room contains unspeakable horrors that \n'
                  'were best left undisturbed.',

                  'An eerie fountain still trickling water is at the center of the room, a \n'
                  'peaceful, almost out of place view.',

                  'Disorienting illusions assault you momentarily as you step into this \n'
                  'room, showing you images of your past.',

                  'This room was once a treasure vault filled with riches, but it has long \n'
                  'since been ransacked.',

                  'A once-lavish parlor now lies in ruin, its grandeur replaced by decay\n'
                  'and the stench of death.',

                  'Rotten piles of furniture and rusted utensils are all you can see in this\n'
                  'room.',

                  'The walls are covered in soot and fire marks, clearly indicating that a \n'
                  'great fire took place here.',

                  'This room is completely empty, except for a thick layer of dust. A set \n'
                  'of human footprints can be seen across the room.',

                  'As you enter this hall you feel an overwhelming sense of \n'
                  'hopelessness, as if all optimism is slowly being drained from your\n'
                  'heart.',

                  'A chamber adorned with gold and jewels. A closer look reveals them \n'
                  'to be just paint and glass.',

                  'A once-revered shrine now stands in darkness, forgotten by all but \n'
                  'malevolent entities.',

                  'Statues of ancient warriors stand guard, their once-pristine surfaces \n'
                  'now marred by crimson stains.',

                  'Old iron ingots are piled in a corner of this room, each one of them \n'
                  'marked with the seal of an ancient house.',

                  'An unnatural wind seems to be constantly coming out of this room, \n'
                  'violently flapping your clothes and gear around you.',

                  'An unquenchable, ghostly flame flickers and dances, casting eerie \n'
]

corr_desc_list = ['The air is heavy with ancient dust, and the walls are lined with\n '
                   '\tcobwebs. The faint echoes of distant footsteps can be heard.',

                   'Flickering torches cast eerie shadows on the stone walls. The air is\n '
                   '\tdamp, and the occasional drip of water can be heard.',

                   'The tunnel is '
                   'barely wide enough for a single person to pass through. \n\tThe walls are'
                   'lined with ancient burial niches, some of which have\n\tbeen disturbed.',

                   'Thick moss covers the damp stone walls, giving the corridor and eerie\n'
                   '\tgreen glow. The sound of water dripping echoes throughout.',

                   'The passage is partially blocked by a cave-in, with rubble and debris \n'
                   '\tscattered across the floor. Dim light filters through cracks in the\n'
                   '\tceiling.',

                   'The walls are adorned with elaborate tomb reliefs and carved epitaphs.\n'
                   '\tThe air feels heavy with the presence of the long-departed.',

                   'The narrow stone hall twists and turns, disappearing into darkness.\n'
                   '\tThe hall seems to have a slight downwards inclination, and it feels\n'
                   '\tworn and slippery',

                   'The air here is stale, and the sound of rats scurrying can be heard in\n '
                   '\tthe distance.',

                   'An eerie silence fills this corridor, broken only by the faint whispers\n'
                   '\tof long-dead spirits. The air is heavy with an otherworldly stillness.',

                   'Strange luminescent fungi cover the walls, casting an ethereal glow.\n'
                   '\tThe tunnel twists and turns, creating an unsettling sense of \n'
                   '\tdisorientation.',

                   'This wide corridor is lined with towering statues and ornate \n'
                   '\tsarcophagi. Faded tapestries hang from the ceiling, telling stories of '
                   '\tancient rulers.',

                   'The tunnel is partially submerged in water, with small ripples \n'
                   '\tdisturbing its still surface. The faint odor of decay permeates the air.',

                   'A hidden aclove of branches, off from the main passage, housing a\n'
                   '\tforgotten altar or lost shrine. Dust-covered offerings lie\n'
                   '\tundisturbed.',

                   'Strange symbols are etched into the walls of this hall, possibly\n'
                   '\tindicating directions.',

                   'The walls of this tunnel bear scorch marks, evidence of past fire\n'
                   '\tor magical explosions. The air carries a faint smell of burnt wood\n'
                   '\tand stone.',

                   'Time and decay have taken their toll on this corridor, with crumbling\n'
                   '\twalls and ceilings. It feels unstable and likely to collapse.',

                   'Faint whispers and hushed voices fill the air, voices echoing throughout\n'
                   '\ttime.',

                   'The stench of decay is overpowering in this tunnel, infested with\n'
                   '\travenous vermin that lurk in the shadows',

                   'Intricate carvings adorn the walls, depicting scenes of ancient rituals\n'
                   '\tand funerary rites. The air is heavy with a sense of solemnity and\n'
                   '\treverence.'

                   'The corridor seems to shimmer with an otherworldly glow.\n'
                   '\tTransparent figures of long-dead souls can be seen drifting\n'
                   '\tthrough the walls, oblivious to the living.'
                   ]
damage_table = str('DIE ROLL  | DAMAGE DEALT\n'
                   f'{'-------------------------':<1}\n'
                   f'{'1':^8} {'|':^3} {0:>5}\n'
                   f'{'2-4':^8} {'|':^3} {1:>5}\n'
                   f'{'5-7':^8} {'|':^3} {2:>5}\n'
                   f'{'8-9':^8} {'|':^3} {3:>5}\n'
                   f'{'10+':^8} {'|':^3} {4:>5}\n'
                   )
DC_table = str('DIFFICULTY | MODIFIER\n'
               f'{'1':^8} {'|':^3} {'+30':>4}'
                f'{'2':^8} {'|':^3} {'+20':>4}'
                f'{'3':^8} {'|':^3} {'+10':>4}'
                f'{'4-5':^8} {'|':^3} {'+0':>4}'
                f'{'6':^8} {'|':^3} {'-10':>4}'
                f'{'7':^8} {'|':^3} {'-20':>4}'
                f'{'8':^8} {'|':^3} {'-30':>4}'
               )
DC_gen_list = ['+30','+20','+10','+0','+0', '-10', '-20', '-30']


crea_trait_list = []
TRAIT = []
room_desc_str = str(choice(room_desc_list))
corr_desc_str = str(choice(corr_desc_list))

def die_roll(DX):
    die_roll = True
    from random import randint
    if DX == str('D100'):
        value = randint(1, 100)
        if (value % 11 == 0) or (value == 100):
            print('C R I T I C A L \n'
                  'R O L L\n')
    elif DX == str('D66'):
        value = ((randint(1,6) * 10) + randint(1,6))
    elif DX == str('D20'):
        value = randint(1, 20)
    elif DX == str('D12'):
        value = randint(1,12)
    elif DX == str('D10'):
        value = randint(1, 10)
    elif DX == str('D8'):
        value = randint(1, 8)
    elif DX == str('D6'):
        value = randint(1, 6)
    elif DX == str('D4'):
        value = randint(1, 4)
    print(f'\t\t\t\t\t\t{DX} Rolled!! Value is {value}!!!')
    return int(value)

###DC GEN DOESNT WORK#####
def dc_gen(die_roll):
    dc_c = str(die_roll(D8))
    if dc_c == '1':
        dc_check = str('+30')
    elif dc_c == '2':
        dc_check = str('+20')
    elif dc_c == '3':
        dc_check = str('+10')
    elif dc_c == '4' or '5':
        dc_check = str('+0')
    elif dc_c == '6':
        dc_check = str('-10')
    elif dc_c == '7':
        dc_check = str('-20')
    elif dc_c == '8':
        dc_check = str('-30')
    return dc_check
###CREATURE STAT GENERATOR#####
mod_creature_str = str('')
def creature_mod_gen(mod_count, creature_str):
    while mod_count != 0:
        crea_mod_roll = die_roll(D66)
        if crea_mod_roll == 11:
            mod_creature_str = str('Resistant ' + f'{creature_str}')
            crea_trait_list.append(str('Resistant'))
            mod_count -= 1
        elif crea_mod_roll == 12:
            mod_creature_str = str('Elemental Misalignment ' + f'{creature_str}')
            crea_trait_list.append('Elemental')
            mod_count -= 1
        elif crea_mod_roll == 13:
            mod_creature_str = str('Reversed Affinity ' + f'{creature_str}')
            crea_trait_list.append('Reversed')
            mod_count -= 1
        elif crea_mod_roll == 14:
            mod_creature_str = str('Armored ' + f'{creature_str}')
            crea_trait_list.append('Armored')
            mod_count -= 1
        elif crea_mod_roll == 15:
            mod_creature_str = str('Suppression Field ' + creature_str)
            crea_trait_list.append('Suppression')
            mod_count -= 1
        elif crea_mod_roll == 16:
            mod_creature_str = str('Draining Spirit' + creature_str)
            crea_trait_list.append('Draining')
            mod_count -= 1
        elif crea_mod_roll == 21:
            mod_creature_str = str('Detonating ' + creature_str)
            crea_trait_list.append('Detonating')
            mod_count -= 1
        elif crea_mod_roll == 22:
            mod_creature_str = str('Spoiled ' + creature_str)
            crea_trait_list.append('Spoiled')
            mod_count -= 1
        elif crea_mod_roll == 23:
            mod_creature_str = str('Alert ' + creature_str)
            crea_trait_list.append('Alert_mod')
            mod_count -= 1
        elif crea_mod_roll == 24:
            mod_creature_str = str('Resilient ' + creature_str)
            crea_trait_list.append('Resilient')
            mod_count -= 1
        elif crea_mod_roll == 25:
            mod_creature_str = str('Strong ' + creature_str)
            crea_trait_list.append('Strong')
            mod_count -= 1
        elif crea_mod_roll == 26:
            mod_creature_str = str('Vital ' + creature_str)
            crea_trait_list.append('Vital')
            mod_count -= 1
        elif crea_mod_roll == 31:
            mod_creature_str = str('Skilled ' + creature_str)
            crea_trait_list.append('Skilled')
            mod_count -= 1
        elif crea_mod_roll == 32:
            mod_creature_str = str('Magic Void ' + creature_str)
            crea_trait_list.append('Magic')
            mod_count -= 1
        elif crea_mod_roll == 33:
            mod_creature_str = str('Vigilant ' + creature_str)
            crea_trait_list.append(['Vigilant', 'Alert'])
            mod_count -= 1
        elif crea_mod_roll == 34:
            mod_creature_str = str('Disturbing ' + creature_str)
            crea_trait_list.append(['Disturbing', 'Frightening'])
            mod_count -= 1
        elif crea_mod_roll == 35:
            mod_creature_str = str('Terrifying ' + creature_str)
            crea_trait_list.append(['Terrifying', 'Horrifying'])
            mod_count -= 1
        elif crea_mod_roll == 36:
            mod_creature_str = str('Rending ' + creature_str)
            crea_trait_list.append(['Rending', 'Penetrating(1)'])
            mod_count -= 1
        elif crea_mod_roll == 41:
            mod_creature_str = str('Relentless ' + creature_str)
            crea_trait_list.append(['Relentless', 'Savage'])
            mod_bool -= 1
        elif crea_mod_roll == 42:
            mod_creature_str = str('Toxic ' + creature_str)
            crea_trait_list.append(['Toxic', 'Venomous'])
            mod_count -= 1
        elif crea_mod_roll == 43:
            mod_creature_str = str('Acidic Blood ' + creature_str)
            crea_trait_list.append('Acidic')
            mod_count -= 1
        elif crea_mod_roll == 44:
            mod_creature_str = str('Undying ' + creature_str)
            crea_trait_list.append('Undying')
            mod_count -= 1
        elif crea_mod_roll == 45:
            mod_creature_str = str('Phasing ' + creature_str)
            crea_trait_list.append('Phasing')
            mod_count -= 1
        elif crea_mod_roll == 46:
            mod_creature_str = str('Vampiric ' + creature_str)
            crea_trait_list.append('Vampiric')
            mod_count -= 1
        elif crea_mod_roll == 51:
            mod_creature_str = str('Raging ' + creature_str)
            crea_trait_list.append('Raging')
            mod_count -= 1
        elif crea_mod_roll == 52:
            mod_creature_str = str('Corrosive ' + creature_str)
            crea_trait_list.append('Corrosive')
            mod_count -= 1
        elif crea_mod_roll == 53:
            mod_creature_str = str('Enfeebling ' + creature_str)
            crea_trait_list.append('Enfeebling')
            mod_count -= 1
        elif crea_mod_roll == 54:
            mod_creature_str = str('Reaper ' + creature_str)
            crea_trait_list.append('Reaper')
            mod_count -= 1
        elif crea_mod_roll == 55:
            mod_creature_str = str('Thieving ' + creature_str)
            crea_trait_list.append('Thieving')
            mod_count -= 1
        elif crea_mod_roll == 56:
            mod_creature_str = str('Lucky ' + creature_str)
            crea_trait_list.append('Lucky')
            mod_bool -= 1
        elif crea_mod_roll == 61:
            mod_creature_str = str('Aether Syphon ' + creature_str)
            crea_trait_list.append('Aether')
            mod_bool -= 1
        elif crea_mod_roll == 62:
            mod_creature_str = str('Reflective ' + creature_str)
            crea_trait_list.append('Reflective')
            mod_bool -= 1
        elif crea_mod_roll == 63:
            mod_creature_str = str('Impervious ' + creature_str)
            crea_trait_list.append('Impervious')
            mod_bool -= 1
        elif crea_mod_roll == 64:
            mod_creature_str = str('Quickened ' + creature_str)
            crea_trait_list.append('Quickened')
            mod_bool -= 1
        elif crea_mod_roll == 65:
            mod_creature_str = str('Unblockable ' + creature_str)
            crea_trait_list.append('Unblockable')
            mod_count -= 1
        elif crea_mod_roll == 66:
            mod_creature_str = str('Legendary '+ creature_str)
            crea_trait_list.append('Legendary')
            mod_count = (mod_count + 2)
            mod_count -= 1
    return mod_creature_str, crea_trait_list

def creature_trait_gen(creature_str):
    #### creature stat list first line = TYPE, NUMBER, AWARENESS, ENDURANCE, ATHLETICS, HEALTH
    #### second line = HIT LOCATION, ARMOR, COMBAT SKILL, MAGIC RESISTANCE, SPOILS
    crea_trait_list = []
    if creature_str == str('Abyssal Vexator'):
        crea_trait_list.append(str('Frightening'))
    elif creature_str == str('Amalgam'):
        crea_trait_list.append(str('Frightening'))
        crea_trait_list.append(str('Undead'))
    elif creature_str == str('Armor Construct'):
        crea_trait_list.append(str('Penetrating(1)'))
    elif creature_str == str('Astral Beast'):
        crea_trait_list.append('Penetrating(1)')
    elif creature_str == str('Bladewings'):
        crea_trait_list.append(str('Swift'))
    elif creature_str == str('Bloodstalker'):
        crea_trait_list.append(str('Penetrating(1)'))
    elif creature_str == str('Blightfang Rats'):
        crea_trait_list.append(str('Pack'))
    elif creature_str == str('Bone Golem'):
        crea_trait_list.append(str('Penetrating(1)'))
        crea_trait_list.append(str('Undead'))
    elif creature_str == str('Bone Spiders'):
        crea_trait_list.append(str('Undead'))
    elif creature_str == str('Cavebound Leech'):
        crea_trait_list.append(str('Penetrating(1)'))
        crea_trait_list.append(str('Alert'))
    elif creature_str == str('Corpse Ants'):
        crea_trait_list.append(str('Penetrating(1)'))
        crea_trait_list.append(str('Pack'))
    elif creature_str == str('Death Sage'):
        crea_trait_list.append(str('Undead'))
        crea_trait_list.append(str('Horrifying'))
    elif creature_str == str('Desiccated Cryptguards'):
        crea_trait_list.append(str('Undead'))
    elif creature_str == str('Dwerax'):
        crea_trait_list.append(str('Frightening'))
        crea_trait_list.append(str('Alert'))
    elif creature_str == str('Fangvine'):
        crea_trait_list.append(str('None'))
    elif creature_str == str('Flesh Eater'):
        crea_trait_list.append(str('Frightening'))
    elif creature_str == str('Fleshmelt Slime'):
        crea_trait_list.append(str('Undead'))
    elif creature_str == str('Giant Spider'):
        crea_trait_list.append(str('Penetrating(1)'))
        crea_trait_list.append(str('Alert'))
    elif creature_str == str('Hive Larvae'):
        crea_trait_list.append(str('Penetrating(1)'))
    elif creature_str == str('Hive Warrior'):
        crea_trait_list.append(str('None'))
    elif creature_str == str('Hollow Shambler'):
        crea_trait_list.append(str('Undead'))
    elif creature_str == str('Living Moss'):
        crea_trait_list.append(str('Undead'))
    elif creature_str == str('Necropede'):
        crea_trait_list.append(str('Venomous'))
        crea_trait_list.append(str('Undead'))
    elif creature_str == str('Netherfiend'):
        crea_trait_list.append(str('Frightening'))
    elif creature_str == str('Plaguebringer'):
        crea_trait_list.append(str('Frightening'))
        crea_trait_list.append(str('Undead'))
        crea_trait_list.append(str('Venomous'))
    elif creature_str == str('Pyreborn'):
        crea_trait_list.append(str('Restored by Fire Damage'))
        crea_trait_list.append(str('Vulnerable to Water Damage'))
    elif creature_str == str('Ratkin Marauders'):
        crea_trait_list.append(str('None'))
    elif creature_str == str('Razorjaw'):
        crea_trait_list.append(str('Penetrating(2)'))
    elif creature_str == str('Reanimated Homunculus'):
        crea_trait_list.append(str('Undead'))
    elif creature_str == str('Rotwalkers'):
        crea_trait_list.append(str('Undead'))
        crea_trait_list.append(str('Frightening'))
    elif creature_str == str('Skeletal Horrors'):
        crea_trait_list.append(str('Undead'))
        crea_trait_list.append(str('Frightening'))
    elif creature_str == str('Stone Warden'):
        crea_trait_list.append(str('Restored by Earth Damage'))
        crea_trait_list.append(str('Vulnerable to Air Damage'))
    elif creature_str == str('Swarmer'):
        crea_trait_list.append(str('Penetrating(1)'))
        crea_trait_list.append(str('Venomous'))
    elif creature_str == str('Tomb Crawler'):
        crea_trait_list.append(str('Venomous'))
    elif creature_str == str('Umbra Fiend'):
        crea_trait_list.append(str('Frightening'))
        crea_trait_list.append(str('Reistant to all Physical non-Magical Damage'))
    elif creature_str == str('Unfettered Familiar'):
        crea_trait_list.append(str('Resistant to all Physical, non-Magical Damage'))
    elif creature_str == str('Vaelorian Magus'):
        crea_trait_list.append(('Undead'))
    elif creature_str == str('Vinekin'):
        crea_trait_list.append(str('None'))
    elif creature_str == str('Voidweaver'):
        crea_trait_list.append(str('Resistant to all Physical, non-Magical Damage'))
    elif creature_str == str('Vorleg'):
         crea_trait_list.append(str('Penetrating(1)'))
         crea_trait_list.append(str('Alert'))
         crea_trait_list.append(str('Venomous'))
    elif creature_str == str('Wraithskull'):
        crea_trait_list.append(str('Undead'))
        crea_trait_list.append(str('Frightening'))
    elif creature_str == str('Wrath Elemental'):
        crea_trait_list.append(str('Swift'))
    return crea_trait_list

def crea_trait_reader(crea_trait_list):
    trait_read_list = []
    for element in crea_trait_list:
        if element == str('Acidic'):
            trait_read_list.append(str("""ACIDIC BLOOD:\n \tEach time the Creature is damaged, it\n\
                                        \t\tdeals D4 - 1 Acid Damage to the PC and their allies. +30 XP"""))
            crea_trait_list.remove(str("""Acidic"""))
        if element == str("""Aether"""):
            trait_read_list.append(str("""AETHER SYPHON:\n \tThis Creature drains 1 Aether per round\n\
            from the PC. +15 XP"""))
            crea_trait_list.remove(str("""Aether"""))
        if element == str('Alert'):
            trait_read_list.append(str('ALERT:\n \tThis creature cannot be surprised in any way'))
            crea_trait_list.remove('Alert')
        if element == str('Alert_mod'):
            trait_read_list.append(str("""ALERT:\n \tCreature's Awareness is increased by +10, +10 XP"""))
            crea_trait_list.remove('Alert_mod')
        if element == str('Armored'):
            trait_read_list.append(str("""ARMORED:\n \tThis Creature gains 1 Armor on a random body part. +15 XP"""))
            crea_trait_list.remove("""Armored""")
        if element == str("""Corrosive"""):
            trait_read_list.append(str("""CORROSIVE:\n \tEvery time this Creature strikes its target on\n\
                                        \tan armored body part, it triggers an Intergrity check. +15 XP"""))
            crea_trait_list.remove("""Corrosive""")
        if element == str("""Detonating"""):
            trait_read_list.append(str("""DETONATING:\n \tWhen defeated, this Creature explodes. Characters\n\
            must pass                   \ta Magic Resistance check, or suffer 2D6 Arcane Damage. +20 XP"""))
            crea_trait_list.remove("""Detonating""")
        if element == str("""Disturbing"""):
            trait_read_list.append("""DISTURBING:\n \tThis Creature gains the FRIGHTENING trait. +20 XP""")
            crea_trait_list.remove("""Disturbing""")
        if element == str("""Draining"""):
            trait_read_list.append(str("""DRAINING SPIRIT:\n \tThe cost of Aether-based Abilities is increase by 1. +15 XP"""))
            crea_trait_list.remove("""Draining""")
        if element == str("""Elemental"""):
            trait_read_list.append(str("""ELEMENTAL MISALIGNMENT:\n \tThe creature Immune to a type of Damage, but Vulnerable\n\
                                        \tto a different one. Roll twice on the Damage Type table(PAGE 206). +20 XP"""))
            crea_trait_list.remove(str("""Elemental"""))
        if element == str("""Enfeebling"""):
            trait_read_list.append(str("""ENFEEBLING:\n \tEach time the creature damages its opponent, their\n\
                                        \tcombat skills are reduced by 10 until the end of combat. +30 XP"""))
            crea_trait_list.remove(str("""Enfeebling"""))
        if element == str('Frightening'):
            trait_read_list.append(str(
                'FRIGHTENING:\n'
                '\tThis creature requires a successful Resolve check at the start of each of \n'
                '\tyour turns, for as long as the creature remains alive or in the same rooom.\n'
                '\tFailure causes 1 Sanity loss. Only one check is needed for one room.'
            ))
            crea_trait_list.remove('Frightening')
        if element == str('Horrifying'):
            trait_read_list.append(str("""HORRIFYING:\n \tThis creature requires a successful Resolve check at the start \
                                        start of each of\n \tyour turns, for as long as the creature remains alive or\
                                        in the same room.\n \tFailure causes 2 Sanity loss."""))
            crea_trait_list.remove(str("""Horrifying"""))
        if element == str("""Impervious"""):
            trait_read_list.append(str("""IMPERVIOUS:\n \tThis Creature is immune to all conditions +50 XP"""))
            crea_trait_list.remove(str("""Impervious"""))
        if element == str("""Lucky"""):
            trait_read_list.append(str("""LUCKY:\n \tThis Creature cannot fumble; instead, all doubles rolled by it\n\
                                        \tare considered a critical strike. +10 XP"""))
            crea_trait_list.remove("""Lucky""")
        if element == str("""Magic"""):
            trait_read_list.append("""MAGIC VOID:\n \tIncrease the Creature's Magic Resistance by +10. +10 XP""")
            crea_trait_list.remove("""Magic""")
        if element == str('Pack'):
            trait_read_list.append(str(
                                    'PACK:\n'
                                    '\tThese creatures receive +5 Combat Skill for each other \n'
                                    '\tPack creature still alive in the room.'))
            crea_trait_list.remove('Pack')
        if (element == str('Penetrating(1)')) or (element == str('Penetrating(2)')):
            trait_read_list.append(str('PENETRATING(X):\n'
                                   "\tThis creature's attacks ignore an amount of armor equal\n"
                                   "\tto (X)"))
        if element == str("""Phasing"""):
            trait_read_list.append(str("""PHASING:\n \tThe creature phases out of reality at the end of each of its\n
                                        \tturns, becoming CONCEALED(requires a successful Perception check to hit) +25 XP"""))
            crea_trait_list.remove(str("""Phasing"""))
        if element == str("""Quickened"""):
            trait_read_list.append(str("""QUICKENED:\n \tThis Creature gets an extra turn every round. +50 XP"""))
            crea_trait_list.remove(str("""Quickened"""))
        if element == str("""Raging"""):
            trait_read_list.append(str("""RAGING:\n \tWhen the Creature loses half of its maximum Health\n
                                        \t(rounding up), its Attack Skill of increase by 10. +15 XP"""))
            crea_trait_list.remove(str("""Raging"""))
        if element == str("""Reaper"""):
            trait_read_list.append(str("""REAPER:\n \tThis Creature's attacks deal +D4 Damage once its target is\n\
                                        \tbelow half its max Toughness. +15 XP"""))
            crea_trait_reader.remove(str("""Reaper"""))
        if element == str("""Reflective"""):
            trait_read_list.append(str("""REFLECTIVE:\n \tEach time the creature receives damage, its next attack\n
                                        deals an extra D6 Damage. +20 XP"""))
            crea_trait_list.remove(str("""Reflective"""))
        if element == str("""Relentless"""):
            trait_read_list.append(str("""This Creatue gains the Savage Trait. +30 XP"""))
            crea_trait_list.remove(str("""Relentless"""))
        if element == str("""Rending"""):
            trait_read_list.append(str("""RENDING:\n \tThe creature gains the PENETRATING(1) Trait. +20 XP"""))
            crea_trait_list.remove(str("""Rending"""))
        if element == str("""Resilient"""):
            trait_read_list.append(str("""RESILIENT:\n \tIncreases the Creature's Endurance by +10. +10 XP"""))
            crea_trait_list.remove(str("""Resilient"""))
        if element == str("""Reversed"""):
            trait_read_list.append(str("""REVERSED AFFINITY\n \tThe Creature becomes Restored by a type of Damage,\n\
                                        \tbut Vulerable by a different one. Roll twice on the Damge Type table(Page 206) +20 XP"""))
            crea_trait_list.remove(str("""Reversed"""))
        if element == str('Savage'):
            trait_read_list.append(str("""SAVAGE:\n \tCharacters cannot parry with Combat Skills, can only use Dodge."""))
            crea_trait_list.remove(str("""Savage"""))
        if element == str("""Skilled"""):
            trait_read_list.append(str("""SKILLED:\n \tIncrease the Creature's Combat Skill by +10. +10 XP."""))
            crea_trait_list.remove(str("""Skilled"""))
        if element == str("""Spoiled"""):
            trait_read_list.append(str("""SPOILED:\n \tWhen defeated, this creature grants no loot. +20 XP"""))
            crea_trait_list.remove(str("""Spoiled"""))
        if element == str("""Strong"""):
            trait_read_list.append(str("""STRONG:\n \tIncrease the Creature's Athletics by 10. +10 XP"""))
            crea_trait_list.remove("""Strong""")
        if element == str("""Suppression"""):
            trait_read_list.append("""SUPPRESSION FIELD:\n \tAether-fueled Abilities do not work in the \n
                                    \tpresence of this creature. +40 XP""")
            crea_trait_list.remove(str("""Suppression"""))
        if element == str('Swift'):
            trait_read_list.append(str('SWIFT:\n'
                                   '\tThis creature ignores all negative Reaction modifiers.'))
            crea_trait_list.remove('Swift')
        if element == str("""Toxic"""):
            trait_read_list.append(str("""TOXIC:\n \tThe Creature gains the VENOMOUS Trait. +15 XP"""))
            crea_trait_list.remove("""Toxic""")
        if element == str("""Thieving"""):
            trait_read_list.append(str("""THIEVING:\n \tThe Creature steals 20 Coins each time it deals Damage.\n\
                                        \tAt the end of combat, only 50% of the total sum stolen is recoverd. +10 XP"""))
            crea_trait_list.remove(str("""Thieving"""))
        if element == str('Undead'):
            trait_read_list.append(str('UNDEAD:\n'
                                   '\tThis creature is IMMUNE to Charm, Poison, Disease.\n'
                                   '\t\tRESTORED by Necrotic Damage\n'
                                   '\t\tVULNERABLE to Holy Damage.'))
            crea_trait_list.remove('Undead')
        if element == str("""Unblockable"""):
            trait_read_list.append(str("""UNBLOCKABLE:\n \tThe Creature's attacks deal damage directly to HEALTH,\n\
                                        \tignoring Toughness. +50 XP"""))
            crea_trait_list.remove(str("""Unblockable"""))
        if element == str("""Undying"""):
            trait_read_list.append(str("""UNDYING: \n \tThis Creature recovers 1 Health each turn it is not Damaged.\n\
                                        \t+25 XP"""))
            crea_trait_list.remove(str("""Undying"""))
        if element == str("""Vampiric"""):
            trait_read_list.append(str("""VAMPIRIC:\n \tThis Creature recovers 1 Health each time it deals damage. +20 XP"""))
            crea_trait_list.remove(str("""Vampiric"""))
        if element == str('Venomous'):
            trait_read_list.append(str('VENOMOUS:\n'
                                   '\tWhen you take damage by this creature, you must pass an\n'
                                   '\tEndurance check or receive the Poisoned(1) condition.'))
            crea_trait_list.remove(str('Venomous'))
        if element == str("""Vital"""):
            trait_read_list.append(str("""VITAL:\n \tIncrease the Creature's Health by 2. +15 XP"""))
            crea_trait_list.remove(str("""Vital"""))
        if element == str("""Vigilant"""):
            trait_read_list.append(str("""VIGILANT:\n \tThis Creature gains the ALERT Trait. +10 XP"""))
            crea_trait_list.remove(str("""Vigilant"""))
    trait_read_list.append(crea_trait_list)
    return trait_read_list


def Hit_table_reader(creature_str):
    Hit_table_str = str('NO HIT TABLE')
    if creature_str == str('Astral Beast') or creature_str == str('Blightfang Rats') or \
        creature_str == str('Razorjaw') or creature_str == str('Vorleg'):
        Hit_table_str = Hit_table_Quadruped
    elif creature_str == str('Fleshmelt Slime') or creature_str == str('Hive Larvae') \
        or creature_str == str('Swarmer'):
        Hit_table_str = Hit_table_str
    elif creature_str == str('Bladewings') or creature_str == str('Netherfiend'):
        Hit_table_str = Hit_table_Winged
    elif creature_str == str('Bone Spiders') or creature_str == str('Giant Spider'):
        Hit_table_str = Hit_table_Arachnid
    elif creature_str == str('Cavebound Leech') or creature_str == str('Fangvine') or \
        creature_str == str('Necropede') or creature_str == str('Tomb Crawler'):
        Hit_table_str = Hit_table_Serpentoid
    elif creature_str == str('Corpse Ants'):
        Hit_table_str = Hit_table_Insectoid
    else:
        Hit_table_str = Hit_table_Humanoid
    return Hit_table_str

def item_gen(die_roll):
    item_roll = die_roll(D8)
    if item_roll == 1:
        item_str = str('Weapon')
    elif item_roll == 2:
        item_str = str('Armor')
    elif item_roll == 3:
        item_str = str('Belt')
    elif item_roll == 4:
        item_str = str('Boots')
    elif item_roll == 5:
        item_str = str('Gloves')
    elif item_roll == 6:
        item_str = str('Amulet')
    elif (item_roll == 7) or (item_roll == 8):
        item_str = str('Ring')
    return item_str


def rarity_gen(die_roll):
    rarity_roll = die_roll(D10)
    if rarity_roll <= 5:
        rarity = str('Uncommon ')
    elif (rarity_roll >= 6) and (rarity_roll <= 8):
        rarity = str('Rare ')
    elif rarity_roll >= 9:
        rarity = str('Epic ')
    return rarity

def amulet_gen(die_roll):
    amulet_roll = int(die_roll(D20)) + 1
    mastery_list = ['0',
        'Abyssal Reaver',
        'Arcanist',
        'Brawler',
        'Bulwark',
        'Duskblade',
        'Emissary',
        'Flamecaster',
        'Frostweaver',
        'Gravecaller',
        'Hexmancer',
        'Icon Caller',
        'Mindbender',
        'Ritualist',
        'Stormbrand',
        'Tracker',
        'Umbra Phantom',
        'Weapon Master',
        'Wraith',
        'Wraithspawn',
        'Zealont'
    ]
    amulet_str = mastery_list[amulet_roll]
    return amulet_str

def weapon_gen(item_str):
    j = 0
    if item_str == str('Weapon'):
        j = j + 1
    while j >= 0:
        weapon_roll = int(die_roll(D100))
        if weapon_roll <= 3:
            weapon_str = str('Bardiche')
            j = j - 1
        elif (weapon_roll >= 4) and (weapon_roll <= 6):
            weapon_str = str('Bastard Sword')
            j = j - 1
        elif (weapon_roll >= 7) and (weapon_roll <= 9):
            weapon_str = str('Billhook')
            j = j - 1
        elif (weapon_roll >= 10) and (weapon_roll <= 12):
            weapon_str = str('Claw')
            j = j - 1
        elif (weapon_roll >= 13) and (weapon_roll <= 15):
            weapon_str = str('Club')
            j = j - 1
        elif (weapon_roll >= 16) and (weapon_roll <= 18):
            weapon_str = str('Dagger')
            j = j - 1
        elif (weapon_roll >= 19) and (weapon_roll <= 21):
            weapon_str = str('Flail')
            j = j - 1
        elif (weapon_roll >= 22) and (weapon_roll <= 24):
            weapon_str = str('Glaive')
            j = j - 1
        elif (weapon_roll >= 25) and (weapon_roll <= 27):
            weapon_str = str('Great Axe')
            j = j - 1
        elif (weapon_roll >= 28) and (weapon_roll <= 30):
            weapon_str = str('Greatclub')
            j = j - 1
        elif (weapon_roll >= 31) and (weapon_roll <= 33):
            weapon_str = str('Great Sword')
            j = j - 1
        elif (weapon_roll >= 34) and (weapon_roll <= 36):
            weapon_str = str('Halberd')
            j = j - 1
        elif (weapon_roll >= 37) and (weapon_roll <= 39):
            weapon_str = str('Hatchet')
            j = j - 1
        elif (weapon_roll >= 40) and (weapon_roll <= 42):
            weapon_str = str('Harpoon')
            j = j - 1
        elif (weapon_roll >= 43) and (weapon_roll <= 45):
            weapon_str = str('Improvised Weapon')
            j = j - 1
        elif (weapon_roll >= 46) and (weapon_roll <= 48):
            weapon_str = str('Knuckles')
            j = j - 1
        elif (weapon_roll >= 49) and (weapon_roll <= 51):
            weapon_str = str('Light Hammer')
            j = j - 1
        elif (weapon_roll >= 52) and (weapon_roll <= 54):
            weapon_str = str('Longsword')
            j = j - 1
        elif (weapon_roll >= 55) and (weapon_roll <= 57):
            weapon_str = str('Maul')
            j = j - 1
        elif (weapon_roll >= 58) and (weapon_roll <= 60):
            weapon_str = str('Mace')
            j = j - 1
        elif (weapon_roll >= 61) and (weapon_roll <= 63):
            weapon_str = str('Morningstar')
            j = j - 1
        elif (weapon_roll >= 64) and (weapon_roll <= 66):
            weapon_str = str('Pike')
            j = j - 1
        elif (weapon_roll >= 67) and (weapon_roll <= 69):
            weapon_str = str('Pilum')
            j = j - 1
        elif (weapon_roll >= 70) and (weapon_roll <= 72):
            weapon_str = str('Quarterstaff')
            j = j - 1
        elif (weapon_roll >= 73) and (weapon_roll <= 75):
            weapon_str = str('Rapier')
            j = j - 1
        elif (weapon_roll >= 79) and (weapon_roll <= 81):
            weapon_str = str('Saber')
            j = j - 1
        elif (weapon_roll >= 82) and (weapon_roll <= 84):
            weapon_str = str('Shiv')
            j = j - 1
        elif (weapon_roll >= 85) and (weapon_roll <= 87):
            weapon_str = str('Shortsword')
            j = j - 1
        elif (weapon_roll >= 88) and (weapon_roll <= 90):
            weapon_str = str('Spear')
            j = j - 1
        elif (weapon_roll >= 91) and (weapon_roll <= 93):
            weapon_str = str('Warhammer')
            j = j - 1
        elif (weapon_roll >= 94) and (weapon_roll <= 96):
            weapon_str = str('War Pick')
            j = j - 1
        else:
            print(str(f'MAGIC:{rarity_gen(die_roll)}'))
            j = j + 1

    return weapon_str

def torso_gen(die_roll):
    torso_roll = int(die_roll(D100))
    jj = 1
    while jj > 0:
        if torso_roll <= 10:
            torso_str = str('Heavy Cloth')
            jj =- 1
        elif (torso_roll >= 11) and (torso_roll <= 20):
            torso_str = str('Soft Leather')
            jj =- 1
        elif (torso_roll >= 21) and (torso_roll <= 30):
            torso_str = str('Hide Scale')
            jj =- 1
        elif (torso_roll >= 31) and (torso_roll <= 40):
            torso_str = str('Laminar')
            jj =- 1
        elif (torso_roll >= 41) and (torso_roll <= 50):
            torso_str = str('Rigid Leather')
            jj =- 1
        elif (torso_roll >= 51) and (torso_roll <= 60):
            torso_str = str('Metal Scale')
            jj =- 1
        elif (torso_roll >= 61) and (torso_roll <= 70):
            torso_str = str('Mail')
            jj =- 1
        elif (torso_roll >= 71) and (torso_roll <= 80):
            torso_str = str('Brigandine')
            jj =- 1
        elif (torso_roll >= 81) and (torso_roll <= 90):
            torso_str = str('Plate')
            jj =- 1
        else:
            print(f'MAGIC ARMOR:{rarity_gen(die_roll)}')
            jj =+ 1
    return torso_str

def VGH_gen(die_roll):
    VGH_roll = int(die_roll(D100))
    if VGH_roll <= 33:
        VGH_str = str('Light')
    elif (VGH_roll >= 34) and (VGH_roll <= 66):
        VGH_str = str('Medium')
    else:
        VGH_str = str('Heavy')
    return VGH_str

def shield_gen(die_roll):
    shield_roll = int(die_roll(D100))
    SR = shield_roll // 25
    if SR == 1:
        shield_str = str('Target')
    elif SR == 2:
        shield_str = str('Normal')
    elif SR == 3:
        shield_str = str('Full')
    elif SR == 4:
        shield_str = str('Wall')
    return shield_str

def armor_gen(die_roll):
    armor_roll = int(die_roll(D20))
    if armor_roll <= 2:
        armor_str = str(f'Full Suit: {torso_gen(die_roll)}')
    elif (armor_roll >= 3) and (armor_roll <= 7):
        armor_str = str(f'Torso Armor: {torso_gen(die_roll)}')
    elif (armor_roll >= 8) and (armor_roll <= 12):
        armor_str = str(f'{VGH_gen(die_roll)} Vambraces')
    elif (armor_roll >= 13) and (armor_roll <= 17):
        armor_str = str(f'{VGH_gen(die_roll)} Greaves')
    elif armor_roll == 18:
        armor_str = str(f'{VGH_gen(die_roll)} Helmet')
    elif (armor_roll >= 19) and (armor_roll <= 20):
        armor_str = str(f'{shield_gen(die_roll)} Shield')
    return armor_str

def magic_item_gen(die_roll):
    item = str(item_gen(die_roll))
    rare = str(rarity_gen(die_roll))
    if item == str('Weapon'):
        magic_str = (rare + weapon_gen('Weapon'))
    elif item == str('Armor'):
        magic_str = (rare + str(f'{armor_gen(die_roll)}'))
    elif item == str('Belt'):
        magic_str = (rare + 'Belt')
    elif item == str('Boots'):
        magic_str = (rare + 'Boots')
    elif item == str('Gloves'):
        magic_str = str(rare + 'Gloves')
    elif item == str('Amulet'):
        magic_str = str(f'{amulet_gen(die_roll)} Amulet')
    elif item == str('Ring'):
        magic_str = str(rare + 'Ring')
    return magic_str

def room_pic_gen(room_roll):
    if room_roll == 53:
        room_pic_str = str(
        '⠀⡠⢠⡄⢄⢄⢄⢄⢄⢄⢄⢄⢄⢠⡀⢴⠀⡄⢤⠠⢄⢤⠄⡤⡠⡠⡠⡀⡆⡠⡀⡄⡠⡀⢤⠠⡀⢄⠄⡄⣰⢀⢄⢠⢀⢄⠠⡆⢠⠠\n'
        '⢈⠦⡑⡎⠦⡱⠔⢕⠔⡇⠦⢣⠪⡢⠕⢼⠨⡪⠢⢓⠆⡺⠔⡌⢶⣎⠢⡊⡇⢜⠌⠦⠪⡰⢱⠨⡊⠦⠱⠌⢼⠠⠣⡢⠱⢌⠆⡇⢎⠜\n'
        '⢘⠔⢌⢎⠒⡌⡪⢢⡑⡕⡑⡕⡱⡘⡌⢺⠐⡅⢕⠱⡨⢪⢊⢬⡟⢿⡌⢌⡇⢪⢊⢊⠕⡌⣪⠐⢕⢌⢊⠪⣸⠨⡢⡑⡑⢕⠌⡇⢢⢑\n'
        '⢐⠕⡨⡃⢕⢌⠪⡂⢎⢎⢘⠔⡡⡊⢜⢸⢈⠪⡂⡣⢪⢘⠆⣾⢫⡛⣷⠐⡇⡱⠨⡢⡑⢌⢲⢁⠣⡢⡑⢅⢺⠐⠔⡌⡘⢔⠑⡇⢅⠕\n'
        '⠨⠮⠬⠧⠵⠬⠮⠼⠤⠧⠵⠬⠦⠵⠥⢺⠤⠧⠼⠬⠦⠵⣹⡯⢮⠳⡽⡧⠧⠪⠮⠴⠵⠬⠦⠕⠵⠬⠮⠦⢽⠬⠮⠴⠬⠢⠕⡧⠪⢜\n'
        '⠰⡑⢕⢇⢑⠪⡂⡣⢊⢇⠪⡢⢃⢎⠪⣸⢐⡊⡒⢕⠪⢨⡿⡸⡕⡝⡜⢿⡇⡱⡑⠜⡢⡑⢜⢌⠪⣂⢓⠜⣸⢂⠎⢢⢊⠪⡐⡇⢪⠢\n'
        '⢘⢌⠢⡇⡱⡑⡌⢪⠂⡇⢕⠜⢔⠡⡣⢸⢠⡑⢅⢕⠑⣾⢣⠳⡜⡜⡪⡚⣷⠨⡈⢎⠰⡁⢳⢈⠆⢥⠑⡕⣸⠄⡫⢂⠕⡱⡈⡇⡑⢕\n'
        '⢐⣅⢕⡕⣌⣢⣑⣅⢕⣕⣌⣪⢊⣎⣢⣹⣠⣊⢦⣡⣹⣯⣣⣫⣪⣪⢎⣕⢿⣇⡪⣢⣑⣌⣪⣐⢕⣢⣑⣌⢼⣈⢦⣑⣕⣌⡪⣎⣘⣔\n'
        '⢐⠔⢄⢇⣔⣄⣆⣔⣢⣆⣔⣔⣢⣢⣔⣴⣠⣢⣢⣄⡿⢰⢆⢖⠔⡆⢗⠬⡣⢿⣔⣤⣢⣰⣰⣐⣆⣔⣄⣆⣼⣠⣢⣢⣔⣔⠔⡥⡐⢔\n'
        '⠠⡣⡑⡍⠻⢯⣝⡭⣫⣏⢝⢭⢫⢍⢏⢽⠩⡭⣍⢝⡱⡱⡣⡪⡊⢎⢪⢊⡧⡹⡩⡫⡝⡭⣫⢝⢭⡹⣩⢫⢽⡩⣏⣽⡽⢛⠡⡇⢜⢌\n'
        '⢘⢔⠱⡕⡱⣄⡙⡻⣶⣕⢧⡳⡱⡱⡡⣻⢘⢆⢎⢦⡱⡸⡪⢜⢌⡣⡱⡡⣇⢪⢪⡪⣪⢪⡺⣘⢆⡳⡱⣕⢽⣾⠟⡡⡢⡑⡅⣇⠪⡢\n'
        '⠈⡎⢜⠕⡌⢆⠜⡰⠄⡝⠷⣵⣩⢪⡊⢾⠰⡡⡣⡒⢕⢜⠜⡢⠱⡌⡪⢢⢇⠕⡥⢪⠢⡣⡺⣌⢮⢪⣾⠞⢫⢐⢌⠢⡊⢔⠌⡆⢕⠸\n'
        '⠸⡈⢎⢇⠪⡢⢣⢊⠪⡒⠔⡌⡙⢷⣭⣺⢑⢕⢌⢎⠎⡼⡡⡓⢕⢜⢌⢣⡇⢕⠪⡪⡱⡱⣝⣴⠿⢋⢅⠪⣸⠠⡃⡕⡡⢣⠨⡇⢌⢣\n'
        '⠰⡡⢃⡇⡱⡘⢔⢅⢑⢅⠣⡊⢜⠤⣈⠻⢷⡕⢕⠕⡕⢜⢆⢝⡘⢆⠧⡑⣇⢣⡙⡜⣜⡾⢛⠡⡊⢆⠱⡁⣺⠈⢎⢔⢡⢃⠪⡃⡪⠢\n'
        '⢉⢩⢉⡍⡩⡉⡍⡩⡉⡍⡩⡉⡍⡩⡉⣩⣿⢩⢍⢍⢍⢭⡩⣉⢍⢍⢍⢍⡍⢭⢩⢝⡌⣿⣉⢍⡉⣉⢍⢉⣩⢉⢍⢩⡉⡍⡩⡍⡩⡩\n'
        '⢐⠕⡰⢇⠜⡨⠢⡪⡐⡕⢌⠲⡨⢢⠑⣼⢇⢕⢕⠕⡕⢲⠢⡊⣆⢣⠪⡢⡇⡣⡣⡪⡪⠼⣧⠢⡨⢂⠆⡅⢼⢀⠇⡢⡘⢔⠐⡇⡘⢔\n'
        '⠰⡑⢌⢇⠪⡨⡊⡢⢊⠎⡌⡪⢢⢃⢸⣟⢜⢪⢊⢎⢪⢸⡑⢜⠔⡕⢕⠬⣇⢪⢒⢕⢍⢎⢿⡆⠪⡢⡑⢌⢺⠠⡣⢊⠔⡡⡑⡅⠪⡢\n'
        '⢈⢎⠒⡇⢓⠜⡘⢢⠃⡗⡘⡢⢃⠣⣿⢱⡓⣕⢣⡓⡕⣵⡑⡣⣋⢎⢳⢑⣇⢳⡱⡱⡣⡳⣙⣿⡘⡢⢓⡘⢪⢊⢒⡑⣊⠒⢌⠇⡓⢜\n'
        '⠐⣌⢊⡇⡱⢡⠙⡔⡡⡣⡘⢌⠪⣸⡏⣺⡘⣎⢮⡾⠟⢹⡇⡳⢌⠦⡣⣹⡏⠻⣮⣺⢜⢎⢮⢺⣧⠊⢆⠥⡹⢠⠑⡌⢢⠑⢌⠇⡜⡰\n'
        '⢘⢄⠪⡆⡱⡁⡣⢊⠔⡕⢌⠪⢢⡿⡸⣞⣼⠞⡋⢔⢅⢹⡇⣝⢪⢪⢎⢼⡏⢔⢌⠙⠷⣯⡺⡕⣿⡎⢢⠑⢼⠠⡃⢜⠰⡡⡑⡇⢜⠔\n'
        '⠐⣃⠚⡖⢊⢒⢑⢃⠚⡒⡑⠓⣾⣳⡿⢛⠡⡚⡘⢒⢂⢻⡗⣕⢳⢓⡓⢾⡗⢊⡒⡙⡒⢌⢛⢿⣜⣷⠑⡃⢻⠐⡓⡘⢒⠒⢜⡃⡚⢜\n'
        '⢐⠌⢌⠇⢥⢑⠅⡅⡱⡡⢊⠙⠟⢡⠐⢼⢈⠎⡌⢕⠤⢹⡇⣗⠵⣱⡙⢾⡏⢔⠱⡈⢎⠢⡱⢄⠌⠻⢃⠕⣹⠐⢌⠢⡡⠣⡨⡇⡸⡐\n'
        '⠨⡊⡢⡓⢔⠱⡘⢔⠔⡅⡪⡈⢎⠢⡑⣹⠠⡃⢎⠔⡑⢼⣇⣏⣞⣜⣜⣽⣇⠱⡡⡑⢅⠣⣚⢄⠣⡑⢅⠪⣸⠐⡅⢪⢐⢕⢐⡇⢌⠪\n'
        '⠨⠮⠔⡧⠪⠮⠼⠴⠕⠵⠬⠪⠮⠪⠦⢺⠔⠵⠬⠮⠦⠺⡇ DOOR⢸⠧⠼⠤⠮⠴⠵⠬⠦⠵⠬⠦⠵⠼⠴⠥⠵⠥⠮⠦⠧⠮⢜\n'
        '⢘⠢⡑⡇⣊⠒⡕⡸⡈⡇⢪⠊⡌⡣⡑⢹⠠⡃⡪⢂⠣⡪⡉⡩⡉⡍⡩⠡⡇⡒⡱⢐⠕⡐⢝⢐⠕⡢⡑⢌⢺⢐⢊⠢⡊⢢⢃⡇⠪⡢\n'


                       )

    return room_pic_str

def fight_check(room_roll, fight_roll):
    if fight_roll == 20:
        print('CREATURE MODIFIER!!!!!')
    if (room_roll <= 24) and (fight_roll >= 15):
        fight = True
    elif (room_roll >= 25) and (fight_roll >= 10):
        fight = True
    else:
        fight = False
    return bool(fight)


def door_generator(room_roll):
    room_roll = int(room_roll)
    i = 0
    ####2 door rooms###
    two_door_list = [1, 5, 8, 9, 11, 12, 13, 16, 17, 18, 23, 24, 26, 27, 30, 32, 33, 36, \
                     39, 41, 45, 46, 47, 48, 50, 55, 56, 57, 58, 59, 61, 66, 67, 68, 72,\
                     74, 75, 76, 80, 81, 82, 86, 88, 93, 94, 95, 97]
    #####3 door rooms#####
    three_door_list = [15, 19, 20, 42, 44, 62, 63, 65, 79, 92, 99, 100]
    ###4 door rooms#####
    four_door_list = [2, 4, 6, 14, 34, 37, 52, 64, 83, 91]
    ###5 door rooms###
    five_door_list = [25, 49, 69]
    ###6 door rooms###
    six_door_list = [7, 70]
    ###8 door rooms####
    eight_door_list = [29, 51, 71]
    ###no door rooms###
    zero_door_list = [3, 10, 21, 22, 28, 31, 35, 38, 40, 43, 53, 54, 60, 73, 77, 78, 84, \
                      85, 87, 89, 90, 96, 98]
    if (room_roll in zero_door_list) == True:
        i = 0
    elif (room_roll in two_door_list) == True:
        i = 2
    elif (room_roll in three_door_list) == True:
        i = 3
    elif (room_roll in four_door_list) == True:
        i = 4
    elif (room_roll in five_door_list) == True:
        i = 5
    elif (room_roll in six_door_list) == True:
        i = 6
    elif (room_roll in eight_door_list) == True:
        i = 8
    return int(i)

def Num_door(i):
    ####while i is less than num of doors so that each door gens new values
   if i > 0:
        ###open check####
        door_open = die_roll(D20)
        if (door_open <= 11):
            door_open_str = str('Door is unlocked and open.\n')
            print('_' * 8)

        elif (door_open >= 12):
            lock_door = choice(DC_gen_list)
            door_open_str = str('Door is closed and locked.\n'
                                f'TO LOCKPICK: {lock_door}\n')
            print("_" * 8)
        return door_open_str

####START PROGRAM#####
####
####

def encounter_roll(fight):
    if fight == False:
        ecount_check = True
        Enc_code = die_roll(D100)
        print(str(f'Encounter code: {Enc_code}'))
    return Enc_code
###TENSION CLASS####
class tension():
    def __init__(self):
        curr_tension = 3
        TX = str('?')

    def __tensionROLL__(self, TX):
        tension_die = die_roll(TX)
        return tension_die
    def __tensionCheck__(self, curr_tension):

        while curr_tension == 0:
            print(str("""!!!!!!!!!!! GROWING DARKNESS TRIGGER !!!!!!!!!!"""))
            curr_tension = 3
            break
        while (curr_tension == 4) and (tension_check_bool == True):
            TX = D10
            tension_die = tension.__tensionROLL__(self, TX)
            if tension_die <= 2:
                curr_tension -= 1
            tension_check_bool = False
            tension_str = str('CHECK FOR TENSION DIE:\n'
                              '-----------------------\n'
                              f'{TX:^5} {'|':^6} {tension_die:>4}')
            print(tension_str)
            break
        while curr_tension == 3:
            TX = D8
            tension_die = tension.__tensionROLL__(self, TX)
            if tension_die <= 2:
                curr_tension -= 1
            tension_check_bool = False
            tension_str = str('CHECK FOR TENSION DIE:\n'
                              '-----------------------\n'
                              f'{TX:^5} {'|':^6} {tension_die:>4}')
            print(tension_str)
            break
        while curr_tension == 2:
            TX = D6
            tension_die = tension.__tensionROLL__(self, TX)
            if tension_die <= 2:
                curr_tension -= 1
            tension_check_bool = False
            tension_str = str('CHECK FOR TENSION DIE:\n'
                              '-----------------------\n'
                              f'{TX:^5} {'|':^6} {tension_die:>4}')
            print(tension_str)
            break
        while curr_tension == 1:
            TX = D4
            tension_die = tension.__tensionROLL__(self, TX)
            if tension_die <= 2:
                curr_tension -= 1
            tension_check_bool = False
            tension_str = str('CHECK FOR TENSION DIE:\n'
                              '-----------------------\n'
                              f'{TX:^5} {'|':^6} {tension_die:>4}')
            print(tension_str)
            break
        return tension_str

####LAIR/EXIT DIE CLASS####
class lair():
    def __init__(self):
        lair_bool = False
        exit_bool = False
        lair_count = 5
        LX = D12
        lair_roll = 0
        lair_str = str('?')
    def __lairRoll__(self, LX):
        lair_roll = die_roll(LX)
        return lair_roll
    def __lair__(self, lair_count):
        while (lair_check_bool == True):
            while (lair_count == 5) and (exit_bool == False) and (lair_bool == True):
                LX = D12
                lair_roll = lair.__lairRoll__(self,LX)
                lair_str = (str('CHECK FOR LAIR DIE:\n'
                '-----------------------\n'
                f'{LX:^5} {'|':^6} {lair_roll:>4}'))
                print(lair_str)
                if lair_roll <= 2:
                    lair_count =- 1
                lair_bool = False
                break
            while (lair_count == 4) and (exit_bool == False) and (lair_bool == True):
                LX = D10
                lair_roll = lair.__lairRoll__(self, LX)
                lair_str = str('CHECK FOR LAIR DIE:\n'
                      '-----------------------\n'
                      f'{LX:^5} {'|':^6} {lair_roll:>4}')
                print(lair_str)
                if lair_roll <= 2:
                    lair_count =- 1
                lair_bool = False
                break
            while (lair_count == 3) and (exit_bool == False) and (lair_bool == True):
                LX = D8
                lair_roll = lair.__lairRoll__(self, LX)
                lair_str = str('CHECK FOR LAIR DIE:\n'
                      '-----------------------\n'
                      f'{LX:^5} {'|':^6} {lair_roll:>4}')
                print(lair_str)
                if lair_roll <= 2:
                    lair_count =- 1
                lair_bool = False
                break
            while (lair_count == 2) and (exit_bool == False) and (lair_bool == True):
                LX = D6
                lair_roll = lair.__lairRoll__(self, LX)
                lair_str = str('CHECK FOR LAIR DIE:\n'
                      '-----------------------\n'
                      f'{LX:^5} {'|':^6} {lair_roll:>4}')
                print(lair_str)
                if lair_roll <= 2:
                    lair_count =- 1
                lair_bool = False
                break
            ####OVERSEER and EXIT TRIGGER#####

            while (lair_count == 1) and (exit_bool == False) and (lair_bool == True):
                LX = D4
                lair_roll = lair.__lairRoll__(self, LX)
                lair_str = (str('CHECK FOR LAIR DIE:\n'
                      '-----------------------\n'
                      f'{LX:^5} {'|':^6} {lair_roll:>4}'))
                print(lair_str)
                if lair_roll <= 2:
                    lair_count = 3
                print('\n!!!! OVERSEER LAIR !!!!\n')
                overseer_bool = True
                exit_bool = True
                lair_bool = False
                break
            while (lair_count == 3) and (exit_bool == True) and (lair_bool == True):
                LX = D8
                lair_roll = lair.__lairRoll__(self, LX)
                lair_str = (str('CHECK FOR EXIT DIE:\n'
                      '-----------------------\n'
                      f'{LX:^5} {'|':^6} {lair_roll:>4}'))
                print(lair_str)
                if lair_roll <= 2:
                    lair_count =- 1
                lair_bool = False
                break
            while (lair_count == 2) and (exit_bool == True) and (lair_bool == True):
                LX = D6
                lair_roll = lair.__lairRoll__(self, LX)
                lair_str = (str('CHECK FOR EXIT DIE:\n'
                      '-----------------------\n'
                      f'{LX:^5} {'|':^6} {lair_roll:>4}'))
                print(lair_str)
                if lair_roll <= 2:
                    lair_count =- 1
                lair_bool = False
                break
            ###EXIT END TRIGGER#####
            while (lair_count == 1) and (exit_bool == True):
                LX = D4
                lair_roll = lair.__lairRoll__(self, LX)
                lair_str = str('CHECK FOR EXIT DIE:\n'
                               '-----------------------\n'
                               f'{LX:^5} {'|':^6} {lair_roll:>4}')
                print(lair_str)
                if lair_roll <= 2:
                    lair_count = 5
                    print("""\n!!!!!!! EXIT FOUND !!!!!!!!\n""")
                    LX = D12
                break
            break
        return lair_str

print(ker_str)
choose = str('')
choose_list_print = ['next room', 'light', 'tension', 'creature',
                     'item', 'armor', 'weapon', 'magic', 'DX', 'EXIT']
choose_list = ['light', 'lair', 'next room', 'tension', 'creature', 'item', 'armor', 'weapon', 'magic', 'D4', 'd4',\
               'd6', 'D6', 'd8', 'D8', 'd10', 'D10', 'd12', 'D12', 'd20', 'D20', 'd66', 'D66',\
               'd100', 'D100', 'EXIT']
LX = D12
light = 20
light_bool = False
door_num = 0
fig = False
lair.__init__(lair)
tension.__init__(tension)
#####BEGIN INPUTS#######
while choose != str('EXIT'):
    while choose not in choose_list:
        print(f'These are your options:\n {choose_list_print}')
        choose = input('WHAT WOULD YOU LIKE TO DO?\n')
        continue

    ####INTERACTIVE OPENING INPUTS#######
    while choose == str('light'):
        light = int(input('Please enter Lightsource left:\n'))
        light_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        if light not in light_list:
            choose = str('light')
        elif light in light_list:
            light_bool = True
            choose = str('tension')
        continue
    while choose == str('tension'):
        TX = input('Please enter current Tension Die:\n')
        if TX not in  [D10, D8, D6, D4]:
            choose = str('tension')
        elif TX in [D10, D8, D6, D4]:
            tension_check_bool = True
            if TX == D10:
                curr_tension = 4
            elif TX == D8:
                curr_tension = 3
            elif TX == D6:
                curr_tension = 2
            elif TX == D4:
                curr_tension = 1
            choose = str('lair')
        continue
    while choose == str('lair'):
        LX = input('Please enter current Lair/Exit Die:\n')
        if LX not in [D12, D10, D8, D6, D4]:
            choose = str('lair')
        lair_input = input('lair or exit Die?\n')
        lair_check_bool = True
        if LX == D12:
            lair_count = 5
        elif LX == D10:
            lair_count = 4
        elif LX == D8:
            lair_count = 3
        elif LX == D6:
            lair_count = 2
        elif LX == D4:
            lair_count = 1
        if lair_input == str('lair'):
            exit_bool = False
        elif lair_input == str('exit'):
            exit_bool = True
        else:
            choose = str('lair')
        choose = str('next room')
        continue

    while choose == str('next room'):
        import random
        from random import choice

        corr_desc_str = str(choice(corr_desc_list))
        room_desc_str = str(choice(room_desc_list))

        input('Room Generating.....')
        print('Rolling for room......\n')
        room_roll = die_roll(D100)
        if room_roll == 53:
            print(f'{room_pic_gen(room_roll)}')
        if (room_roll >= 26) and (light_bool == False):
            print('!!!!!!MINUS ONE LIGHTSOURCE!!!!!!\n')
        if (room_roll >= 26) and (light_bool == True):
            if light in light_list:
                light -= 1
                if light in light_list:
                    print(f'LIGHT REMAINING:\n'
                      f'================\n {light:^12}')
                elif light not in light_list:
                    print('!!!!!! LIGHT SOURCE DEPLETED !!!!!!!')
                    light = 20

        if tension_check_bool == False:
            print('CHECK FOR TENSION DIE:\n'
                  "-------------------------------\n"
                  f'D10: | {die_roll(D10)} \n'
                  f'D8:  | {die_roll(D8)}  \n'
                  f'D6:  | {die_roll(D6)}  \n'
                  f'D4:  | {die_roll(D4)}  \n'
                  )
        elif tension_check_bool == True:
            tension_str = (tension.__tensionCheck__(tension, curr_tension))

        if (room_roll >= 26) and (lair_check_bool == False):
            print('CHECK FOR LAIR DIE:\n'
                  "-------------------------------\n"
                    f'D12: | {die_roll(D12)} \n'
                    f'D10: | {die_roll(D10)} \n'
                    f'D8:  | {die_roll(D8)}  \n'
                    f'D6:  | {die_roll(D6)}  \n'
                    f'D4:  | {die_roll(D4)}  \n')
        elif (room_roll >= 26) and (lair_check_bool == True):
            lair_str = (lair.__lairRoll__(lair, LX))
            print('CHECK FOR LAIR DIE:\n'
                  '------------------------------\n'
                f'{LX} {'|':^3}{lair_str}')
        print('______________________________________________________________\n')

        ###ROOM ROLL###

        print(f'Your room number is\n {room_roll}.\n')
        if room_roll <= 25:
            print(corr_desc_str)
            print('\n')

        elif room_roll >= 26:
            print(room_desc_str)
            print('\n')
        print('Rolling for combat.....')

        fight_roll = die_roll(D20)
        fig = fight_check(room_roll, fight_roll)
        print('______________________________________________________________\n')
        print(f'COMBAT?:\n {fig}')
        if (fig == True) and (overseer_bool == False):
            TRAIT = (creature_trait_gen(creature_str))
            if fight_roll == 20:
                mod_creature_str = creature_mod_gen(1, creature_str)
                print(mod_creature_str[0])

                for element in crea_trait_reader(mod_creature_str[1]):
                    print(element)

            elif fight_roll != 20:
                print(creature_str)
            print(*crea_trait_reader(TRAIT), sep='\n')
            print(f'{creature_str} rolls a {die_roll(D100)} for Awareness Check!\n')
            print(f'You rolled a {die_roll(D100)} for your Perception Check!')
            print(f'\n\tCREATURE ROLLED A {die_roll(D6)} FOR ITS FIRST MOVE\n')
            print(Hit_table_reader(creature_str))
            print(damage_table)
            if ((Hit_table_reader(creature_str)) != str(f'{Hit_table_Humanoid}')):
                print(f'{Hit_table_Humanoid}')
            creature_str = choice(creature_list)
        elif (room_roll >= 26):
            print(f'Event roll: {die_roll(D100)}')

        print('____________________________________________________________\n')
        if room_roll >= 25:
            print('SCAVANGE CHECK: '
                  f'{die_roll(D100)}')

        if (fig == True):
            print(f'{die_roll(D4)} Toughness restored!!!\n')
            print('ARMOR BREAK CHECK!!')
            if creature_str in res_table_crea_list:
                print(f'RESOURCE ROLL:\n')
                spoils_str = str(f'{res_table_crea_function(die_roll)}')
                print(str(spoils_str))
            elif creature_str not in res_table_crea_list:
                print(f'Spoils table roll:\n'
                  f'{die_roll(D6)}')
        print('____________________________________________________________\n')
        i = door_generator(room_roll)
        print(f'NUMBER OF DOORS: {i}')

        while i > 1:
            print(Num_door(i))
            i = i - 1

        choose = input('Next room?\n')
        continue




    while (choose == str('magic')):
        MAGIC = str(f'{magic_item_gen(die_roll)}')
        print(MAGIC)
        choose = input('magic, item, DX, creature, next room?\n')
        continue
    while (choose == str('item')):
        ITEM = str(f'{item_gen(die_roll)}')
        print(ITEM)
        choose = input('magic, item, DX, creature, next room?\n')
        continue
    while (choose == str('armor')):
        ARMOR = str(f'{armor_gen(die_roll)}')
        print(ARMOR)
        choose = input('Next room?\n')
        continue
    while (choose == str('creature')):
        creature_str = choice(creature_list)
        print("COMBAT GENERATED:\n")
        print(f'{creature_str}')
        print('_' * 16)
        print(f'{creature_str} rolled a {die_roll(D100)} for Awareness Check!')
        print(f'You rolled a {die_roll(D100)} for Perception Check!!\n')
        print(f'\tCreature rolled a {die_roll(D6)} for its first move!!\n')
        print(damage_table)
        choose = input('DX, next room, creature, or exit\n')
        continue
    while (choose == str("DX")):
        choose = input("What die do you want to roll?\n")
        if choose == D4 or (choose == (str('d4'))):
            print(f'{die_roll(D4)}')
        elif choose == D6 or (choose == (str('d6'))):
            print(f'{die_roll(D6)}')
        elif choose == D8 or (choose == (str('d8'))):
            print(f'{die_roll(D8)}')
        elif choose == D10 or (choose == (str('d10'))):
            print(f'{die_roll(D10)}')
        elif choose == D12 or (choose == (str('d12'))):
            print(f'{die_roll(D12)}')
        elif choose == D20 or (choose == (str('d20'))):
            print(f'{die_roll(D20)}')
        elif choose == D100 or (choose == (str('d100'))):
            print(f'{die_roll(D100)}')
        choose = input("Next room, or roll another DX?\n")
        continue
    while (choose == D4) or (choose == (str('d4'))):
        print(f'{die_roll(D4)}')
        choose = input("Next room, or roll another DX?\n")
        continue
    while (choose == D6) or (choose == (str('d6'))):
        print(f'{die_roll(D6)}')
        choose = input("Next room, or roll another DX?\n")
        continue
    while (choose == D8) or (choose == (str('d8'))):
        print(f'{die_roll(D8)}')
        choose = input("Next room, or roll another DX?\n")
        continue
    while (choose == D10) or (choose == (str('d10'))):
        print(f'{die_roll(D10)}')
        choose = input("Next room, or roll another DX?\n")
        continue
    while (choose == D12) or (choose == (str('d12'))):
        print(f'{die_roll(D12)}')
        choose = input("Next room, or roll another DX?\n")
        continue
    while (choose == D20) or (choose == (str('d20'))):
        print(f'{die_roll(D20)}')
        choose = input("Next room, or roll another DX?\n")
        continue
    while (choose == D66) or (choose == (str('d66'))):
        print(f'{die_roll(D66)}')
        choose = input("Next room, or roll another DX?\n")
        continue
    while (choose == D100) or (choose == (str('d100'))):
        print(f'{die_roll(D100)}')
        choose = input("Next room, or roll another DX?\n")
        continue

    while choose == str('weapon'):
        print(f'{weapon_gen(str('Weapon'))}')
        choose = input('Next room?\n')
        continue































