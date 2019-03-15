"""
a=[1,2,3]
b=[1.1,1.2,2.1,2.2,3.1,3.2]
print answer
>>[1.1,2.1,3.1]
"""

a = [1,2,3]
b=[1.1,1.2,2.1,2.2,3.1,3.2]


def find_closest(anchor, comparisons):
    # find index of number in comparisons that is closest to anchor
    diffs = [abs(anchor-val) for val in comparisons]
    minimum_index = diffs.index(min(diffs))
    return comparisons[minimum_index]
answer = []
for comp in a:
    answer.append(find_closest(comp,b))




print(answer)
