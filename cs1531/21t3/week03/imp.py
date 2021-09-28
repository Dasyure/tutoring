### Part 1
import foo
print(foo.bar('hi')) # 1 # More verobse, useful when you need context

import fooooooooooooooooo as f
print(fooFile.bar('hi')) # 2 #Used to shorten

from foo import bar
print(bar('hi')) # 3 # GOOD

from foo import *
print(bar('hi')) # 4 # BAD

### Part 2
import foo
print(foo.getName())
foo.editName('Hayden')
print(foo.getName())
