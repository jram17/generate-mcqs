import json
import random

def loadJson(fname):
    with open(fname, 'r') as file:
        mcqs = json.load(file)
    return mcqs

def generateQues(mcqs, fname):
    with open(fname, "w") as file:
        file.write("Multiple Choice Questions\n\n")
        for i, mcq in enumerate(mcqs):
            file.write(f"Question {i + 1}: {mcq['question']}\n")
            for j, option in enumerate(mcq["options"]):
                file.write(f"{chr(65 + j)}. {option}\n")
            file.write("\n")
    
    return mcqs

# def generateAns(mcqs, fname):
#     with open(fname, "w") as file:
#         file.write("Answers\n\n")
#         for i, mcq in enumerate(mcqs):
#             file.write(f"Question {i + 1}: {mcq['correct_option']}\n")

def main():
    mcqs = loadJson('mcqs.json')
    
    if mcqs:
        allMcqs = []
        for i in range(4):
            newMcqs = mcqs[:]
            random.shuffle(newMcqs)
            mcqsfile = f"mcqs{i}.txt"
            allMcqs.append((mcqsfile, newMcqs))
            generateQues(newMcqs, mcqsfile)
        
        
        with open("answers.txt", "w") as ansFile:
            for mcqsfile, mcqs in allMcqs:
                ansFile.write(f"Answers for {mcqsfile}\n")
                for i, mcq in enumerate(mcqs):
                    ansFile.write(f"Question {i + 1}: {mcq['correct_option']}\n")
                ansFile.write("\n")
    else:
        print("dint receive mcqs")

if __name__ == "__main__":
    main()
