from trainmodel import run_training
from transformers import AutoTokenizer
import torch

model_type = "albert-base-v2"
train_path = "data/fen_games_train.txt"
test_path = "data/fen_games_test.txt"


model = run_training(model_type, train_path, test_path)

# All this should be made into a "next_move" function or something similar
input_sequence = "SHOULD TAKE AS INPUT FOR FUNCTION"
tokenizer = AutoTokenizer.from_pretrained(model_type, eos_token='<|endoftext|>')
# Encode the input sequence as a list of token indices
input_tokens = tokenizer.encode(input_sequence)

# Convert the list of token indices to a tensor
input_tensor = torch.tensor(input_tokens).unsqueeze(0)  # add a batch dimension

# Generate the next move
with torch.no_grad():  # disable gradient calculation to speed up the prediction
    output_tokens = model.generate(input_tensor, max_length=1, pad_token_id=tokenizer.pad_token_id)

# Decode the predicted tokens to get the next move
next_move = tokenizer.decode(output_tokens[0], skip_special_tokens=True)