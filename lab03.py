# Import the random library to use for the dice later
import random

# Create dice options using list() and range()
diceOptions = list(range(1, 7))

# Define weapons array
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear bomb"]

# Display available weapons using a for loop
print("Available Weapons:")
for i, weapon in enumerate(weapons, start=1):
    print(f"{i}. {weapon}")

# Get and validate player inputs for combat strengths
while True:
    try:
        combatStrength = int(input("Enter your combat strength (1-6): "))
        if 1 <= combatStrength <= 6:
            break
        else:
            print("Combat strength must be between 1 and 6.")
    except ValueError:
        print("Invalid input. Please enter an integer between 1 and 6.")

while True:
    try:
        mCombatStrength = int(input("Enter monster's combat strength (1-6): "))
        if 1 <= mCombatStrength <= 6:
            break
        else:
            print("Monster's combat strength must be between 1 and 6.")
    except ValueError:
        print("Invalid input. Please enter an integer between 1 and 6.")

# Simulate battle sequence for 10 rounds with specified conditions
for roundNum in range(1, 20, 2):
    # Roll dice for hero and monster
    heroRoll = random.choice(diceOptions)
    monsterRoll = random.choice(diceOptions)

    # Add dice rolls to strengths
    heroStrength = combatStrength + heroRoll
    monsterStrength = mCombatStrength + monsterRoll

    # Determine selected weapons
    heroWeapon = weapons[heroRoll - 1]
    monsterWeapon = weapons[monsterRoll - 1]

    # Announce the round and results
    print(f"\nRound {roundNum}: Hero rolled {heroRoll}, Monster rolled {monsterRoll}.")
    print(f"Hero selected: {heroWeapon}, Monster selected: {monsterWeapon}.")
    print(f"Hero Total Strength: {heroStrength}, Monster Total Strength: {monsterStrength}.")

    # Determine round winner
    if heroStrength > monsterStrength:
        print("Hero wins the round!")
    elif monsterStrength > heroStrength:
        print("Monster wins the round!")
    else:
        print("It's a tie!")

    # Check for break condition
    if roundNum == 11:
        print("Battle Truce declared in Round 11. Game Over!")
        break
