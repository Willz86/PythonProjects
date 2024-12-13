import re

def identify_hash(hash_string):
    # Define patterns for different hash types
    hash_patterns = {
        'MD5': {'pattern': r'^[a-f0-9]{32}$', 'hashcat': '0', 'john': 'raw-md5'},
        'SHA1': {'pattern': r'^[a-f0-9]{40}$', 'hashcat': '100', 'john': 'raw-sha1'},
        'SHA-256': {'pattern': r'^[a-f0-9]{64}$', 'hashcat': '1400', 'john': 'raw-sha256'},
        'SHA-512': {'pattern': r'^[a-f0-9]{128}$', 'hashcat': '1700', 'john': 'raw-sha512'}
    }

    # Check each pattern to see if it matches the hash string
    for hash_type, info in hash_patterns.items():
        if re.match(info['pattern'], hash_string):
            return hash_type, info['hashcat'], info['john']
    
    return 'Unknown', 'N/A', 'N/A'

def main():
    # Ask the user for the hash string
    hash_string = input("Enter the hash string: ").strip().lower()

    # Identify the hash
    hash_type, hashcat_option, john_command = identify_hash(hash_string)

    # Print the results
    print(f"Hash Type: {hash_type}")
    print(f"Hashcat Option: -m {hashcat_option}")
    print(f"John the Ripper Command: {john_command}")

if __name__ == "__main__":
    main()

