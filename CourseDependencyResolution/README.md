# Course Dependency Resolution

## Project Overview
This project provides a Python implementation of a Course Dependency Resolution algorithm. It is designed to help students plan their learning paths by resolving course prerequisites and optimizing course completion time.

## Features
- **Graph-Based Course Representation**: Courses and their prerequisites are represented as nodes in a directed graph.
- **Cycle Detection**: Detects circular dependencies among courses.
- **Topological Sorting**: Generates a valid order for course completion based on prerequisites.
- **Course Completion Optimization**: Calculates the total time to complete all courses in sequence.

## Approach
The algorithm uses a directed graph to represent courses and their prerequisites. Each course is a node, and a directed edge from one course to another represents a prerequisite relationship.

### Cycle Detection
We use Depth-First Search (DFS) to detect cycles in the graph. If a cycle is found, it indicates that there are circular dependencies among courses, which is not feasible in a real-world scenario.

### Topological Sorting
Once we have verified that there are no cycles, we perform a topological sort on the graph. This sorting provides us with an order in which students can complete courses, respecting all prerequisite requirements.

### Optimization
The current implementation assumes that courses are completed sequentially. The `optimize_course_path` function calculates the total time to complete all courses based on their individual lengths.

## Assumptions
- **Sequential Course Completion**: The current optimization assumes that courses are taken one after another without parallel enrollment.
- **No Parallel Enrollment**: The algorithm does not currently support taking multiple courses concurrently.
- **Course Lengths**: The course lengths provided are assumed to be the only factor in determining the total completion time.

## Getting Started
To run this project, you will need Python 3.x. No additional libraries are required.

## Usage
Define your course list and prerequisites, then run the script to get the optimized course path.

## Example:
course_list = ['Math', 'Physics', 'Chemistry']
prerequisites_list = [('Physics', 'Math'), ('Chemistry', 'Physics')]
course_lengths = {'Math': 10, 'Physics': 20, 'Chemistry': 30}

# The script will output the optimized course path
