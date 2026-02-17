def find(search_list, value):
    left = 0
    right = len(search_list) - 1

    while left <= right:
        mid = (left + right) // 2
        middle_element = search_list[mid]

        if middle_element == value:
            return mid
        
        if middle_element < value:
            left = mid + 1
        else:
            right = mid - 1

    # If the loop finishes, the song isn't in the playlist
    raise ValueError("value not in array")