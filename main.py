import re

def valid_email(email):
    match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)

    if match == None:
        return False
    return True


def filter_email(emails):

    email_valido = []
    email_valido = list(filter(valid_email, emails))
    return email_valido



emails= ['rase23@hach.com', 'daniyal@gmail.coma']

filter_email(emails)