# data_utils.py

import os

# Example of populating train_texts with training text data
train_texts = []
neg_texts = []
pos_texts = []

# Assuming you have text files in a directory named 'train'
train_dir = 'train'
for category in ['neg', 'pos']:
    category_dir = os.path.join(train_dir, category)
    for filename in os.listdir(category_dir):
        if filename.endswith('.txt'):
            file_path = os.path.join(category_dir, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                train_texts.append(content)
                if category == 'neg':
                    neg_texts.append(content)
                else:
                    pos_texts.append(content)
