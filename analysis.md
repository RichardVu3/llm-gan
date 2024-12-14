# Performance Analysis

## Results
| Model             | % Correct |
|--------------------|-----------|
| Llama3.1 8B       | 10%       |
| Llama3.1 70B      | 30%       |
| Llama3.1 405B     | 43.33%    |
| Mistral           | 20%       |
| Human Baseline    | 40%       |

### Key Observations
1. **Training Data Rarity**:
   - Riddles and uncommon question formats challenged models, likely due to their scarcity in training data.

2. **Distracting Details**:
   - Questions with lengthy, noisy, or misleading details disrupted model focus.
   - Example: *The mother of the person in this photograph is the daughter of my mother.*

3. **Human Ingenuity**:
   - Humans excel at filtering noise and applying logic, capabilities that remain challenging for models.

4. **GAN-Inspired Process**:
   - The iterative refinement process revealed LLMs' competence.
   - On average, three iterations were needed to transform questions into their most challenging forms.

## Discussion
- Larger models, like **Llama3.1 405B**, demonstrated near-human performance in specialized tasks.
- Smaller models and alternative architectures, such as **Mistral**, underperformed compared to larger models and humans.

### Conclusion
- Model size correlates with performance, as seen in the improvement from **Llama3.1 8B** to **Llama3.1 405B**.
- Despite progress, human participants showcased unique problem-solving abilities, particularly in filtering noise and logical reasoning, areas where models still face significant challenges.
- Larger LLMs are approaching human-level performance in specialized scenarios but require further advancements to consistently outperform human baselines.
