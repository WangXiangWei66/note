def change(amount, denom_list):
    alternatives_list = []
    rec_change(amount, denom_list, [], alternatives_list)
    return alternatives_list


def rec_change(amount, denom_list, change_list, alternatives_list):
    if denom_list:
        denom = denom_list[0]
        extra_change = []
        for i in range(0, amount + 1, denom):
            if i == amount:
                alternatives_list.append(change_list + extra_change)
            else:
                rec_change(amount - i, denom_list[1:], change_list + extra_change, alternatives_list)
            extra_change += [denom]

#n = change(20,[5,10,20])
n=change(10,[5,10])
print(n)