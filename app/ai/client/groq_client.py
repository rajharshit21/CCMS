from groq import Groq

from app.core.config import settings


class GroqClient:
    """
    Wrapper around the Groq API.
    """

    def __init__(self):
        self.client = Groq(
            api_key=settings.GROQ_API_KEY,
        )

        self.model = settings.GROQ_MODEL

    def generate(
        self,
        prompt: str,
    ) -> str:
        """
        Send a prompt to the Groq model and return the response text.
        """

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            temperature=0.2,
        )

        content = response.choices[0].message.content

        # ---------- Debug Output ----------
        print("\n" + "=" * 80)
        print("GROQ RAW RESPONSE")
        print("=" * 80)
        print(repr(content))
        print("=" * 80 + "\n")
        # -------------------------------

        return content.strip()