import unittest
from f_records import Accounts

# this is the initial class before setting the setUp() method
# remove the docstring operators to run it on previous test
"""
class TestAccount(unittest.TestCase):

    def test_original_balance(self):
        # test account before deposit
        account = Accounts()
        self.assertEqual(account.balance, 0)

        # test account after deposit
        account = Accounts(100)
        self.assertEqual(account.balance, 100)


unittest.main()
"""


class TestAccount(unittest.TestCase):

    def setUp(self):
        self.account = Accounts()

    def test_original_bal(self):
        # test balance before depositing
        self.assertEqual(self.account.balance, 0)

        # test balance after depositing
        account = Accounts(100)
        self.assertEqual(account.balance, 100)

    def test_deposit(self):
        # test first deposit in the accout
        self.account.deposit(100)
        self.assertEqual(self.account.balance, 100)

        # test multiple additional deposits
        self.account.deposit(100)
        self.account.deposit(100)
        self.assertEqual(self.account.balance, 300)

    def test_withdrawal(self):

        # test a single withdrawal from the account
        self.account.deposit(1000)
        self.account.withdraw(100)
        self.assertEqual(self.account.balance, 900)


unittest.main()


"""
It only makes sense to make changes to the initial test if the requirements of your program change during 
the development life cycle else, test failures are an implicaation that your new code does not adhere to the
initial requirements of the test, hence it is only plausible that you make your code agree with the rules. 
"""
