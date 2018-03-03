from graders.match_flag import match_flag
correct_flag="mUtUal_aUth_2way_sTreeT"
def grade(team, key):
    if match_flag(key, correct_flag):
        return True, 'You got it!'
    else:
        return False, 'You didnt.'
