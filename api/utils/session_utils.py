from flask import session

def is_logged():
    if session:
        return True
    else:
        return False
    
def verify_user(user_id):
    if session['user_id']==user_id:
        return True
    else:
        return False

def is_owner(user_id):
    if session['user_id']==user_id:
        return True
    else:
        return False