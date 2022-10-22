def F(x):
    y = -1
    a_rep_len = 0
    b_rep_len = 0
    while x != 0:
        if y == x:
            a_rep_len += 1
        else:
            y = x
            b_rep_len = max(b_rep_len, a_rep_len)
            a_rep_len = 1
        x = int(input())
    b_rep_len = max(b_rep_len, a_rep_len)
    print(b_rep_len)
F(x = int(input()))
