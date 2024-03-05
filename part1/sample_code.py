from typing import Dict, List, Optional, Tuple


def find_user_clubs(clubs: Dict[str, List[str]], users: List[str]) -> Dict[str, List[str]]:
    """
    Find clubs for each user.

    Args:
        clubs (Dict[str, List[str]]): A dictionary mapping club names to a list of members.
        users (List[str]): A list of user names.

    Returns:
        Dict[str, List[str]]: A dictionary mapping each user to a list of clubs they belong to.
    """
    user_clubs: Dict[str, List[str]] = {}
    for user in users:
        user_clubs[user] = []
        for club, members in clubs.items():
            if user in members:
                user_clubs[user].append(club)
    return user_clubs


def get_pair_with_sum(num_lst: List[int], target_sum: int) -> Optional[Tuple[int, int]]:
    """
    Find a pair of numbers in a list that sum to a target sum.

    Args:
        List[int]: A list of integers.
        target_sum (int): The target sum.

    Returns:
        Optional[Tuple[int, int]]: A tuple of two integers that sum to the target sum.
    """
    num_set = set()
    for num in num_lst:
        if target_sum - num in num_set:
            return (num, target_sum - num)
        num_set.add(num)
    return


def get_pair_with_half_sum(num_lst: List[int]) -> Optional[Tuple[int, int]]:
    """
    Find a pair of numbers in a list that sum to half of the total sum of the list.

    Args:
        List[int]: A list of integers.

    Returns:
        Optional[Tuple[int, int]]: A tuple of two integers that sum to half of the total sum of the list.
    """
    total_sum = sum(num_lst)
    if total_sum % 2 != 0:
        return
    half_sum = total_sum // 2
    # half_sum, remainder = divmod(total_sum, 2) alternaeive way to calculate half_sum and remainder. This is more efficient.
    num_set = set()
    for num in num_lst:
        search_num = half_sum - num
        if search_num in num_set:
            return num, search_num
        num_set.add(num)
        


if __name__ == "__main__":
    from pprint import pprint


    # find_user_clubs
    clubs = {
        "club1": ["user1", "user2"],
        "club2": ["user2", "user3", "user4"],
        "club3": ["user1", "user3", "user4"],
        "club4": ["user1", "user3", "user4"],
    }
    users = ["user1", "user2", "user3", "user4", "user5"]
    pprint(find_user_clubs(clubs, users))
    
    # get_pair_with_sum
    num_lst = [11, 2, 5, 9, 10, 31]
    target_sum = 12
    pprint(get_pair_with_sum(num_lst, target_sum))
    
    # get_pair_with_half_sum
    num_lst = [11, 2, 5, 9, 10, 3]
    pprint(get_pair_with_half_sum(num_lst))