# Python + Pytest + Playwright + POM

A beginner-friendly UI test framework for the QAFox website, organized with the
Page Object Model (POM). Tests use the Playwright sync API and pytest-playwright
fixtures so browser and page cleanup is managed by the plugin.

## Prerequisites

- Windows 10 or later
- Python 3.10+
- Visual Studio Code (optional)
- Internet access to reach `https://www.qafox.com/`

## Project structure

```text
python-playwright-pom/
|-- .github/
|   `-- workflows/
|       `-- tests.yml
|-- pages/
|   |-- base_page.py
|   |-- home_page.py
|   |-- navigation_page.py
|   `-- search_results_page.py
|-- reports/
|-- screenshots/
|-- test_data/
|   `-- test_data.json
|-- tests/
|   |-- test_home_page.py
|   |-- test_navigation.py
|   `-- test_search.py
|-- utils/
|   `-- config.py
|-- conftest.py
|-- pytest.ini
|-- requirements.txt
`-- README.md
```

## Set up in Windows PowerShell

Open PowerShell in this project folder, then create and activate a virtual
environment:

```powershell
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, use the virtual environment's Python directly:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Install dependencies and Chromium:

```powershell
python -m pip install -r requirements.txt
python -m playwright install chromium
```

The `python` commands below assume the virtual environment is active.

## Configuration

The default URL and timeout are in `utils/config.py`. Override them without
editing page objects by setting environment variables:

```powershell
$env:QAFOX_BASE_URL = "https://www.qafox.com/"
$env:QAFOX_TIMEOUT_MS = "15000"
```

## Run tests

Run all tests in Chromium (headless by default):

```powershell
python -m pytest
```

Run a single test file:

```powershell
python -m pytest tests/test_home_page.py
```

Run with a visible browser:

```powershell
python -m pytest --headed
```

Create an HTML report (the `reports` directory is included in the project):

```powershell
python -m pytest --html=reports/report.html --self-contained-html
```

Open `reports/report.html` in a browser to review the report. A screenshot is
automatically captured for each test that fails during its test phase and saved
in `screenshots/`.

## Continuous integration with GitHub Actions

The workflow in `.github/workflows/tests.yml` runs the test suite on pushes and
pull requests targeting `main`, and can also be started manually from the
repository's **Actions** tab. It installs Python dependencies and Chromium,
generates an HTML report, and uploads the report and any failure screenshots as
a downloadable artifact, including when a test fails.

After pushing this project to GitHub, open the **Actions** tab in the repository
to see each run. No repository secrets are required for these public-site tests.
Because they exercise a live website, network outages or site changes can cause
CI failures unrelated to changes in this project.

## Included scenarios

- TC001: Homepage opens and displays the QAFox logo.
- TC002: Homepage title matches the title observed on the live site.
- TC003: Homepage's Courses navigation link is visible.
- TC004: Expected primary homepage content is visible.
- TC005: Homepage URL is correct.
- Navigation: The verified “170 plus Software Testing Types” link opens its
  QAFox article.
- Data-driven search: terms and expected first results are defined in
  `test_data/test_data.json` and run as separate pytest cases.

These tests depend on the live website, so a site outage, redesign, network
issue, or anti-automation response can cause failures unrelated to the
framework.

## Troubleshooting

- **Chromium is missing:** Run `python -m playwright install chromium`.
- **`pytest` or plugin option is missing:** Activate `.venv`, then run
  `python -m pip install -r requirements.txt`.
- **PowerShell does not allow activation:** Use
  `.\.venv\Scripts\python.exe -m pytest` instead.
- **A live-site test times out:** Check the internet connection and open the
  QAFox URL in a regular browser; the website may be unavailable or may have
  changed.
- **The report command cannot write the report:** Confirm that `reports` exists
  and that the project folder is writable.
