from collections import defaultdict
from collections import deque

class CourseNode:
    def __init__(self, course_id):
        self.course_id = course_id
        self.prerequisites = []  # List of prerequisite course nodes

def build_course_graph(course_list, prerequisites_list):
    graph = {}
    for course in course_list:
        graph[course] = CourseNode(course)
    for course, prereq in prerequisites_list:
        graph[course].prerequisites.append(graph[prereq])
    return graph

def detect_cycles(graph):
    visited = set()
    rec_stack = set()

    def dfs(course_id):
        if course_id in rec_stack:
            return True
        if course_id in visited:
            return False
        visited.add(course_id)
        rec_stack.add(course_id)
        for neighbor in graph[course_id].prerequisites:
            if dfs(neighbor.course_id):  # Use course_id to reference the neighbor
                return True
        rec_stack.remove(course_id)
        return False

    for course_id in graph:
        if dfs(course_id):
            return True
    return False

def topological_sort(graph):
    indegree = {node.course_id: 0 for node in graph.values()}  # Use course_id for keys
    for node in graph.values():
        for neighbor in node.prerequisites:
            indegree[neighbor.course_id] += 1  # Increment using neighbor's course_id

    queue = deque([node.course_id for node in graph.values() if indegree[node.course_id] == 0])  # Use course_id
    sorted_courses = []

    while queue:
        course_id = queue.popleft()
        sorted_courses.append(course_id)
        for neighbor in graph[course_id].prerequisites:
            indegree[neighbor.course_id] -= 1  # Decrement using neighbor's course_id
            if indegree[neighbor.course_id] == 0:
                queue.append(neighbor.course_id)  # Append neighbor's course_id

    if len(sorted_courses) == len(graph):
        return sorted_courses
    else:
        return []  # Cycle detected or graph is not connected

def optimize_course_path(sorted_courses, course_lengths):
    # Initialize the total time to 0
    total_time = 0
    # Iterate over the sorted courses
    for course in sorted_courses:
        # Add the length of each course to the total time
        total_time += course_lengths[course]
    # Return the total time as the optimized path
    return total_time

# Example usage
sorted_courses = topological_sort(course_graph)
if sorted_courses:
    optimized_path = optimize_course_path(sorted_courses, course_lengths)
    print("Optimized course path:", optimized_path)
else:
    print("Circular dependency detected or graph is not connected")