class PromptOptimizer:
    def __init__(self, base, eval_fn): self.base, self.eval = base, eval_fn
    def optimize(self, iters=10):
        best, bs = self.base, self.eval(self.base)
        for _ in range(iters):
            v = self._mutate(best); s = self.eval(v)
            if s > bs: best, bs = v, s
        return best
    def _mutate(self, p): return p
