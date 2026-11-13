def test_branch_can_open_close_and_keep_valid_phone_number(branch):
    branch.open_branch()
    assert branch.Status == "opened"
    branch.PhoneNumber = "1234"
    branch.PhoneNumber = ""
    assert branch.PhoneNumber == "1234"
    branch.close_branch()
    assert branch.Status == "closed"
    assert "Adelaide" in str(branch)
