from typing import List, Dict

class PromptFormatter:
    @classmethod
    def messages_to_query(cls, messages: List[Dict[str, str]]) -> str:
        query_string = ""
        for message in messages:
            role = message.get("role", "unknown").capitalize()
            content = message.get("content", "")
            query_string += f"{role}: {content}\\n"
        return query_string.strip()
