Forward reference issue with SQLModel + SQLAlchemy 1.4

Reproduction steps:
1. create virtual env and activate it.
2. make install (pip install -r requirements.txt)
3. make run -> Works (python main.py)
4. make upgrade (pyupgrade --py310-plus main.py) -> Removes quotes from Relationship type annotation: `list["Address"]` -> `list[Address]`
5. make run -> Error
6. Move User class below Address class
7. make run -> Works

Info:
from __future__ import annotations # is included in the file.
Type annotations are a problem when the type is a `list[...]`, as seen in step #5.
Forward refs are not an issue with type annotations that are not lists, as seen in step #7.
