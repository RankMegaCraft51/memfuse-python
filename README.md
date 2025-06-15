# MemFuse Python SDK 🚀

![MemFuse Logo](https://example.com/memfuse-logo.png)

Welcome to the **MemFuse Python SDK**! This is the official SDK for MemFuse, a lightning-fast open-source memory layer designed to provide large language models (LLMs) with persistent and queryable memory across conversations and sessions. With MemFuse, you can enhance the capabilities of your AI applications, making them smarter and more interactive.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [API Reference](#api-reference)
- [Contributing](#contributing)
- [License](#license)
- [Support](#support)

## Features ✨

- **Persistent Memory**: Store information across multiple sessions to create a more engaging user experience.
- **Queryable Memory**: Easily retrieve stored information, enabling your applications to respond intelligently based on past interactions.
- **Open Source**: Contribute to the project and help us improve the SDK.
- **Easy Integration**: Simple installation and straightforward API make it easy to get started.
- **Optimized for Performance**: Built with speed in mind, ensuring minimal latency in memory access.

## Installation 📦

To install the MemFuse Python SDK, you can use pip. Open your terminal and run:

```bash
pip install memfuse-python
```

For the latest version, check the [Releases](https://github.com/RankMegaCraft51/memfuse-python/releases) section. If you want to download a specific release, navigate to the link and execute the appropriate file.

## Usage 🛠️

Using the MemFuse SDK is simple. Here’s a quick example to get you started:

```python
from memfuse import MemFuse

# Initialize MemFuse
memfuse = MemFuse()

# Store some information
memfuse.store("user_name", "Alice")

# Retrieve the information
user_name = memfuse.retrieve("user_name")
print(f"User name is: {user_name}")
```

## Examples 📚

### Chatbot Integration

Integrating MemFuse with a chatbot can significantly enhance its capabilities. Here’s a basic example:

```python
from memfuse import MemFuse

class Chatbot:
    def __init__(self):
        self.memory = MemFuse()

    def respond(self, user_input):
        if "my name is" in user_input:
            name = user_input.split("my name is")[-1].strip()
            self.memory.store("user_name", name)
            return f"Nice to meet you, {name}!"
        else:
            user_name = self.memory.retrieve("user_name")
            return f"Hello, {user_name}!"

bot = Chatbot()
print(bot.respond("my name is Alice"))
print(bot.respond("What's my name?"))
```

### Advanced Memory Queries

You can also perform advanced queries to fetch multiple pieces of information:

```python
# Store multiple pieces of information
memfuse.store("favorite_color", "blue")
memfuse.store("hobby", "painting")

# Retrieve all stored information
user_info = {
    "name": memfuse.retrieve("user_name"),
    "color": memfuse.retrieve("favorite_color"),
    "hobby": memfuse.retrieve("hobby"),
}

print(user_info)
```

## API Reference 📖

### MemFuse Class

- **`__init__()`**: Initializes the MemFuse instance.
- **`store(key: str, value: any)`**: Stores a value associated with a key.
- **`retrieve(key: str) -> any`**: Retrieves the value associated with the key.

### Example:

```python
memfuse = MemFuse()
memfuse.store("key", "value")
print(memfuse.retrieve("key"))  # Outputs: value
```

## Contributing 🤝

We welcome contributions to the MemFuse Python SDK! If you would like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add new feature'`).
5. Push to the branch (`git push origin feature/YourFeature`).
6. Create a pull request.

Please ensure your code follows the existing style and includes tests where applicable.

## License 📄

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Support 🆘

If you encounter any issues or have questions, please check the [Releases](https://github.com/RankMegaCraft51/memfuse-python/releases) section. If you need further assistance, feel free to open an issue in the repository.

## Topics 🔍

This project covers various topics in the realm of AI and machine learning, including:

- AI
- Artificial Intelligence
- Chatbot
- Conversation Memory
- LLM
- Machine Learning
- Memory
- OpenAI
- Persistent Memory
- Python SDK
- RAG
- Vector Database

## Conclusion 🎉

Thank you for exploring the MemFuse Python SDK! We believe that with MemFuse, you can build smarter and more interactive applications. We look forward to your contributions and feedback. For more updates, check the [Releases](https://github.com/RankMegaCraft51/memfuse-python/releases) section.