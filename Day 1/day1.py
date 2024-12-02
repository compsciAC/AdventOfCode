
def getLists():
    inputFile = "/day1Input"
    first_list = []
    second_list = []

    with open(inputFile, "r") as file:
        for line in file:
            numbers = line.split()
            first_list.append(int(numbers[0]))
            second_list.append(int(numbers[1]))
        first_list.sort()
        second_list.sort()
    return first_list, second_list

def calculateDiff():
    first_list, second_list = getLists()
    diff = 0
    for i in range(len(first_list)):
        diff += (abs(first_list[i] - second_list[i]))
    return diff


def binary_search_count(list, element):
    def find_first(list, element):
        low, high = 0, len(list) - 1
        first_index = -1
        while low <= high:
            mid = (low + high) // 2
            if list[mid] == element:
                first_index = mid
                high = mid - 1
            elif list[mid] < element:
                low = mid + 1
            else:
                high = mid - 1
        return first_index

    def find_last(list, element):
        low, high = 0, len(list) - 1
        last_index = -1
        while low <= high:
            mid = (low + high) // 2
            if list[mid] == element:
                last_index = mid
                low = mid + 1
            elif list[mid] < element:
                low = mid + 1
            else:
                high = mid - 1
        return last_index

    first_index = find_first(list, element)
    if first_index == -1:
        return 0
    last_index = find_last(list, element)
    return last_index - first_index + 1

def calculateSimilarityScore():
    first_list, second_list = getLists()
    similarityScore = 0

    for element in first_list:
        similarityScore += binary_search_count(second_list, element) * element
    return similarityScore

print(calculateDiff())
print(calculateSimilarityScore())