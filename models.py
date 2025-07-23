# models.py
from pydantic import BaseModel, Field, field_validator
from enum import Enum
from typing import Optional, List

# Define additional enumerations for new fields
class ConsultationType(str, Enum):
    REGULAR = "Regular"
    POP_UP = "Pop-up"

class MaturityLevel(str, Enum):
    LOW = "Low"
    MODERATE = "Moderate"
    HIGH = "High"

class CompanyType(str, Enum):
    STARTUP = "Startup"
    ESTABLISHED = "Established company"


# Define the enumerations for domains and AI fields
class Domain(str, Enum):
    HEALTHCARE = "Healthcare & wellbeing"
    AUTOMOTIVE = "Automotive"
    CONSTRUCTION = "Construction"
    MANUFACTURING = "Manufacturing"
    CULTURAL = "Cultural & creative industries"
    DEFENSE = "Defense"
    EDUCATION = "Education & training"
    ENVIRONMENT = "Environment & sustainability"
    FINANCE = "Finance"
    LEGAL = "Legal"
    SECURITY = "Security"
    SMART_CITIES = "Smart cities"
    TRANSPORT = "Transport, mobility, logistics"
    TRAVEL = "Travel & tourism"
    BUSINESS = "Business development/business services"
    REAL_ESTATE = "Real estate & property"
    ARTS = "Arts & entertainment"
    OTHER = "Other"



# Define individual Pydantic models
class CompanyDomain(BaseModel):
    """Model for company domain classification"""
    domain: Domain = Field(
        ..., 
        description="""The primary industry domain the company belongs to. Choose ONE from:
        - Healthcare & wellbeing: Medical, healthcare, wellness, fitness, health services, diagnostics, devices, mental health
        - Automotive: Car manufacturers, parts suppliers, automotive software, autonomous vehicles
        - Construction: Building construction, architecture, civil engineering, construction materials, planning
        - Manufacturing: Physical goods production, industrial production, factories, automation
        - Cultural & creative industries: Design, publishing, media production, art, cultural heritage, creative content
        - Defense: Military, defense technologies, security forces, governmental defense
        - Education & training: Educational services, training, e-learning platforms, educational content, academic tools
        - Environment & sustainability: Environmental protection, sustainability, renewable energy, conservation, climate monitoring
        - Finance: Banking, insurance, fintech, investment, accounting, financial services
        - Legal: Legal services, legal tech, compliance tools, regulatory assistance
        - Security: Cybersecurity, physical security, surveillance, identity verification, threat detection
        - Smart cities: Urban infrastructure technologies, city planning, urban monitoring, smart city initiatives
        - Transport, mobility, logistics: Transportation services, logistics, supply chain, shipping, freight, mobility
        - Travel & tourism: Travel industry, tourism, hospitality, booking services, travel planning
        - Business development/business services: B2B services, consulting, business optimization, productivity tools
        - Real estate & property: Property management, real estate services, property development, facility management
        - Arts & entertainment: Entertainment, media, gaming, arts, leisure sectors
        - Other: Companies that don't clearly fit into any of the above categories"""
    )

class AIField(str, Enum):
    GENERATIVE_AI = "Generative AI"
    MACHINE_LEARNING = "Machine learning"
    PREDICTIVE_ANALYTICS = "Predictive analytics"
    COMPUTER_VISION = "Computer vision & image processing"
    RULE_BASED = "Rule-based systems"
    OTHER = "Other"

class CompanyAIField(BaseModel):
    """Model for AI field classification"""
    ai_field: AIField = Field(
        ..., 
        description="""The primary AI field the company is using or planning to use. Choose ONE from:
        - Generative AI: Content generation (text, images, audio, code), large language models, retrieval augment generation, chatbots, text-to-speech, speech-to-text, model context protocol, AI agents
        - Machine learning: Traditional ML algorithms, neural networks, deep learning, clustering, classification, pattern recognition
        - Predictive analytics: Statistical algorithms for forecasting, trend analysis, predictive modeling based on historical data
        - Computer vision & image processing: Image processing, image recognition, object detection, obejct tracking, facial recognition, image segmentation, image description or labeling, video analysis, eye-tracking
        - Rule-based systems: Predefined rules, logic, knowledge bases, expert systems, decision trees, rule-based reasoning
        - Other: AI field that doesn't clearly fit into any of the above categories"""
    )

class Services(str, Enum):
    TECHNICAL_ADVICE = "Technical advice"
    PoC_DEV = "PoC development"
    DATA_ANALYSIS = "Data analysis"
    AI_ROADMAP = "AI roadmap design"
    FUNDING_SUPPORT = "Funding application support"
    THESIS_SUPPORT = "Student thesis project"
    COLLABORATION = "Networking support"
    RnD_SUPPORT = "R&D collaboration"
    DATA_COLLECTION = "Data collection"
    USE_CASE_DESIGN = "Use case design"
    TECHNICAL_REVIEW = "Technical review"

class ServicesDescriptions(BaseModel):
    """Model for selecting FAIR services - allows multiple services"""
    services: List[Services] = Field(
        ...,
        description = """The services sought by the company. Choose one or more relevant services from:
        - Technical advice: Services related to algorithmic design, model selection, training, testing, deployment, or other technical aspects
        - PoC development: Support in developing proof of concept
        - Data analysis: Support in analyzing data and getting insights from it. 
        - AI roadmap design: Support in designing a concrete AI strategy or roadmap
        - Funding application support: Support in applying for funding 
        - Student thesis project: Developing a prototype or proof of concept through a student thesis project (master thesis).
        - Networking support: Connecting with other companies for collaboration
        - R&D collaboration: Partenering in R&D and co-research or co-development projects
        - Data collection: Support in collecting data for training AI models
        - Use case design: Support in understanding AI integration and use case design. Required by companies which do not know which use-case is suitable for their business needs. 
        - Technical review: Technical review of the existing AI solution or product
        - Other: Services required by the company that don't clearly fit into any of the above categories

        
        Return as a list of services, for example: ["Technical advice", "PoC development"] or ["AI roadmap design"]
        """
    )
    
    @field_validator('services', mode='before')
    @classmethod
    def validate_services(cls, v):
        """Convert string or single service to list"""
        if isinstance(v, str):
            # If it's a string, convert to list
            return [v]
        elif isinstance(v, Services):
            # If it's a single Services enum, convert to list
            return [v]
        elif isinstance(v, list):
            # If it's already a list, return as is
            return v
        else:
            # Fallback
            return [v] if v else []

class TargetGroup(str, Enum):
    """
    Comprehensive yet streamlined target groups for AI usage.
    Merged from multiple sources and deduplicated for practical use.
    """
    
    # Healthcare & Medical
    HEALTHCARE_PROFESSIONALS = "Healthcare professionals"
    PATIENTS_CONSUMERS = "Patients and healthcare consumers"
    MEDICAL_RESEARCHERS = "Medical researchers"
    PHARMACEUTICAL = "Pharmaceutical companies"
    DENTAL_PROFESSIONALS = "Dental professionals"
    MENTAL_HEALTH_PROVIDERS = "Psychologists, psychiatrists, and psychotherapists"
    ELDERLY_CARE_PROVIDERS = "Elderly care homes and assisted living providers"
    SPECIALIZED_MEDICAL = "Functional medicine clinics and specialized healthcare providers"
    
    # Business & Enterprise
    SMALL_MEDIUM_BUSINESSES = "Small and medium businesses"
    LARGE_ENTERPRISES = "Large enterprise companies and corporations"
    STARTUPS_ENTREPRENEURS = "Startups and entrepreneurs"
    BUSINESS_PROFESSIONALS = "Business analysts, consultants, and advisors"
    
    # Technology & Development
    SOFTWARE_DEVELOPERS = "Software developers and tech companies"
    AI_ML_RESEARCHERS = "AI/ML researchers and data scientists"
    IT_PROFESSIONALS = "IT professionals and system administrators"
    
    # Education & Training
    STUDENTS_PRIMARY = "School students"
    STUDENTS_HIGHER = "College/University students"
    TEACHERS_EDUCATORS = "Teachers & educational professionals"
    EDUCATIONAL_INSTITUTIONS = "Educational institutions & schools"
    ONLINE_LEARNING = "Online learning platforms"
    TRAINING_ORGANIZATIONS = "Organizations providing employee training and workforce education"
    JOB_SEEKERS = "Job seekers"
    
    # Government & Public Sector
    GOVERNMENT_AGENCIES = "Government agencies and public sector organizations"
    MUNICIPALITIES = "Municipalities and city governments"
    DEFENSE_FORCES = "Defense forces and military organizations"
    PUBLIC_SAFETY = "Law enforcement & security"
    EMERGENCY = "Emergency services"
    
    # Finance & Legal
    FINANCIAL_INSTITUTIONS = "Banks & financial institutions"
    INSURANCE = "Insurance companies"
    FINTECH_COMPANIES = "FinTech companies & payment processors"
    LEGAL_PROFESSIONALS = "Law firms & legal professionals"
    
    # Construction & Real Estate
    CONSTRUCTION_COMPANIES = "Construction companies, contractors, and related sectors"
    ARCHITECTS_ENGINEERS = "Architects, engineers, and building designers"
    REAL_ESTATE_PROFESSIONALS = "Real estate agents, property managers, and investors"
    PROPERTY_OWNERS = "Property owners, landlords, and facility managers"
    
    # Manufacturing & Industry
    MANUFACTURING_COMPANIES = "Manufacturing companies and industrial producers"
    AUTOMOTIVE_COMPANIES = "Automotive manufacturers and car dealerships"
    MACHINE_PARTS_VENDORS = "Machine parts vendors and equipment suppliers"
    
    # Logistics & Transportation
    LOGISTICS_COMPANIES = "Logistics companies and transportation operators"
    
    # Retail & E-commerce
    RETAILERS_ECOMMERCE = "Retail companies and e-commerce platforms"
    FOOD_BRANDS_PRODUCERS = "Food brands, producers, and farmers"
    CUSTOMER_SERVICE = "Customer service and support teams"
    
    # Creative & Media
    CONTENT_CREATORS = "Content creators and digital artists"
    MEDIA_ENTERTAINMENT = "Media companies, streaming services, and entertainment industry"
    MUSIC_INDUSTRY = "Music schools, teachers, and music professionals"
    ADVERTISING_MARKETING = "Advertising agencies and marketing firms"
    
    # Hospitality & Events
    HOSPITALITY_VENUES = "Hospitality industry, venues, and event management"
    TRAVEL_TOURISM = "Travel agencies and tourism providers"
    SHOPPING_ENTERTAINMENT = "Shopping centers, sports arenas, and entertainment venues"
    
    # Energy & Environment
    ENERGY_UTILITIES = "Energy companies and utility providers"
    ENVIRONMENTAL_ORGANIZATIONS = "Environmental and sustainability organizations"
    COMPLIANCE_ORGANIZATIONS = "Organizations needing CSRD/ESRS compliance"
    
    # Research & Development
    RESEARCH_INSTITUTIONS = "Research institutions, think tanks, and inventors"
    PHARMACEUTICAL_BIOTECH = "Pharmaceutical and biotech companies"
    EU_FUNDING_SEEKERS = "Organizations seeking EU funding and grants"
    
    # Agriculture & Food
    AGRICULTURE_FOOD = "Agriculture, food industry, and farmers"
    
    # Specialized Services
    IMMIGRATION_SERVICES = "Immigration authorities, migrants, and employers"
    RECRUITING_HR = "Recruiters, HR departments, and employment services"
    FITNESS_WELLNESS = "Fitness trainers and wellness coaches"
    
    # General Users
    GENERAL_CONSUMERS = "General consumers and public users"
    SENIOR_EXECUTIVES = "Senior executives and C-level leaders"
    KNOWLEDGE_WORKERS = "Knowledge workers and professionals"
    
    #Sports 
    SPORTS = "Sport professionals"
    GAMING = "Gaming companies, game programmers"
    
    # Other
    OTHER = "Other target groups not specified above"

class CompanyTargetGroup(BaseModel):
    """Model for company target group classification"""
    target_group: List[TargetGroup] = Field(
        ..., 
        description="""The primary target group that would most benefit from the AI solution. Choose ONE from:
        - Healthcare professionals: Medical practitioners, clinical staff, healthcare facilities
        - Patients and healthcare consumers: End users of healthcare services, health-conscious consumers, chronic disease patients
        - Medical researchers: Research scientists, drug developers, clinical researchers
        - Pharmaceutical companies: Pharmaceutical companies
        - Dental professionals: Dental professionals and oral healthcare providers
        - Psychologists, psychiatrists, and psychotherapists: Mental health professionals and therapy providers
        - Elderly care homes and assisted living providers: Senior care facilities and eldercare professionals
        - Functional medicine clinics and specialized healthcare providers: Alternative and specialized medical practitioners
        - Small and medium businesses: Small business owners, medium-sized companies, entrepreneurial ventures
        - Large enterprise companies and corporations: Fortune 500 companies, multinational corporations, large organizations
        - Startups and entrepreneurs: New business ventures, startup founders, entrepreneurial companies
        - Business analysts, consultants, and advisors: Management consultants, business strategy advisors, professional services
        - Software developers and tech companies: Programming professionals, technology companies, software development firms
        - AI/ML researchers and data scientists: Artificial intelligence researchers, machine learning specialists, data professionals
        - IT professionals and system administrators: Information technology specialists, system administrators, IT support
        - School students: K-12, basic or elementary school students.
        - College/University students: Students of higher educational institutes
        - Job seekers: People seeking jobs
        - Teachers & educational professionals: Educators, instructors, academic staff, educational administrators
        - Educational institutions & schools: Schools, universities, colleges
        - Online learning platforms: Online learning platforms
        - Organizations providing employee training and workforce education: Corporate training, professional development providers
        - Government agencies and public sector organizations: Federal agencies, state governments, public sector
        - Municipalities and city governments: Local government officials, municipal administrators, city planners
        - Defense forces and military organizations: Armed forces, military personnel, defense contractors
        - Law enforcement & security: Police, cybersecurity, security companies
        - Emergency services: Public emergency responders
        - Banks & financial institutions: Traditional banks and credit unions
        - Insurance companies: insurance companies
        - FinTech companies & payment processors: Financial technology startups, digital payment companies
        - Law firms & legal professionals: Legal service providers, attorneys, corporate legal departments
        - Construction companies, contractors, and related sectors: Building contractors, construction firms, construction industry
        - Architects, engineers, and building designers: Building designers, structural engineers, construction planners
        - Real estate agents, property managers, and investors: Property sales professionals, property management, real estate investment
        - Property owners, landlords, and facility managers: Building owners, rental property managers, facility operators
        - Manufacturing companies and industrial producers: Factory owners, industrial manufacturers, production companies
        - Automotive manufacturers and car dealerships: Car manufacturers, vehicle producers, automotive sales
        - Machine parts vendors and equipment suppliers: Industrial equipment suppliers, machinery vendors
        - Logistics companies and transportation operators: Freight companies, shipping services, transportation providers
        - Retail companies and e-commerce platforms: Physical retail stores, online retailers, digital marketplaces
        - Food brands, producers, and farmers: Food manufacturers, agricultural producers, food industry
        - Customer service and support teams: Customer support professionals, service representatives, help desk teams
        - Content creators and digital artists: YouTubers, bloggers, digital designers, creative professionals
        - Media companies, streaming services, and entertainment industry: TV, radio, film, gaming, streaming platforms
        - Music schools, teachers, and music professionals: Music education, music industry professionals, music fans
        - Advertising agencies and marketing firms: Ad agencies, marketing professionals, brand managers
        - Hospitality industry, venues, and event management: Hotels, restaurants, event organizers, venue operators
        - Travel agencies and tourism providers: Travel service providers, tourism industry, hospitality providers
        - Shopping centers, sports arenas, and entertainment venues: Entertainment facilities, retail venues, sports organizations
        - Energy companies and utility providers: Electric utilities, power generation, renewable energy companies
        - Environmental and sustainability organizations: Conservation groups, environmental agencies, green tech companies
        - Organizations needing CSRD/ESRS compliance: Companies requiring sustainability reporting and compliance
        - Research institutions, think tanks, and inventors: Academic research organizations, policy research, innovation labs
        - Pharmaceutical and biotech companies: Drug development companies, biotechnology firms, medical research
        - Organizations seeking EU funding and grants: Grant applicants, research funding seekers, EU project participants
        - Agriculture, food industry, and farmers: Agricultural workers, food production, farming communities
        - Immigration authorities, migrants, and employers: Immigration services, migrant support, international employment
        - Recruiters, HR departments, and employment services: Human resources, talent acquisition, employment agencies
        - Fitness trainers and wellness coaches: Personal trainers, wellness professionals, fitness industry workers
        - General consumers and public users: Everyday consumers, general public, end-user consumers
        - Senior executives and C-level leaders: CEOs, executive leadership, senior management professionals
        - Knowledge workers and professionals: Professional workers, office workers, skilled professionals
        - Sport professionals: Sportsmen, game players, gaming institutes
        - Gaming companies, game programmers: Gaming companies, game programmers

        - Other target groups not specified above: Target groups that don't clearly fit into any of the above categories
        
        Return as a list of target groups, for example: ["Healthcare professionals", "Patients and healthcare consumers"] or ["Job seekers"].

        """
    )
    @field_validator('target_group', mode='before')
    @classmethod
    def validate_target_group(cls, v):
        """Convert string or single target group to list"""
        if isinstance(v, str):
            return [v]
        elif isinstance(v, TargetGroup):
            return [v]
        elif isinstance(v, list):
            return v
        else:
            return [v] if v else []

class DataType(str, Enum):
    """
    High-level data type categories for AI solutions.
    Simplified classification focusing on major data formats and domains.
    """
    
    TEXT_DATA = "Text data"
    IMAGE_DATA = "Image data"
    VIDEO_DATA = "Video data"
    AUDIO_DATA = "Audio and speech data"
    TABULAR_DATA = "Tabular and structured data"
    ELECTRONIC_HEALTH_RECORDS = "Electronic health records and medical data"
    GEOSPATIAL_DATA = "Geospatial and location data"
    SENSOR_DATA = "Sensor signals and IoT data"
    FINANCIAL_DATA = "Financial and business data"
    GENOMICS_DATA = "Genomics and biological data"
    ENGINEERING_DATA = "Engineering drawings and technical data"
    OTHER = "Other data types"

class DataRequirements(BaseModel):
    """Model for data requirements classification"""
    data_type: List[DataType]  = Field(
        ..., 
        description="""The primary type of data required for the AI solution. Choose one or more relevant data types from:
        - Text data: Text documents, reports, scientific papers, legal contracts, patient notes, therapy transcripts, regulatory documents, user comments, CVs, job descriptions, and any textual content
        - Image data: Medical images (X-rays, CT scans, MRIs, ultrasounds), photographs, facial images, dental images, cellular imaging, engineering drawings, building drawings, 2D technical diagrams, and any visual content
        - Video data: Video recordings, annotated video feeds, multimedia content, video data with audio tracks, training videos, and any moving visual content
        - Audio and speech data: Speech recordings, audio data, voice transcripts, audio tracks, heartbeat sounds, lung sounds, and any audio content
        - Tabular and structured data: Spreadsheets, databases, numerical data, statistical data, laboratory results, demographic data, metadata, activity data from devices, and structured datasets
        - Electronic health records and medical data: Patient records, medical history, treatment data, clinical data, health metrics, physiological signals (ECG, vital signs), medical device data, and healthcare-specific information
        - Geospatial and location data: GPS coordinates, location metadata, geographical information, mapping data, spatial coordinates, and location-based information
        - Sensor signals and IoT data: Sensor measurements, IoT device signals, physiological monitoring data, environmental sensors, smart device data, and automated data collection
        - Financial and business data: Accounting data, financial records, business operations data, tendering information, procurement data, and business metrics
        - Genomics and biological data: DNA sequences, genetic information, biological samples, genomics data, and biological research data
        - Engineering drawings and technical data: CAD drawings, technical blueprints, 3D point cloud data, architectural plans, engineering specifications, and technical documentation
        - Other data types: Data types that don't clearly fit into any of the above categories
        
        Return as a list of data types, for example: ["Text and document data", "Image and visual data"] or ["Audio and speech data"]
        """
    )
    @field_validator('data_type', mode='before')
    @classmethod
    def validate_data_type(cls, v):
        """Convert string or single data type to list"""
        if isinstance(v, str):
            return [v]
        elif isinstance(v, DataType):
            return [v]
        elif isinstance(v, list):
            return v
        else:
            return [v] if v else []


# Main CompanyInfo model that integrates the individual models
class CompanyInfo(BaseModel):
    """Main model for company information extraction"""
    company_name: str = Field(..., description="The name of the company")
    
    country: str = Field(..., description="Country where the company is located or headquartered")
    
    consultation_date: str = Field(
        ..., 
        description="Date of the consultation or report in dd-mm-yyyy format (e.g., 15-03-2024). "
    )
    
    experts: str = Field(
        ..., 
        description="Names of the persons providing AI consultancy. If multiple experts, separate them with commas."
    )
    
    consultation_type: ConsultationType = Field(
        ..., 
        description="Type of consultation - either 'Regular' or 'Pop-up'. This must be explicitly mentioned in the document."
    )
    
    domain_info: CompanyDomain = Field(
        ..., 
        description="Domain classification information for the company"
    )
    
    ai_field_info: CompanyAIField = Field(
        ..., 
        description="AI field classification information for the company"
    )
    
    intended_solution: str = Field(
        ..., 
        description="Brief description (one phrase not exceeding a few words) of the company's proposed or intended AI solution. Examples: 'AI-based healthcare app for lifestyle recommendations', 'AI-based language learning platform', 'Computer vision system for quality control', etc."
    )
    
    ai_maturity_level: MaturityLevel = Field(
        ..., 
        description="Company's AI maturity level - Low, Moderate, or High. "
    )
    
    technical_expertise: MaturityLevel = Field(
        ..., 
        description="Company's technical expertise and capability level - Low, Moderate, or High."
    )
    
    company_type: CompanyType = Field(
        ..., 
        description="Type of company - either 'Startup' or 'Established company'."
    )
    
    target_market: CompanyTargetGroup = Field(
        ..., 
        description="Identified target market or customers. Select one or more relevant target groups. If multiple points, separate them with semicolons."
    )
    
    data_requirements: DataRequirements = Field(
        ..., 
        description="Type and format of data required for the intended AI integration. Select one or more relevant target groups. If multiple points, separate them with semicolons."
    )
    
    fair_services_sought: ServicesDescriptions = Field(
        ..., 
        description="Services expected by the company. Select one or more relevant services. If multiple points, separate them with semicolons."
    )
    
    recommendations: str = Field(
        ..., 
        description="Very brief summary of key recommendations focusing on the most important suggested actions. If multiple points, separate them with semicolons. Keep it concise and actionable. Each action point should be a very brief phrase."
    )