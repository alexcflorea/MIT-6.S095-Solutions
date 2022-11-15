#Programming for the Puzzled -- Srini Devadas
#The Best Time to Party
#Given a list of intervals when celebrities will be at the party
#Output is the time that you want to go the party when the maximum number of
#celebrities are still there.
#Clever algorithm that will work with fractional times

sched = [(6, 8), (6, 12), (6, 7), (7, 8), (7, 10), (8, 9), (8, 10), (9, 12), (9, 10), (10, 11), (10, 12), (11, 12)]
sched2 = [(6.0, 8.0), (6.5, 12.0), (6.5, 7.0), (7.0, 8.0), (7.5, 10.0), (8.0, 9.0), (8.0, 10.0), (9.0, 12.0), (9.5, 10.0), (10.0, 11.0), (10.0, 12.0), (11.0, 12.0)]
sched3 = [(6, 7), (7,9), (10, 11), (10, 12), (8, 10), (9, 11), (6, 8), (9, 10), (11, 12), (11, 13), (11, 14)]


def bestTimeToPartyEfficient(schedule):
    
    maxcount = 0
    time = 0
    
    #Convert schedule to list of start times and end times marked as such
    for i in range(len(schedule)):
        rcount = 0
        for c in schedule:
            start = schedule[i][0]
            if start >= c[0] and start < c[1]:
                rcount += 1
        if rcount > maxcount:
            maxcount = rcount
            time = start

    #Output best time to party
    print ('Best time to attend the party is at', time, 'o\'clock', ':', maxcount, 'celebrities will be attending!')
    


# bestTimeToPartyEfficient(sched)
# bestTimeToPartyEfficient(sched2)
bestTimeToPartyEfficient(sched3)