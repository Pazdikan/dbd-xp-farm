import configparser
import json
import os

class Config:
    def __init__(self, filename='config.ini'):
        self.filename = filename
        self.config = configparser.ConfigParser()
        self.default_config = configparser.ConfigParser()
        
        # Load default config
        if os.path.exists('default_config.ini'):
            self.default_config.read('default_config.ini')
        
        # Create config file from default if it doesn't exist
        if not os.path.exists(self.filename):
            if os.path.exists('default_config.ini'):
                # Copy default config to new config file
                for section in self.default_config.sections():
                    self.config[section] = {}
                    for key in self.default_config[section]:
                        self.config[section][key] = self.default_config[section][key]
                # Copy DEFAULT section if it exists
                if 'DEFAULT' in self.default_config:
                    self.config['DEFAULT'] = dict(self.default_config['DEFAULT'])
            else:
                self.config['DEFAULT'] = {}
            self.save()
        else:
            self.config.read(self.filename)

    def get(self, key, default=None, section='DEFAULT'):
        """Get a value from config by key"""
        try:
            return self.config[section][key]
        except:
            # Try to get from default config
            try:
                value = self.default_config[section][key]
                self.set(key, value, section)
                return value
            except:
                return default

    def set(self, key, value, section='DEFAULT'):
        """Set a value in config by key"""
        if not self.config.has_section(section):
            self.config[section] = {}
        self.config[section][key] = str(value)
        self.save()

    def save(self):
        """Save config to file"""
        with open(self.filename, 'w') as configfile:
            self.config.write(configfile)


    def get_json(self):
        """Get config as JSON"""
        config_dict = {}
        for section in self.config.sections():
            config_dict[section] = dict(self.config[section])
        if 'DEFAULT' in self.config:
            config_dict['DEFAULT'] = dict(self.config['DEFAULT'])
        return config_dict

    def set_json(self, data):
        """Set config from JSON"""
        self.config = configparser.ConfigParser()
        self.config.read_dict(data)
        self.save()