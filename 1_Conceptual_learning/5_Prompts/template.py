from langchain_core.prompts import PromptTemplate


#We should make a separate file for template.
#This makes the prompt reusable
template = PromptTemplate(
    template = """
    Summarize the following text.
    Text:
    {input_text}

    Requirements:
    - Length: {desired_length}
    - Focus on: {optional_focus}
    - Output format: {output_format}
    """,
    input_variables=['input_text','desired_length','optional_focus','output_format'],
    validate_template=True
)


template.save('1_Conceptual_learning/5_Prompts/template.json')
#run file as "python 1_Conceptual_learning\5_Prompts\template.py"


"""
Why use PromptTemplate, when f string does the same thing?
PrompTemplate gives some benefits: 
1. Default Validation: Validation of inputs in the template "validate_template=True"
2. Easy integration with langchain ecosystem
3. Reusablity
"""