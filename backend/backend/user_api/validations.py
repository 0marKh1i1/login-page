from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
UserModel = get_user_model()

def custom_validation(data):
    
    username = data.get('username', '').strip()
    password = data.get('password', '').strip()
    ##
    if not password or len(password) < 8:
        raise ValidationError('choose another password, min 8 characters')
    ##
    if not username:
        raise ValidationError('choose another username')
    return data

def validate_username(data):
    username = data.get('username', '').strip()
    if not username:
        raise ValidationError('choose another username')
    return True

def validate_password(data):
    password = data.get('password', '').strip()
    if not password:
        raise ValidationError('a password is needed')
    return True