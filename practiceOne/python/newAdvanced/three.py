
"""
three.py - Python learning flow

This file is a self-contained guided tour of Python. Run it and read the
comments to follow along. Each section demonstrates a concept with a small
example you can modify and re-run.

Sections:
 1. Basics: variables, types, printing
 2. Data structures: list, tuple, set, dict
 3. Control flow: if/for/while, comprehensions
 4. Functions: args, kwargs, closures, lambda
 5. Modules & imports
 6. File I/O and exceptions
 7. Classes & OOP
 8. Decorators
 9. Generators & iterators
10. Context managers
11. Async/await (simple)
12. Typing and dataclasses
13. Small examples: itertools, collections

This file is intentionally explanatory — keeping examples short and focused.
"""

from __future__ import annotations

import asyncio
import contextlib
import dataclasses
import itertools
import math
import time
from collections import Counter, defaultdict, deque
from typing import Callable, Generator, Iterable, List, Dict, Tuple, Optional


def section(title: str) -> None:
	"""
	Print a formatted section header.

	Parameters
	----------
	title : str
		The text to display as the section title.

	Returns
	-------
	None
		This function prints the formatted header to standard output.

	Behavior
	--------
	Prints a blank line, a line of 60 '=' characters, the title, another line of 60
	'=' characters, and a trailing blank line to separate sections.

	Notes
	-----
	'=' * 60 creates a string consisting of 60 '=' characters used as a horizontal separator.
	"""

	print("\n" + "=" * 60)
	print(title)
	print("=" * 60 + "\n")


def basics() -> None:
	"""Show basic types and print simple examples."""
	section("1. Basics: variables, types, printing")

	# variables and types
	a = 10               # int
	b = 3.14             # float
	name = "Alice"     # str
	flag = True          # bool

	# printing and f-strings
	print("a:", a, " type:", type(a))
	print(f"Name: {name}, pi approx: {b:.2f}")

	# multiple assignment and swapping
	x, y = 1, 2
	x, y = y, x
	print("Swapped x,y:", x, y)


def data_structures() -> None:
	"""Demonstrate list/tuple/set/dict with small examples."""
	section("2. Data structures: list, tuple, set, dict")

	# list (mutable)
	fruits: List[str] = ["apple", "banana", "cherry"]
	fruits.append("date")
	print("List:", fruits)

	# tuple (immutable)
	point: Tuple[int, int] = (10, 20)
	x, y = point
	print("Tuple point:", point, " unpacked:", x, y)

	# set (unique items)
	colors = {"red", "green", "blue", "red"}
	print("Set (unique):", colors)

	# dict (mapping)
	ages: Dict[str, int] = {"Alice": 30, "Bob": 25}
	ages["Charlie"] = 22
	print("Dict ages:", ages)


def control_flow() -> None:
	"""Show if/for/while and comprehensions by printing results."""
	section("3. Control flow: if/for/while, comprehensions")

	for i in range(3):
		print("for loop i=", i)

	n = 5
	if n % 2 == 0:
		print("n is even")
	else:
		print("n is odd")

	# while loop
	i = 0
	while i < 3:
		print("while i=", i)
		i += 1

	# list comprehension, dict and set comprehensions
	squares = [i * i for i in range(6)]
	even_squares = {i: i * i for i in range(6) if i % 2 == 0}
	evens = {i for i in range(6) if i % 2 == 0}
	print("squares:", squares)
	print("even_squares dict:", even_squares)
	print("evens set:", evens)


def functions_and_closures() -> None:
	"""Explain functions, args/kwargs, closures, and lambda with examples."""
	section("4. Functions: args, kwargs, closures, lambda")

	def greet(name: str, /, greeting: str = "Hello") -> str:
		return f"{greeting}, {name}!"

	print(greet("World"))
	print(greet("Jane", greeting="Hi"))

	# *args and **kwargs
	def summarize(*values: int, **options) -> Dict[str, float]:
		total = sum(values)
		count = len(values)
		avg = total / count if count else 0
		return {"total": total, "count": count, "avg": avg}

	print(summarize(1, 2, 3, mode="fast"))

	# closure example
	def make_multiplier(factor: int) -> Callable[[int], int]:
		def multiplier(x: int) -> int:
			return x * factor

		return multiplier

	doubler = make_multiplier(2)
	print("doubler(5):", doubler(5))

	# lambda
	inc = lambda x: x + 1
	print("inc(5):", inc(5))


def modules_and_imports() -> None:
	"""Show importing modules and calling a function (math.sqrt)."""
	section("5. Modules & imports")
	print("You can import modules like math, time, itertools, etc.")
	print("math.sqrt(16):", math.sqrt(16))


def file_io_and_exceptions(tmpfile: str = "example.txt") -> None:
	"""Write and read a file, showing try/except/finally behavior."""
	section("6. File I/O and exceptions")

	try:
		with open(tmpfile, "w", encoding="utf-8") as f:
			f.write("Hello file\nLine 2\n")
		with open(tmpfile, "r", encoding="utf-8") as f:
			content = f.read()
		print("File content:\n", content)
	except OSError as e:
		print("File operation failed:", e)
	finally:
		print("Finished file I/O example")


def exceptions_demo() -> None:
	"""Raise and catch a custom exception (MyError)."""
	section("6b. Exceptions and custom exceptions")

	class MyError(Exception):
		pass

	try:
		raise MyError("something went wrong")
	except MyError as e:
		print("Caught MyError:", e)


def classes_and_oop() -> None:
	"""Define classes, inheritance, and properties; show usage."""
	section("7. Classes & OOP")

	class Animal:
		def __init__(self, name: str):
			self.name = name

		def speak(self) -> str:
			return f"{self.name} makes a sound"

		def __repr__(self) -> str:  # helpful for debugging
			return f"Animal(name={self.name!r})"

	class Dog(Animal):
		def speak(self) -> str:
			return f"{self.name} barks"

	dog = Dog("Buddy")
	print(dog)
	print(dog.speak())

	# properties
	class Circle:
		def __init__(self, radius: float):
			self.radius = radius

		@property
		def area(self) -> float:
			return math.pi * self.radius ** 2

	c = Circle(2)
	print("Circle area:", c.area)


def dataclasses_and_typing() -> None:
	"""Demonstrate `dataclass` and simple typing use."""
	section("12. Typing and dataclasses")

	@dataclasses.dataclass
	class Person:
		name: str
		age: int

	p = Person("Eve", 29)
	print(p)


def decorators_demo() -> None:
	"""Show a timing decorator and its effect on a function."""
	section("8. Decorators")

	def timer(func: Callable[..., object]) -> Callable[..., object]:
		from functools import wraps
		import time

		@wraps(func)
		def wrapper(*args, **kwargs):
			start = time.perf_counter()
			result = func(*args, **kwargs)
			end = time.perf_counter()
			print(f"{func.__name__} took {end - start:.6f}s")
			return result

		return wrapper

	@timer
	def compute(n: int) -> int:
		total = 0
		for i in range(n):
			total += i
		return total

	print("compute(10000):", compute(10000))


def generators_and_iterators() -> None:
	"""Create and consume generators; show generator expression."""
	section("9. Generators & iterators")

	def count_up_to(n: int) -> Generator[int, None, None]:
		i = 0
		while i < n:
			yield i
			i += 1

	for v in count_up_to(5):
		print("gen value:", v)

	# generator expression
	gen = (i * i for i in range(5))
	print("generator expr next:", next(gen))


def context_managers() -> None:
	"""Demonstrate generator-based context manager.

	Shows three phases succinctly:
	- acquire: setup before `yield`
	- yield: hand resource into `with` block
	- release: cleanup in `finally`, always runs
	"""
	section("10. Context managers")

	# create a context manager from a generator function
	@contextlib.contextmanager
	def make_resource(name: str):
		# acquire/setup
		print(f"acquiring {name}")
		try:
			# yield passes the resource into the with-block
			yield {"name": name}
		finally:
			# release/cleanup (runs on normal exit or exception)
			print(f"releasing {name}")

	# usage: enters make_resource -> runs acquire, executes body, then release
	with make_resource("res1") as r:
		print("inside with, resource:", r)


def async_example() -> None:
	"""Run simple async tasks with asyncio.gather and sleep."""
	section("11. Async/await (simple)")

	async def say_after(delay: float, message: str) -> None:
		await asyncio.sleep(delay)
		print(message)

	async def run_async():
		await asyncio.gather(say_after(0.5, "hello"), say_after(0.1, "world"))

	# run the async example
	asyncio.run(run_async())


def small_tools() -> None:
	"""Show small stdlib utilities: Counter, defaultdict, deque, itertools."""
	section("13. Small examples: itertools, collections")
	print("Counter example:", Counter(["a", "b", "a"]))
	print("defaultdict example:", defaultdict(list, {"x": [1]}))
	print("deque operations:")
	d = deque([1, 2, 3])
	d.appendleft(0)
	d.append(4)
	print(d)
	print("itertools.product example:", list(itertools.product([1, 2], ["a", "b"])))


def main() -> None:
	"""Run each section in order to demonstrate Python features."""
	basics()
	data_structures()
	control_flow()
	functions_and_closures()
	modules_and_imports()
	file_io_and_exceptions()  # writes example.txt in cwd
	exceptions_demo()
	classes_and_oop()
	dataclasses_and_typing()
	decorators_demo()
	generators_and_iterators()
	context_managers()
	async_example()
	small_tools()
	print("\nEnd of three.py learning flow")


if __name__ == "__main__":
	main()

