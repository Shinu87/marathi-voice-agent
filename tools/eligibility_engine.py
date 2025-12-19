from tools.scheme_db import SCHEMES

def check_eligibility(profile):
    eligible = []
    for scheme in SCHEMES:
        if profile["income"] <= scheme["income_limit"]:
            eligible.append(scheme["name"])
    return eligible
