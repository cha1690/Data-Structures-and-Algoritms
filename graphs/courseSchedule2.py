def canFinish(numCourses, prerequisistes):
    courseList = [0 for _ in range(numCourses)]
    courseDict = collections.defaultDict(List)

    for courses in prerequisistes:
        course, prereq = courses
        courseDict[course].append(prereq)

    courseSeq=[]
    for i in range(numCourses):
        if not dfs(courseList, courseDict, i, courseSeq):
            return False
    return True

def dfs(visited, graph, course_index, courseSeq):
    if visited[course_index] == -1:
        return False

    if visited[course_index] == 1:
        return True

    visited[course_index] = -1

    if course_index in graph:
        for neighbor in graph[course_index]:
            if not dfs(visited,graph,neighbor, courseSeq):
                return False

    visited[course_index] = 1
    courseSeq.append(course_index)
    return True
