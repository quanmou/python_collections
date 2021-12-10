from typing import Callable, Any, List, Dict


class Module:

    def _call_impl(self, *input, **kwargs):
        print(1)

    __call__: Callable[..., Any] = _call_impl

    def func(self, a: List[Any], b: Dict[str, bool]):
        print(a, b)

    score = 100


m = Module()
m()
print(m.score)
print(Module.score)
m.func([1], {'a': True})
m.func(['s'], {'a': 1})
