# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

Review `app.py` for logic bugs — specifically a reversed hint, a UI issue where
only the submitted guess seems to show after the 2nd click, and any scoring
issues — and point out the exact line numbers.

**What did the agent do?**

Read through `app.py` and identified the following bugs with line references:

| # | Bug | Line(s) |
|---|---|---|
| 1 | Reversed hint messages — `"Too High"` paired with "Go HIGHER" instead of "Go LOWER", and vice versa | 39, 41 (duplicated at 47, 48) |
| 2 | Secret type-flip forces a lexicographic string comparison instead of numeric | 159-162 (triggers except branch at 42-48) |
| 3 | Off-by-one in the win points formula (extra `+ 1`) | 53 |
| 4 | "Too High" branch rewards +5 on even attempt numbers instead of always deducting | 58-61 |
| 5 | Init/reset inconsistency (`attempts = 1` vs. `attempts = 0`); New Game ignores the difficulty range | 97, 136, 137 |
| 6 | Text input key doesn't vary per attempt, so the box doesn't clear after submit | 122-125 |

**What did you have to verify or fix manually?**

Manually traced the attempt-parity logic to confirm the secret-type bug
triggers on guess #1 (not #2 as it first appeared from the UI symptom), by
walking through `attempts` starting at 1 and incrementing before the parity
check. Still need to apply the fixes and re-test each scenario (hint
direction, scoring, new game reset) to confirm no other bugs surface.

**Bug Reproduction Logs**

| Input Used | Expected Behavior | Actual Behavior | Console Error / Output | Suspected Code Location |
|---|---|---|---|---|
| Guess of 60 when secret is 30 | "Too High" hint (📉 Go LOWER) | "📈 Go HIGHER!" hint shown | none | `app.py`, `check_guess` (lines 38-41) |
| Guess of 9 when secret is 10, on an even-numbered attempt | "Too Low" outcome (9 < 10) | "Too High" outcome (wrong, string `"9" > "10"` compares lexicographically) | none | `app.py`, `check_guess` except branch (lines 42-48) + secret stringify (lines 159-162) |
| Win on attempt 1 | Score +90 (`100 - 10*1`) | Score +80 (`100 - 10*(1+1)`) | none | `app.py`, `update_score` (line 53) |
| Wrong guess ("Too High") on attempt 2 | Score -5 | Score +5 | none | `app.py`, `update_score` (lines 58-61) |
| Fresh page load, no guesses yet | "Attempts left: 8" (full limit) | "Attempts left: 7" | none | `app.py`, lines 97, 112 |
| Click "New Game" while Difficulty = Easy | Secret range 1-20 | Secret randomized 1-100 | none | `app.py`, line 137 |
| Submit guess "50", then start typing next guess | Input box empty, ready for new guess | Previous guess "50" still shown in box | none | `app.py`, lines 122-125 |

---

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.

| Edge Case | Prompt Used | AI-Suggested Test | Did It Pass? | Your Reasoning |
|-----------|-------------|-------------------|--------------|----------------|
| | | | | |
| | | | | |
| | | | | |

---

## Linting & Style (SF9)

> Document your use of AI for linting or code style improvements.

**Prompt used:**

```
<!-- Paste the prompt you gave the AI -->
```

**Linting output before:**

```
<!-- Paste relevant linter warnings/errors -->
```

**Changes applied:**

<!-- Describe what you changed based on the AI's suggestions -->

---

## Model Comparison (SF11)

> Compare two AI models on the same task.

**Task given to both models:**

<!-- Describe what you asked each model to do -->

| | Model A | Model B |
|-|---------|---------|
| **Model name** | | |
| **Response summary** | | |
| **More Pythonic?** | | |
| **Clearer explanation?** | | |

**Which did you prefer and why?**

<!-- Your conclusion -->
