from tools.eligibility_engine import check_eligibility

def executor(action, memory):
    if "income" in memory.data:
        return check_eligibility(memory.data)
    return None
