from statistics import mean

def game_score_analysis(scores):
    # Stage 1 : Normalizing the data
    a = min(scores)
    b = max(scores)
    if b == a:
        return 0
    score = [(x-a)/(b-a) for x in scores]

    # Stage 2 : Trend analysis
    performance = 0
    for i in range(len(scores)-1):
        if score[i] > score[i+1]:
            performance -= (score[i]-score[i+1])
        else:
            performance += (score[i+1]-score[i])

    growth_rate = round(performance*100,2)
    return growth_rate

pool = {
    "intro":{
        1: [
            "What is your age?",
            "What is your gender?",
            "How are you feeling today?",
            "Have u ever consulted a psychologist before?"],
        2: [
            "How active do you feel today?",
            "How dependant are you on substances?",
            "How much pressure are you under?",
            "How many hours can you work at a time?",
            "How motivated are you to do work?"]

    },
    "depression" : {
        3: [
            "In the past two weeks, how often have you felt, down, depressed, or hopeless?",
            "Have you had any thoughts of suicide?",
            "How is your sleep?",
            "How is your energy?",
            "Do you prefer to stay at home rather than going out and doing new things?"
        ],
        4: [
            "Little interest or pleasure in doing things?",
            "Feeling down, depressed, or hopeless?",
            "Trouble falling or staying asleep, or sleeping too much?",
            "Feeling tired or having little energy",
            "Poor appetite or overeating?"
        ],
        5: [
            "How much of a change have u seen in yourself after our sessions?",
            "Feeling bad about yourself -- or feel that your a failure or have let yourself of your family down?",
            "Trouble concentrating or things such as reading the newspaper or watching television?",
            "Moving or speaking so slowly that other people could have noticed? Or the opposite -- being so fidgety or restless that you have been moving around a lot more than usual",
            "Thoughts that you would be better off dead of of hurting yourself in some way or the other"
        ]
    },
    "addiction" : {
        3: ["Have you used drugs other than those required for medical reasons?",
            "Do you abuse more than one drug at a time?",
            "Are you unable to stop using drugs when you want to?",
            "Have you ever had blackouts or flashback as a result of drug use?",
            "Do you ever feel bad or guilty about your involvement with drugs?"
            ],
        4: ["How much in control are you of yourself after the last session?"
            "Have you neglected your family because of your use of drugs?",
            "Have you ever experienced withdrawal symptoms when you stopped taking drugs?",
            "Have you had medical problems as a result of your drug use <eg. memory loss, hepatitis, convulsions, bleeding?",
            "Have you engaged in illegal activities in order to obtain drugs?"
            ],
        5: [
            "How much of a change have u seen in yourself after our sessions?",
            "Feeling bad about yourself -- or feel that your a failure or have let yourself of your family down?",
            "Trouble concentrating or things such as reading the newspaper or watching television?",
            "Moving or speaking so slowly that other people could have noticed? Or the opposite -- being so fidgety or restless that you have been moving around a lot more than usual",
            "Thoughts that you would be better off dead of of hurting yourself in some way or the other"
        ]
    },
    "stress" : {
        3: [
            "Do you experience excessive worry?",
            "Is your worry excessive in intensity, frequency, or amount of distress it causes?",
            "Do you find it difficult ot control the worry < or stop worrying > once it starts?",
            "Do you worry excessively or uncontrollably about minor things such as being late for an appointment, minor repairs, homework, etc.?",
            "Do you ever feel the need to take sleeping pills?"
        ],
        4: [
            "I’ve had trouble on the job because of my temper",
            "People tell me that I become too angry, too quickly",
            "After arguing with someone, I often hate myself for losing my temper",
            "I find it very hard to forgive someone who has done me wrong.",
            "I hate lines, and I especially hate waiting in lines"
        ],
        5: [
            "In the past two weeks, how often have you felt, down, depressed, or hopeless?",
            "Have you had any thoughts of suicide?",
            "How is your sleep?",
            "How is your energy?",
            "Do you prefer to stay at home rather than going out and doing new things?"
        ]
    },
    "burnout" : {
        3: ["I’ve had trouble on the job because of my temper",
            "People tell me that I become too angry, too quickly",
            "After arguing with someone, I often hate myself for losing my temper",
            "I find it very hard to forgive someone who has done me wrong.",
            "I hate lines, and I especially hate waiting in lines"
            ],
        4: ["Do you feel any change in you after the last session",
            "At times I have gotten so angry that I have slammed doors, thrown things, broken items or punched walls",
            "I am apt to take frustration so badly, I cannot get it out of my mind.",
            "I still get angry when I think of the bad things people did to me in the past",
            "I often make critical, judgmental comments to others, even if they do not ask me for advice or help"
            ],
        5: ["After the last session, how often do u nend up in arguments?",
            "When riled, I often blurt out things I later regret saying",
            "People I’ve trusted have often let me down, leaving me feeling angry or betrayed",
            "I use abusive language, such as name-calling, insults, sarcasm or swearing",
            "I’m an angry person. My temper has already caused lots of problems, and I need help changing it"
            ]
    }
}
# depression, burnout, anxiety, addiction

def get_session_question_count(keyword, session):
    filter1 = pool[keyword]
    question_set = filter1[session]
    return len(question_set)

def get_next_question(keyword, session, count):
    filter1 = pool[keyword]
    question_set = filter1[session]
    return question_set[count]

def analysis_per_session(answers):
    """
    2 = Still needs sessions
    1 = Improved after previous session
    0 = Significant improvement
    """
    no = len(answers)
    p = sum(answers)
    if p >= 3.5*no:
        result = [2]
    elif p >= 2.52*no and p < 3.5*no:
        result = [1]
    elif p < 2.52*no:
        result = [0]
    result.append((p/(5*no))*100)
    return result

def overall_analysis(session_scores):
    """
    2 = Patient needs consultation
    1 = Patient might still face some issue (conduct expert survey)
    0 = Patient is healthy
    """
    no = len(session_scores)
    p = sum(session_scores)
    if p > 52.5:
        result = [2]
    elif p > 37.82 and p < 52.5:
        result = [1]
    elif p < 37.82:
        result = [0]
    result.append((p/75)*100)
    return result

#print(analysis_per_session([3,4,3,4,4,3]))
#print(overall_analysis([17,18,18]))

