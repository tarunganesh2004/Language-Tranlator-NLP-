## How to fix google-trans 

1) uninstall googletrans
```bash 
pip uninstall googletrans
```

2) Install the latest version from GitHub

```bash
git clone https://github.com/alainrouillon/py-googletrans.git
cd py-googletrans
python setup.py install
```


```mermaid 
graph TD;
A[Text]
B[Text to phone Converter ]
C[Encoder pre-net]

D[Multi-head attention]
E[Add and Norm]
F[Feed Forward]
G[Add and Norm]
 
A --> B
B --> C
C --> D 
C --> D
C --> D
C --> E
D --> E
E --> F
F --> G
E --> G



```