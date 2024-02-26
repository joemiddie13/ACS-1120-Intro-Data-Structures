from linkedlist import LinkedList

class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        self.buckets = [LinkedList() for _ in range(init_size)]

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table."""
        all_keys = []
        for bucket in self.buckets:
            all_keys.extend([key for key, _ in bucket.items()])
        return all_keys

    def values(self):
        """Return a list of all values in this hash table."""
        all_values = []
        for bucket in self.buckets:
            all_values.extend([value for _, value in bucket.items()])
        return all_values

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table."""
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets."""
        return sum(bucket.length() for bucket in self.buckets)

    def contains(self, key):
        """Return True if this hash table contains the given key, or False."""
        bucket = self.buckets[self._bucket_index(key)]
        return bucket.find(lambda key_value: key_value[0] == key) is not None

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError."""
        bucket = self.buckets[self._bucket_index(key)]
        for key_value in bucket.items():
            if key_value[0] == key:
                return key_value[1]
        raise KeyError('Key not found: {}'.format(key))

    def set(self, key, value):
        """Insert or update the given key with its associated value."""
        bucket = self.buckets[self._bucket_index(key)]
        entry = bucket.find(lambda key_value: key_value[0] == key)
        if entry is not None:
            bucket.replace(entry, (key, value))
        else:
            bucket.append((key, value))

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError."""
        bucket = self.buckets[self._bucket_index(key)]
        entry = bucket.find(lambda key_value: key_value[0] == key)
        if entry is not None:
            bucket.delete(entry)
        else:
            raise KeyError('Key not found: {}'.format(key))

def test_hash_table():
  if __name__ == '__main__':
    test_hash_table()
