from rdflib import Graph, Namespace, RDF, RDFS
import nltk

# nltk.download('punkt_tab')

class MACEChatbot:
    def __init__(self):
        self.graph = Graph()
        self.mace = Namespace("http://mace.org#")
        self._build_ontology()

    def _build_ontology(self):
        """Defines the ontology for MACE College."""
        g, mace = self.graph, self.mace

        # Define Classes
        g.add((mace.College, RDF.type, RDFS.Class))
        g.add((mace.Department, RDF.type, RDFS.Class))
        g.add((mace.Faculty, RDF.type, RDFS.Class))
        g.add((mace.StudentService, RDF.type, RDFS.Class))
        g.add((mace.Facility, RDF.type, RDFS.Class))

        # Define Relationships
        g.add((mace.hasDepartment, RDF.type, RDF.Property))
        g.add((mace.hasFaculty, RDF.type, RDF.Property))
        g.add((mace.providesService, RDF.type, RDF.Property))
        g.add((mace.hasFacility, RDF.type, RDF.Property))
        g.add((mace.teaches, RDF.type, RDF.Property))

        # Define College
        g.add((mace.MACE, RDF.type, mace.College))

        # Define Departments
        g.add((mace.CSE, RDF.type, mace.Department))
        g.add((mace.ECE, RDF.type, mace.Department))
        g.add((mace.ME, RDF.type, mace.Department))
        g.add((mace.CE, RDF.type, mace.Department))

        g.add((mace.MACE, mace.hasDepartment, mace.CSE))
        g.add((mace.MACE, mace.hasDepartment, mace.ECE))
        g.add((mace.MACE, mace.hasDepartment, mace.ME))
        g.add((mace.MACE, mace.hasDepartment, mace.CE))

        # Define Faculty Members
        g.add((mace.Prof_Rajan, RDF.type, mace.Faculty))
        g.add((mace.Prof_Asha, RDF.type, mace.Faculty))
        g.add((mace.Prof_John, RDF.type, mace.Faculty))

        g.add((mace.Prof_Rajan, mace.teaches, mace.CSE))
        g.add((mace.Prof_Asha, mace.teaches, mace.ECE))
        g.add((mace.Prof_John, mace.teaches, mace.ME))

        # Define Student Services
        g.add((mace.Library, RDF.type, mace.StudentService))
        g.add((mace.Hostel, RDF.type, mace.StudentService))
        g.add((mace.PlacementCell, RDF.type, mace.StudentService))

        g.add((mace.MACE, mace.providesService, mace.Library))
        g.add((mace.MACE, mace.providesService, mace.Hostel))
        g.add((mace.MACE, mace.providesService, mace.PlacementCell))

        # Define Facilities
        g.add((mace.Labs, RDF.type, mace.Facility))
        g.add((mace.SportsComplex, RDF.type, mace.Facility))
        g.add((mace.Auditorium, RDF.type, mace.Facility))

        g.add((mace.MACE, mace.hasFacility, mace.Labs))
        g.add((mace.MACE, mace.hasFacility, mace.SportsComplex))
        g.add((mace.MACE, mace.hasFacility, mace.Auditorium))

    def get_response(self, user_input):
        """Processes user queries and retrieves information from the ontology."""
        tokens = nltk.word_tokenize(user_input.lower())

        if "departments" in tokens:
            return self.list_departments()
        elif "faculty" in tokens or "professor" in user_input:
            return self.list_faculty()
        elif "services" in tokens or "student services" in user_input:
            return self.list_services()
        elif "facilities" in tokens:
            return self.list_facilities()
        elif "who teaches cse" in user_input:
            return "Professor Rajan teaches in the CSE department."
        elif "who teaches ece" in user_input:
            return "Professor Asha teaches in the ECE department."
        elif "who teaches me" in user_input:
            return "Professor John teaches in the ME department."
        elif "what services are available" in user_input:
            return "MACE offers Library, Hostel, and Placement Cell services."
        else:
            return "I'm not sure. Can you ask something related to MACE?"

    def list_departments(self):
        """Lists all departments in MACE."""
        query_result = self.graph.objects(self.mace.MACE, self.mace.hasDepartment)
        departments = [obj.split('#')[-1].replace('_', ' ') for obj in query_result]
        return f"MACE has the following departments: {', '.join(departments)}."

    def list_faculty(self):
        """Lists faculty members and their respective departments."""
        faculty = []
        for prof in self.graph.subjects(RDF.type, self.mace.Faculty):
            dept = next(self.graph.objects(prof, self.mace.teaches), None)
            faculty.append(f"{prof.split('#')[-1]} (Teaches: {dept.split('#')[-1]})")
        return "Faculty members: " + ", ".join(faculty)

    def list_services(self):
        """Lists student services available at MACE."""
        services = [obj.split('#')[-1] for obj in self.graph.objects(self.mace.MACE, self.mace.providesService)]
        return f"Student services available: {', '.join(services)}."

    def list_facilities(self):
        """Lists facilities available at MACE."""
        facilities = [obj.split('#')[-1] for obj in self.graph.objects(self.mace.MACE, self.mace.hasFacility)]
        return f"Facilities at MACE: {', '.join(facilities)}."

# Running the chatbot
chatbot = MACEChatbot()

while True:
    user_query = input("You: ")
    if user_query.lower() in ["exit", "quit"]:
        print("Chatbot: Goodbye!")
        break
    response = chatbot.get_response(user_query)
    print(f"Chatbot: {response}")
