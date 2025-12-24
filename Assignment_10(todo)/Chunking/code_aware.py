from langchain_text_splitters import RecursiveCharacterTextSplitter

spillter=RecursiveCharacterTextSplitter.from_language(language="python", chunk_size=800,chunk_overlap=50)  #type:ignore

text='''
import random
import time
import sys
from typing import List, Dict, Optional, Union

# --- Configuration & Constants ---
SCREEN_WIDTH = 60
DIVIDER = "-" * SCREEN_WIDTH
GAME_TITLE = " || THE ABYSSAL ARCHIVE || "

# --- Utility Functions ---

def slow_print(text: str, delay: float = 0.02) -> None:
    """
    Prints text to stdout one character at a time to simulate typing.
    
    Args:
        text (str): The text to print.
        delay (float): Time delay between characters.
    """
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Newline

def roll_dice(sides: int = 20) -> int:
    """
    Simulates rolling a die with 'sides' number of faces.
    
    Args:
        sides (int): The number of faces on the die.
        
    Returns:
        int: A random integer between 1 and sides.
    """
    return random.randint(1, sides)

# --- Class Definitions ---

class Entity:
    """
    The base class for all living things in the game (Player and Enemies).
    
    Attributes:
        name (str): The name of the entity.
        max_hp (int): Maximum Health Points.
        hp (int): Current Health Points.
        strength (int): Physical attack power.
        defense (int): Damage reduction capability.
        is_alive (bool): Status of the entity.
    """

    def __init__(self, name: str, hp: int, strength: int, defense: int):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.strength = strength
        self.defense = defense
        self.is_alive = True

    def attack(self, target: 'Entity') -> str:
        """
        Calculates damage and inflicts it on a target.
        
        Args:
            target (Entity): The entity being attacked.
            
        Returns:
            str: A description of the attack event.
        """
        # Calculate raw damage
        base_damage = self.strength + roll_dice(6)
        # Calculate mitigated damage
        damage_dealt = max(0, base_damage - target.defense)
        
        target.take_damage(damage_dealt)
        
        return (f"{self.name} attacks {target.name} for {damage_dealt} damage "
                f"(Blocked: {target.defense})!")

    def take_damage(self, amount: int) -> None:
        """
        Reduces HP by the specified amount and checks for death.
        
        Args:
            amount (int): The damage to subtract from HP.
        """
        self.hp -= amount
        if self.hp <= 0:
            self.hp = 0
            self.is_alive = False

    def heal(self, amount: int) -> int:
        """
        Restores HP up to the maximum limit.
        
        Args:
            amount (int): The amount of HP to restore.
            
        Returns:
            int: The actual amount healed.
        """
        original_hp = self.hp
        self.hp = min(self.max_hp, self.hp + amount)
        return self.hp - original_hp

    def __str__(self) -> str:
        return f"{self.name} [HP: {self.hp}/{self.max_hp}]"


class Item:
    """
    Represents an object that can be stored in an inventory.
    """
    def __init__(self, name: str, item_type: str, value: int, description: str):
        self.name = name
        self.item_type = item_type  # 'weapon', 'potion', 'armor'
        self.value = value  # Damage for weapons, Heal for potions
        self.description = description

    def __repr__(self):
        return self.name


class Hero(Entity):
    """
    The player character class. Extends Entity with inventory and leveling logic.
    
    Attributes:
        level (int): Current player level.
        exp (int): Current experience points.
        exp_to_next_level (int): XP required to level up.
        inventory (List[Item]): List of items carried.
    """

    def __init__(self, name: str):
        # Initialize the base Entity
        super().__init__(name, hp=100, strength=10, defense=2)
        
        self.level = 1
        self.exp = 0
        self.exp_to_next_level = 100
        self.inventory: List[Item] = [
            Item("Small Potion", "potion", 20, "Restores 20 HP"),
            Item("Rusty Dagger", "weapon", 2, "A blunt blade")
        ]
        self.equipped_weapon: Optional[Item] = None

    def gain_exp(self, amount: int) -> None:
        """
        Adds experience points and handles leveling up.
        """
        self.exp += amount
        print(f"You gained {amount} experience points.")
        
        if self.exp >= self.exp_to_next_level:
            self.level_up()

    def level_up(self) -> None:
        """
        Increases stats when the player levels up.
        """
        self.level += 1
        self.exp -= self.exp_to_next_level
        self.exp_to_next_level = int(self.exp_to_next_level * 1.5)
        
        # Stat boosts
        self.max_hp += 20
        self.hp = self.max_hp
        self.strength += 3
        self.defense += 1
        
        print(DIVIDER)
        print(f"*** LEVEL UP! You are now level {self.level} ***")
        print(f"Stats Increased: HP -> {self.max_hp}, STR -> {self.strength}")
        print(DIVIDER)

    def use_potion(self) -> None:
        """
        Searches inventory for a potion and consumes it.
        """
        # Filter inventory for potions
        potions = [item for item in self.inventory if item.item_type == 'potion']
        
        if not potions:
            print("You have no potions left!")
            return

        # Use the first potion found
        potion_to_use = potions[0]
        healed = self.heal(potion_to_use.value)
        self.inventory.remove(potion_to_use)
        print(f"You used {potion_to_use.name} and recovered {healed} HP.")

    def show_stats(self) -> None:
        """Displays full character sheet."""
        print(f"\n--- {self.name} (Lvl {self.level}) ---")
        print(f"HP: {self.hp}/{self.max_hp}")
        print(f"STR: {self.strength} | DEF: {self.defense}")
        print(f"EXP: {self.exp}/{self.exp_to_next_level}")
        print(f"Inventory: {', '.join([i.name for i in self.inventory])}")
        print(DIVIDER)


class Monster(Entity):
    """
    Represents enemies. Generates loot upon defeat.
    """
    def __init__(self, name: str, level: int):
        # Scale stats based on level
        hp = 20 + (level * 10)
        strength = 4 + (level * 2)
        defense = level
        super().__init__(name, hp, strength, defense)
        self.level = level
        self.xp_reward = 30 * level

# --- Core Game Engine ---

class GameEngine:
    """
    Manages the game loop, state, and encounter generation.
    """
    
    def __init__(self):
        self.running = True
        self.player: Optional[Hero] = None
        self.turn_counter = 0

    def start_game(self) -> None:
        """Initializes the game and character creation."""
        print(DIVIDER)
        print(GAME_TITLE.center(SCREEN_WIDTH))
        print(DIVIDER)
        
        player_name = input("Enter your Hero's name: ").strip() or "Adventurer"
        self.player = Hero(player_name)
        
        slow_print(f"Welcome, {self.player.name}. The Abyss awaits...")
        time.sleep(1)
        
        self.main_loop()

    def main_loop(self) -> None:
        """The primary game loop handling movement and choices."""
        while self.running and self.player.is_alive:
            print("\nWhat would you like to do?")
            print("1. Explore (Find Enemy)")
            print("2. Check Stats")
            print("3. Rest (Heal small amount)")
            print("4. Quit")
            
            choice = input(">> ")
            
            if choice == "1":
                self.generate_encounter()
            elif choice == "2":
                self.player.show_stats()
            elif choice == "3":
                self.rest_player()
            elif choice == "4":
                self.running = False
                print("You flee the dungeon. Game Over.")
            else:
                print("Invalid command.")

    def rest_player(self) -> None:
        """Allows the player to recover some health safely."""
        print("You find a quiet corner to rest...")
        time.sleep(1)
        healed = self.player.heal(10)
        print(f"You rested and recovered {healed} HP.")
        # Chance of ambush could be added here

    def generate_encounter(self) -> None:
        """Creates a random monster and initiates combat."""
        monster_names = ["Goblin", "Skeleton", "Orc", "Dark Wizard", "Slime"]
        name = random.choice(monster_names)
        # Monster level is loosely based on player level
        level = max(1, self.player.level + random.randint(-1, 1))
        
        enemy = Monster(name, level)
        slow_print(f"A wild {enemy.name} (Lvl {enemy.level}) appears!", 0.03)
        
        self.combat_system(enemy)

    def combat_system(self, enemy: Monster) -> None:
        """
        Handles the turn-based combat logic.
        
        Args:
            enemy (Monster): The enemy entity the player is fighting.
        """
        print(DIVIDER)
        print("--- COMBAT STARTED ---")
        
        while self.player.is_alive and enemy.is_alive:
            # Player Turn
            print(f"\n{self.player.name}: {self.player.hp} HP  vs  {enemy.name}: {enemy.hp} HP")
            print("Actions: [A]ttack | [H]eal (Potion) | [R]un")
            action = input(">> ").lower()
            
            if action == 'a':
                msg = self.player.attack(enemy)
                print(msg)
            elif action == 'h':
                self.player.use_potion()
            elif action == 'r':
                # 50% chance to run
                if random.random() > 0.5:
                    print("You escaped successfully!")
                    return
                else:
                    print("Failed to escape!")
            else:
                print("You hesitate... (Turn skipped)")

            # Check if enemy died
            if not enemy.is_alive:
                self.victory(enemy)
                return

            time.sleep(0.5)

            # Enemy Turn
            if enemy.is_alive:
                msg = enemy.attack(self.player)
                print(f"Enemy Turn: {msg}")
                
            # Check if player died
            if not self.player.is_alive:
                self.game_over()
                return

    def victory(self, enemy: Monster) -> None:
        """Handles post-combat rewards."""
        print(f"\nYou defeated the {enemy.name}!")
        self.player.gain_exp(enemy.xp_reward)
        
        # Chance to find items
        if random.random() > 0.6:
            loot = Item("Small Potion", "potion", 20, "Restores HP")
            self.player.inventory.append(loot)
            print(f"You found a {loot.name} on the corpse.")

    def game_over(self) -> None:
        """Handles player death."""
        print(DIVIDER)
        print("You have fallen in battle...")
        print(f"Final Level: {self.player.level}")
        print("GAME OVER")
        print(DIVIDER)
        self.running = False


# --- Main Execution Block ---

def main():
    """
    The entry point of the script. Checks if the script is run directly.
    """
    try:
        engine = GameEngine()
        engine.start_game()
    except KeyboardInterrupt:
        print("\n\nGame force closed. Goodbye!")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
'''

doc=spillter.create_documents([text])

print("len-->",len(doc))
for chunk in doc:
    print(chunk)