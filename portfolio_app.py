import streamlit as st
import base64
import os
from datetime import datetime
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Akshay Salvi - Senior Data Engineer",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for modern styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: 700;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    .section-header {
        font-size: 2rem;
        font-weight: 600;
        color: #2c3e50;
        border-bottom: 3px solid #3498db;
        padding-bottom: 0.5rem;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    .experience-card {
        background-color: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #3498db;
        margin-bottom: 1rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .skill-badge {
        display: inline-block;
        background-color: #3498db;
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        margin: 0.25rem;
        font-size: 0.9rem;
    }
    .project-card {
        background-color: #ffffff;
        padding: 1.5rem;
        border-radius: 10px;
        border: 1px solid #e0e0e0;
        margin-bottom: 1rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .contact-info {
        background-color: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        text-align: center;
    }
    .metric-card {
        background-color: #ffffff;
        padding: 1rem;
        border-radius: 10px;
        border: 1px solid #e0e0e0;
        text-align: center;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

# Function to load and display profile image
def load_profile_image():
    """Load and display profile image with fallback to placeholder"""
    try:
        # Try to load actual profile image
        if os.path.exists("profile_photo.jpg"):
            st.image("profile_photo.jpg", width=200, use_column_width=False)
        elif os.path.exists("profile_placeholder.jpg"):
            st.image("profile_placeholder.jpg", width=200, use_column_width=False)
        else:
            # Fallback to CSS placeholder
            st.markdown("""
            <div style="text-align: center; margin-bottom: 2rem;">
                <div style="width: 200px; height: 200px; border-radius: 50%; background-color: #3498db; margin: 0 auto; display: flex; align-items: center; justify-content: center; color: white; font-size: 4rem;">
                    AS
                </div>
            </div>
            """, unsafe_allow_html=True)
    except Exception as e:
        # Fallback to CSS placeholder if image loading fails
        st.markdown("""
        <div style="text-align: center; margin-bottom: 2rem;">
            <div style="width: 200px; height: 200px; border-radius: 50%; background-color: #3498db; margin: 0 auto; display: flex; align-items: center; justify-content: center; color: white; font-size: 4rem;">
                AS
            </div>
        </div>
        """, unsafe_allow_html=True)

# Main header
st.markdown('<h1 class="main-header">Akshay Salvi</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Senior Data Engineer | Data Pipeline Architect | Cloud Solutions Expert</p>', unsafe_allow_html=True)

# Load profile image
load_profile_image()

# Navigation
st.markdown("---")
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    if st.button("About", use_container_width=True):
        st.session_state.page = "about"
with col2:
    if st.button("Experience", use_container_width=True):
        st.session_state.page = "experience"
with col3:
    if st.button("Skills", use_container_width=True):
        st.session_state.page = "skills"
with col4:
    if st.button("Projects", use_container_width=True):
        st.session_state.page = "projects"
with col5:
    if st.button("Contact", use_container_width=True):
        st.session_state.page = "contact"

# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = "about"

st.markdown("---")

# About Section
if st.session_state.page == "about":
    st.markdown('<h2 class="section-header">About Me</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        <div style="font-size: 1.1rem; line-height: 1.6;">
        <p>I am a passionate Senior Data Engineer with over 6+ years of experience in designing, building, and maintaining 
        scalable data infrastructure and pipelines. I specialize in transforming raw data into actionable insights that 
        drive business decisions.</p>
        
        <p>My expertise spans across cloud platforms (AWS, Azure, GCP), big data technologies (Spark, Hadoop, Kafka), 
        and modern data stack tools. I have a proven track record of leading data engineering teams and delivering 
        high-impact projects that improve data quality, reduce processing time, and enable real-time analytics.</p>
        
        <p>I am passionate about staying current with emerging technologies and best practices in the data engineering 
        space, and I enjoy mentoring junior engineers and contributing to open-source projects.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        # Key metrics
        st.markdown('<h3 style="color: #2c3e50;">Key Metrics</h3>', unsafe_allow_html=True)
        
        col2_1, col2_2 = st.columns(2)
        with col2_1:
            st.markdown("""
            <div class="metric-card">
                <h3 style="color: #3498db; margin: 0;">6+</h3>
                <p style="margin: 0;">Years Experience</p>
            </div>
            """, unsafe_allow_html=True)
            
        with col2_2:
            st.markdown("""
            <div class="metric-card">
                <h3 style="color: #3498db; margin: 0;">50+</h3>
                <p style="margin: 0;">Projects Delivered</p>
            </div>
            """, unsafe_allow_html=True)
        
        col2_3, col2_4 = st.columns(2)
        with col2_3:
            st.markdown("""
            <div class="metric-card">
                <h3 style="color: #3498db; margin: 0;">15+</h3>
                <p style="margin: 0;">Technologies</p>
            </div>
            """, unsafe_allow_html=True)
            
        with col2_4:
            st.markdown("""
            <div class="metric-card">
                <h3 style="color: #3498db; margin: 0;">5+</h3>
                <p style="margin: 0;">Cloud Platforms</p>
            </div>
            """, unsafe_allow_html=True)

# Experience Section
elif st.session_state.page == "experience":
    st.markdown('<h2 class="section-header">Professional Experience</h2>', unsafe_allow_html=True)
    
    # Experience timeline
    experiences = [
        {
            "title": "Senior Data Engineer",
            "company": "TechCorp Solutions",
            "duration": "2022 - Present",
            "description": [
                "Led a team of 5 data engineers in designing and implementing scalable data pipelines processing 10TB+ daily",
                "Architected cloud-native data solutions on AWS, reducing infrastructure costs by 40%",
                "Implemented real-time streaming pipelines using Apache Kafka and Apache Spark",
                "Collaborated with data scientists to deploy ML models in production environments",
                "Mentored junior engineers and established best practices for code review and documentation"
            ]
        },
        {
            "title": "Data Engineer",
            "company": "DataFlow Inc.",
            "duration": "2020 - 2022",
            "description": [
                "Built and maintained ETL pipelines processing 5TB+ of data daily using Python and Apache Airflow",
                "Optimized SQL queries and data warehouse performance, improving query speed by 60%",
                "Implemented data quality monitoring and alerting systems",
                "Worked with cross-functional teams to understand business requirements and deliver data solutions",
                "Contributed to the migration from on-premises to cloud infrastructure"
            ]
        },
        {
            "title": "Junior Data Engineer",
            "company": "Analytics Pro",
            "duration": "2018 - 2020",
            "description": [
                "Developed data pipelines using Python, SQL, and Apache Spark",
                "Created automated data validation and quality checks",
                "Assisted in building data warehouses and data lakes",
                "Participated in agile development processes and code reviews",
                "Gained experience with various database technologies (PostgreSQL, MongoDB, Redis)"
            ]
        }
    ]
    
    for exp in experiences:
        st.markdown(f"""
        <div class="experience-card">
            <h3 style="color: #2c3e50; margin-top: 0;">{exp['title']}</h3>
            <h4 style="color: #3498db; margin: 0.5rem 0;">{exp['company']}</h4>
            <p style="color: #666; font-style: italic; margin: 0.5rem 0;">{exp['duration']}</p>
            <ul style="margin: 1rem 0;">
        """, unsafe_allow_html=True)
        
        for desc in exp['description']:
            st.markdown(f"<li>{desc}</li>", unsafe_allow_html=True)
        
        st.markdown("</ul></div>", unsafe_allow_html=True)

# Skills Section
elif st.session_state.page == "skills":
    st.markdown('<h2 class="section-header">Technical Skills</h2>', unsafe_allow_html=True)
    
    # Skills categories
    skills_data = {
        "Programming Languages": ["Python", "SQL", "Scala", "Java", "R", "Bash"],
        "Big Data Technologies": ["Apache Spark", "Apache Kafka", "Apache Airflow", "Hadoop", "Hive", "Presto"],
        "Cloud Platforms": ["AWS", "Azure", "Google Cloud Platform", "Databricks", "Snowflake"],
        "Databases": ["PostgreSQL", "MySQL", "MongoDB", "Redis", "Elasticsearch", "DynamoDB"],
        "Data Tools": ["dbt", "Great Expectations", "Apache Superset", "Tableau", "Power BI"],
        "DevOps & CI/CD": ["Docker", "Kubernetes", "Jenkins", "Git", "Terraform", "Ansible"]
    }
    
    # Create skill visualization
    col1, col2 = st.columns([2, 1])
    
    with col1:
        for category, skills in skills_data.items():
            st.markdown(f"<h4 style='color: #2c3e50; margin-top: 1.5rem;'>{category}</h4>", unsafe_allow_html=True)
            skill_html = ""
            for skill in skills:
                skill_html += f'<span class="skill-badge">{skill}</span>'
            st.markdown(skill_html, unsafe_allow_html=True)
    
    with col2:
        # Skills proficiency chart
        st.markdown('<h4 style="color: #2c3e50;">Skills Proficiency</h4>', unsafe_allow_html=True)
        
        proficiency_data = {
            'Skill': ['Python', 'SQL', 'Apache Spark', 'AWS', 'Apache Kafka', 'Docker', 'Apache Airflow', 'PostgreSQL'],
            'Proficiency': [95, 90, 85, 80, 75, 70, 85, 80]
        }
        
        df = pd.DataFrame(proficiency_data)
        fig = px.bar(df, x='Proficiency', y='Skill', orientation='h', 
                    color='Proficiency', color_continuous_scale='Blues')
        fig.update_layout(height=400, showlegend=False, 
                         plot_bgcolor='rgba(0,0,0,0)', 
                         paper_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig, use_container_width=True)

# Projects Section
elif st.session_state.page == "projects":
    st.markdown('<h2 class="section-header">Featured Projects</h2>', unsafe_allow_html=True)
    
    projects = [
        {
            "title": "Real-Time Analytics Platform",
            "description": "Built a comprehensive real-time analytics platform processing 1M+ events per second using Apache Kafka, Apache Spark Streaming, and Apache Druid.",
            "technologies": ["Apache Kafka", "Apache Spark", "Apache Druid", "Python", "AWS", "Docker"],
            "impact": "Reduced data processing latency by 80% and enabled real-time business insights"
        },
        {
            "title": "Data Lake Migration & Modernization",
            "description": "Led the migration of legacy data warehouse to modern cloud data lake architecture on AWS, implementing data governance and quality frameworks.",
            "technologies": ["AWS S3", "Apache Spark", "dbt", "Great Expectations", "Apache Airflow", "Terraform"],
            "impact": "Reduced infrastructure costs by 50% and improved data accessibility across the organization"
        },
        {
            "title": "ML Pipeline Automation",
            "description": "Designed and implemented automated ML pipeline for model training, validation, and deployment using MLOps best practices.",
            "technologies": ["Python", "Apache Airflow", "Docker", "Kubernetes", "MLflow", "AWS SageMaker"],
            "impact": "Reduced model deployment time from weeks to hours and improved model accuracy by 15%"
        },
        {
            "title": "Data Quality Monitoring System",
            "description": "Developed a comprehensive data quality monitoring system with automated alerting and data lineage tracking.",
            "technologies": ["Python", "Great Expectations", "Apache Airflow", "PostgreSQL", "Grafana"],
            "impact": "Improved data quality by 90% and reduced data-related incidents by 70%"
        }
    ]
    
    for i, project in enumerate(projects):
        st.markdown(f"""
        <div class="project-card">
            <h3 style="color: #2c3e50; margin-top: 0;">{project['title']}</h3>
            <p style="font-size: 1.1rem; line-height: 1.6; margin: 1rem 0;">{project['description']}</p>
            <h4 style="color: #3498db; margin: 1rem 0 0.5rem 0;">Technologies Used:</h4>
        """, unsafe_allow_html=True)
        
        tech_html = ""
        for tech in project['technologies']:
            tech_html += f'<span class="skill-badge">{tech}</span>'
        st.markdown(tech_html, unsafe_allow_html=True)
        
        st.markdown(f"""
        <h4 style="color: #27ae60; margin: 1rem 0 0.5rem 0;">Impact:</h4>
        <p style="font-style: italic; color: #666;">{project['impact']}</p>
        </div>
        """, unsafe_allow_html=True)

# Contact Section
elif st.session_state.page == "contact":
    st.markdown('<h2 class="section-header">Get In Touch</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        <div class="contact-info">
            <h3 style="color: #2c3e50;">Let's Connect!</h3>
            <p style="font-size: 1.1rem; margin: 1rem 0;">
                I'm always interested in discussing new opportunities, 
                data engineering challenges, and innovative projects.
            </p>
            
            <div style="margin: 2rem 0;">
                <h4 style="color: #3498db;">📧 Email</h4>
                <p>akshay.salvi@email.com</p>
                
                <h4 style="color: #3498db;">💼 LinkedIn</h4>
                <p><a href="https://www.linkedin.com/in/akshay-salvi-2869b2125/" target="_blank">linkedin.com/in/akshay-salvi-2869b2125/</a></p>
                
                <h4 style="color: #3498db;">🐙 GitHub</h4>
                <p><a href="https://github.com/akshaysalvi" target="_blank">github.com/akshaysalvi</a></p>
                
                <h4 style="color: #3498db;">📍 Location</h4>
                <p>Mumbai, India</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        # Contact form
        st.markdown('<h3 style="color: #2c3e50;">Send a Message</h3>', unsafe_allow_html=True)
        
        with st.form("contact_form"):
            name = st.text_input("Name")
            email = st.text_input("Email")
            subject = st.text_input("Subject")
            message = st.text_area("Message", height=150)
            submit_button = st.form_submit_button("Send Message")
            
            if submit_button:
                if name and email and subject and message:
                    st.success("Thank you for your message! I'll get back to you soon.")
                else:
                    st.error("Please fill in all fields.")
    
    # Additional info
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666; margin-top: 2rem;">
        <p>Available for freelance projects and full-time opportunities</p>
        <p>Response time: Usually within 24 hours</p>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; margin-top: 2rem;">
    <p>&copy; 2024 Akshay Salvi. Built with ❤️ using Streamlit</p>
</div>
""", unsafe_allow_html=True)
