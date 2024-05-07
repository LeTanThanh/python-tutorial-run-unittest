# Organizing Code & Running unittest

- Reference: https://www.pythontutorial.net/python-unit-testing/python-run-unittest

- Run all unittest

```bash
python -m unittest discover -v
```

- Run unittest in a single test module

```bash
python -m unittest tests.test_circle -v
```

- Run unittest in a single test class

```bash
python -m unittest tests.test_circle.TestCircle -v
```

- Run unittest in a single test method

```bash
python -m unittest tests.test_circle.TestCircle.test_init_raises_value_error -v
```
