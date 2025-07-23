import os
import glob
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pydantic import BaseModel, Field, field_validator
from enum import Enum
from typing import Optional, List
import streamlit as st
from docx import Document
import time
import json
from llama_cloud_services import LlamaExtract, EU_BASE_URL

# Read the LlamaCloud API key from Streamlit secrets
LLAMA_CLOUD_API_KEY = st.secrets["LLAMA_CLOUD_API_KEY_EU"]

#### Set up the LlamaExtract client
llama_extract = LlamaExtract(api_key=LLAMA_CLOUD_API_KEY, base_url=EU_BASE_URL) 


# Import models
from models import (
    ConsultationType,
    MaturityLevel,
    CompanyType,  
    Services,  
    Domain, 
    TargetGroup, 
    AIField, 
    CompanyDomain, 
    CompanyTargetGroup, 
    CompanyAIField, 
    ServicesDescriptions,
    CompanyInfo,
    DataType,
    DataRequirements
)

# Function to create or get extraction agent
def setup_extraction_agent():
    """Set up the LlamaExtract agent with the CompanyInfo schema"""
    try:
        # Try to get existing agent
        existing_agents = llama_extract.list_agents()
        for agent in existing_agents:
            if agent.name == "company-info-extractor":
                print("Using existing extraction agent...")
                return agent
    except Exception as e:
        print(f"Error checking existing agents: {e}")
        pass
    
    print("Creating new extraction agent...")
    agent = llama_extract.create_agent(
        name="company-info-extractor",
        data_schema=CompanyInfo
    )
    return agent

# Function to extract company information using LlamaExtract
def extract_company_info_llama(file_path):
    """Extract company information using LlamaExtract"""
    file_name = os.path.basename(file_path)
    company_name = os.path.splitext(file_name)[0]
    
    try:
        print(f"  Analyzing document with LlamaExtract...")
        start_time = time.time()
        
        # Get the extraction agent
        agent = setup_extraction_agent()
        
        # Extract information from the document
        extraction_result = agent.extract(file_path)
        
        elapsed_time = time.time() - start_time
        print(f"  LlamaExtract analysis completed in {elapsed_time:.2f} seconds")
        
        # Get the extracted data
        if extraction_result and hasattr(extraction_result, 'data'):
            extracted_data = extraction_result.data
            
            # Convert the extracted data to CompanyInfo object if it's a dict
            if isinstance(extracted_data, dict):
                # Clean and validate the extracted data
                cleaned_data = clean_extracted_data(extracted_data, company_name)
                
                # Create CompanyInfo object from the cleaned data
                company_info = CompanyInfo(**cleaned_data)
                return company_info
            else:
                # If it's already a CompanyInfo object
                if not extracted_data.company_name or extracted_data.company_name.strip() == "":
                    extracted_data.company_name = company_name
                return extracted_data
        else:
            raise Exception("No data extracted from document")
    
    except Exception as e:
        print(f"  Error extracting information with LlamaExtract: {e}")
        print(f"  Falling back to default values...")
        
        # Return a default object with minimal information
        return CompanyInfo(
            company_name="n/a",
            country="n/a",
            consultation_date="n/a",
            experts="Unknown",
            consultation_type="n/a",  # Use enum value
            domain_info="n/a",
            ai_field_info="n/a",
            intended_solution="n/a",
            ai_maturity_level="n/a",
            technical_expertise="n/a",
            company_type="n/a",
            target_market="n/a",
            data_requirements="n/a",
            fair_services_sought="n/a",  # Use list
            recommendations="n/a"
        )

def clean_extracted_data(extracted_data, fallback_company_name):
    """Clean and validate extracted data with special handling for list fields"""
    cleaned = extracted_data.copy()
    
    # Ensure company name is set
    if not cleaned.get('company_name') or cleaned.get('company_name', '').strip() == "":
        cleaned['company_name'] = fallback_company_name
    
    # Ensure consultation_date and country are strings, not None
    if cleaned.get('consultation_date') is None:
        cleaned['consultation_date'] = "n/a"
    if cleaned.get('country') is None:
        cleaned['country'] = "n/a"
    
    # Handle services field - ensure it's in the right format
    if 'fair_services_sought' in cleaned and isinstance(cleaned['fair_services_sought'], dict):
        services_data = cleaned['fair_services_sought']
        if 'services' in services_data:
            services = services_data['services']
            if isinstance(services, str):
                services_data['services'] = [services]
            elif not isinstance(services, list):
                services_data['services'] = [str(services)]
    
    # Handle target_market field - ensure it's in the right format
    if 'target_market' in cleaned and isinstance(cleaned['target_market'], dict):
        target_data = cleaned['target_market']
        if 'target_group' in target_data:
            target_group = target_data['target_group']
            if isinstance(target_group, str):
                target_data['target_group'] = [target_group]
            elif not isinstance(target_group, list):
                target_data['target_group'] = [str(target_group)]
    
    # Handle data_requirements field - ensure it's in the right format
    if 'data_requirements' in cleaned and isinstance(cleaned['data_requirements'], dict):
        data_req = cleaned['data_requirements']
        if 'data_type' in data_req:
            data_type = data_req['data_type']
            if isinstance(data_type, str):
                data_req['data_type'] = [data_type]
            elif not isinstance(data_type, list):
                data_req['data_type'] = [str(data_type)]
    
    return cleaned

# Function to process all documents in a folder
def process_documents(folder_path):
    # Get all files in the folder
    docx_files = glob.glob(os.path.join(folder_path, '*.docx')) #replace (or add) with the file extension(s) of your choice
    total_files = len(docx_files)
    
    print(f"Found {total_files} documents to process")
    
    # Initialize a list to store the extracted information
    results = []
    
    # Process each file with progress tracking
    for i, file_path in enumerate(docx_files, 1):
        file_name = os.path.basename(file_path)
        print(f"\nProcessing document {i}/{total_files}: {file_name}")
        
        # Extract company info using LlamaExtract
        company_info = extract_company_info_llama(file_path)
        results.append(company_info)
        
        print(f"  Results:")
        print(f"    Company: {company_info.company_name}")
        print(f"    Country: {company_info.country}")
        print(f"    Consultation Date: {company_info.consultation_date}")
        print(f"    Experts: {company_info.experts}")
        print(f"    Consultation Type: {company_info.consultation_type.value}")
        print(f"    Domain: {company_info.domain_info.domain.value}")
        print(f"    AI Field: {company_info.ai_field_info.ai_field.value}")
        print(f"    Intended Solution: {company_info.intended_solution}")
        print(f"    AI Maturity Level: {company_info.ai_maturity_level.value}")
        print(f"    Technical Expertise: {company_info.technical_expertise.value}")
        print(f"    Company Type: {company_info.company_type.value}")
        print(f"    Target Market: {'; '.join([tg.value for tg in company_info.target_market.target_group])}")
        print(f"    Data Requirements: {'; '.join([dt.value for dt in company_info.data_requirements.data_type])}")
        print(f"    FAIR Services Sought: {'; '.join([service.value for service in company_info.fair_services_sought.services])}")
        print(f"    Recommendations: {company_info.recommendations}")
    
    print(f"\nAll {total_files} documents processed successfully!")
    return results

# Function to save results to Excel
def save_to_excel(results, output_file):
    print(f"\nSaving results to Excel file...")
    
    # Convert results to a pandas DataFrame
    data = [
        {
            "Company Name": result.company_name,
            "Country": result.country,
            "Consultation Date": result.consultation_date,
            "Experts": result.experts,
            "Consultation Type": result.consultation_type.value,
            "Domain": result.domain_info.domain.value,
            "AI Field": result.ai_field_info.ai_field.value,
            "Intended Solution": result.intended_solution,
            "AI Maturity Level": result.ai_maturity_level.value,
            "Technical Expertise": result.technical_expertise.value,
            "Company Type": result.company_type.value,
            "Target Market": "; ".join([tg.value for tg in result.target_market.target_group]),
            "Data Requirements": "; ".join([dt.value for dt in result.data_requirements.data_type]),
            "FAIR Services Sought": "; ".join([service.value for service in result.fair_services_sought.services]),
            "Recommendations": result.recommendations
        }
        for result in results
    ]
    
    df = pd.DataFrame(data)
    
    # Save to Excel
    df.to_excel(output_file, index=False)
    print(f"Results saved to {output_file}")
    
    return df


# Main function
def main():
    print("=" * 80)
    print("AI CONSULTANCY DOCUMENT ANALYSIS")
    print("=" * 80)
    
    import os

    # Set the folder paths
    input_folder = 'input'
    output_folder = 'output'

    # Check if input folder exists, create if it doesn't
    if not os.path.exists(input_folder):
        os.makedirs(input_folder)

    # Check if output folder exists, create if it doesn't
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    print("Analyzing documents...")
    results = process_documents(input_folder)
    
    # Save the results to Excel
    output_file = os.path.join(output_folder, 'company_analysis_llama_extract.xlsx')
    df = save_to_excel(results, output_file)

    print("\n" + "=" * 80)
    print(f"Analyzed {len(results)} documents")
    print(f"Results saved to: {output_folder}")
    print("=" * 80)

if __name__ == "__main__":
    main()
