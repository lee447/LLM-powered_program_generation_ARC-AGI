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
- add_tasks: Adds the current tasks demonstration pairs to a given prompt.
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



# 02.04

## Additions to pipeline:
Added the following functions:
- build_prompts: Runs all the different functions for creating the task-tailored prompts. Essentially, when called, runs the process of creating the prompt for program generation.
- create_programs: Loops for a specified amount (currently 2) and calls the LLM with the task-tailored prompt and subsequently runs the save_prompt function, saving each program in their respective folder.
- load_program: Loads a created program from the specified directory.
- evaluate_programs: Receives the task data and index to evaluate all created programs on the tasks demonstration pairs. A score is calculated (amount correct/amount of demonstration pairs) to identify wether a program was able to solve all demonstration pairs.
- Adjusted Pipeline to: 
    1. Iterate over specified amount of tasks.
    2. For each create the task-tailored prompt.
    3. Create programs (currently 2).
    4. Evaluate created programs.
    5. Print results.

## Current results:
The current, unfinished, pipeline **(using GPT-o3-mini)** was tested on the first 10 tasks of the created Evaluation_set (0 100 tasks). The costs were about 2CHF (1.95CHF) The following are the results:

    Saved program for task 1 as version 1: Candidate_programs\task_1\solution_v1.py
    Saved program for task 1 as version 2: Candidate_programs\task_1\solution_v2.py
    Program solution_v1.py solved 0 out of 3 pairs.
    Score: 0.00
    Program solution_v2.py solved 0 out of 3 pairs.
    Score: 0.00
    ==================================================
    Saved program for task 2 as version 1: Candidate_programs\task_2\solution_v1.py
    Saved program for task 2 as version 2: Candidate_programs\task_2\solution_v2.py
    Program solution_v1.py solved 0 out of 4 pairs.
    Score: 0.00
    Program solution_v2.py solved 0 out of 4 pairs.
    Score: 0.00
    ==================================================
    Saved program for task 3 as version 1: Candidate_programs\task_3\solution_v1.py
    Saved program for task 3 as version 2: Candidate_programs\task_3\solution_v2.py
    Program solution_v1.py solved 0 out of 3 pairs.
    Score: 0.00
    Program solution_v2.py solved 0 out of 3 pairs.
    Score: 0.00
    ==================================================
    Saved program for task 4 as version 1: Candidate_programs\task_4\solution_v1.py
    Saved program for task 4 as version 2: Candidate_programs\task_4\solution_v2.py
    Program solution_v1.py solved 2 out of 2 pairs.
    Score: 1.00
    Program solution_v2.py solved 2 out of 2 pairs.
    Score: 1.00
    ==================================================
    Saved program for task 5 as version 1: Candidate_programs\task_5\solution_v1.py
    Saved program for task 5 as version 2: Candidate_programs\task_5\solution_v2.py
    Program solution_v1.py solved 3 out of 3 pairs.
    Score: 1.00
    Program solution_v2.py solved 3 out of 3 pairs.
    Score: 1.00
    ==================================================
    Saved program for task 6 as version 1: Candidate_programs\task_6\solution_v1.py
    Saved program for task 6 as version 2: Candidate_programs\task_6\solution_v2.py
    Program solution_v1.py solved 1 out of 3 pairs.
    Score: 0.33
    Program solution_v2.py solved 3 out of 3 pairs.
    Score: 1.00
    ==================================================
    Saved program for task 7 as version 1: Candidate_programs\task_7\solution_v1.py
    Saved program for task 7 as version 2: Candidate_programs\task_7\solution_v2.py
    Program solution_v1.py solved 0 out of 3 pairs.
    Score: 0.00
    Program solution_v2.py solved 0 out of 3 pairs.
    Score: 0.00
    ==================================================
    Saved program for task 8 as version 1: Candidate_programs\task_8\solution_v1.py
    Saved program for task 8 as version 2: Candidate_programs\task_8\solution_v2.py
    Program solution_v1.py solved 3 out of 4 pairs.
    Score: 0.75
    Program solution_v2.py solved 4 out of 4 pairs.
    Score: 1.00
    ==================================================
    Saved program for task 9 as version 1: Candidate_programs\task_9\solution_v1.py
    Saved program for task 9 as version 2: Candidate_programs\task_9\solution_v2.py
    Program solution_v1.py solved 4 out of 4 pairs.
    Score: 1.00
    Program solution_v2.py solved 4 out of 4 pairs.
    Score: 1.00
    ==================================================
    Saved program for task 10 as version 1: Candidate_programs\task_10\solution_v1.py
    Saved program for task 10 as version 2: Candidate_programs\task_10\solution_v2.py
    Error while executing program solution_v2.py for pair 1: list index out of range
    Error while executing program solution_v2.py for pair 3: list index out of range
    Program solution_v1.py solved 3 out of 4 pairs.
    Score: 0.75
    Program solution_v2.py solved 0 out of 4 pairs.
    Score: 0.00
    ==================================================

---
---

**When manually evaluating the programs on the test tasks of those 10 tasks the following accuracies were received:**

---

Task 1: 
- Program 1: Incorrect
- Program 2: Incorrect

Task 2: 
- Program 1: Incorrect
- Program 2: Incorrect

Task 3: 
- Program 1: Incorrect
- Program 2: Incorrect

Task 4: 
- **Program 1: Correct**
- **Program 2: Correct**

Task 5: 
- **Program 1: Correct**
- **Program 2: Correct**

Task 6: 
- Program 1: Incorrect
- Program 2: Incorrect

Task 7: 
- Program 1: Incorrect
- Program 2: Incorrect

Task 8: 
- Program 1: Incorrect
- **Program 2: Correct**

Task 9: 
- Program 1: Incorrect
- Program 2: Incorrect

Task 10: 
- Program 1: Incorrect
- Program 2: Incorrect

---

**Score: 3/10 or 30%**

---
---

# 03.04

## Additions:
Implemented a Revision-Step:
- For each LLM-generated program the performance on the demonstration pairs is evaluated. The revision-step is meant to only be used, if a program is unable to solve all of the tasks demonstration pairs correctly. Therefor for each program a score is calculated:

        Amount of correct transformations / 
        Amount of demonstration pairs

- Each program that has a score < 1 will be be sent back to the LLM together with the tasks demonstration pair inputs, outputs and the programs generated output. The LLM will be asked to create another program that is added to the task folder together with the already present programs.
- For each task there are currently 2-4 programs: 2 if both initial programs solve all demonstration pairs correctly, 3 if only one of the initial programs solves them all correctly, 4 if both initial programs were unable to solve the tasks demonstration pairs correctly.

---

**Revision Prompt:**


    revision_prompt = """
    In the following you'll receive a Python function that attempted to solve the following task. It did'nt succeed and you are tasked with fixing it.

    - The function must be named: `solve(grid: List[List[int]]) -> List[List[int]]`
    - Include only the code and necessary imports (e.g., `import numpy as np`)
    - Do not include comments, explanations, or print statements
    - Do not hard-code values or specific grid sizes — the function must generalize based on the patterns in the examples
    - Ensure your solution works for all provided input-output pairs
    """

---


The cost for solving 10 tasks, including the revision step, are about 2.27CHF. This could be higher, when the initial programs are not effective at solving the tasks (therefor leading to more revised programs being generated and thereby more API calls). There was'nt a improvement in the accuracy for the first 10 tasks of the Evaluation_set. Most revised programs (so programs of tasks that were'nt able to solve the demonstration pairs) were also unable to solve the demonstration pairs (with some improvements see e.g. task 8 where solution_v4.py [revision of solution_v2.py] was improved from no correct predictions to 0.5 [50%] correct predictions):



    Built tailored prompt.
    Saved program for task 1 as version 1: Candidate_programs\task_1\solution_v1.py
    Saved program for task 1 as version 2: Candidate_programs\task_1\solution_v2.py
    Revising solution_v1.py...
    Saved program for task 1 as version 3: Candidate_programs\task_1\solution_v3.py
    Revising solution_v2.py...
    Saved program for task 1 as version 4: Candidate_programs\task_1\solution_v4.py
    Task 1 evaluation results:
    Program solution_v1.py solved 0 out of 3 pairs. Score: 0.00
    Program solution_v2.py solved 0 out of 3 pairs. Score: 0.00
    Program solution_v3.py solved 0 out of 3 pairs. Score: 0.00
    Program solution_v4.py solved 0 out of 3 pairs. Score: 0.00
    ==================================================
    Built tailored prompt.
    Saved program for task 2 as version 1: Candidate_programs\task_2\solution_v1.py
    Saved program for task 2 as version 2: Candidate_programs\task_2\solution_v2.py
    Revising solution_v1.py...
    Saved program for task 2 as version 3: Candidate_programs\task_2\solution_v3.py
    Revising solution_v2.py...
    Saved program for task 2 as version 4: Candidate_programs\task_2\solution_v4.py
    Task 2 evaluation results:
    Program solution_v1.py solved 0 out of 4 pairs. Score: 0.00
    Program solution_v2.py solved 0 out of 4 pairs. Score: 0.00
    Program solution_v3.py solved 0 out of 4 pairs. Score: 0.00
    Program solution_v4.py solved 0 out of 4 pairs. Score: 0.00
    ==================================================
    Built tailored prompt.
    Saved program for task 3 as version 1: Candidate_programs\task_3\solution_v1.py
    Saved program for task 3 as version 2: Candidate_programs\task_3\solution_v2.py
    Revising solution_v1.py...
    Saved program for task 3 as version 3: Candidate_programs\task_3\solution_v3.py
    Revising solution_v2.py...
    Saved program for task 3 as version 4: Candidate_programs\task_3\solution_v4.py
    Task 3 evaluation results:
    Program solution_v1.py solved 0 out of 3 pairs. Score: 0.00
    Program solution_v2.py solved 0 out of 3 pairs. Score: 0.00
    Program solution_v3.py solved 0 out of 3 pairs. Score: 0.00
    Program solution_v4.py solved 0 out of 3 pairs. Score: 0.00
    ==================================================
    Built tailored prompt.
    Saved program for task 4 as version 1: Candidate_programs\task_4\solution_v1.py
    Saved program for task 4 as version 2: Candidate_programs\task_4\solution_v2.py
    Task 4 evaluation results:
    Program solution_v1.py solved 2 out of 2 pairs. Score: 1.00
    Program solution_v2.py solved 2 out of 2 pairs. Score: 1.00
    ==================================================
    Built tailored prompt.
    Saved program for task 5 as version 1: Candidate_programs\task_5\solution_v1.py
    Saved program for task 5 as version 2: Candidate_programs\task_5\solution_v2.py
    Task 5 evaluation results:
    Program solution_v1.py solved 3 out of 3 pairs. Score: 1.00
    Program solution_v2.py solved 3 out of 3 pairs. Score: 1.00
    ==================================================
    Built tailored prompt.
    Saved program for task 6 as version 1: Candidate_programs\task_6\solution_v1.py
    Saved program for task 6 as version 2: Candidate_programs\task_6\solution_v2.py
    Task 6 evaluation results:
    Program solution_v1.py solved 3 out of 3 pairs. Score: 1.00
    Program solution_v2.py solved 3 out of 3 pairs. Score: 1.00
    ==================================================
    Built tailored prompt.
    Saved program for task 7 as version 1: Candidate_programs\task_7\solution_v1.py
    Saved program for task 7 as version 2: Candidate_programs\task_7\solution_v2.py
    Revising solution_v1.py...
    Saved program for task 7 as version 3: Candidate_programs\task_7\solution_v3.py
    Revising solution_v2.py...
    Saved program for task 7 as version 4: Candidate_programs\task_7\solution_v4.py
    Task 7 evaluation results:
    Program solution_v1.py solved 0 out of 3 pairs. Score: 0.00
    Program solution_v2.py solved 0 out of 3 pairs. Score: 0.00
    Program solution_v3.py solved 0 out of 3 pairs. Score: 0.00
    Program solution_v4.py solved 0 out of 3 pairs. Score: 0.00
    ==================================================
    Built tailored prompt.
    Saved program for task 8 as version 1: Candidate_programs\task_8\solution_v1.py
    Saved program for task 8 as version 2: Candidate_programs\task_8\solution_v2.py
    Revising solution_v1.py...
    Saved program for task 8 as version 3: Candidate_programs\task_8\solution_v3.py
    Revising solution_v2.py...
    Saved program for task 8 as version 4: Candidate_programs\task_8\solution_v4.py
    Task 8 evaluation results:
    Program solution_v1.py solved 2 out of 4 pairs. Score: 0.50
    Program solution_v2.py solved 0 out of 4 pairs. Score: 0.00
    Program solution_v3.py solved 0 out of 4 pairs. Score: 0.00
    Program solution_v4.py solved 2 out of 4 pairs. Score: 0.50
    ==================================================
    Built tailored prompt.
    Saved program for task 9 as version 1: Candidate_programs\task_9\solution_v1.py
    Saved program for task 9 as version 2: Candidate_programs\task_9\solution_v2.py
    Task 9 evaluation results:
    Program solution_v1.py solved 4 out of 4 pairs. Score: 1.00
    Program solution_v2.py solved 4 out of 4 pairs. Score: 1.00
    ==================================================
    Built tailored prompt.
    Saved program for task 10 as version 1: Candidate_programs\task_10\solution_v1.py
    Saved program for task 10 as version 2: Candidate_programs\task_10\solution_v2.py
    Revising solution_v2.py...
    Saved program for task 10 as version 3: Candidate_programs\task_10\solution_v3.py
    Task 10 evaluation results:
    Program solution_v1.py solved 4 out of 4 pairs. Score: 1.00
    Program solution_v2.py solved 0 out of 4 pairs. Score: 0.00
    Program solution_v3.py solved 0 out of 4 pairs. Score: 0.00
    ==================================================

---

**Manual evaluation on the programs performance on the 10 tasks test inputs:**

---

Task 1: 
- Program 1: Incorrect
- Program 2: Incorrect
- Revised Program 1: Incorrect
- Revised Program 2: Incorrect

Task 2: 
- Program 1: Incorrect
- Program 2: Incorrect
- Revised Program 1: Incorrect
- Revised Program 2: Incorrect

Task 3: 
- Program 1: Incorrect
- Program 2: Incorrect
- Revised Program 1: Incorrect
- Revised Program 2: Incorrect

Task 4: 
- **Program 1: Correct**
- **Program 2: Correct**

Task 5: 
- **Program 1: Correct**
- **Program 2: Correct**

Task 6: 
- Program 1: Incorrect
- Program 2: Incorrect (Very close though)

Task 7: 
- Program 1: Incorrect
- Program 2: Incorrect
- Revised Program 1: Incorrect
- Revised Program 2: Incorrect

Task 8: 
- Program 1: Incorrect
- Program 2: Incorrect
- Revised Program 1: Incorrect
- Revised Program 2: Incorrect

Task 9: 
- Program 1: Incorrect
- Program 2: Incorrect

Task 10: 
- Program 1: Incorrect
- Program 2: Incorrect
- Revised Program 2: Incorrect

**Score: 2/10 or 20%** 


*Note: Task 8 before:

    def solve(grid):
        R, C = len(grid), len(grid[0])
        cols = [c for c in range(C) if grid[-1][c] != 0]
        for c in cols:
            val = None
            for r in range(R-1, -1, -1):
                if grid[r][c] != 0:
                    val = grid[r][c]
                elif val is not None:
                    grid[r][c] = val
        return grid

---
---

# 05.04

## Additions:
Implemented the the determination and selection of the two best performing programs for each task. 

- The programs (2-4) are sorted based on their score on the demonstration pairs.
- The path to the two best performing programs is returned.
- These two programs are then loaded and each generate a prediction for each of the tasks test inputs.
- The generated predictions are saved in a dict and subsequently in a .json file holding all solved tasks predictions.

This includes the following two functions:
- get_best_programs: Gets the two best performing programs for the task.
- generate_test_predictions: Generates the predictions for the tasks test inputs and saves them in a submissions dict.

## Current iteration of prompts (examples from task 1 in Evaluation_set):

**Keep in mind, that the system prompt containing role information, etc., is also passed to the LLM. Here the actual contents of the demonstration pairs has been replaced by "...", since they take a lot of space**

Secondary Prompt 1:

    List visual observations from the training pairs.

    - Use bullet points (max 10).
    - Focus on colors, shapes, object counts, positions, and differences.
    - Avoid reasoning or explanations.
    - Be concise. No full sentences, no extra formatting.

    Here are the demonstration pairs (JSON data):

    Train Input 1: ...
    Train Output 1: ...

    Train Input 2: ...
    Train Output 2: ...

    Train Input 3: ...
    Train Output 3: ...

---

Secondary Prompt 2:

    Describe the transformation(s) from input to output grids.

    - Use 3 to 5 short sentences.
    - Focus on what changes: movement, color, shape, duplication, etc.
    - Mention if the transformation is based on position, context, or rules.
    - Avoid implementation hints or code.

    Here are visual observations of the task at hand, that may assist you in identifying the transformation:

    - Black (0) used as background in all grids.
    - Train Input 1 shows contiguous blocks of pink (6), green (3), and light blue (8).
    - Rectangular and stripe‐like arrangements in Train Input 1.
    - Train Input 2 features clusters with blue (1), red (2), green (3), and light blue (8) in repeating sequences.
    - Horizontal and vertical regularity in object placement in Train Input 2.
    - Train Input 3 contains blocks of red (2) and green (3) with occasional blue (1) elements.
    - Several shapes form clearly defined, repeated patterns across rows.
    - Output grids simplify and extend contiguous color regions while erasing isolated markings.
    - Objects generally appear in organized, symmetric arrangements.
    - Consistent removal of non‐object pixels to emphasize core patterns.

    Now provide your transformation analysis based on these observations.

    Here are the demonstration pairs (JSON data):

    Train Input 1: ...
    Train Output 1: ...

    Train Input 2: ...
    Train Output 2: ...

    Train Input 3: ...
    Train Output 3: ...

---

Secondary Prompt 3:

    Reflect on how you would solve the task in Python.

    - Use 3 to 5 sentences.
    - Mention your overall approach, logical steps, and possible uncertainties.
    - Do not return code or pseudocode.

    Here are visual observations of the task that may help inform your implementation:
    - Black (0) used as background in all grids.
    - Train Input 1 shows contiguous blocks of pink (6), green (3), and light blue (8).
    - Rectangular and stripe‐like arrangements in Train Input 1.
    - Train Input 2 features clusters with blue (1), red (2), green (3), and light blue (8) in repeating sequences.
    - Horizontal and vertical regularity in object placement in Train Input 2.
    - Train Input 3 contains blocks of red (2) and green (3) with occasional blue (1) elements.
    - Several shapes form clearly defined, repeated patterns across rows.
    - Output grids simplify and extend contiguous color regions while erasing isolated markings.
    - Objects generally appear in organized, symmetric arrangements.
    - Consistent removal of non‐object pixels to emphasize core patterns.

    Here are the transformation rules that have been identified based on the task:
    The transformation first identifies regions of contiguous non‐background colors and discards isolated or stray pixels. It then simplifies these regions by extending them into uniform, rectangular blocks with consistent color filling, resulting in symmetric and regularly positioned patterns. The output retains the central, repeated color structures while the background remains black, emphasizing the core design. Overall, the process is based on spatial connectivity and regularity in the arrangement of color blocks.

    Now reflect on how you would implement a solution to this task in Python, following the instructions above.

    Here are the demonstration pairs (JSON data):

    Train Input 1: ...
    Train Output 1: ...

    Train Input 2: ...
    Train Output 2: ...

    Train Input 3: ...
    Train Output 3: ...

---

Task-tailored Prompt:

    Implementation Reflection:
    I would begin by scanning the input grid to identify contiguous regions of non‑background pixels using a flood-fill or connected component analysis. Once identified, I would compute the bounding box for each component and filter out any regions that are too isolated or small to be considered objects. For retained regions, I would extend the boundaries to form clean rectangular blocks and fill them uniformly with the corresponding color, ensuring that the symmetric and regular patterns emerge. One uncertainty is tuning the thresholds for what counts as an “object” versus stray pixels and handling edge cases where the contiguous region might not form a neatly defined rectangle.

    Write a Python function that correctly transforms each input grid into its corresponding output grid based on the given examples.

    - The function must be named: `solve(grid: List[List[int]]) -> List[List[int]]`
    - Include only the code and necessary imports (e.g., `import numpy as np`)
    - Do not include comments, explanations, or print statements
    - Do not hard-code values or specific grid sizes — the function must generalize based on the patterns in the examples
    - Ensure your solution works for all provided input-output pairs

    Here are the demonstration pairs (JSON data):

    Train Input 1: ...
    Train Output 1: ...

    Train Input 2: ...
    Train Output 2: ...

    Train Input 3: ...
    Train Output 3: ...

=> To save tokens only the reflection of the code implementation (response to secondary prompt 3), was added to the task-tailored prompt for now. Later on effectivity will be checked, if all information (secondary prompt 1-3) is added to the task-tailored prompt.

---

Revision Prompt:

    In the following you'll receive a Python function that attempted to solve the following task. It did'nt succeed and you are tasked with fixing it.

    - The function must be named: `solve(grid: List[List[int]]) -> List[List[int]]`
    - Include only the code and necessary imports (e.g., `import numpy as np`)
    - Do not include comments, explanations, or print statements
    - Do not hard-code values or specific grid sizes — the function must generalize based on the patterns in the examples
    - Ensure your solution works for all provided input-output pairs


    Here is the generated code:
    def solve(grid):
        from collections import Counter
        h = len(grid)
        if h == 0:
            return grid
        w = len(grid[0])
        out = [row[:] for row in grid]
        # determine contiguous groups of rows that are “non‐empty”
        groups = []
        i = 0
        while i < h:
            if any(val != 0 for val in grid[i]):
                start = i
                while i < h and any(val != 0 for val in grid[i]):
                    i += 1
                groups.append(list(range(start, i)))
            else:
                i += 1
        # for each group, process column segments where at least one row has a nonzero
        for group in groups:
            # create a boolean mask for columns in group
            colmask = [False]*w
            for j in range(w):
                for r in group:
                    if grid[r][j] != 0:
                        colmask[j] = True
                        break
            # find contiguous segments in colmask
            segs = []
            j = 0
            while j < w:
                if colmask[j]:
                    start = j
                    while j < w and colmask[j]:
                        j += 1
                    segs.append((start, j-1))
                else:
                    j += 1
            # for each segment, update the rows column‐by‐column
            for seg in segs:
                s, e = seg
                # for the top row of the group, take the mode of its nonzero values in the segment
                top_vals = [grid[group[0]][j] for j in range(s, e+1) if grid[group[0]][j] != 0]
                if top_vals:
                    top_mode = Counter(top_vals).most_common(1)[0][0]
                else:
                    top_mode = 0
                # For top row, if the entire segment has a mode different from a mixed pattern, force it uniform.
                out[group[0]] = out[group[0]][:1] + out[group[0]][1:]
                for j in range(s, e+1):
                    out[group[0]][j] = top_mode
                # For each subsequent row in the group, update column j if that row is nonzero in that column.
                for r in group[1:]:
                    for j in range(s, e+1):
                        if grid[r][j] != 0:
                            # collect all nonzero values in column j for rows in group excluding the top row
                            vals = [grid[r2][j] for r2 in group[1:] if grid[r2][j] != 0]
                            if vals:
                                mode_val = Counter(vals).most_common(1)[0][0]
                            else:
                                mode_val = grid[r][j]
                            out[r][j] = mode_val
        return out


    if __name__ == '__main__':
        import sys, json
        data = sys.stdin.read().strip()
        if not data:
            exit(0)
        arr = json.loads(data)
        res = solve(arr)
        sys.stdout.write(json.dumps(res))

    Demonstration Pairs:
    1. Input: ...
    Expected Output: ...
    Generated Output: ...
    2. Input: ...
    Expected Output: ...
    Generated Output: ...
    3. Input: ...
    Expected Output: ...
    Generated Output: ...

    Please revise the code.