from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

opportunities = [
    {
        "university": "Northwestern University",
        "department": "Cross-disciplinary",
        "title": "Undergraduate Research Advising & Funding Pathway",
        "organization": "Office of Undergraduate Research-style pathway",
        "description": "A student can develop a research interest, find a faculty mentor, apply for funding, and build an independent research project.",
        "skills": ["Faculty outreach", "Proposal writing", "Research planning", "Academic writing"],
        "interests": ["independent research", "faculty mentorship", "grant funding", "interdisciplinary research"],
        "commitment": "Varies by project",
        "type": "Advising, funding, and independent research support",
        "source": "Modeled after Northwestern's public undergraduate research resources"
    },
    {
        "university": "University of Southern California",
        "department": "School-based research",
        "title": "Student Research Opportunity",
        "organization": "USC Student Research-style pathway",
        "description": "Students can explore undergraduate research opportunities through schools, institutes, and faculty-led programs across campus.",
        "skills": ["Research communication", "Lab support", "Data analysis", "Faculty outreach"],
        "interests": ["engineering", "public policy", "communication", "science", "humanities"],
        "commitment": "Varies by school or program",
        "type": "School-based research and summer research opportunities",
        "source": "Modeled after USC's public student research resources"
    },
    {
        "university": "UC Berkeley",
        "department": "Faculty research projects",
        "title": "Undergraduate Research Apprentice",
        "organization": "Berkeley URAP-style opportunity",
        "description": "Students work with faculty members and research staff on research projects while developing deeper knowledge in a specific area.",
        "skills": ["Project support", "Reading academic papers", "Data collection", "Research assistance"],
        "interests": ["faculty research", "apprenticeship", "graduate school preparation", "academic research"],
        "commitment": "Semester or academic-term based",
        "type": "Faculty project apprenticeship",
        "source": "Modeled after UC Berkeley's public URAP structure"
    },
    {
        "university": "University of Michigan",
        "department": "Research mentorship",
        "title": "Research Opportunity Program Participant",
        "organization": "Michigan UROP-style pathway",
        "description": "Students connect with mentors, gain hands-on research experience, and explore research across diverse fields.",
        "skills": ["Mentor communication", "Research basics", "Team collaboration", "Project execution"],
        "interests": ["arts", "sciences", "social science", "engineering", "health"],
        "commitment": "Academic-year style research involvement",
        "type": "Mentored undergraduate research",
        "source": "Modeled after University of Michigan's public UROP structure"
    },
    {
        "university": "Any University",
        "department": "Campus Ambassador Network",
        "title": "Campus Research Scout",
        "organization": "ResearchMatch campus network",
        "description": "A student ambassador helps identify professors, labs, and research openings at their school so opportunities become easier to discover.",
        "skills": ["Networking", "Cold outreach", "Campus knowledge", "Organization"],
        "interests": ["startup building", "research access", "student leadership", "campus partnerships"],
        "commitment": "Flexible",
        "type": "ResearchMatch network role",
        "source": "Internal ResearchMatch growth model"
    }
]

students = [
    {
        "name": "Lucas Coriaty",
        "school": "Northwestern University",
        "major": "Economics",
        "year": "Undergraduate",
        "interests": "finance, economics, behavioral research, data analysis",
        "skills": "Excel, Python basics, finance research, writing, athlete discipline"
    }
]

waitlist = []


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/opportunities")
def show_opportunities():
    return render_template("opportunities.html", opportunities=opportunities)


@app.route("/students")
def show_students():
    return render_template("students.html", students=students)


@app.route("/waitlist", methods=["GET", "POST"])
def waitlist_page():
    if request.method == "POST":
        person = {
            "name": request.form.get("name"),
            "email": request.form.get("email"),
            "school": request.form.get("school"),
            "role": request.form.get("role"),
            "research_area": request.form.get("research_area"),
            "interests": request.form.get("interests"),
            "how_found": request.form.get("how_found")
        }

        waitlist.append(person)

        return render_template("waitlist_success.html", person=person)

    return render_template("waitlist.html")


@app.route("/signup", methods=["GET", "POST"])
def old_signup_redirect():
    return redirect(url_for("waitlist_page"))


if __name__ == "__main__":
    app.run(debug=True, port=8000)
