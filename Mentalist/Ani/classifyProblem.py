answers = [["Meet up with friends", "Go out by yourself", "Stay at home alone", "Lie in bed all day"],
                [ "Not really", "Once in a while", "Yes, all the time"],
                [ "Not really", "Tolerable amount", "Yes, very high"],
                [">5-6 hrs", "3-5 hrs", "1-3 hrs", "<1 hr"],
                ["Yes", "No"]]


def classify(scores):
    if scores[1] == 5:
        return "addiction"
    elif scores[2] == 5:
        return "stress"
    else:
        total = 0
        for s in scores:
            total += s
        total = total/5
        if total < 12.5:
            return "burnout"
        else:
            return "depression"