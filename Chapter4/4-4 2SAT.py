import random
import math
from collections import defaultdict

def read_file(filepath):
    # Given Condition
    with open(filepath, 'r') as f:
        num = int(f.readline())
        
        lines = f.readlines()
        clauses = []
        for line in lines:
            clause = []
            l = line.split()
            clause.append(int(l[0]))
            clause.append(int(l[1]))
            clauses.append(clause)
 
    return clauses
    
def random_assignment(previous_assignment: set, num: int):
    # Generate Random Initial Assignment
    assignment = [None]*num
    for i in range(num):
        assignment[i] = random.choice([True, False])
    
    # Check if in set and recursively generate Assignment
    if assignment not in previous_assignment:
        return random_assignment(previous_assignment, num)
    else:
        return assignment


def check_SAT(clauses, assignment):
    # Check if the assignment satisfies clauses & store to dict
    sat_dict = defaultdict(bool)
    
    for i, clause in enumerate(clauses):
        if clause[0] > 0 and clause[1] > 0:
            sat = assignment[clause[0]-1] or assignment[clause[1]-1]
        elif clause[0] > 0 and clause[1] < 0:
            sat = assignment[clause[0]-1] or not assignment[-clause[1]-1]
        elif clause[0] < 0 and clause[1] > 0:
            sat =  not assignment[-clause[0]-1] or assignment[clause[1]-1]
        else:
            sat = not assignment[-clause[0]-1] or not assignment[-clause[1]-1]
        sat_dict[i] = sat
    
    return sat_dict


def update_assignment(assignment, sat_dict, clauses):
    # Check "sat_dict" to check unsatisfied, visit "Clauses" to update "assignment", check 
    unsat_index = list(sat_dict.values()).index(False)
    
    # Get literal index to change from the clauses
    clause_random_index = random.choice(unsat_index)
    lit1 = abs(clauses[clause_random_index][0])
    lit2 = abs(clauses[clause_random_index][1])
    literal_random_index = random.choice([lit1, lit2])
    
    if assignment[literal_random_index] is True:
        assignment[literal_random_index] = False
    else:
        assignment[literal_random_index] = True
    
    return assignment


def two_SAT(filepath, num):
    clauses = read_file(filepath)

    # tracker for assignments, number of operation
    prev_assignments = set(())
    i = 0
    j = 0
    
    while i < math.ceil(math.log(num, 2)):
        # Choose random initial sssignment, update assignment
        assignment = random_assignment(prev_assignments, num)
        prev_assignments.add(assignment)
        
        while j < 2*num**2:
            sat_dict = check_SAT(clauses, assignment)
            if False not in list(sat_dict.values()):
                print("Satisfiable")
                break
            else:
                assignment = update_assignment(assignment, sat_dict, clauses)
            j += 1
        i += 1
    print("unsatisfiable")

def main():
    two_SAT("Chapter4\\4-4 2SAT1.txt", 100000)
    
if __name__ == '__main__':
    main()