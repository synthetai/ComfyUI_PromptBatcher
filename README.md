# ComfyUI_PromptBatcher

A custom node extension for ComfyUI that enables batch processing of prompts from text files to generate multiple images.

[中文文档](README_CN.md)

## Features

- Load multiple prompt files from a directory
- Filter files by prefix
- Limit the number of files to process
- Start from a specific index
- Force reload option for dynamic workflows

## Installation

1. Clone this repository into your ComfyUI custom nodes folder:
```bash
cd ComfyUI/custom_nodes/
git clone https://github.com/USERNAME/ComfyUI_PromptBatcher.git
```

2. Restart ComfyUI

## Usage

The extension adds a new node called "Load Prompts From Dir" in the JMNodes category.

### Node Inputs

- **directory**: Path to the folder containing your prompt text files
- **file_prefix** (optional): Only load files that start with this prefix
- **file_load_cap** (optional): Limit the number of files to load (0 = no limit)
- **start_index** (optional): Start loading from this index in the file list
- **load_always** (optional): Force reload files on every execution

### Node Outputs

- **PROMPT**: A list of prompt strings loaded from the text files
- **FILE_PATH**: A list of absolute file paths for the loaded files

## Example Workflow

1. Add the "Load Prompts From Dir" node
2. Connect it to a "KSampler (Advanced)" node
3. Set up a batch workflow to process each prompt in sequence

## Example Directory Structure

```
prompts/
├── prompt1.txt
├── prompt2.txt
└── prompt3.txt
```

Each text file should contain a single prompt.

## Project Structure

```
ComfyUI_PromptBatcher/
├── nodes/                    # Custom nodes implementation
│   ├── __init__.py           # Node registration
│   ├── prompt_batcher.py     # LoadPromptsFromDir node
│   └── ...                   # Future nodes can be added here
├── examples/                 # Example workflows and prompts
│   ├── basic_batch_workflow.json
│   └── prompts/
│       ├── prompt1.txt
│       └── prompt2.txt
├── __init__.py               # Package initialization
├── setup.py                  # Installation setup
├── requirements.txt          # Dependencies (none required)
├── README.md                 # English documentation
├── README_CN.md              # Chinese documentation
└── LICENSE                   # MIT License
```

## License

MIT License

## Credits

Created by [Your Name]