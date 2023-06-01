import config
import openai

class ChatGPT:
    def __init__(self):
        self.api_key = config.api_key

    def ask(self, question, model='gpt-3.5-turbo'):
        openai.api_key = self.api_key

        prompt = f'Q: {question}\nA:'
        response = openai.Completion.create(
            engine=model,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.7,
        )
        answer = response.choices[0].text.strip()
        return answer

openai.api_key = config.api_key

message = [{"role": "system", "content": ""}]
content = input("Que deseas saber? ")
chatbot = ChatGPT()
answer = chatbot.ask(content, model='gpt-3.5-turbo')
message[0]["content"] = answer
print(message[0]["content"])
