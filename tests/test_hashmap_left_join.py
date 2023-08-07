import pytest
from hashtable.hashtable import HashTable
from hashmapLeftJoin.hashmap_left_join import hashmap_left_join


def test_hashmap_left_join():
    table1 = HashTable()
    table2 = HashTable()

    table1.set("apple", "red")
    table1.set("banana", "yellow")
    table1.set("grape", "purple")

    table2.set("apple", "green")
    table2.set("orange", "orange")

    result = hashmap_left_join(table1, table2)

    assert result.get("apple") == ["red", "green"]
    assert result.get("banana") == ["yellow", None]
    assert result.get("grape") == ["purple", None]

    empty_table1 = HashTable()
    empty_table2 = HashTable()

    empty_result = hashmap_left_join(empty_table1, empty_table2)
    assert len(empty_result.keys()) == 0

    table3 = HashTable()
    table3.set("apple", "red")
    table3.set("banana", "yellow")

    empty_result = hashmap_left_join(table3, empty_table2)
    assert empty_result.get("apple") == ["red", None]
    assert empty_result.get("banana") == ["yellow", None]

    empty_result = hashmap_left_join(empty_table1, table3)
    assert len(empty_result.keys()) == 0

if __name__ == "__main__":
    pytest.main()