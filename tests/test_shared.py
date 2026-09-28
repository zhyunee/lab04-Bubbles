def test_funded_account_starts_with_1000(funded_account):
    assert funded_account.balance == 1000


def test_funded_account_deposit(funded_account):
    funded_account.deposit(200)
    assert funded_account.balance == 1200