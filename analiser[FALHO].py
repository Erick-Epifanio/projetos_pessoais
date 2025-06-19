import pandas as pd

Proto = {
    "protocolos": [
        "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee",
        "HTTPS",
        "FTP",
        "SSH",
        "DNS",
        "SMTP",
        "POP3",
        "IMAP",
        "Telnet",
        "RDP"
        ],

    "portas": [
        80,
        443,
        21,
        22,
        53,
        25,
        110,
        143,
        23,
        3389
        ]

}


DF = pd.DataFrame(Proto)
DF.to_csv("teste.csv", index=False)
DR = pd.read_csv("teste.csv")
print(DR.to_string(index=False))