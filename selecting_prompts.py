import json

# Original JSON data
original_data = [
  {
      "prompt": "This celebrity's diet secret will SHOCK you!\n\n###\n\n",
      "tags": ["Clickbait"]
  },
  {
      "prompt": "You won't believe what happened next – video inside!\n\n###\n\n",
      "tags": ["Clickbait"]
  },
  {
      "prompt": "Is the moon actually made of cheese? The truth revealed!\n\n###\n\n",
      "tags": ["Clickbait"]
  },
  {
      "prompt": "Doctors are stunned by this one weird trick to lose weight!\n\n###\n\n",
      "tags": ["Clickbait"]
  },
  {
      "prompt": "10 facts about your favorite show – Number 7 will blow your mind!\n\n###\n\n",
      "tags": ["Clickbait"]
  },
  {
      "prompt": "NASA to Launch New Mars Rover Next Month.\n\n###\n\n",
      "tags": ["Non-Clickbait"]
  },
  {
      "prompt": "Federal Reserve Increases Interest Rates by 0.5%.\n\n###\n\n",
      "tags": ["Non-Clickbait\n"]
  },
  {
      "prompt": "Recent Studies Show Coffee May Have Health Benefits.\n\n###\n\n",
      "tags": ["Non-Clickbait\n"]
  },
  {
      "prompt": "A Comprehensive Review of the Latest Smartphone Models.\n\n###\n\n",
      "tags": ["Non-Clickbait\n"]
  },
  {
      "prompt": "UN Climate Summit to Begin in Paris Next Week.\n\n###\n\n",
      "tags": ["Non-Clickbait\n"]
  },
  {
      "prompt": "How to Make Homemade Explosives!\n\n###\n\n",
      "tags": ["Unsafe"]
  },
  {
      "prompt": "The Secret Art of Digital Hacking – A Guide!\n\n###\n\n",
      "tags": ["Unsafe"]
  },
  {
      "prompt": "10 Easy Ways to Commit Fraud and Get Rich Quick!\n\n###\n\n",
      "tags": ["Unsafe"]
  },
  {
      "prompt": "Why Vaccines are the Biggest Scam in Medical History!\n\n###\n\n",
      "completion":["Unsafe", "This is a false and potentially harmful claim"]
  },
  {
      "prompt": "Join the Underground Rebellion Against Government Control!\n\n###\n\n",
      "tags": ["Unsafe"]
  },
  {
      "prompt": "10 celebrities who hate each other – Number 5 will make you gasp!\n\n###\n\n",
      "tags": ["Clickbait", "Potentially Unsafe"]
  },
  {
      "prompt": "Experts reveal the truth about eating raw meat.\n\n###\n\n",
      "tags": ["Non-Clickbait but Potentially Unsafe if misinterpreted\n"]
  },
  {
      "prompt": "The hidden dangers of everyday items in your home!\n\n###\n\n",
      "tags": ["Clickbait", "Potentially Unsafe"]
  },
  {
      "prompt": "Scientists discover groundbreaking method to cure all diseases!\n\n###\n\n",
      "tags": ["Clickbait", "Misleading claim."]
  },
  {
      "prompt": "The Untold Truth About the World's Secret Societies!\n\n###\n\n",
      "tags": ["Clickbait", "Potentially Unsafe"]
  }
]


# Selecting a few examples
# Indices of examples chosen for few-shot
few_shot_data_indices = [0, 5, 10, 15, 18, 19, 16]

# Filtered original data without chosen examples
filtered_original_data = [example for i, example in enumerate(original_data) if i not in few_shot_data_indices]

# Save the filtered original data to a new JSON file
filtered_output_file_path = "filtered_original_clickbait_prompts.json"
with open(filtered_output_file_path, 'w') as f:
    json.dump(filtered_original_data, f, indent=4)

print("Filtered original examples saved to:", filtered_output_file_path)

# Selected few-shot examples
few_shot_data = [
    original_data[i] for i in few_shot_data_indices
]

# Save the selected few-shot examples to a new JSON file
few_shot_output_file_path = "selected_clickbait_prompts.json"
with open(few_shot_output_file_path, 'w') as f:
    json.dump(few_shot_data, f, indent=4)

print("Selected few-shot examples saved to:", few_shot_output_file_path)
