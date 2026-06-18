# Prompt Engineering Toolkit

Systematic prompt engineering toolkit with automatic optimization.

## Features
- Few-shot example selection (similarity-based, stratified)
- Chain-of-thought prompting
- DSPy-based automatic prompt optimization
- A/B testing framework for prompts

## Example
```python
from prompt_toolkit import PromptOptimizer
opt = PromptOptimizer(model='gpt-4')
best_prompt = opt.optimize(train_examples, metric='accuracy')
```

## License
MIT
