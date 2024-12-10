import random
from time import sleep

def dungeon_crawler():
    print("🕹️ Welcome to Dungeon Crawler!")
    hero_name = input("What is your hero's name? ")
    print(f"\nHello {hero_name}! 🧙‍♂️ You wake up in a dark dungeon. Survive for 10 days and gain as much experience as possible!")
    input("Press Enter to begin your adventure...")

    
    hp = 100
    xp = 0
    days = 0
    spellbook = False
    fireball = False
    superpotion = False

    while days < 10:
        days += 1
        print(f"\n🌞 Day {days}")
        print(f"❤️ Health: {hp}, ✨ XP: {xp}, 🎒 Backpack: {'Spellbook' if spellbook else 'Empty'}{' | Fireball' if fireball else ''}{' | Superpotion' if superpotion else ''}")

        action = input("(F) Fight a goblin or (A) Avoid the fight? ").lower()

        if action == 'f':  # Fight
            print("🚨 You engage in a fight with a goblin...")
            sleep(1.5)  

            if fireball:
                print("🔥 You cast a mighty fireball and incinerated the goblin!")
                xp_gain = random.randint(10, 25)
                xp += xp_gain
                print(f"✨ You gained {xp_gain} XP!")
            else:
                damage = random.randint(20, 35)
                xp_gain = random.randint(10, 25)
                hp -= damage
                xp += xp_gain
                print(f"⚔️ You fought bravely, taking {damage} damage, but gained {xp_gain} XP!")
                if hp <= 0:
                    print("💀 You succumbed to your injuries. Game over!")
                    return

            input("Press Enter to continue...")

            if random.random() < 0.15:  
                superpotion = True
                print("✨ The goblin dropped a glowing superpotion! You put it in your backpack.")

        elif action == 'a':  # Avoid
            print("🛡️ You decided to avoid the fight and explore...")
            sleep(1)  # Delay for exploration

            if random.random() < 0.6:  
                if spellbook or random.random() < 0.5:
                    heal = random.randint(10, 25)
                    hp = min(100, hp + heal)
                    print(f"🍵 You found a healing potion and restored {heal} HP!")
                else:
                    poison = random.randint(10, 30)
                    hp -= poison
                    print(f"☠️ You accidentally drank poison and lost {poison} HP!")
                    if hp <= 0:
                        print("💀 You succumbed to the poison. Game over!")
                        return
            else:
                print("🚶‍♂️ You avoided the fight but found nothing.")

            input("Press Enter to continue...")

        else:
            print("🤷‍♂️ You hesitated and wasted the day.")
            input("Press Enter to continue...")

        # Day 5: Find spellbook
        if days == 5 and not spellbook:
            print("📖 You discovered an ancient spellbook! You now:")
            sleep(1)
            print("- 🔓 Know how to identify poisonous potions (all potions are now healing).")
            print("- 🔥 Can learn fireball at 100 XP (no health loss in fights).")
            print("- 🧪 Recognize superpotions that fully restore health.")
            spellbook = True
            input("Press Enter to continue...")

        # Unlock fireball
        if xp >= 100 and not fireball:
            print("🔥 You've mastered the fireball spell! Goblins are no longer a threat.")
            fireball = True
            input("Press Enter to continue...")

        
        if superpotion:
            use_potion = input("💡 Do you want to drink the superpotion to restore health to 100 HP? (Y/N) ").lower()
            if use_potion == 'y':
                hp = 100
                superpotion = False
                print("🍷 You drank the superpotion and your health is fully restored!")
            else:
                print("🎒 You decided to save the superpotion for later.")
            input("Press Enter to continue...")

        # End of the day
        print("💤 You rest for the night...")
        sleep(2)

    # End of game
    print(f"\n🎉 Congratulations, {hero_name}! You survived the dungeon!")
    print(f"🏆 Final Stats: ❤️ Health: {hp}, ✨ XP: {xp}")
    if xp == 0:
        print("Game Over! You escaped but gained no experience. 😔")
    else:
        print("✨ You are victorious! 🏅")

# Start the game
while True:
    dungeon_crawler()
    if input("\n🔁 Play again? (Y/N) ").lower() != 'y':
        print("👋 Thanks for playing Dungeon Crawler! Goodbye!")
        break
