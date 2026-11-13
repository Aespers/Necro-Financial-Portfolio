"""Play the Necromancer game in the terminal."""

from death_knight import DeathKnight
from necromancer import Necromancer
from phantom_guardian import PhantomGuardian
from putrid_zombie import PutridZombie
from ritual import Ritual
from skeleton_warrior import SkeletonWarrior
from vengeful_ghost import VengefulGhost


def show_rituals(rituals: list[Ritual]) -> None:
    """Show the undead that can be summoned and their resource costs."""
    print("\n=== Rituals ===")
    for number, ritual in enumerate(rituals, 1):
        print(f"{number}. {ritual.ritual_name} ({ritual.undead_name})")
        print(
            f"   Necrotic: {ritual.necrotic}, Spirit: {ritual.spirit}, "
            f"Bone: {ritual.bone}, Flesh: {ritual.flesh}, "
            f"Ectoplasm: {ritual.ectoplasm}"
        )


def show_undead(necro: Necromancer) -> None:
    """Show the ID, level and command for each summoned undead."""
    print("\n=== Your undead ===")
    if not necro.collection:
        print("You have not summoned any undead yet.")
    for undead in necro.collection:
        print(f"#{undead.id} | Level {undead.level} | {undead.command()}")


def choose_undead(necro: Necromancer) -> int | None:
    """Return the chosen undead ID, or None if there is no match."""
    show_undead(necro)
    if not necro.collection:
        return None

    choice = input("Enter the undead ID (or press Enter to go back): ").strip()
    for undead in necro.collection:
        if choice == str(undead.id):
            return undead.id

    if choice:
        print("No undead has that ID.")
    return None


def main() -> None:
    """Let the player collect resources and manage their undead."""
    rituals = [
        Ritual("Raise Skeleton", "Skeleton Warrior", 35, 25,
               2, 0, 2, 0, 1, SkeletonWarrior),
        Ritual("Call Ghost", "Vengeful Ghost", 30, 40,
               0, 3, 0, 0, 2, VengefulGhost),
        Ritual("Raise Zombie", "Putrid Zombie", 45, 20,
               1, 0, 0, 3, 1, PutridZombie),
        Ritual("Call Guardian", "Phantom Guardian", 50, 35,
               2, 2, 2, 0, 2, PhantomGuardian),
        Ritual("Call Death Knight", "Death Knight", 70, 60,
               4, 5, 2, 0, 4, DeathKnight),
    ]

    print("=== Necromancer ===")
    name = input("Enter your necromancer's name: ").strip() or "Morgana"
    necro = Necromancer(name, 4, 3, 3, 3, 3)
    next_id = 101
    print(f"Welcome, {necro.name}. Collect resources and raise your army.")

    while True:
        resources = necro.resources
        print("\n=== Choose an action ===")
        print(
            f"Necrotic: {resources.necrotic} | Spirit: {resources.spirit} | "
            f"Bone: {resources.bone} | Flesh: {resources.flesh} | "
            f"Ectoplasm: {resources.ectoplasm}"
        )
        print("1. Collect resources")
        print("2. Cast a ritual")
        print("3. View your undead")
        print("4. Level up an undead")
        print("5. Dismiss an undead")
        print("0. Quit")
        choice = input("> ").strip()

        if choice == "1":
            resources.collect(necrotic=2, spirit=2, bone=2, flesh=2,
                              ectoplasm=2)
            print("You collected 2 of each resource.")
        elif choice == "2":
            show_rituals(rituals)
            selected = input("Choose a ritual (0 to go back): ").strip()
            if selected == "0":
                continue
            if selected not in [str(n) for n in range(1, len(rituals) + 1)]:
                print("Please choose a ritual from the list.")
                continue

            ritual = rituals[int(selected) - 1]
            print(f"Casting {ritual.ritual_name}...")
            # Keep the same ID for the next try if the ritual fails.
            if necro.cast_ritual(ritual, next_id):
                next_id += 1
            else:
                print("Collect more resources and try again.")
        elif choice == "3":
            show_undead(necro)
        elif choice == "4":
            undead_id = choose_undead(necro)
            if undead_id is not None:
                necro.level_undead(undead_id)
                show_undead(necro)
        elif choice == "5":
            undead_id = choose_undead(necro)
            if undead_id is not None and necro.dismiss_undead(undead_id):
                print(f"You dismissed undead #{undead_id}.")
        elif choice == "0":
            print(f"Goodbye, {necro.name}.")
            break
        else:
            print("Please choose an action from the menu.")


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print("\nGame closed.")
