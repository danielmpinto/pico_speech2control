# # from google import genai
# import os, subprocess
# from google import genai

# # client = genai.Client()

# # doc_datasheet = client.files.upload(file="RP-008299-DS-3-pico-2-datasheet.pdf")
# # doc_sdk = client.files.upload(file="RP-008355-DS-1-raspberry-pi-pico-python-sdk.pdf")





# # install requirements inside environment
# # subprocess.Popen(["pip", "install", "-r", "requirements.txt"])

# # ## ask llm for code
# # interaction = client.interactions.create(
# #     model="gemini-3.8-flash",
# #     input=[
# #         # {"type": "document", "uri": doc_datasheet.uri, "mime_type": doc_datasheet.mime_type},
# #         # {"type": "document", "uri": doc_sdk.uri, "mime_type": doc_sdk.mime_type},
# #         {"type": "text", "text": "Create a micropython code for controlling a motor connected in pins 14,15,16 and 17. Pico 2. Returning only code, please, withou any other caracter."}
# #     ]
# # )
# # print(interaction.output_text)
# client = genai.Client()

# interaction = client.interactions.create(
#     model="gemini-3.8-flash",
#     input="Explain how AI works in a few words"
# )
# print(interaction.output_text)

# ## creates file

# # input = 3
# code = str(input)
# subprocess.Popen(["echo", code])



# ## compiles and test
# ## send to target

from google import genai
import subprocess

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash-lite",
    input="Create a micropython code for controlling a motor connected in pins 14,15,16 and 17. Pico 2. Returning only code, please, withou any other caracter."
)
# print(interaction.output_text)


# ## creates file

# input = 3
code = str(input) + " >" + " output.py"
subprocess.Popen(["echo ", code])