nums = [[5, 2, 6, 8, 4], [3, 4, 9, 1, 12], [24, 9, 2, 4, 7], [1, 1, 7, 5, 3], [15, 2, 4, 7, 1]]
N = 5


def calc_average(col):
    sum = 0
    for num in col:
        sum += num
    average = sum / N

    return average

def make_string(dict):
    string = ""
    for i in range(N):
        for j in range(N):
            string += str(dict[j][i]) + " "
            if j == N - 1:
                string += "\n"
    return string



nums_str = make_string(nums)

print("We have:")
print(nums_str)


averages = []

for col in nums:
    averages.append(calc_average(col))

for i in range(len(averages)):
    print(f"Average in col {i}: {averages[i]}")


print("")
response = input("Sort? (yes): ")
print("")

if response.strip() == "yes":
    sorted_nums = sorted(nums, key = calc_average)
    sorted_str = make_string(sorted_nums)
    print(sorted_str)
else:
    print("Bye")