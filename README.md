<a name="readme-top"></a>

# QC Grade Distribution Formatter

Python script to convert grades exported from CUNYfirst Query Viewer to QC Grade Distribution sheet format

## Table of Contents
<a name="readme-toc"></a>
- [Description](#description)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Contributing](#contributing)
- [Privacy](#privacy)
- [License](#license)
- [Acknowledgements](#acknowledgements)
- [Disclaimer](#disclaimer)

## Description

It too long for the original maintainer to update the grade distribution [spreadsheet](https://docs.google.com/spreadsheets/d/1mS6khEB6m8cPNenNvY9Tg6bJ6YkmcvCI/edit?gid=1942445276#gid=1942445276). Therefore, I decided to improvise myself.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Getting Started

Below are some brief instructions on setting up this project *locally*. To get a local copy up and running follow these simple example steps.

**🛑 If you only want to check the grade distribution, not contribute to it, you should use [this](https://docs.google.com/spreadsheets/d/1mS6khEB6m8cPNenNvY9Tg6bJ6YkmcvCI/edit?gid=1942445276#gid=1942445276) or [this](https://qc-prof-stat.web.app/) instead. 🛑**

### Prerequisites

* Access to Query Viewer in CUNYfirst for data download
    - Campus Solutions Access Request [Form](https://www.cuny.edu/about/administration/offices/cis/information-security/cunyfirst-peoplesoft-security/) can be submitted by your supervisor
* Python 3.9 or above

### Installation

1. Download data from CUNYfirst:
    - Open [Query Viewer](https://home.cunyfirst.cuny.edu/)
    - Run the following query for _Institution: QNS01_ and _Term: Use the appropriate term code_:
        - `CU_SR_GRADE_ROSTER` - Grades By Term
        - `CU_SR_CLASS_ENRL_ALL` - Class Details
    - [How to: Run a CUNYfirst Query](https://employees.brooklyn.edu/base/how-to-run-a-cunyfirst-query/)
    - [CUNYfirst Query List](https://www.cs.qc.cuny.edu/CUNYfirst/QCCV_queries.pdf)
2. Clone the repo:
   ```sh
   git clone https://github.com/popoway/qc-grade-dist-formatter.git
   ```
3. Install dependency packages:
   ```sh
   pip install -r requirements.txt
   ```
4. Improvise:
   ```sh
   python3 grade_summary.py --grade CU_SR_GRADE_ROSTER_339412345.xlsx --details CU_SR_CLASS_ENRL_ALL_126512345.xlsx --term SP24
   ```
4. Profit ✨

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Contributing

If you found a bug or have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".  

To report a security vulnerability, please review the [Security Policy](https://github.com/popoway/qc-grade-dist-formatter/blob/main/SECURITY.md).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Privacy

No data is collected by the app.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## License

[MIT](https://popoway.mit-license.org/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Acknowledgements

Special thanks to `shiv` and `amart` from [QC CS Discord](https://discord.gg/b4kfsBkDnP) for their support and testing.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Disclaimer

"Disclaimer: While I am an employee of Queens College, the "qc-grade-dist-formatter" app is a personal project developed during my summer break. The content, views, and opinions expressed within the app are solely my own and do not reflect the positions, strategies, or opinions of Queens College. This app is neither officially associated with nor maintained by Queens College as part of my employment."

Users should also be aware that use of Query Viewer output consititutes agreement of Confidentiality Statement and are individually accountable for such use.

<p align="right">(<a href="#readme-top">back to top</a>)</p>
