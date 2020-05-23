https://towardsdatascience.com/understand-how-to-use-namedtuple-and-dataclass-in-python-e82e535c3691


method	                                size	    object-creation-time   attribute-access-time
Regular Python class	                64bytes	            456ms	                34ms
collections.namedtuple	                80bytes	            435ms	                47ms
typing.NamedTuple	                    80bytes	            432ms	                45ms
dataclass	                            64bytes	            448ms	                44ms
dataclass with slots(DataClass_Ex)	    72bytes	            388ms	                43ms