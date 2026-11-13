# clients: client number, name, telephone number, dateofJoin, age
# client method: change contact detail

from client import Client
from account import Account
from transaction import Transaction
from branch import Branch

client1 = Client(1, "John", "00000001", "2026/08/05", 20, True)
client2 = Client(2, "May", "00000010", "2026/08/06", 19, True)
client3 = Client(3, "Chen", "00000011", "2026/08/07", 21, False)


account1 = Account(1, "individual", 1000, 1)
account2 = Account(2, "business", 100000, 2)
account3 = Account(3, "charity", 5000, 3)

client1.display_client()
account1.display_account()
account1.deposit(30)
account1.display_account()
account1.withdrawal(2000)
account1.display_account()


trans1 = Transaction("deposit", 100, "A business transaction")
trans1.confirm_transfer(account1)
trans1.display_transaction()


branch1 = Branch(1, "Adelaide branch", "Adelaide", "00001111")
branch2 = Branch(2, "Melbourne branch", "Melbourne", "11110000")

branch1.display_branch()
branch2.display_branch()

branch1.open_branch()
branch2.update_phone("12345678")
branch2.display_branch()