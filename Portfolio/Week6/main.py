
"""
Play through the core Necromancer features.

"""

from necromancer import Necromancer
from ritual import Ritual
from skeleton_warrior import SkeletonWarrior
from vengeful_ghost import VengefulGhost
from putrid_zombie import PutridZombie
from phantom_guardian import PhantomGuardian


# Declare all the ritual that exists, giving it all the parameter.
skeleton_ritual = Ritual("Raise Skeleton", "Skeleton Warrior", 35, 25,
                         2, 0, 2, 0, 1, SkeletonWarrior)
ghost_ritual = Ritual("Call Ghost", "Vengeful Ghost", 30, 40,
                      0, 3, 0, 0, 2, VengefulGhost)
zombie_ritual = Ritual("Raise Zombie", "Putrid Zombie", 45, 20,
                       1, 0, 0, 3, 1, PutridZombie)
guardian_ritual = Ritual("Call Guardian", "Phantom Guardian", 50, 35,
                         2, 2, 2, 0, 2, PhantomGuardian)
deathknight_ritual = Ritual(
    "Call Death Knight", "Death Knight", 70, 60, 4, 5, 2, 0, 4)

# Manually creates the necromancer, and manually assigns the amount of the resource to begin with
necro = Necromancer("Morgana", 4, 3, 3, 3, 3)
print("\n=== A necromancer begins the game ===")
print("Necromancer ID:", necro.id)
print(necro)

print("\n=== Summon a Skeleton Warrior ===")
print("Can cast:", skeleton_ritual.check_ritual_require(necro.resources))
print("Cast succeeded:", necro.cast_ritual(skeleton_ritual, 101))
print("Resources after the summon:\n", necro.resources, sep="")

print("\n=== Summon a Vengeful Ghost ===")
print("Cast succeeded:", necro.cast_ritual(ghost_ritual, 102))
print("Resources after the summon:\n", necro.resources, sep="")

print("\n=== Try to summon a Phantom Guardian without enough resources ===")
print("Can cast:", guardian_ritual.check_ritual_require(necro.resources))
print("Cast succeeded:", necro.cast_ritual(guardian_ritual, 103))
print("Resources after the failed attempt:\n", necro.resources, sep="")
print("Undead currently controlled:", len(necro.collection))

print("\n=== Collect resources and try again ===")
necro.resources.collect(spirit=2, bone=1, ectoplasm=2)
print("Resources collected:\n", necro.resources, sep="")
print("Can cast now:", guardian_ritual.check_ritual_require(necro.resources))
print("Cast succeeded:", necro.cast_ritual(guardian_ritual, 103))
print("Resources after the summon:\n", necro.resources, sep="")

print("\n=== Collect resources and summon a Putrid Zombie ===")
necro.resources.collect(necrotic=1, ectoplasm=1)
print("Cast succeeded:", necro.cast_ritual(zombie_ritual, 104))
print("Resources after the summon:\n", necro.resources, sep="")

print("\n=== Try to use an ID that is already in the army ===")
print("Cast succeeded:", necro.cast_ritual(skeleton_ritual, 101))
print("Undead currently controlled:", len(necro.collection))

print("\n=== Give commands to the summoned undead ===")
for creature in necro.collection:
    print(f"#{creature.id} ({type(creature).__name__}): {creature.command()}")

print("\n=== Level up the Skeleton Warrior ===")
for creature in necro.collection:
    if creature.id == 101:
        print("Before:\n", creature, sep="")
necro.level_undead(101)
for creature in necro.collection:
    if creature.id == 101:
        print("After:\n", creature, sep="")

print("\n=== Dismiss the Vengeful Ghost ===")
print("Dismiss succeeded:", necro.dismiss_undead(102))
print("Dismiss the same ID again:", necro.dismiss_undead(102))

print("\n=== Final necromancer, resources, and army ===")
print(necro)
