# Personal Blog Platform - "The Archive" 🚀

A high-performance, aesthetically driven personal blog platform . This project was developed as part of my portfolio at **MIT CSN**.

## 👤 About the Author
**Sanjay Wanekar** *B.Tech in Computer Science and Design | MIT CSN* Focusing on the intersection of robust backend logic (Python) and elegant, high-contrast user interfaces.

---

## ✨ Features
- **Dynamic Hero Slider:** Showcases featured blog posts with an automated cross-fade transition.
- **Full-Stack Backend:** Powered by Python and Flask with a relational SQLite database.
- **Admin Dashboard:** Secure interface to publish new entries, categorize content, and toggle "Featured" status.
- **Aesthetic UI:** A custom "Slate & Gold" dark theme designed for high readability and professional appeal.
- **Responsive Design:** Fully functional across desktop and mobile browsers.
- **Dedicated Archive:** A separate listing page to browse all historical posts.

 🛠️ Tech Stack
- **Backend:** Python 3.x, Flask
- **Database:** SQLAlchemy (ORM), SQLite
- **Frontend:** HTML5, CSS3 (Custom Grid & Flexbox), Vanilla JavaScript (Slider Logic)
- **Templating:** Jinja2

 🚀 Getting Started

# Prerequisites
Ensure you have Python installed. You will need to install the following dependencies:

pip install flask flask-sqlalchemy

Installation & Setup
Clone the repository:

git clone [https://github.com/YOUR_USERNAME/02_Personal_blog.git](https://github.com/YOUR_USERNAME/02_Personal_blog.git)
cd 02_Personal_blog
Initialize the Database:
The script is designed to automatically create the blog.db and populate it with seed data (regarding MIT CSN, Cricket, and Future Tech) on the first run.

Run the Application:

python app.py
Access the Site:
Open your browser and navigate to http://127.0.0.1:5000

📂 Project Structure
02_Personal_blog/
├── app.py              # Main Flask application & Backend logic
├── blog.db             # SQLite Database (Auto-generated)
├── static/
│   ├── style.css       # Custom aesthetic styling
│   └── sanjay.jpg.jpeg # Profile imagery
└── templates/          # Jinja2 HTML Templates
    ├── index.html      # Homepage with Slider, About, and Contact
    ├── all_blogs.html  # Full blog archive
    ├── post.html       # Individual post view
    ├── admin.html      # Content management portal
    └── about.html      # Detailed biography