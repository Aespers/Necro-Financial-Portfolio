# clients: client number, name, telephone number, date of Join, age
# client method: change contact detail

from client import Client
from branch import Branch
from transaction import Transaction
from account import Account

# Create Branch objects.
branch1 = Branch(
    1,
    "Adelaide branch",
    "Adelaide",
    "00001111"
)

branch2 = Branch(
    2,
    "Melbourne branch",
    "Melbourne",
    "11110000"
)


# Create Client objects.
client1 = Client(
    1,
    "John",
    "00000001",
    "2026/08/05",
    20,
    True,
    branch1
)

client2 = Client(
    2,
    "May",
    "00000010",
    "2026/08/06",
    19,
    True,
    branch2
)

client3 = Client(
    3,
    "Chen",
    "00000011",
    "2026/08/07",
    21,
    False
)


# Create Account objects.
account1 = Account(1, "individual", 1000, 1)
account2 = Account(2, "business", 100000, 2)
account3 = Account(3, "charity", 5000, 3)


# Link each account to its client.
client1.add_account(account1)
client2.add_account(account2)
client3.add_account(account3)


print("----- CLIENT TESTS -----")

client1.display_client()

print(client1.Contact)

client1.set_contact("00009999")
print(client1.Contact)

# Change client3's preferred branch.
client3.set_preferred_branch(branch1)


print("\n----- ACCOUNT TESTS -----")

account1.display_account()

# Test deposit.
account1.deposit(30)

# Test successful withdrawal.
account1.withdrawal(200)

# Test withdrawal with insufficient balance.
account1.withdrawal(5000)

print(account1)





print("\n----- BRANCH TESTS -----")

branch1.display_branch()
branch2.display_branch()

# Test opening and closing a branch.
branch1.open_branch()
branch1.close_branch()

# Test getting and updating the phone number.
print("Branch 2 phone:", branch2.PhoneNumber)

branch2.PhoneNumber = "12345678"
branch2.display_branch()


