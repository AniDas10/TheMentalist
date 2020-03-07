from statistics import mean

def game_score_analysis(scores):
    # Stage 1 : Normalizing the data
    a = min(scores)
    b = max(scores)
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
    "depression" : {
        3: ["Question 1",
            "Question 2",
            "Question 3",
            "Question 4",
            "Question 5"
            ],
        4: ["Question 1",
            "Question 2",
            "Question 3",
            "Question 4",
            "Question 5"
            ],
        5: ["Question 1",
            "Question 2",
            "Question 3",
            "Question 4",
            "Question 5"
            ]
    },
    "addiction" : {
        3: ["Question 1",
            "Question 2",
            "Question 3",
            "Question 4",
            "Question 5"
            ],
        4: ["Question 1",
            "Question 2",
            "Question 3",
            "Question 4",
            "Question 5"
            ],
        5: ["Question 1",
            "Question 2",
            "Question 3",
            "Question 4",
            "Question 5"
            ]
    },
    "phobia" : {
        3: ["Question 1",
            "Question 2",
            "Question 3",
            "Question 4",
            "Question 5"
            ],
        4: ["Question 1",
            "Question 2",
            "Question 3",
            "Question 4",
            "Question 5"
            ],
        5: ["Question 1",
            "Question 2",
            "Question 3",
            "Question 4",
            "Question 5"
            ],
        
    },
    "anxiety" : {
        3: ["Question 1",
            "Question 2",
            "Question 3",
            "Question 4",
            "Question 5"
            ],
        4: ["Question 1",
            "Question 2",
            "Question 3",
            "Question 4",
            "Question 5"
            ],
        5: ["Question 1",
            "Question 2",
            "Question 3",
            "Question 4",
            "Question 5"
            ]
    },
    "burnout" : {
        3: ["Question 1",
            "Question 2",
            "Question 3",
            "Question 4",
            "Question 5"
            ],
        4: ["Question 1",
            "Question 2",
            "Question 3",
            "Question 4",
            "Question 5"
            ],
        5: ["Question 1",
            "Question 2",
            "Question 3",
            "Question 4",
            "Question 5"
            ]
    }
}
# depression, burnout, anxiety, phobia, addiction

def generate_set(keyword, session):
    filter1 = pool[keyword]
    question_set = filter1[session]
    return question_set

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

