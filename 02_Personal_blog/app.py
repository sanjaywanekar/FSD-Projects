from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    subtitle = db.Column(db.String(300))
    content = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(50), default="General")
    # New column to identify posts for the Tim Ferriss slider
    is_featured = db.Column(db.Boolean, default=False)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)

def seed_data():
    if Post.query.count() == 0:
        p1 = Post(title="Design & Code converge at MIT CSN", subtitle="B.Tech journey in Computer Science.", content="Studying CS&D has taught me that code is the architecture of the user experience...", category="Education", is_featured=True)
        
        p2 = Post(title="The Technical Precision of Kohli's Cover Drive", subtitle="Analyzing technical mastery from a Design perspective.", content="A perfectly timed cover drive isn't just talent; it's physics. The kinetic chain starts from the precise footwork...", category="Sports", is_featured=True)
        
        p3 = Post(title="Flutter ERP for Final Year Projects", subtitle="Using Flutter to build full-scale business applications.", content="For my project, I am designing an Inventory Management system (ERP) that handles complex data flows with minimal latency...", category="Technology", is_featured=True)
        
        p4 = Post(title="Badminton Smash: Technical Breakdown", subtitle="Kinetic energy transfer in elite sports.", content="Whether bug-free deployment or a badminton smash, technical precision is my goal...", category="Sports", is_featured=False)
        
        p5 = Post(title="Future Tech: ERP and AI", subtitle="Will ERP systems become truly intelligent?", content="My ERP project aims to optimize supply chains. Next year, it will need predictive AI to analyze reorder points automatically...", category="Future", is_featured=False)
        
        db.session.add_all([p1, p2, p3, p4, p5])
        db.session.commit()

@app.route('/')
def index():
    # Fetch posts specifically for the Tim Ferriss-style slider
    featured_posts = Post.query.filter_by(is_featured=True).all()
    
    # Fetch normal recent posts for the rest of the list
    recent_posts = Post.query.filter_by(is_featured=False).order_by(Post.date_posted.desc()).limit(5).all()
    
    return render_template('index.html', featured=featured_posts, posts=recent_posts)

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        is_feat = True if request.form.get('is_featured') else False
        new_post = Post(
            title=request.form['title'], subtitle=request.form['subtitle'], 
            content=request.form['content'], category=request.form.get('category', 'General'),
            is_featured=is_feat
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('admin.html')

@app.route('/post/<int:post_id>')
def view_post(post_id):
    # This looks for the blog post in the database using its ID
    post = Post.query.get_or_404(post_id)
    # This renders the detailed page for that specific blog
    return render_template('post.html', post=post)

@app.route('/blogs')
def all_blogs():
    # Fetching all posts to show them in a clean list
    posts = Post.query.order_by(Post.date_posted.desc()).all()
    return render_template('all_blogs.html', posts=posts)
# (Other basic routes like /post remain the same)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        seed_data()
    app.run(debug=True)