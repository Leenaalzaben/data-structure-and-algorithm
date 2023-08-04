from hash_table.hash_table import HashTable

def test_set_and_get_value_in_hash_table():
    hash_table = HashTable()

    key = "testKey"
    value = "testValue"

    hash_table.set(key, value)
    retrieved_value = hash_table.get(key)
    assert retrieved_value == value

def test_retrieving_value_in_hash_table():
    hash_table = HashTable()

    key = "testKey"
    value = "testValue"

    hash_table.set(key, value)
    retrieved_value = hash_table.get(key)
    assert retrieved_value == value

def test_retrieving_non_existing_key_in_hash_table():
    hash_table = HashTable()

    key = "existingKey"
    value = "existingValue"

    hash_table.set(key, value)
    non_existing_key = "nonExistingKey"
    retrieved_value = hash_table.get(non_existing_key)
    assert retrieved_value is None

def test_getting_all_unique_keys_in_hash_table():
    hash_table = HashTable()

    hash_table.set("key1", "value1")
    hash_table.set("key2", "value2")
    hash_table.set("key3", "value3")

    all_keys = hash_table.get_keys()
    expected_keys = ["key1", "key2", "key3"]
    assert set(all_keys) == set(expected_keys)

def test_handle_collision_in_hash_table():
    hash_table = HashTable()

    key1 = "testKey1"
    value1 = "testValue1"
    key2 = "testKey2"
    value2 = "testValue2"

    hash_table.set(key1, value1)
    hash_table.set(key2, value2)

    retrieved_value1 = hash_table.get(key1)
    retrieved_value2 = hash_table.get(key2)

    assert retrieved_value1 == value1
    assert retrieved_value2 == value2

def test_retrieve_value_from_bucket_with_collision():
    hash_table = HashTable()

    key1 = "testKey1"
    value1 = "testValue1"
    key2 = "testKey2"
    value2 = "testValue2"

    hash_table.set(key1, value1)
    hash_table.set(key2, value2)

    retrieved_value1 = hash_table.get(key1)
    retrieved_value2 = hash_table.get(key2)

    assert retrieved_value1 == value1
    assert retrieved_value2 == value2

def test_hash_key_to_in_range_value():
    hash_table = HashTable()

    key = "testKey"

    hashed_index = hash_table._HashTable__hash(key)
    assert 0 <= hashed_index < 1024


