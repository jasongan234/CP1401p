def main():
    score = float(input("Enter score: "))
    print(score_checker(score))


def score_checker(score):
    if score < 0:
        return "Invalid score"
    elif score > 100:
        return "Invalid score"
    elif score >= 50 and score < 90:
        return "Passable"
    elif score > 90:
        return "Excellent"
    elif score < 50:
        return "Bad"
main()