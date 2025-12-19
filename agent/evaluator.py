def evaluator(result):
    if not result:
        return "कृपया तुमचे उत्पन्न आणि व्यवसाय सांगा."
    return f"तुम्ही या योजनांसाठी पात्र आहात: {', '.join(result)}"
