# JSON Search & Audit Tool 🔎 #

A powerful Python CLI tool to search, audit, and analyze JSON files using:

* ✅ Key search
* ✅ Value search
* ✅ Key + Value search
* ✅ Regular Expressions
* ✅ Matched results
* ✅ Non-matched results
* ✅ Match counts
* ✅ Audit-ready output

**Designed for:**
- Infrastructure inventory validation
- CMDB audits
- Security posture checks
- Wiz / cloud export validation
- Compliance reporting
- Large JSON dataset analysis


**Features**
* ✔ Search by key
* ✔ Search by value
* ✔ Search by key AND value
* ✔ Regex support
* ✔ Count matched objects
* ✔ Count unmatched objects
* ✔ Show only matched
* ✔ Show only unmatched
* ✔ Clean CLI interface
* ✔ Recursive search (nested JSON supported)
* ✔ No duplicate objects

**Expected JSON Format**
The script expects the top-level JSON to be a list of objects, for example:
~~~
[
  {
    "server_name": "prod-web-01",
    "server_ip_address": "10.0.1.10",
    "os_vendor": "Ubuntu",
    "os_version": "22.04",
    "application": "Nginx",
    "publicly_exposed": true,
    "environment": "Production"
  }
]
~~~

**🚀 Installation**

**1️⃣ Clone the repository or download the file**
~~~
git clone https://github.com/yourusername/json-search-audit-tool.git
cd json-search-audit-tool
~~~
**2️⃣ Ensure Python 3.8+**
~~~
python --version
~~~
No external dependencies required. Uses only Python standard library.

**▶️ Usage**
~~~
python search_json.py <file> [options]
~~~
**🔎 Available Options**

Option	Description

* **--key**	Search by key
* **--value**	Search by value
* **--regex**	Enable regex matching
* **--count-only**	Show only match counts
* **--show-matched**	Show only matched objects
* **--show-unmatched**	Show only unmatched objects

**📌 Examples**

1️⃣ Search by Key

`python search_json.py servers.json --key environment`

2️⃣ Search by Value

`python search_json.py servers.json --value Production`

3️⃣ Search by Key AND Value

`python search_json.py servers.json --key environment --value Production`

4️⃣ Regex Search

Search for all production-like environments:

`python search_json.py servers.json --value "^Prod.*" --regex`

5️⃣ Get Only Counts (Audit Mode)

`python search_json.py servers.json --value true --count-only`

Example output:

`Matched Count   : 12
Unmatched Count : 38
Total Objects   : 50
`

6️⃣ Show Only Unmatched Objects

`python search_json.py servers.json --key publicly_exposed --value false --show-unmatched`


**🧠 How It Works**

* Recursively scans each object
* If any key/value pair matches criteria → object is marked as matched
* Remaining objects are classified as unmatched
* Entire object is returned (no partial fragments)
* Ensures clean audit segmentation

**🎯 Real-World Use Cases**

**Infrastructure Audit**

Find all publicly exposed production servers:

`python search_json.py servers.json --key environment --value Production`

**Compliance Check**

Find servers missing required OS version pattern:

`python search_json.py servers.json --key os_version --value "^22.*" --regex --show-unmatched`

**CMDB Validation**

Count how many servers are externally exposed:


`python search_json.py servers.json --key publicly_exposed --value true --count-only`

**⚠️ Limitations**

* Expects top-level JSON to be a list
* Large files (>2GB) may require streaming optimization
* 🛠 Future Improvements (Optional Roadmap)
* Export matched/unmatched to separate files
* CSV export
* Case-insensitive option
* Streaming mode for very large JSON
* Summary statistics by field
* Interactive TUI mode

**📜 License**
MIT License

**🤝 Contributions**
Pull requests are welcome.
If you find issues or have feature requests, open an issue.

⭐ If You Found This Useful

Give it a star on GitHub!
