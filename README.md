# Evaluating LLM Performance on Challenging Questions

This project explores the ability of Large Language Models (LLMs) to solve challenging questions, comparing their performance to human participants. A Generative Adversarial Network (GAN)-inspired approach was used to generate and refine questions for testing model capabilities under increasing difficulty.

## Project Setup
The project utilized a GAN-inspired setup:
1. **Generator**: Created answers for 30 challenging questions.
2. **Discriminator**: Rephrased questions to increase difficulty, incorporating up to five feedback rounds per question.

### Special Features
- **GAN Workflow with LangGraph**: Utilized LangGraph to construct and visualize the GAN-inspired workflow, enabling seamless integration and execution of the question generation and evaluation process.
- **API Abstraction with LangChain**: Leveraged LangChain to abstract API calls, simplifying interactions with various LLMs and ensuring modular and maintainable code.
- **Adaptive Question Difficulty**: Implemented a feedback loop mechanism to iteratively increase question difficulty, challenging LLMs progressively.
- **Automated Evaluation**: Integrated automated evaluation using advanced LLMs to assess the correctness of generated answers, providing immediate feedback and scoring.

### Question Design
- Focused on riddles, lengthy distracting details, and confusing phrasing to challenge LLMs while remaining solvable for humans.
- Example: *The mother of the person in this photograph is the daughter of my mother.*

### How to run the program

1. **Install dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

2. **Set up environment variables**:
    ```sh
    export OPENAI_API_KEY="your_openai_api_key"
    export OPENAI_API_BASE="your_openai_api_base"
    export MODEL="your_model_name"
    ```

3. **Run the main script**:
    ```sh
    python run.py
    ```

4. **View the generated questions and answers**:
    ```sh
    cat question-answer.json
    ```

### Evaluation
- **Automatic Scoring**: Used Llama3.1 405B to evaluate answers based on semantic and logical correctness.
- **Human Baseline**: Performance data was collected from three CS students and averaged.
- **Model Comparisons**: Llama3.1 (8B, 70B, 405B) and Mistral (running in Ollama) were tested and compared against human performance.

### Results Summary
- **Llama3.1 405B** achieved the highest score (43.33%), surpassing the human baseline (40%).
- Smaller models like **Llama3.1 8B** and **Mistral** struggled, scoring 10% and 20%, respectively.
- Human participants demonstrated strengths in logic and noise filtering, presenting challenges for LLMs to replicate.

For detailed results and analysis, see the [Performance Analysis](analysis.md).
