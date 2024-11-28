
# Python Utilities: Observer, Async Processing, and Expression Evaluation

## Description

This repository provides three Python utility modules, each designed to demonstrate or solve specific programming challenges:

1. **Observer Pattern (`observer.py`)**:
   - Implements the classic Observer design pattern to manage relationships between subjects and observers.
   - Includes concrete implementations for managing state changes and notifying observers.

2. **Asynchronous Processes (`example.py`)**:
   - Showcases Python's `asyncio` library for running concurrent tasks.
   - Demonstrates task synchronization, global state management, and graceful termination.

3. **Mathematical Expression Evaluator (`eval.py`)**:
   - Provides a robust evaluator for mathematical expressions supporting addition, subtraction, multiplication, division, parentheses, and operator precedence.
   - Includes error handling for invalid expressions and division by zero.

## Requirements

- Python 3.7 or higher

## Mode of Use

### 1. Observer Pattern

#### Steps:
1. Import or copy `observer.py` into your project.
2. Create instances of `Subject` and attach `Observer` instances.
3. Change the state of the `Subject` to see the notifications triggered.

#### Example:
```python
from observer import ConcreteSubject, ConcreteObserver

subject = ConcreteSubject("Initial State")
observer1 = ConcreteObserver()
observer2 = ConcreteObserver()

subject.attach(observer1)
subject.attach(observer2)

subject.state = "New State"
```

### 2. Asynchronous Processes

#### Steps:
1. Run `example.py` directly to execute the example of concurrent tasks.
2. Modify or extend the `count` function and other tasks as needed.

#### Run:
```bash
python example.py
```

#### Output:
Observe the interleaving of tasks, global state updates, and final synchronization:
```
processo 1 rodando
processo 2 rodando
processo 3 rodando
hello
...
real end 4
```

### 3. Mathematical Expression Evaluator

#### Steps:
1. Import `calculate` function from `eval.py`.
2. Use it to evaluate mathematical expressions.

#### Example:
```python
from eval import calculate

result = calculate("3 + 5 * (2 - 8) / 4")
print(f"The result is: {result}")
```

#### Expected Output:
```
The result is: -4.0
```

## Key Features

### Observer Pattern
- Dynamic management of observer relationships.
- Real-time state updates and notifications.
- Simple extension via `Subject` and `Observer` subclasses.

### Asynchronous Processing
- Demonstrates practical use of Python's `asyncio` for concurrency.
- Provides a foundation for building multi-task applications with synchronization needs.

### Mathematical Expression Evaluator
- Handles complex expressions with nested parentheses.
- Safeguards against division by zero and malformed expressions.
- Lightweight and self-contained for easy integration.

## License

This project is provided "as-is" with no specific licensing applied. Feel free to use and adapt it for your needs.
