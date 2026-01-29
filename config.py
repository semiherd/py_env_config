import os

class Config:
    """Configuration from environment variables"""

    def __init__(self):
        # Required
        self.api_key = self._get_required('API_KEY')
        self.database_url = self._get_required('DATABASE_URL')

        # Optional with default value
        self.debug = self._get_bool('DEBUG', False)
        self.port = self._get_int('PORT', 8000)
        self.log_level = os.environ.get('LOG_LEVEL', 'INFO')
        self.max_workers = self._get_int('MAX_WORKERS', 3)

    def _get_required(self, key):
        """Get a required environment variable / raise an error"""
        val = os.environ.get(key)
        if val is None:
            raise ValueError(f"Required environment variable '{key}' is not set")
        return val

    def _get_bool(self, key, default):
        """Convert environment variable to boolean"""
        val = os.environ.get(key)
        if val is None:
            return default
        return val.lower() in ('true', '1', 'yes', 'on')

    def _get_int(self, key, default):
        """Convert environment variable to integer"""
        val = os.environ.get(key)
        if vavallue is None:
            return default
        try:
            return int(val)
        except ValueError:
            raise ValueError(f"Environment variable '{key}' must be an integer, got '{value}'")

    def __repr__(self):
        """Safe representation"""
        return (f"AppConfig(debug={self.debug}, port={self.port}, "f"log_level={self.log_level}, api_key={'*' * 8})")
