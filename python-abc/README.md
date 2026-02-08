# Python ABC exercises

Small, single-file examples that illustrate Python's abstract base classes (ABCs), duck typing, mixins, and multiple inheritance. Each script is runnable on its own and prints simple demo output.

## File guide
- `task_00_abc.py` – Minimal `Animal` ABC with `Dog` and `Cat` implementations.
- `task_01_duck_typing.py` – `Shape` ABC (`Circle`, `Rectangle`) plus `shape_info` function to show duck typing.
- `task_02_verboselist.py` – `VerboseList` that extends `list` and logs when items are added or removed.
- `task_03_countediterator.py` – `CountedIterator` wrapper that tracks how many items have been yielded.
- `task_04_flyingfish.py` – `Fish`, `Bird`, `FlyingFish` example showing multiple inheritance and method resolution order.
- `task_05_dragon.py` – `SwimMixin`, `FlyMixin`, and `Dragon` combining behaviors via mixins.

## How to run
From this `python-abc` directory:
```bash
python3 task_00_abc.py
python3 task_01_duck_typing.py
python3 task_02_verboselist.py
python3 task_03_countediterator.py
python3 task_04_flyingfish.py
python3 task_05_dragon.py
```
Each script prints a short demonstration; no extra input or dependencies are required.

## What you’ll practice
- Defining and implementing abstract base classes.
- Leveraging duck typing to accept any object with the right methods.
- Subclassing built-ins to customize behavior.
- Building iterators that maintain internal state.
- Using multiple inheritance and mixins to compose behaviors.
