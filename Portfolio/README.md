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
