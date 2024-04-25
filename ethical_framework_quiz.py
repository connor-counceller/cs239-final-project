class Quiz:
    def __init__(self):
        # Titles of frameworks
        self.ethical_frameworks = [["The Utilitarian Approach", "Some ethicists emphasize that the ethical action is the one that provides the most good or does the least harm, or, to put it another way, produces the greatest balance of good over harm. The ethical corporate action, then, is the one that produces the greatest good and does the least harm for all who are affected -- customers, employees, shareholders, the community, and the environment. Ethical warfare balances the good achieved in ending terrorism with the harm done to all parties through death, injuries, and destruction. The utilitarian approach deals with consequences; it tries both to increase the good done and to reduce the harm done."],
                                   ["The Rights Approach", "Other philosophers and ethicists suggest that the ethical action is the one that best protects and respects the  moral rights of those affected. This approach starts from the belief that humans have a dignity based on their  human nature per se or on their ability to choose freely what they do with their lives. On the basis of such dignity, they have a right to be treated as ends and not merely as means to other ends. The list of moral rights, including the rights to make one's own choices about what kind of life to lead, to be told the truth, not to be  injured, to a degree of privacy, and so on, is widely debated; some now argue that nonhumans have rights too. Also, it is often said that rights imply duties -- in particular, the duty to respect others' rights."],
                                   ["The Fairness or Justice Approach", "Aristotle and other Greek philosophers have contributed the idea that all equals should be treated equally. Today we use this idea to say that ethical actions treat all human beings equally -- or if unequally, then fairly, based on some standard that is defensible. We pay people more based on their harder work or the greater  amount that they contribute to an organization, and say that is fair. But there is a debate over CEO salaries that are hundreds of times larger than the pay of others; many ask whether the huge disparity is based on a  defensible standard or whether it is the result of an imbalance of power and hence is unfair."],
                                   ["The Common Good Approach", "The Greek philosophers have also contributed the notion that life in community is a good in itself and our actions should contribute to that life. This approach suggests that the interlocking relationships of society are the basis of ethical reasoning and that respect and compassion for all others -- especially the vulnerable -- are  requirements of such reasoning. This approach also calls attention to the common conditions that are  important to the welfare of everyone. This may be a system of laws, effective police and fire departments, health care, a public educational system, or even public recreation areas."],
                                   ["The Virtue Approach", """A very ancient approach to ethics is that ethical actions ought to be consistent with certain ideal virtues that provide for the full development of our humanity. These virtues are dispositions and habits that enable us to act according to the highest potential of our character and on behalf of values like truth and beauty. Honesty, courage, compassion, generosity, tolerance, love, fidelity, integrity, fairness, self-control, and prudence are all examples of virtues. Virtue ethics asks of any action, "What kind of person will I become if I do this?" or "Is this action consistent with my acting at my best?" """]]
        
        # Number of questions answered in favor of each framework
        self.framework_counts = [0, 0, 0, 0, 0]

        # A list of questions, their answers, and an index value for which framework count should be incremented when that answer is selected.
        self.questions = [   
            ["You are the CEO of a tech startup that has developed a new app designed to help people manage and reduce their carbon footprint. The app has gained popularity quickly, and you've received a buyout offer from a major tech corporation. They plan to integrate your app into their existing platform but intend to use the data collected for targeted advertising, which was not the original purpose of your app. You are aware that users trust your app with their personal data and may not be comfortable with this change. What would you do?",
             [["Accept the buyout offer from the major tech corporation, allowing your startup to grow and reach a larger audience, even if it means compromising the original purpose of the app and user data privacy.", 0],
              ["Decline the buyout offer and continue to operate independently, maintaining the original purpose of the app and respecting user data privacy.", 1],
              ["Negotiate with the major tech corporation to maintain the original purpose of the app and ensure strict data privacy protections as part of the buyout agreement.", 2],
              ["Accept the buyout offer and pledge to use a portion of the proceeds to support environmental causes and data privacy initiatives.", 3],
              ["Modify the app to focus on another aspect of sustainability that does not involve collecting personal user data and then sell it to the major tech corporation.", 4]]],
            
            ]
        self.selected_framework_list = []
    
    def take_quiz(self):
        self.display_intro()

        for q in self.questions:
            self.ask_question(q)
        
        self.display_results()

    def display_intro(self):
        print('------------------------------\n')
        print('Welcome to this ethical frameworks quiz! You will be presented with scenarios/questions and possible answers to these questions. You will respond to each question with a single letter ("A", "B", etc.) corresponding to the answer you most agree with. Once you have answered all questions, you will be shown which of the five major ethical frameworks your choices most relate to. Good luck!\n')

    def ask_question(self, q):
        self.display_question_and_choices(q)
        selection = self.convert_selection(input('\nAnswer: '))
        self.framework_counts[q[1][selection][1]] += 1
        print()

    def display_results(self):
        max_count = max(self.framework_counts)

        for i in range(len(self.framework_counts)):
            if self.framework_counts[i] == max_count:
                self.selected_framework_list.append(self.ethical_frameworks[i])

        print('------------------------------\n')

        if (len(self.selected_framework_list) == 1):
            print(f"The framework that most closely follows your choices is '{self.selected_framework_list[0][0]}' which states the following: ")
            print(f"'{self.selected_framework_list[0][1]}'")

        elif (len(self.selected_framework_list) > 1):
            print("It looks like there was a tie for which framework most closely follows your choices! So I will least each framework and their descriptions below.\n")
            for fw in self.selected_framework_list:
                print(f"Framework: '{fw[0]}'")
                print(f"Description: '{fw[1]}'\n")

    def display_question_and_choices(self, q):
        q_index = self.questions.index(q) + 1
        print('------------------------------\n')
        print(f'{q_index}. {q[0]}\n')
        letters = ['A', 'B', 'C', 'D', 'E']

        for c in q[1]:
            c_index = q[1].index(c)
            print(f'\t{letters[c_index]}. {c[0]}')
    
    def convert_selection(self, user_input):
        user_input = user_input.upper()
        choices = ['A', 'B', 'C', 'D', 'E']
        if (user_input in choices):
            index = choices.index(user_input)
        else:
            print("ERROR: Invalid user input. Please enter 'A', 'B', 'C', 'D', or 'E'.")
            exit()
        
        return index

###################### Execution ######################

quiz = Quiz()

quiz.take_quiz()