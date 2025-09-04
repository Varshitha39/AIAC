import re
def is_valid_email(email):
    # Must contain exactly one @
    if email.count('@') != 1:
        return False
    local, domain = email.split('@')
    # Must not start or end with special characters in local or domain
    if not local or not domain:
        return False
    if not local[0].isalnum() or not local[-1].isalnum():
        return False
    if not domain[0].isalnum() or not domain[-1].isalnum():
        return False
    # Must contain at least one dot in domain part
    if '.' not in domain:
        return False
    # No consecutive dots
    if '..' in email:
        return False
    # Only allowed characters: letters, digits, ., -, _
    allowed = re.compile(r'^[A-Za-z0-9._-]+$')
    if not allowed.match(local) or not allowed.match(domain.replace('.', '')):
        return False
    # Domain parts (split by .) must not start or end with hyphen or underscore
    for part in domain.split('.'):
        if not part or not part[0].isalnum() or not part[-1].isalnum():
            return False

    return True