'''
    This file contains the template for CodeProject1.  For testing it, I will place it
    in a different directory, call the function <shortest_useful_rope>, and check its output.
    So, you can add/remove  whatever you want to/from this file.  But, don't change the name
    of the file or the name/signature of the following function.

    Also, I will use <python3> to run this code.
'''

def shortest_useful_rope(input_file_path, output_file_path):
    '''
        This function will contain your code.  It will read from the file <input_file_path>,
        and will write its output to the file <output_file_path>.
    '''
    pass

    r = []
    with open("C:\\Users\Srivastchavan\Desktop\DAA Coding Project\codetests\input0.in", "r") as my_file:
        for line in my_file:
            str = line
            r.append(str)
    print(r)
    p = []
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
                    p.append(s)
                    s = ''
                if (len(p) % 2 == 0 and p != []):
                    r1.append(p)
                    p = []
            j += 1
        r2.append(r1)
        r1 = []
    print(r2)



'''
    To test your function, you can uncomment the following command with the input/output
    files paths that you want to read from/write to.
'''
# shortest_useful_rope('', '')


