import g4f

MODEL = "gpt-3.5-turbo"
ROLE = "user"


class GPT:
    def send(self, message: str):
        data = []
        for m in self.create_response(message):
            data.append(m)
        return ''.join(data)

    @staticmethod
    def create_response(message: str):
        return g4f.ChatCompletion.create(
            model=MODEL,
            messages=[{"role": ROLE, "content": message}],
            stream=True,
        )


def main():
    gpt = GPT()
    result = gpt.send('Как подключиться к аккаунту в телеграмме через бота')
    print(result)
    # gpt.sendMany(['Как подключиться к акануту в телеграмме через бота', 'Как сварить картошку'])


if __name__ == '__main__':
    main()

