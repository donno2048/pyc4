# pyc4

A Python extension to run C code in Python based on [c4](https://github.com/rswier/c4).

## Install

```sh
pip install pyc4
```

## Use

The first argument is the code the rest are the `argv`

```py
>>> import c4
>>>
>>> c4.execute(r"""
... int main() {
...     printf("hi");
...     return 0;
... }
... """)
hi
exit code: 0
>>> c4.execute(r"""
... int main(int argc, char **argv) {
...     printf("%s", argv[0]);
...     return 0;
... }
... """, "hi")
hi
exit code: 0
```
