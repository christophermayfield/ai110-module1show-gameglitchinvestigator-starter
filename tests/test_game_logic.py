from logic_utils import check_guess, update_score

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"

def test_update_score_win():
    # Test scoring when winning on the first attempt
    new_score = update_score(0, "Win", 1)
    assert new_score == 80  # 100 - 10 * (1 + 1) = 80

def test_update_score_wrong():
    # Test scoring when wrong guess, should not change score
    new_score = update_score(50, "Too High", 2)
    assert new_score == 50
