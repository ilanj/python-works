import collections

TransactionNamedTuple = collections.namedtuple('TransactionNamedTuple',['sender','receiver','date', 'amount'])
# TransactionDefault = collections.namedtuple('TransactionDefault',['sender','receiver','date','amount'], defaults=['jojo', 'xiaoxu', None, None])
# TransactionDefault2 = collections.namedtuple('TransactionDefault2',['sender','receiver','date','amount'], defaults=[None])
record = TransactionNamedTuple(sender="jojo",receiver="xiaoxu",date="2020-06-08",amount=1.0)
print(record)
print(record[0])
print(record.sender)
print(TransactionNamedTuple.__dict__)