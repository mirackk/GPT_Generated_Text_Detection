# GPT_GENERATED_TEXT_DETECTION

## Summary
This is a simple project to test whether some simple models can identify some text is generated by AI or human.

## Data
### Format
Input: 2 cols
id | labels | text
labels: Whether the essay was written by a human (0) or generated by an LLM (1)
example
```
123 0 Cars have been around since they became famous in the 1900s, when Henry Ford created and built the first ModelT. Cars have played a major role in our every day lives since then. But now, people are starting to question if limiting car usage would be a good thing. To me, limiting the use of cars might be a good thing to do.
```
The model is expected to classify a text to label 0 or 1

## Result
### Metrics
Accuracy
F1 score
Auc
Trainint time
Inference Time