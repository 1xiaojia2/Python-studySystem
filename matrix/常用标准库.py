import openai

# set your API key
openai.api_key = "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"

# use the GPT-3 model
prompt = f"Please generate a text with GPT-3"

completions = openai.Completion.create(
    engine="text-davinci-002",
    prompt="介绍一下你自己",
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

# print the generated text
message = completions.choices[0].text
print(message)
