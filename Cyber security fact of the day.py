import random

# List of cybersecurity facts
cybersecurity_facts = [
    "The most commonly used password is '123456'.",
    "Two-factor authentication (2FA) enhances security by requiring two forms of verification.",
    "A 'firewall' is a network security device that filters incoming and outgoing network traffic.",
    "Phishing is a common cyberattack where attackers trick individuals into revealing sensitive information.",
    "Ransomware is malware that encrypts your data and demands a ransom for decryption.",
    "Ethical hackers, also known as 'white hat' hackers, help organizations by identifying security vulnerabilities.",
    "Regular software updates and patches are essential for maintaining strong cybersecurity.",
    "Social engineering is a tactic that exploits human psychology to gain unauthorized access to systems.",
]

# Randomly select and display a cybersecurity fact
random_fact = random.choice(cybersecurity_facts)
print("Cybersecurity fact of the day:")
print(random_fact)