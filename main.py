def email_slicer(email):
    """Extracts the username and domain from an email"""
    username, domain = email.split("@")
    return f"Username: {username}, Domain: {domain}"



