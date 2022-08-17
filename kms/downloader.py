import requests
import markdown

subjects = {
    'xss': 'https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/XSS%20Injection',
    'crlf injection': 'https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/CRLF%20Injection',
    'csrf injection': 'https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/CSRF%20Injection',
    'csv injection': 'https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/CSV%20Injection',
    'cve exploits': 'https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/CVE%20Exploits',
    'command injection': 'https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Command%20Injection',
    'dns rebinding': 'https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/DNS%20Rebinding',
    'directory traversal': 'https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Directory%20Traversal',
    'file inclusion': 'https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/File%20Inclusion',
    'jwt': 'https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/JSON%20Web%20Token',
    'ldap injection': 'https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/LDAP%20Injection',
    'nosql injection': 'https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/NoSQL%20Injection',
    'race condition': 'https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Race%20Condition',
    'sql injection': 'https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/SQL%20Injection',
    'ssrf': 'https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Server%20Side%20Request%20Forgery',
    'ssti': 'https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Server%20Side%20Template%20Injection',
    'type juggling': 'https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Type%20Juggling',
    'xpath injection': 'https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/XPATH%20Injection'
}


def get_subjects():
    return list(subjects.keys())


def get_raw_url(url: str):
    return url.replace("https://github.com", 'https://raw.githubusercontent.com').replace("/tree/", "/")


def get_subject_url(subject: str):
    subject = subject.lower().strip()
    try:
        return subjects[subject]
    except:
        try:
            return subjects[subject.replace("-", " ").replace("_", " ").replace("  ", " ")]
        except:
            return None


def download(subject: str, output: str = None, convert: bool = True):
    subject_url = get_subject_url(subject)
    if subject_url:
        markdown_answer = download_from_url(subject_url)
        if convert:
            html_answer = convert_to_html(markdown_answer)
            if output:
                f = open(output, "w")
                f.write(html_answer)
                f.close()
            return html_answer
        return markdown_answer
    return None


def download_from_url(url: str):
    url += "/README.md"
    url = get_raw_url(url)
    r = requests.get(url)
    return r.text


def convert_to_html(markdown_text: str):
    return markdown.markdown(markdown_text)
