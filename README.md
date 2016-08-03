# simple-frontmatter

This is a simple, unlicensed, frontmatter parser for Python 2.x.

```
# post.rst
title: The best post ever
author: John
...

This really is the best post ever
=================================

I assure you.
```

```python
>>> import simple_frontmatter
>>> with open("post.rst") as f:
...     frontmatter, contents = simple_frontmatter.load(f)
...
>>> frontmatter
{'title': 'The best post ever', 'author': 'John'}
>>> contents
'\nThis really is the best post ever\n=================================\n\nI assure you.\n'
```

You can include the actual module, but I'd just copy and paste the code in `simple_frontmatter.py` into your project.
