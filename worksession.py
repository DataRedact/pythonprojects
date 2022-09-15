# There are n tasks assigned to you. The task times are represented as an integer array tasks of length n, where the ith task takes tasks[i] hours to finish. A work session is when you work for at most sessionTime consecutive hours and then take a break.

# You should finish the given tasks in a way that satisfies the following conditions:

# If you start a task in a work session, you must complete it in the same work session.
# You can start a new task immediately after finishing the previous one.
# You may complete the tasks in any order.
# Given tasks and sessionTime, return the minimum number of work sessions needed to finish all the tasks following the conditions above.

# The tests are generated such that sessionTime is greater than or equal to the maximum element in tasks[i].

from requests import session


def minSessions(tasks, sessionTime):
    timeNeeded = sum(tasks)
    if timeNeeded <= sessionTime:
        return 1
    sessions = 0
    culmSum = 0
    for i in range(len(tasks)):
        culmSum += tasks[i]
        print(culmSum)
        if culmSum == sessionTime:
            sessions += 1
            
            culmSum = 0
        elif culmSum > sessionTime:
            sessions += 1
            culmSum -= sessionTime
    return sessions
        
print(minSessions([3,1,3,1,1], 8))

        
