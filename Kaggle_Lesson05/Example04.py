def estimate_average_slot_payout(n_runs):
    '''Run the slot machine n_runs times and return the average net profit per run.
    Example calls (note that return value is nondeterministic!):
    >>> estimate_average_slot_payout(1)
    -1
    >>> estimate_average_slot_payout(1)
    0.5
    '''
    winings = 0
    for run in range (n_runs):
        winings = winings + run
    winings = winings - n_runs
    return winings/n_runs
estimate_average_slot_payout(10)