✨ Features

Capability

Flag / Action

Notes

Check a single password

-p "Passw0rd!"

Validates length, letters, digits, symbols.

Batch‑check many passwords

-f passwords.txt or pipe via echo ... |

Each line evaluated separately.

Generate strong password

-g 16 (length)

Guarantees policy compliance.

Zero dependencies

–

Uses only the Python stdlib.

🚀 Quick Start

# clone repo
$ git clone https://github.com/YOUR_USERNAME/simple-password-checker.git
$ cd simple-password-checker

# run checker
$ python3 password_checker.py -p "Sup3rSecr3t!"

# generate a 14‑character password
$ python3 password_checker.py -g 14

Need Python ≥ 3.11. No pip install required.

⚙️ Command‑line Reference

usage: password_checker.py [-h] (-p PASSWORD | -f FILE | -g [LEN])

Lightweight password checker + generator

options:
  -h, --help            show this help message and exit
  -p PASSWORD, --password PASSWORD
                        password to check
  -f FILE, --file FILE  newline‑separated passwords file
  -g [LEN], --generate [LEN]
                        generate a strong password (default 12)

📂 Project Structure

.
├── password_checker.py   # main script
├── README.md             # you are here
└── .github/
    └── workflows/
        └── ci.yml        # GitHub Action (optional)

🛠️ Continuous Integration (optional)

Add a simple GitHub Action to run on each push:

# .github/workflows/ci.yml
name: CI
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - run: python password_checker.py -g 10  # sanity check

Green badge appears automatically in the header.

📈 Roadmap



🤝 Contributing

Fork the repo & create your branch: git checkout -b feat/AmazingFeature

Commit your changes: git commit -m 'feat: add AmazingFeature'

Push to the branch: git push origin feat/AmazingFeature

Open a Pull Request.

Please follow Conventional Commits for clear changelogs.

📝 License

Distributed under the MIT License. See LICENSE for details.

🧑‍💻 Author

Made with  by Tejas.

