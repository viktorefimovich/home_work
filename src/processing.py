from typing import Dict, List, Any


def filter_by_state(list_dict: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """Функция фильтрации операций по ключу state"""

    new_list_dict = []
    for dict_ in list_dict:
        if dict_.get("state") == state:
            new_list_dict.append(dict_)
    return new_list_dict


def sort_by_date(list_dict: list[dict[str, Any]], ascending: bool = True) -> list[dict[str, Any]]:
    """Функция сортировки операций по дате"""

    list_dict_sort = sorted(list_dict, key=lambda x: x["date"], reverse=ascending)
    return list_dict_sort


if __name__ == "__main__":
    print(
        filter_by_state(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            "EXECUTED",
        )
    )
    print(
        sort_by_date(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ]
        )
    )
