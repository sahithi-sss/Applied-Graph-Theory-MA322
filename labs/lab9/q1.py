n = int(input())
pref_A = [] #mentor preference lists (space separated student indices)
for _ in range(n):
    pref = list(map(int,input().split()))
    pref_A.append(pref)
pref_B = [] #the preference list of students, containing mentors
for _ in range(n):
    pref = list(map(int,input().split()))
    pref_B.append(pref)

#A contains the pref of mentors, B of students
def GS(n,pref_A, pref_B):
    free_A = list(range(n)) # all mentors are free initially
    current_matches = [-1] * n
    proposals = [set() for _ in range(n)]

    while free_A : #while there exists a free mentor (since set is made of mentors 
        #and their corresponding prefernce list of students)
        m = free_A[0] # let m be that man(mentor)
        for s in pref_A[m]: #traversing through the already order list of prefernces
            if s not in proposals[m]:
                proposals[m].add(s)

                if current_matches[s] == -1:
                    #woman (student) is unmatched
                    current_matches[s] = m
                    free_A.pop(0)
                    break
                else:
                    other_m = current_matches[s]
                    if pref_B[s].index(m) < pref_B[s].index(other_m):
                        #if the new man is of greater pref than the prev man
                        current_matches[s] = m
                        free_A.pop(0)
                        free_A.append(other_m)
                        break
    return current_matches

matches = GS(n,pref_A, pref_B)
for s, m in enumerate(matches):
    print(f"Student {s} ↔ Mentor {m}")