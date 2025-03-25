from openai import AzureOpenAI


def llm_call(prompt: str, client: AzureOpenAI, system_prompt: str = "", model="gpt-4o") -> str:
    """
    Calls the Azure OpenAI model with the given prompt and returns the response.

    Args:
        prompt (str): The user prompt to send to the model.
        system_prompt (str, optional): The system prompt to send to the model. Defaults to "".
        model (str, optional): The model to use for the call. Defaults to "gpt-4o".

    Returns:
        str: The response from the language model.
    """
    messages = [{"role": "system", "content": system_prompt}, {"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        max_tokens=4096,
        temperature=0.1
    )

    # Access the content of the first message in choices
    return response.choices[0].message.content
