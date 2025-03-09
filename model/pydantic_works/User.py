from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel


class User(BaseModel):
    id: int
    name = "Ilanchezhian J"
    signup_ts: Optional[datetime] = None
    friends: List[int] = []


class AnotherUser(BaseModel):
    no: int = 0
    id: int = 0


external_data = {
    "id": "123",
    "signup_ts": "2019-06-01 12:22",
    "friends": [1, 2, "3"],
}
# in friends '3' is string, but automatically typecasted to integer.
user = User(**external_data)
print(user.id)
# > 123
print(repr(user.signup_ts))
# > datetime.datetime(2019, 6, 1, 12, 22)
print(user.friends)
# > [1, 2, 3]
print(user.dict())
"""
{
    'id': 123,
    'signup_ts': datetime.datetime(2019, 6, 1, 12, 22),
    'friends': [1, 2, 3],
    'name': 'John Doe',
}
"""
another_user = AnotherUser()
another_user.id += 1
print(another_user.id)
