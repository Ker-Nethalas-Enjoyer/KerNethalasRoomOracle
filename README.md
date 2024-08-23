ROOM ORACLE:
For a new room, type 'next room'
To end program, type 'EXIT'
For a magic item generator, type 'magic'
for a normal item, type 'item'
for a random armor, type 'armor'
for a random weapon, type 'weapon'
for a random creature, type 'creature'
for a die roller, type 'DX', where X = the number of sides. supported dice: D4, D6, D8, D10, D12, D20, D66, D100
FUNCTIONS THAT DO NOT WORK:
'light', 'lair', 'tension'
-'light' might work, the purpose was to count down from user input
-'lair' was supposed to keep track of current lair/exit die, but this does not work
-'tension' was supposed to keep track of current tension die. Would need additional code for tension die triggers from other sources
Even though these do not work, the program reminds you to reduce light source, and rolls for all possible lair and tension dice

TO USE THIS PROGRAM:
Prepare outside tables and resources. Please support Black Oath Games, this program needs the book for reference. 
When you have your tables and book ready, and are ready to generate a room, type 'next room'.
FIRST BLOCK OF INFO:
  Record light loss if notified (only room rolls >= 26 will trigger a light source use)
  Compare your current Tension and Lair die to the tables provided. On a roll of 1 or 2, reduce your respective die by a stage.
    If you trigger Growing Darkness, roll a D100 either physically or by typing 'D100', and then refer to the growing darkness table.
    If you trigger a Lair, IGNORE ALL INFORMATION EXCEPT FOR THE ROOM ROLL, this is where your Overseer is located.
    If you trigger an Exit, the next room you enter is a new domain.
-------------------------------------
SECOND BLOCK OF INFO
  This is where your room roll is displayed. Refer to the room table for the shape of the room, and then draw it physically.
  A description is given from the book for rooms and corridors
  Combat is rolled here, the number is displayed
-----------------------------------
THIRD BLOCK OF INFO
  Combat? will tell you True or False. 
    If Combat? False: 
      An event roll is given. Refer to the event table in the book.
    If Combat? True:
      The creature name is given
      Traits are displayed, BUGGY!!!!!
      Below Traits, a list has been created with all traits of the creature, sometimes the traits are not read, so be sure to
        refer to the creature section of the book. Sometimes this list is empty
      An Awareness check is rolled for the creature, compare to the given value in the book.
      A Perception check is rolled for the player, compare to your character sheet.
      Creature gets a roll for its first move. 
      If the creature has a hit table, it will be displayed, unless it is a Humanoid.
      Damage table is displayed for easy reference
      Humanoid Hit Location table is displayed for the player, and creature if that creature is a humanoid
----------------------------------------------------
FOURTH BLOCK OF INFO:
  A scavange check is automatically rolled
  IF Combat? True:
    Toughness restored is rolled
    An ARMOR BREAK CHECK!! reminder is given. Only roll for armor usage die if you were hit physically in combat.
    Spoils or Resources is automatically rolled. Refer to the book for spoils,
      Resources is BUGGY and might not display. 
  IF Combat? False:
    This could be an empty block if the room is a corridor
  --------------------------------------------------
  FIFTH BLOCK OF INFO:
  NUMBER OF DOORS: X
    The door counter does not roll for the door you entered from.
    Some rooms have exits, but no door, these will not be counted here.
    Each door is rolled to first see if it is locked or open, then for its lockpicking difficulty.
    The doors are meant to be mapped to the room in a clockwise manner, starting with the door you entered from.
