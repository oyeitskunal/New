

# Code Word Transformer

## Description
This Python program allows you to encode and decode text based on a specific transformation rule applied to each word. You can either encode words using a custom cipher method or decode previously encoded words back to their original form.

## Features
- **Encoding:** Transforms words based on a specific cipher rule.
- **Decoding:** Reverts encoded words back to their original form.
- **Custom Rules:** Applies transformation rules based on word length and specific prefixes/suffixes.

## Usage
1. **Input**: Enter a code word or phrase.
2. **Mode Selection**: Choose between encoding (1) or decoding (0).
3. **Output**: See the transformed text based on your selection.

## Encoding Method
- For encoding, the program prefixes the word with "dsf", appends "jkr", and rotates the middle characters.
- Example: "example" becomes "dsxamlepjkr".

## Decoding Method
- For decoding, the program identifies words prefixed with "dsf" and suffixed with "jkr", then reverses the transformation.
- Example: "dsxamlepjkr" decodes back to "example".

## Requirements
- Python 3.x

## How to Run
1. Clone the repository: `git clone https://github.com/oyeitskunal/new.git`
2. Navigate to the project directory: `cd your-repo`
3. Run the script: `python code_word_transformer.py`
4. Follow the prompts to encode or decode text as desired.

## Contribution
Contributions are welcome! If you have ideas for improvements, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

