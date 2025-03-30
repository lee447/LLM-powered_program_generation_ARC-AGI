# 30.03
=================

## Created v1 of prompts:

System Prompt:

    "You are a visual reasoning and Python programming expert solving ARC-AGI (Abstraction and Reasoning Corpus - Artificial General Intelligence) tasks.

    Each integer in the grid represents a color:
    0 = black, 1 = blue, 2 = red, 3 = green, 4 = yellow,
    5 = grey, 6 = pink, 7 = orange, 8 = light blue, 9 = brown."


Base Prompt:

    "Write a Python function that correctly transforms each input grid into its corresponding output grid based on the given examples.

    - The function must be named: `solve(grid: List[List[int]]) -> List[List[int]]`
    - Include only the code and necessary imports (e.g., `import numpy as np`)
    - Do not include comments, explanations, or print statements
    - Do not hard-code values or specific grid sizes — the function must generalize based on the patterns in the examples
    - Ensure your solution works for all provided input-output pairs"
    
    
Secondary Prompt 1:

    "List visual observations from the training pairs.

    - Use bullet points (max 10).
    - Focus on colors, shapes, object counts, positions, and differences.
    - Avoid reasoning or explanations.
    - Be concise. No full sentences, no extra formatting."


Secondary Prompt 2:

    "Describe the transformation(s) from input to output grids.

    - Use 3 to 5 short sentences.
    - Focus on what changes: movement, color, shape, duplication, etc.
    - Mention if the transformation is based on position, context, or rules.
    - Avoid implementation hints or code."


Secondary Prompt 3:

    "Reflect on how you would solve the task in Python.

    - Use 3 to 5 sentences.
    - Mention your overall approach, logical steps, and possible uncertainties.
    - Do not return code or pseudocode."


Each prompt is combined with the current tasks demonstrations pairs. Prompt 2 is additionally combined with the response for prompt 1; prompt 3 is additionally combined with the responses for prompt 1 and 2.
The base prompt is transformed to a task-tailored prompt by being combined with the LLMs response to secondary prompt 3.

TODO: Check cost-efficiency and possible better accuracy by adding the responses of prompts 1 and 2 to the base prompt as well.



## Created Evaluation set:

Randomly picked 100 tasks from the public evaluation dataset and added them to the folder "Evaluation_set". These tasks can be used to evaluate the efficiency of the pipeline.


## Created basic functions:

- load_tasks: Loads the tasks from the Evaluation_set folder.
- load_api_key: Loads the API-Key for GPT-models.
- build_prompt: Adds the current tasks demonstration pairs to a given prompt.
- combine_prompts_1_and_2: Adds the response to prompt 1 to prompt 2.
- combine_prompts_1_2_and_3: Adds the response to prompt 1 and prompt 2 to prompt 3.
- combine_prompts_3_and_base: Adds the response to prompt 3 to the base prompt resulting in a task-tailored prompt.
- save_program: Saves the response to the task-tailored prompt in a .py file in the Candidate_programs folder. In the Candidate_programs folder a folder is created, named after the Tasks position in the sorted Evaluation_set folder (e.g. Task 1 for the first Task in the sorted list).
- call_gpt: Calls GPT-Model with a given prompt.


## Pipeline:
Created the general flow of the pipeline up to the program generation. This includes calling the LLM with the three secondary prompt and based on its responses creating the subsequent prompts until the task-tailored prompt is finished. The LLM is then called to create one single candidate program right now. 

Went back to run with GPT-Model, since the locally run LLMs mostly failed already on secondary prompt 1 (recognizing patterns in the data). GPT was able to correctly solve 1 out of 3 tested tasks with the current iteration of the pipeline (evaluated manually for now).

TODO: 
- Check cost-efficiency.
- Implement Evaluation.
- Check GPT-4o-mini (does'nt cost much).
- Generate 2-4 programs per task (depending on the cost).