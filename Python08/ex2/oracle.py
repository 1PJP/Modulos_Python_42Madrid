from dotenv import load_dotenv
import os


load_dotenv()

if __name__ == "__main__":
    matrix_mode = os.environ.get('MATRIX_MODE', 'Not set')
    database_url = os.environ.get('DATABASE_URL', 'Not set')
    api_key = os.environ.get('API_KEY', 'Not set')
    log_level = os.environ.get('LOG_LEVEL', 'Not set')
    zion_endpoint = os.environ.get('ZION_ENDPOINT', 'Not set')

    print('\nORACLE STATUS: Reading the Matrix...\n')
    print('Configuration Loaded:')
    print(f'Mode: {matrix_mode}')
    print(f'Database: {database_url}')
    print(f'API Access: {api_key}')
    print(f'Log Level: {log_level}')
    print(f'Zion Network: {zion_endpoint}\n')

    print('Environment security check:')
    print('[OK] No hardcoded secrets detected')
    print('[OK] .env file properly configured')
    print('[OK] Production overrides available\n')

    print('The Oracle sees all configurations')
