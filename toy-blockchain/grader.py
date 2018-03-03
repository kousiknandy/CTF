from graders.match_flag import match_flag

correct_flag="Bl0CK_chaIn_Ea5Y_to_CreAte"

def grade(team, key):
    if match_flag(key, correct_flag):
        return True, 'You got it!'
    else:
        return False, 'You didnt.'
