# CONTROLLER MODULE FOR SESSION CREATION

import uuid

def generate_session():
    return str(uuid.uuid4())