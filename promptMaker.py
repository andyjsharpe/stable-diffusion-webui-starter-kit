### Constants for formatting

# Any value in the /scripts/prompts_from_file.py's prompt_tags dictionary can be used, though not all are implemented
lineFormat = "--prompt {} --negative_prompt {}"  # PositivePrompt, NegativePrompt
weightFormat = "({}:{})"  # Prompt, weight
mixPromptFormat = "{{({}:{}) | ({}:{})}}"  # Start, interp, End, 1-interp
stepPromptFormat = "[{} : {} : {}]"  # Start, End, 1-interp


### Helper Functions

def set_weight(prompt, weight):
    return weightFormat.format(prompt, weight)


def blend_prompts(prompt1, prompt2, interpolator):
    return mixPromptFormat.format(prompt1, str(interpolator), prompt2, str(1 - interpolator))


def blend_prompts_step(prompt1, prompt2, interpolator):
    return stepPromptFormat.format(prompt1, prompt2, str(1 - interpolator))


def create_line(positivePrompts, negativePrompts):
    return lineFormat.format(positivePrompts, negativePrompts)


def put_lines_in_file(lineArray, fileName):
    f = open(fileName, "w+")
    for line in lineArray:
        print(line)
        f.write(line + "\n")
    f.close()


### Code to output prompts

positivePrompt = set_weight("crowded highway", 1.25) + blend_prompts("red car", "purple car", 0.5)
negativePrompt = "trucks"

lines = [create_line(positivePrompt, negativePrompt), create_line(set_weight(positivePrompt, 0.5) + "volcano", negativePrompt)]

put_lines_in_file(lines, "out.txt")
