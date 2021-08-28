from tikv_client import TransactionClient

client = TransactionClient.connect("127.0.0.1:2379")

# put
txn = client.begin()
txn.put(b"k1", b"Hello")
txn.put(b"k2", b",")
txn.put(b"k3", b"World")
txn.put(b"k4", b"!")
txn.put(b"k5", b"TXN KV")
txn.commit()

snapshot = client.snapshot(client.current_timestamp())

# get
print(snapshot.get(b"k1"))

# batch get
print(snapshot.batch_get([b"k1", b"k3"]))

# scan
print(snapshot.scan(b"k1", end=b"k5", limit=10, include_start=True, include_end=True))
