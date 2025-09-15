from invoice2data import extract_data
from invoice2data.extract.loader import read_templates

templates = read_templates('templates/')

def extract_invoice_data(file_path):
    result = extract_data(file_path, templates=templates)
    return result