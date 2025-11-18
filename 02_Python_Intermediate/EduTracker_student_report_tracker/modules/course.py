class course:

    def __init__(self, course_name, duration, topics = []):
        self.__course_name = course_name
        self.__duration = duration
        self.__topics = topics
        print(f"Course Created \nCourse name: {self.__course_name}\nCourse Duration: {self.__duration}")

    def add_topic(self,a_course):
        self.__topics.append(a_course)
    
    def remove_topic(self, r_course):
        self.__topics.remove(r_course)

    def disp(self):
        print(f"Topics {self.__topics}")

    def __len__(self):
        return f"No of Topics in the course {len(self.__topics)}"

    def __iter__(self):
        return iter(self.__topics)