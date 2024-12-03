# sample instructions 

def convert_best_practices_to_markdown(data):
    markdown_output = ""
    for i, item in enumerate(data):
        markdown_output += f"{str(i+1)}. {item['title']}\n\n"
        markdown_output += f"{item['explanation']}\n\n"
        if "examples" in item:
            markdown_output += "> Examples:\n\n"
            for example in item["examples"]:
                markdown_output += f"- **{example['description']}**\n\n"
                markdown_output += f"```python\n{example['code']}\n```\n\n"
    return markdown_output

def convert_list_to_markdown(data) : 
    markdown_output = ""
    for i, item in enumerate(data) : 
        markdown_output += f"{str(i+1)}. {item}"
        
    return markdown_output