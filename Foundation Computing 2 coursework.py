import random


PURPLE = "\033[0;35m"
GREEN = "\033[0;32m"
RED = "\033[0;31m"
RESET = "\033[0m"

# the player, goal and enemy classes are made here
class mainCharacter:
    def __init__(self, icon, health, score):
        self.icon = icon
        self.health = health
        self.score = score
        self.x = random.randint(0, 19)
        self.y = random.randint(0, 19)

class Finish:
    def __init__(self, icon):
        self.icon = icon
        self.x = random.randint(0, 19)
        self.y = random.randint(0, 19)

class Attacker:
    def __init__(self, icon, damage):
        self.icon = icon
        self.damage = damage
        self.x = random.randint(0, 19)
        self.y = random.randint(0, 19)

#enemy movement 
    def move(self):
        direction = random.choice(["up", "down", "left", "right"])

        if direction == "up":
            if self.x > 0:
                self.x -= 1
        elif direction == "down":
            if self.x < 19:
                self.x += 1
        elif direction == "left":
            if self.y > 0:
                self.y -= 1
        elif direction == "right":
            if self.y < 19:
                self.y += 1


###########################################################################################################

player = mainCharacter("P", 100, 0)
goal = Finish("G")


enemies = []


for _ in range(9):
    enemies.append(Attacker(f"{RED}E{RESET}", 9))


def print_grid():
    grid_size = 20
    grid = [["#"] * 20 for _ in range(grid_size)]

    grid[player.x][player.y] = f"{GREEN}{player.icon}{RESET}"
    grid[goal.x][goal.y] = f"{PURPLE}{goal.icon}{RESET}"

    
    for enemy in enemies:
        grid[enemy.x][enemy.y] = enemy.icon

    
    for row in grid:
        print(" ".join(row))


def move():
    print("MOVE USING w/a/s/d")
    move_choice = input("> ")

    
    if move_choice == "w" and player.x > 0:
        player.x -= 1
    elif move_choice == "a" and player.y > 0:
        player.y -= 1
    elif move_choice == "s" and player.x < 19:
        player.x += 1
    elif move_choice == "d" and player.y < 19:
        player.y += 1


    # player losing health everytime they move 
    player.health -= 1
    print(f"Health: {player.health}")

    # this part checks if player is over enemy and makes them lose health when it happens 
    global enemies
    for enemy in enemies[:]:
        if player.x == enemy.x and player.y == enemy.y:
            player.health -= enemy.damage
            enemies.remove(enemy)  
            print(f"You stepped on an enemy! You lost {enemy.damage} health.")
            break  

    
    for enemy in enemies:
        enemy.move()

def win():
    if player.x == goal.x and player.y == goal.y:
        print("Congratulations you have won!")
        quit()

while player.health > 0:
    print_grid()
    print(f"Health: {player.health}")
    move()
    win()

   
    if player.health <= 0:
        print("You have lost!")
        break
    
