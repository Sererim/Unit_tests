msgs: tuple[str] = (
    "Первый список имеет большее среднее значение", # Если среднее значение первого списка больше
    "Второй список имеет большее среднее значение", # Если среднее значение второго списка больше
    "Средние значения равны"                        # Если средние значения списков равны
)


def find_average(lst: list[int]) -> int:
    """Function for finding an average value of a list.
    Args:
        lst (list[int]): list to find the average value in.

    Returns:
        int: Calculates the average like this:
        lst = [1, 2, 3, 4]
        average = (1 + 2 + 3 + 4) / 4 = 2.5
    """
    num: int = 0
    
    for i in lst:
        num += i
    num /= len(lst)
    
    return num


def compare(lst_1: list[int], lst_2: list[int]) -> eval:
    global msgs
    message: int = 0
    
    if (find_average(lst_1) < find_average(lst_2)):
        message = 1
    elif(find_average(lst_1) == find_average(lst_2)):
        message = 2
    
    return msgs[message]

if __name__ == "__main__":
    print(compare([1, 2, 3, 4], [1, 2, 3]))
    print(compare([1, 2, 3, 4], [1, 2, 8]))
    print(compare([1, 2, 3], [1, 2, 3]))
    