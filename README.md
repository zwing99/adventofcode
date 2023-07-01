# zwing99's Advent of Code solutions

## usage

```bash
cp -r template $year/$day

```

**Now start solving**

## the template

includes basic parsing and file handling logic

```python
#!/usr/bin/env python

import sys
filename = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]
```

