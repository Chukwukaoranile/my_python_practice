phone_no = input('Enter Phone no ')
num_in_fig = {
    "1": "x",
    "2": "xx",
    "3": "xxx",
    "4": "xxxx"
}
output = " "
for fig_num in phone_no:
    output += num_in_fig.get(fig_num, "!") + ""
    print(output)
