# the case where every mentor has a specific capacity if studets they can take in
m, n = map(int, input().split())
mentor_prefs = [list(map(int, input().split())) for _ in range(m)]
student_prefs = [list(map(int, input().split())) for _ in range(n)]
mentor_cap = list(map(int, input().split()))

def gale_shapley_with_capacity(m, n, mentor_prefs, student_prefs, mentor_cap):
    # Each mentor can accept up to mentor_cap[i] students
    free_mentors = list(range(m))
    current_matches = {i: [] for i in range(m)}  # mentor -> list of students
    student_match = [-1] * n                     # student -> mentor
    proposals = [set() for _ in range(m)]        # track whom each mentor has proposed to

    while free_mentors:
        mentor = free_mentors[0]
        for student in mentor_prefs[mentor]:
            if student not in proposals[mentor]:
                proposals[mentor].add(student)

                # Student is free → accept immediately
                if student_match[student] == -1:
                    student_match[student] = mentor
                    current_matches[mentor].append(student)

                    # Mentor full? remove from free list
                    if len(current_matches[mentor]) == mentor_cap[mentor]:
                        free_mentors.pop(0)
                    break

                # Student already matched → check preference
                else:
                    other_mentor = student_match[student]
                    if student_prefs[student].index(mentor) < student_prefs[student].index(other_mentor):
                        # Student prefers new mentor
                        student_match[student] = mentor
                        current_matches[mentor].append(student)
                        current_matches[other_mentor].remove(student)

                        # Add old mentor back if they now have space
                        if len(current_matches[other_mentor]) < mentor_cap[other_mentor]:
                            if other_mentor not in free_mentors:
                                free_mentors.append(other_mentor)

                        # Mentor full? remove
                        if len(current_matches[mentor]) == mentor_cap[mentor]:
                            free_mentors.pop(0)
                        break
        else:
            # Mentor has proposed to everyone → remove
            free_mentors.pop(0) # covers the case of unequal numbers

    return current_matches, student_match


matches, student_match = gale_shapley_with_capacity(m, n, mentor_prefs, student_prefs, mentor_cap)
for mentor in range(m):
    print(f"Mentor {mentor} ({mentor_cap[mentor]} slots) → {matches[mentor]}")
for s, mentor in enumerate(student_match):
    if mentor == -1:
        print(f"Student {s} ↔ No match")
    else:
        print(f"Student {s} ↔ Mentor {mentor}")