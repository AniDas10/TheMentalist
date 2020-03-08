def process_emotions(emotions):
    total = {
        'Fear': 0,
        'Sad': 0,
        'Bored': 0,
        'Happy': 0,
        'Excited': 0,
        'Angry': 0
    }
    length = len(emotions)
    for emotion in emotions:
        total['Fear'] += emotion['Fear']
        total['Sad'] += emotion['Sad']
        total['Bored'] += emotion['Bored']
        total['Happy'] += emotion['Happy']
        total['Excited'] += emotion['Excited']
        total['Angry'] += emotion['Angry']
    total = [(x, y/length) for x, y in total.items()]
    return max(total, key=lambda x: x[1])[0]

def get_emotion(sentence):
    import paralleldots
    paralleldots.set_api_key("AWDCWos9GlVND0R3Pf8L6D3NDjRAKQzDDWsgdtW0Pbw")
    text = sentence.split('.')
    response = paralleldots.batch_emotion(text)
    return process_emotions(response['emotion'])

# if __name__ == '__main__':
#     text=["Choke me daddy"]
#     response=paralleldots.batch_emotion(text)
#     # print(response)
#     print(f'You are {process_emotions(response["emotion"])}')