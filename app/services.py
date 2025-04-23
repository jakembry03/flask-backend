def classify_task(importance, urgency):
    """Classify a task into the Eisenhower Matrix."""
    if importance == 'low' and urgency == 'low':
        return 'Do Later (Blue)'
    elif importance == 'high' and urgency == 'low':
        return 'Plan (Green)'
    elif importance == 'low' and urgency == 'high':
        return 'Delegate (Yellow)'
    elif importance == 'high' and urgency == 'high':
        return 'Do Now (Red)'
    return 'Unclassified'
