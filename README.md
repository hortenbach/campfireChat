# campfireChat
ChatGPT RPG – Prompt Engineering For Storytellers

## How To Use

Note: You need you own openAI api key.
Create an .env file in the root directory and provide your api key
```
API_KEY=superSecretKeyNoQuotasNeeded123
```

## About Prompt Engineering
Prompt engineering refers to the process of carefully crafting prompts or instructions to guide language models like ChatGPT in producing desired outputs. It involves constructing prompts in a way that elicits specific responses or behaviors from the model.

Effective prompt engineering is essential for achieving the desired results when using language models. Here are some strategies and techniques commonly used in prompt engineering:

    Specify the format: Clearly define the desired format of the answer or response you expect from the model. For example, you can explicitly state that you want a bullet-point list, a complete sentence, or a short paragraph.

    Provide context: Set the context for the model by including relevant information in the prompt. This can help the model understand the background and context necessary to generate accurate and meaningful responses.

    Ask the model to think step-by-step: If you want the model to provide a detailed response or perform a series of actions, ask it to think through the process step-by-step. This can help avoid the model overlooking important details.

    Specify the desired output length: You can control the length of the generated response by setting a maximum token limit. Tokens represent individual words or characters in the model's input and output.

    Use system messages: You can use system-level instructions or messages to guide the model's behavior. System messages are prefixes provided to the model to influence its response style. For example, you can use a system message like "You are an expert in this field, provide a detailed explanation."

    Experiment and iterate: Prompt engineering often requires experimentation and iteration. Start with simple prompts, test the model's responses, and refine your prompts based on the results. Continuously refine and improve your prompts to achieve better outcomes.

It's important to note that prompt engineering can be a complex process, and the effectiveness of prompts may vary based on the specific language model, task, and domain. It's recommended to experiment with different prompt strategies, iterate, and evaluate the model's responses to refine your prompt engineering approach.

## chatGPT prompts vs messages
The old syntac was sending a prompt. In fact thats what the model suggested when I asked it to teach me prompt engineering. 
The current state of the art is sending messages. A message consists of a role and a content.