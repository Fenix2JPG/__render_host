from akinator_python import Akinator

class ModuleAkinator():
    def __init__(self) -> None:
        


        self.akinator=Akinator(lang="es")
        self.akinator.start_game()

        # Sí : y 
        # No : n 
        # No lo sé : idk
        # probablemente : p 
        # probablemente no : pn
        self.list_y = ["y","yes","si"]
        self.list_n = ["n","no","not"]
        self.list_idk = ["idk","I don't know","no lo se"]
        self.list_p = ["p","probably","probablemente"]
        self.list_pn = ["pn","probably not","problamente no"]

        self.answer = None

    def get_question(self):
        return self.akinator.question

    def convert_answer(self,answer):
        if any(subcadena in answer for subcadena in self.list_y):
            return "y"
        if any(subcadena in answer for subcadena in self.list_n):
            return "n"
        if any(subcadena in answer for subcadena in self.list_idk):
            return "idk"
        if any(subcadena in answer for subcadena in self.list_p):
            return "p"
        if any(subcadena in answer for subcadena in self.list_pn):
            return "pn"


    def post_answer(self,answer):
        try:
            answer = self.convert_answer(answer)
            if answer=="b": #retroceder a la pregunta anterior
                self.akinator.go_back()
            else:
                self.akinator.post_answer(answer)
                if self.akinator.answer_id:
                    self.answer = self.akinator
                    #print(f"{self.akinator.name} / {self.akinator.description}")
                    """
                    answer=input("is it correct?：")
                    if answer=="n":
                        self.akinator.exclude()
                    elif answer=="y":
                        #break
                        pass
                    else:
                        pass
                        #break
                    """
            return self.akinator.question
        except Exception as e:
            print(e)
            #continue

    def get_answer_name(self):
        if self.answer == None:
            return None
        return self.answer.name
    def get_answer_description(self):
        return self.answer.description

if __name__ == "__main__":
    m = ModuleAkinator()
    print(m.get_question())
    while True:
        print(m.post_answer(input("ANSWER:")))
        print(m.get_answer_name())
                