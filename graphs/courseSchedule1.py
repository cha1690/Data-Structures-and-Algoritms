def canFinish(numCourses, prerequisistes):
    courseList = [0 for _ in range(numCourses)]
    courseDict = collections.defaultDict(List)

    for courses in prerequisistes:
        course, prereq = courses
        courseDict[course].append(prereq)

    for i in range(numCourses):
        if not dfs(courseList, courseDict, i):
            return False
    return True

def dfs(visited, graph, course_index):
    if visited[course_index] == -1:
        return False

    if visited[course_index] == 1:
        return True

    visited[course_index] = -1

    if course_index in graph:
        for neighbor in graph[course_index]:
            if not dfs(visited,graph,neighbor):
                return False

    visited[course_index] = 1

    return True






