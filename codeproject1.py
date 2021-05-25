"""
    This file contains the template for CodeProject1.  For testing it, I will place it
    in a different directory, call the function <shortest_useful_rope>, and check its output.
    So, you can add/remove  whatever you want to/from this file.  But, don't change the name
    of the file or the name/signature of the following function.

    Also, I will use <python3> to run this code.
"""
import math


def shortest_useful_rope(input_file_path, output_file_path):
    """
        This function will contain your code.  It will read from the file <input_file_path>,
        and will write its output to the file <output_file_path>.
    """
    pass

    r=[]
    with open("C:\\Users\Srivastchavan\Desktop\DAA Coding Project\codetests\input1.in", "r") as my_file:
        for line in my_file:
            str = line
            r.append(str)
        # print(r)
        m = []
        r1 = []
        r2 = []
        for i in range(len(r)):
            j = 0
            s = ''
            while j < len(r[i]):
                if (r[i][j] != '(' and r[i][j] != ')' and r[i][j] != ',' and r[i][j] != ' '):
                    s = s + r[i][j]
                else:
                    if (s != ''):
                        m.append(s)
                        s = ''
                    if (len(m) % 2 == 0 and m != []):
                        r1.append(m)
                        m = []
                    j += 1
                r2.append(r1)
    p=[]
    q=[]

    p = r2[0]
    q = r2[1]

    print(p)


    lenp = p.length
    lenq = q.length
    ca = [[0 for x in range(lenp)] for y in range(lenq)]

    for i in range(lenp):
        for j in range(lenq):
            ca[i][j] = 0
    
    for i in range(lenp):
        for j in range(lenq):
            d = distance(p[i], q[j])

            if i > 0 and j > 0:
                ca[i][j] = max(min(ca[i - 1][j],
                                   ca[i - 1][j - 1],
                                   ca[i][j - 1]), d)
            elif i > 0 and j == 0:
                ca[i][j] = max(ca[i - 1][0], d)
            elif i == 0 and j > 0:
                ca[i][j] = max(ca[0][j - 1], d)
            else:
                ca[i][j] = d
    return ca[lenp - 1][lenq - 1]



def distance(pt1, pt2):

    return math.ceil(math.sqrt((pt2[0] - pt1[0]) * (pt2[0] - pt1[0]) + (pt2[1] - pt1[1]) * (pt2[1] - pt1[1])))


#ans1 = distance([1, 1], [2, 2])
inpath = "C:\\Users\Srivastchavan\Desktop\DAA Coding Project\codetests\input1.in"
shortest_useful_rope(inpath, " ")
print(ans)


'''
    To test your function, you can uncomment the following command with the input/output
    files paths that you want to read from/write to.
'''
# shortest_useful_rope('', '')
