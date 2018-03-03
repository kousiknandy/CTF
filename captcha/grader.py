from graders.match_flag import match_flag
correct_flag="sCrIpt_paSSed_TurIng_TeSt"
def grade(team, key):
    if match_flag(key, correct_flag):
        return True, 'You got it!'
    else:
        return False, 'You didnt.'
