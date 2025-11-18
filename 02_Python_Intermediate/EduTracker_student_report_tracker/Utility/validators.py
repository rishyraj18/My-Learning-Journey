def validate_mark(value):
        if 0 < value >= 100:
            return True
        else:
            return False

def validate_name(value):
        if value.istitle():
            return True
        else:
            return False
        
def validate_roll(value):
        if isinstance(value, int):
            return True
        else:
            return False