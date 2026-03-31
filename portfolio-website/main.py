from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/profile")
def get_profile():
    return {
        "name": "Sanjay Wanekar",
        "bio": "B.Tech student and Full Stack Developer",
        "title": "Full Stack Developer",
        "email": "sanjay@email.com",
        "github": "github.com/sanjaywanekar",
        "linkedin": "linkedin.com/in/sanjaywanekar"
    }

@app.get("/api/stats")
def get_stats():
    return {"projects": 5, "skills": 10, "years_exp": 1}

@app.get("/api/skills")
def get_skills():
    return [
        {"name": "Python", "level": 85, "category": "Programming"},
        {"name": "Java", "level": 80, "category": "Programming"},
        {"name": "HTML", "level": 90, "category": "Frontend"},
        {"name": "CSS", "level": 85, "category": "Frontend"},
        {"name": "JavaScript", "level": 75, "category": "Frontend"},
        {"name": "FastAPI", "level": 70, "category": "Backend"},
        {"name": "MySQL", "level": 65, "category": "Database"},
    ]
@app.get("/api/projects")
def get_projects():
    return [
        {
            "title": "Job Portal",
            "description": "A job portal system using Java",
            "tech_stack": ["Java", "MySQL"],
            "github_url": "#",
            "live_url": "#",
            "featured": True
        }
    ]

@app.get("/api/experience")
def get_experience():
    return [
        {
            "role": "Student Developer",
            "company": "Self Learning",
            "duration": "2024 - Present",
            "description": "Learning full stack development"
        }
    ]

@app.post("/api/contact")
def contact(data: dict):
    return {"message": "Message sent successfully!"}