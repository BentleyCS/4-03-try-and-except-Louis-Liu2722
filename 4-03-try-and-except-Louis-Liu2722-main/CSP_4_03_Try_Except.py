#No using the built in type check function
#https://www.w3schools.com/python/python_try_except.asp


def sum(arr : list) -> int:
    """
    Modify the function such that it returns the sum of all numebrs within the given list.
    :param arr:
    :return:
    """
    total=0
    for value in arr:
        try:
            total=total+value
        except:
            TypeError
            pass
    return total

    pass

def cleanData(rawData : list) ->list:
    """
    modify the function such that it takes in a list as an argument will return a new list that
     contains only the valeus that can be typecast to a float.
    :param rawData:
    :return:
    """
    clean=[]
    for value in rawData:
        try:
            clean.append(float(value))
        except (ValueError, TypeError):
            pass
    return clean
    pass
def unreliableCalculator(divisors : list) -> list:
    """
    Modify the function such that it takes in a list as an argument and returns a new list where each
    index is 100 divided by the values from the input list.
    If division ever causes an error instead have the value be the type of error as a string.
    Example the list [100,50,25,"5"] as an argument would return [1, 2, 4, "TypeError"]
    :param divisors:
    :return:
    """
    list=[]
    for value in divisors:
        try:
            list.append(100/value)
        except TypeError:
            list.append("TypeError")
        except ZeroDivisionError:
            list.append("ZeroDivisionError")
    return list


    pass


def upperAll(arr : list) -> None:
    """
    Modify the function such that is uppercases all strings within the given argument list.
    The string method .upper() turns all characters in as stirng uppercase.
    You should modify the original list not return a new list.
    :param arr:
    :return:
    """
    for i in range(len(arr)):
        try:
            arr[i]=arr[i].upper()
        except AttributeError:
            pass
    x = "hello"
    print(x)
    x = x.upper()
    print(x)


def firstItems(arr : list) -> list:
    """
    Modify the function below such that given a list of values. Many of the list elements will be lists
    themselves. For any list element that is a list grab the first element from that list. If the list
    element is not a list then just grab the value itself.
    Create a new list of all the first indexes of inner lists or just values themselves.
    Example firstItems( [[1,2],[3,4],[5,6],[7,8]],9 ) == [1,3,5,7,9]
    :param arr:
    :return:
    """
    list=[]
    for value in arr:
        try:
            list.append(value[0])
        except TypeError:
            list.append(value)
    return list

    pass

