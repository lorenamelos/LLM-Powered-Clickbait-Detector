# LLM-Powered Clickbait Detector 🦈

## Overview
This project aims to build an LLM-powered clickbait detector, making use of prompt techniques such as few-shot, zero-shot, CoT, etc.

### Part 1: Dataset Creation
- Design a prompt/chain to detect if an article is clickbait or not based on its headline.
- Convert provided article headlines along with their corresponding labels into a dataset.
- Specify instructions and criteria for what constitutes clickbait in the prompt.

### Part 2: Moderation Tool Integration
- Utilize a moderation tool (e.g., OpenAI moderation APIs) to classify whether news articles contain harmful information.
- Define safety parameters in the prompt and determine what constitutes safe or unsafe content.

### Part 3: GPT-3.5-Turbo Experimentation
- Experiment with GPT-3.5-Turbo for the task and log prompt + results using Comet's prompting tools.
- Use tags to label articles as safe/unsafe and clickbait/not clickbait.
- Apply CoT, few-shot, and zero-shot prompting techniques and compare their performance.

### Part 4: Tagging System Implementation
- Create a tagging system to label articles as safe/unsafe and clickbait/not clickbait.
- If the headline is unsafe or clickbait, use GPT-3.5-Turbo or GPT-4 to rewrite the article as safe and devoid of clickbait.
- Log results to Comet for debugging and evaluation.


## Requirements
- Python
- OpenAI moderation APIs
- GPT-3.5-Turbo or GPT-4
- Comet's prompting tools

## Contributors
- [Lorena Melo - Linkedin](https://www.linkedin.com/in/lorenamelodev/)




