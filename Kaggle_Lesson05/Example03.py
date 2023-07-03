def menu_is_boring(meals):
    """Given a list of meals served over some period of time, return True if the
    same meal has ever been served two days in a row, and False otherwise.
    """
    previous_meal = None
    for meal in meals:
        if meal == previous_meal:
            return True
    else:
        return False