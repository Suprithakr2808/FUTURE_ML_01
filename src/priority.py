def assign_priority(text):
    text = text.lower()

    # High priority conditions
    if ("urgent" in text or "immediately" in text or 
        "asap" in text or "server down" in text or 
        "refund" in text):
        return "High"

    # Medium priority
    elif ("not working" in text or "failed" in text or 
          "error" in text):
        return "Medium"

    # Low priority
    else:
        return "Low"