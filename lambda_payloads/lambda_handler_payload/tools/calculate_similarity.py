# Function to calculate audio features similarity
def calculate_similarity(features1, features2):
    print('executing: calculate_similarity')
    if features1 is None or features2 is None:
        return float('inf')
    similarity = 0

    for feature in ['danceability', 'energy', 'valence', 'tempo']:
        similarity += abs(features1[feature] - features2[feature])

    return similarity