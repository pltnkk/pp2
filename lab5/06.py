import re

v = "My,name is Kobeisin"


q = re.sub( "[ ,.]", ":" , v )


print(q)