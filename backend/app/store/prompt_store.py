MILESTONE_BREAKDOWN = """
    Generate a structured milestone plan for a project:

    ### Description: 
    # {project_description}    

    Please provide the output in the following format:
    {format_instructions}

    > Project description must be atleast 100 words.
    > Each milestone description must be atleast 200 words.
    > Each task description must be atleast 500 words.

    ```````
    NOTE: in the milestones only given milestone name no milestone numbers and there shouldn't be any more than 5 milestones.
"""

SUMMARIZE_PDF = """
    You are an intelligent Ai agent specialized in summarizing `Project reports` uploaded by students. 
    You have to make it brief so that the instructor can easily go through the report at once. You have to break it down to the following points : 
        - summary
        - key insights 
        - additional notes 
        - tags 

    ### Project report : 
    # {project_report}

    Please provide the output in the following format:
    {format_instructions}

    ```````
    NOTE: DO NOT exceed the defined `max_lengths` for any parameter. Try to keep the output as brief as possible
"""

GENERATE_BEST_PRACTICES = """
    You are an intelligent Ai agent specialized in code reviewing. 
    You have to list down top 5 coding practices for {language} and also provide some example of that practice. 

    ```````
    ## Example : 
    Language: Python
    #### 1. **Use Type Hints**
        - Python supports type hints, which improve code readability and make it easier to catch errors.
        ```python
        def add_numbers(a: int, b: int) -> int:
            return a + b
        ```

    #### 2. **Use Docstrings for Documentation**
        - Add docstrings to modules, classes, and functions to explain what they do.
        - Follow the PEP 257 convention for docstrings.

        ```python
        def add(a: int, b: int) -> int:
            """"Return the sum of two numbers.""""
            return a + b
    ```

    #### 7. **Keep Code DRY (Don’t Repeat Yourself)**
        - Avoid redundant code by using functions or classes for repeated logic.
        - Promote code reuse and modularity.

    ```````
    
    ## Prompt : 
    Please generate top 5 best coding practices for {language}

    Please provide the output in the following format:
    {format_instructions}

"""

EXPAND_TEXT = """
    You are an intelligent Ai agent specialized in explaining projects in more detail.

    Explain the project in more detail given the following within {token_limits} words.

    ### project description : {description}
    ### project title : {title} 

    Please provide the output in the following format:
    {format_instructions}

    ```````
"""

GUIDELINE_CHECK = """
    You are an intelligent Ai agent specialized in code reviewing.  
    You have to check if the best pratices guidelines are followed for the give code below

    ### code : 
    ```{language}

    {code}
    
    ```

    You have to check if the code is following all the best practices mentioned below :
        {best_practices_list}

    > Keep the titles for best practices as it is. 
        
    Please provide the output in the following format:
    {format_instructions}
    
    ```````
    NOTE: Comments and Overall_feedback should be atleast 100 words each.
"""



SUMMARIZE_CODE = """
    You are an intelligent Ai agent specialized in summarizing multiple homogeneous texts.  
    Given a list of sentences you have to summarize them into multiple point, each point will be having title and descriptions.

    ### Text content : 
    {text_content}

    Please provide the output in the following format:
    {format_instructions}
    
    ```````
    NOTE: Descriptions should be atleast 100 words each.
"""

TEST_CASE_FAILED = """
    A given code section has failed to follow the following best practice and there are some comments given below. 
    Your task is to summarize the comments and give suggestions to improve the code so that it can follow the best practice.

    ### Best practice : 
    {best_practice}
    ### comments : 
    {comments}

    Please provide the output in the following format:
    {format_instructions}
    ```````
"""

TEST_CASE_PASSED = """
    A given code section has followed the following best practice and there are some comments given below. 
    Your task is to summarize the comments and give suggestions to improve the code further to follow the best practice more effectively.

    ### Best practice : 
    {best_practice}
    ### comments : 
    {comments}

    Please provide the output in the following format:
    {format_instructions}

    ```````
"""