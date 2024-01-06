from helperfunc import *

# Text to summarize
prod_review = """
These headphones are a lifesaver for my commute!
They block out all the noise from the train and let me focus on my music or podcasts.
The sound quality is amazing, and they're super comfortable to wear for hours.
I was a bit hesitant about the price, but they're worth every penny.
The free shipping was a nice bonus too!
"""

# General
prompt = f"""
Summarize the general sentiment and main features 
mentioned in these product reviews
below, delimited by triple 
backticks. 

Review: ```{prod_review}```
"""

response = get_completion(prompt)
print(f'\nResponse: {response}')

# Summarize with a focus on shipping and delivery
prompt = f"""
Summarize the review below, delimited by triple 
backticks, in at most 30 words, and focusing on any aspects \
that mention shipping and delivery of the product.

Review: ```{prod_review}```
"""

response = get_completion(prompt)
print(f'\n\n\nResponse: {response}')

# Summarize with a focus on price and value
prompt = f"""
Summarize the review below, delimited by triple 
backticks, in at most 30 words, and focusing on any aspects \
that are relevant to the price and perceived value. 

Review: ```{prod_review}```
"""

response = get_completion(prompt)
print(f'\nResponse: {response}')

# Word Limit and Pros/Cons
prompt = f"""
From the review below, delimited by triple quotes \
extract the information relevant to shipping and \ 
delivery. Limit to 30 words. Highlight pros and cons.
Review: ```{prod_review}```
"""

response = get_completion(prompt)
print(f'\n\n\nResponse: {response}')