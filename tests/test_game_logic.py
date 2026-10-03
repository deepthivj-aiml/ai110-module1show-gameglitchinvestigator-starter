from logic_utils import check_guess, update_score

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"

def test_win_on_first_attempt_scores_90_not_80():
    # Regression test for the off-by-one bug: formula used to be
    # 100 - 10 * (attempt_number + 1), scoring 80 instead of 90.
    result = update_score(current_score=0, outcome="Win", attempt_number=1)
    assert result == 90

def test_too_high_always_deducts_even_on_even_attempt():
    # Regression test for the parity bug: "Too High" used to add +5
    # instead of -5 when attempt_number was even.
    result = update_score(current_score=0, outcome="Too High", attempt_number=2)
    assert result == -5
