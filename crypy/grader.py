from graders.match_flag import match_flag
correct_flag="CryPy_aInt_thaT_brigHt"
def grade(team, key):
    if match_flag(key, correct_flag):
        return True, 'You got it!'
    else:
        return False, 'You didnt.'
