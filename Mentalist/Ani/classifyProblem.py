intro = {
    1: ["What is your age?", "What is your gender?", "How are you feeling today?", "Have u ever consulted a psychcologist before?"],
    2: ["What do you feel like doing?", "Do you feel like you need to depend on substances?", "Are you under a lot of pressure?", 
        "How long can you work for at a time?", "Do you have any motivation to do work?"]
}
answers = [["Meet up with friends", "Go out by yourself", "Stay at home alone", "Lie in bed all day"], 
                [ "Not really", "Once in a while", "Yes, all the time"], 
                [ "Not really", "Tolerable amount", "Yes, very high"], 
                [">5-6 hrs", "3-5 hrs", "1-3 hrs", "<1 hr"], 
                ["Yes", "No"]]


def classify(scores):
    if scores[1] == 3:
        return "addiction"
    elif scores[2] == 3:
        return "stress"
    else:
        total = 0
        for s in scores:
            total += s
        total = total/5
        if total < 7.5:
            return "burnout"
        else:
            return "depression"