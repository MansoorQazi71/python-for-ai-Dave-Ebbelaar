class BaseModel:

    def __init__(self, model_name):

        self.model_name = model_name

        self.is_loaded = False
    
    def load(self):

        print(f"Loading {self.model_name}...")

        self.is_loaded = True


class TextModel(BaseModel):

    def __init__(self, model_name, max_length=1000):

        super().__init__(model_name)
        self.max_length = max_length
    
    def process_text(self, text):
        if not self.is_loaded:
            self.load()
        # Truncate if needed
        if len(text) > self.max_length:
            text = text[:self.max_length]
            print(f"Warning: text truncated to {self.max_length} characters")

        return f"Processed: {text}"


# Use the model - with named arguments

model = TextModel(model_name="gpt-3.5-turbo", max_length=100)


# Call method - notice no 'self' parameter needed

result = model.process_text(text="""
Why do we use it?
It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).
""")

print(result)  # Loading gpt-3.5-turbo...

               # Processed: Hello world

# print(model.max_length)
# print(len(result))                         