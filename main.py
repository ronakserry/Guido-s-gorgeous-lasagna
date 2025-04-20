#let's bake lasagna together 
#they are all in minutes
EXPECTED_BAKE_TIME=40
PREP_TIME=2

def bake_time_remaining(elapsed_bake_time):
    return EXPECTED_BAKE_TIME-elapsed_bake_time

def prepartion_in_minutes(layers):
    return PREP_TIME*layers

def elapsed_time_in_minutes(layers, elapsed_bake_time):
    pass

