
# Python Asynchronous

## Description

This project demonstrates the use of asynchronous programming in Python. It includes a basic example showcasing how to implement asynchronous functions to improve efficiency and performance in concurrent tasks.

## Requirements

- Python 3.7 or higher

## Mode of Use

1. Clone the repository:
   ```bash
   git clone https://github.com/ferrerallan/python-asynchronous.git
   ```
2. Navigate to the project directory:
   ```bash
   cd python-asynchronous
   ```
3. Run the example script:
   ```bash
   python example.py
   ```

## Example Code

```python
import asyncio

async def main():
    print('Hello ...')
    await asyncio.sleep(1)
    print('... World!')

asyncio.run(main())
```

## License

This project is licensed under the MIT License.
