# lab04-Bubbles

## Who Did What

| Member | GitHub Username | File |
|---|---|---|
| Phone Pyae | zhyunee | test_deposit.py |
| Chit Myat Noe | 6705142017-CMN | conftest.py |
| Pyae Pyae Phyo | 6705140068-PPP | test_withdraw.py |
| Eaint Kyar Phyu Linn | Eaint-kpl | test_shared.py |
| Soe Wai Yan Htet | wy69-stack | test_teardown.py |
| Eaindi Linn Moe Oo | Eaindi | test_extra.py |

## Our Merge Conflict

Our group created a merge conflict while multiple group members were editing the same section of README.md at roughly the same time.

The conflict occurred because different group members made changes to the same part of README.md. Git could not automatically determine which changes should be kept.

The conflict markers were:

<<<<<<< HEAD
| Member | GitHub Username | File |
=
| Member | GitHub Username | File |
>>>>>>> other commit

We kept the contributions from all group members in the final README. The conflict markers were removed, and the README was saved with all required rows.

Git could not resolve the conflict automatically because the changes were made to the same part of the same file. Manual resolution was required to combine the contributions correctly.

## Git Contribution Summary

The repository contains contributions from all group members.

Run `git shortlog -sn` to verify the number of commits made by each contributor.

## Reflection Questions

### 1. Why was your push rejected, and how did you fix it?

The push was rejected because another team member had pushed changes to the shared GitHub repository before my push. My local repository was therefore behind the remote repository. I fixed the problem by running `git pull` and then pushing my changes again.

### 2. Why could Git not resolve the README conflict automatically?

Git could not resolve the conflict because multiple group members changed the same part of README.md. Git could not determine automatically which version should be kept, so we had to resolve the conflict manually.

### 3. What is the difference between committing and pushing?

Committing saves a snapshot of changes in the local Git repository. Pushing uploads those commits to the shared GitHub repository so that other group members can see them.

### 4. How do fixtures reduce duplicated setup code in tests?

Fixtures provide reusable setup code for tests. Instead of creating the same object and setup steps in every test, a fixture creates the required setup and provides it to the tests that need it.

## Test Results

The complete test suite was run using:

`python -m pytest -v`

All 8 tests passed successfully.

```text
8 passed

Our Link Url - https://github.com/zhyunee/lab04-Bubbles
