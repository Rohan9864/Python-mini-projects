class Quiz:
    def __init__(self,question, answer) -> None:
        self.question=question
        self.answer=answer
    
Questions=["What is the full form of oop?\n a. object oriented programming\n b. opinion oriented programming\n c.objective oriented programming\n d.oracle oriented programming\n",
           "How many types of method classes are there in python?\n a.1\n b.2\n c.3\n d.4\n",
           "What is the full form of ABS in python?\n a.Absolutr base class\n b.Alphabet based class\n c.Arithmetic based class\n d.Abstract based class"
           ]

# for i in Questions:
#     print(i)

Answers=[Quiz(Questions[0],'a'),
         Quiz(Questions[1],'c'),
         Quiz(Questions[2],'d')
         ]

def show(Answers):
    marks=0
    for i in Answers:
        ask=input(f"{i.question} \n Enter your Answer:")
        if ask==i.answer:
            marks+=1
        else:
            print(f"You answer is incorect. the correct answer is {i.answer}")


    print(f"Your total marks is {marks}\{len(Questions)}")

show(Answers)

