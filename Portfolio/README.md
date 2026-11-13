# Code Review

## Week 2 Code Review

I was given suggestions on my transaction class. At first I created a transaction class including all working functions, but they do not actually apply on the accounts created in other modules. Than I imported other modules to make transaction to have effects to the accounts.

## Week 3 Code Review

1. improved validation in the constructor of objects
2. added type hints in the initializer
3. added the list to store clients for account owner

## Week 4 Code Review

1. Start creating the uml diagram
2. Complete the code for Necromancer, add doc string, type hints, return type to make the code more readable

    ```python
        def dismiss_undead(self, undead_id):
        if lib.find_undead(undead_id, self.__collection) != -1:
            self.__collection.remove(lib.find_undead(undead_id, self.__collection))
            return True

        print("No such undead")
        return False
    ```

3. Complete the finance system code
4. Prepare for next weeks review

## Week 5 Code Review

1. Doc string for all functions need to be added
2. Create and finish the UML diagram, for the Necromancer project
3. Do noy use __ in the UML, since it is already implied with "-" to show it is private
4. Go through all the multiplicity
5. Do not add the __init__ and __str__ in the UML diagram
6. Add all the necessary method to the UML diagram
7. Add labels for association in the UML diagram
8. Add formatter to the code to make it easier to read and more organized
9. Add __str__ and __repr__ to all the classes
10. Fix the constructor for Necromancer, so that the amount of resource to start with is manually entered.
11. Fix the way of assigning ID to Necromancer. Necromancer should get auto incremented ID, not manually entered ID

    ```python
        def __init__(self, name: str, necrotic):
            self.__name = name if lib.is_valid_string(name) else "Name is error"
            self.__resource_object = Resources(10, 10, 10, 10, 50)
            self.__collection = []
            self.__id = id if lib.is_valid_integer(id) else "Error"
    ```

## Week 6 Code Review

1. Make sure the code and the UML diagram matches
2. Return a copy of a list, not list itself

    ```python

        def __init__(self, name: str, necrotic: int, spirit: int, bone: int, flesh: int, ectoplasm: int) -> None:

            self.__name = name if lib.is_valid_string(name) else "Name is error"
            self.__resource_object = Resources(
                necrotic, spirit, bone, flesh, ectoplasm)
            self.__collection = []

        def get_collection(self) -> list:
            """Gets the collection of Necromancer's summoned undead and returns it"""
            return self.__collection.copy()
    ```

3. Remove the redundant code like display, since __str__ exists
4. Make the test code in main file to test all the behaviour
5. Show evidence of code in README
6. Include all required document
S

## Week 7 Code Review

1. I was given suggestions on how to use inheritance for deposit and withdrawal in the Finance project. Both account types use the same deposit and withdrawal methods from `Account`. The child classes only add their own withdrawal checks. This means the balance and the transaction history are updated in one place. The Week 8 files show the result of this change.

    ```python
    def deposit(self, amount: int | float) -> bool:
        """Add the amount and record the deposit.

        Return False and leave the balance and history unchanged.
        """
        if not self.valid_amount(amount):
            print("Deposit amount must be a positive number.")
            return False
        self.__balance += amount
        self.__record_transaction("deposit", amount)
        return True

    def withdrawal(self, amount: int | float) -> bool:
        """Withdraw the amount and record the transaction.

        Return False without changing the balance or transaction history
        if the withdrawal is rejected.
        """
        if not self.valid_withdrawal(amount):
            return False
        # Wait for the account checks before changing the balance.
        self.__balance -= amount
        self.__record_transaction("withdrawal", amount)
        return True
    ```

    ```python
    def valid_withdrawal(self, amount: int | float) -> bool:
        """Check that enough money will remain after the withdrawal."""
        if not super().valid_withdrawal(amount):
            return False
        if self.Balance - amount < self.MINIMUM_BALANCE:
            print("The account would fall below the minimum balance.")
            return False
        return True
    ```

2. I was also advised to make the Necromancer main file feel more like a game. The updated main lets the player choose what to do, such as collect resources or choose a ritual. It still uses the existing classes to do the work, and the player can try again if a ritual fails.

    ```python
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
    ```

## Week 8 Code Review

1. Put the effects of a card into a list and executing them one by one. In CardGame, Shield Bash uses a damage effect first and an armour effect second. The same loop can also work for cards with a different list of effects.

    ```python
    def create_shield_bash() -> AttackCard:
        """Create a fresh card that attacks and grants armour."""
        return AttackCard(
            id=2,
            name="Shield Bash",
            description="Deal 6 damage plus power. Gain 4 armour.",
            cost=2,
            effects=[
                DamageEffect("Damage", "Deal damage.", 6),
                ArmourEffect("Armour", "Gain armour.", 4),
            ],
        )
    ```

    ```python
    def apply_effects(self, user, target):
        results = []

        for effect in self.__effects:
            result = effect.apply(user, target)
            results.append(result)

        return results
    ```

2. Use a dictionary to store effects. The enemy now uses the action name as the key and a list of effects as the value. This lets the enemy look up the effects for its current action.

    ```python
    self.__actions = {
        "attack": [
            DamageEffect("Attack", "Deal damage.", self.__attack_damage),
        ],
        "guard": [
            ArmourEffect("Guard", "Gain armour.", armour_amount),
        ],
        "heal": [
            HealEffect("Heal", "Restore health.", heal_amount),
        ],
        "multi_attack": []
    }
    ```

    ```python
    for effect in self.__actions[self.__intent]:
        if not target.is_alive():
            break

        results.append(effect.apply(self, target))
    ```

## Week 9 Code Review

1. I was given suggestions to add different tests instead of only checking when an operation succeeds. The Finance tests check both sides of the savings minimum: when the remaining balance is exactly 1000, the withdrawal works; when it would go below 1000, the balance and transaction list stay the same.

    ```python
    def test_savings_can_reach_minimum_balance(savings):
        assert savings.withdrawal(2000)
        assert savings.Balance == 1000
        assert savings.transaction_count() == 1


    def test_savings_cannot_go_below_minimum_balance(savings):
        assert savings.withdrawal(2001) is False
        assert savings.Balance == 3000
        assert savings.TransactionCollection == []
    ```

2. The tests also use a client with two different account types. The same withdrawal amount is accepted by one and rejected by the other. The test checks both the balances and the number of transactions.

    ```python
    def test_accounts_with_different_rules_share_the_same_operation(
        client_with_accounts
    ):
        accounts = [client_with_accounts.get_account(n) for n in (101, 102)]
        assert [account.withdrawal(2500) for account in accounts] == [
            False, True
        ]
        assert [account.Balance for account in accounts] == [3000, 5500]
        assert [account.transaction_count() for account in accounts] == [0, 1]
    ```

## Week 10 Code Review

1. Add tests to my own project, CardGame. One test
   checks that an unaffordable card stays in the player's hand, and that the
   player's energy and the enemy's health and armour do not change.

    ```python
    def test_payment_failure_preserves_state(
        battle, player_with_deck_strike_mend, enemy, strike
    ):
        player = player_with_deck_strike_mend
        player.spend_energy(2)
        hand_before = player.hand_pile

        assert battle.play_card(strike) is False
        assert player.energy == 1
        assert player.hand_pile == hand_before
        assert player.discard_pile == []
        assert enemy.health == 20
        assert enemy.armour == 3
    ```

2. Another test checks that the Warrior can use the skill again after the enemy's turn and that the damage uses the Warrior's new armour value.

    ```python
    def test_skill_refreshes_after_enemy_turn_and_uses_new_armour(warrior):
        enemy = Enemy("Guardian", 100, 0, 0, attack_damage=5)
        battle = Battle(warrior, enemy)
        battle.start_battle()
        assert battle.use_skill() is True
        assert enemy.health == 92

        assert battle.end_turn() is True
        assert warrior.armour == 3
        assert warrior.health == 50
        assert not battle.skill_used
        assert battle.use_skill() is True
        assert enemy.health == 89
        assert warrior.armour == 3
    ```
