# QA Automation Portfolio - Python, pytest, Playwright

This repository contains QA automation projects built as I transition from Manual QA toward Automation QA / SDET-style work.

It currently includes:

- **Session_2**: API automation project using **Python + pytest + requests**
- **Session_3_ui**: early UI automation practice using **Python + pytest + Playwright**

---

## Tech Stack

- Python
- pytest
- requests
- Playwright
- Git / GitHub

---

## Repository Structure

```text
.
├── .gitignore
├── README.md
├── requirements.txt
├── Session_2/
│   ├── config.py
│   ├── http_client.py
│   ├── tests/
│   └── validations/
├── Session_3_ui/
│   ├── config.py
│   ├── test_data.py
│   └── tests/
```

---

## What This Repository Demonstrates

This repository demonstrates practical QA automation fundamentals with a focus on clean test design and gradual framework thinking.

It includes:

- reusable API client setup
- pytest fixtures for shared setup
- reusable response contract / structure validations
- positive, negative, and edge-case API tests
- parametrized test coverage
- early UI automation practice with Playwright
- clearer separation between test scenarios, validations, and shared infrastructure

---

## Session_2 — API Automation

`Session_2` is the main API automation part of this repository.

It is built around **Python + pytest + requests** and focuses on writing maintainable API tests with reusable infrastructure and validations.

### What it demonstrates

- reusable `HttpClient`
- fixture-based setup with `api_client`
- centralized JSON parsing through `parse_json()`
- reusable response structure / contract validations
- separation between:
  - scenario assertions
  - contract / structure validations
  - shared infrastructure
- positive, negative, and edge-case tests
- parametrized tests across endpoints and scenarios

### API test flow used in the suite

1. send request
2. assert status code
3. parse JSON response
4. validate response structure / contract
5. assert scenario-specific expectations

### Notes

The API automation work in `Session_2` is based on **JSONPlaceholder**, which is a fake/demo API.

Because of that, some negative scenarios reflect **observed fake API behavior**, not strict real-world backend validation behavior.

For example, some invalid payloads may still return success responses and be echoed back instead of being rejected by the server.

---

## Session_3_ui — UI Automation

`Session_3_ui` contains early UI automation practice using **Python + pytest + Playwright**.

It is currently smaller in scope than the API project and represents an early Playwright practice stage.

### What it demonstrates

- Playwright page interaction
- locator usage
- assertions with `expect()`
- navigation and redirect validation
- separation of tests by behavior
- use of fixtures and test data / constants

### Current UI examples

- homepage heading visibility
- navigation / redirect validation

---

### Debugging Playwright Failures

Playwright UI tests are configured to keep debugging artifacts only when a test fails.

Generated artifacts may include:

* `trace.zip`
* failure screenshots
* failure videos

These files are generated under `test-results/` and are ignored by Git because they are test execution artifacts, not source code.

To run the UI test suite:

```bash
python -m pytest -q Session_3_ui
```

To open the first available Playwright trace after a failure:

```powershell
$trace = Get-ChildItem -Recurse test-results -Filter trace.zip | Select-Object -First 1
python -m playwright show-trace "$($trace.FullName)"
```

When diagnosing a Playwright failure, check:

1. the failed test and line from the stack trace
2. the Playwright call log to see what action or assertion was attempted
3. the current page state in the trace viewer
4. whether the failure is caused by a locator issue, wrong expected data, navigation problem, page state issue, environment problem, or real application behavior


## Setup

Create and activate a virtual environment, then install the project dependencies.

```bash
python -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
python -m playwright install
```

---

## How to Run

### Run all API tests

```bash
python -m pytest -q Session_2
```

### Run all UI tests

```bash
python -m pytest -q Session_3_ui
```

### Run a single API test file

```bash
python -m pytest -q Session_2/tests/test_posts_api.py
```

### Run a single UI test file

```bash
python -m pytest -q Session_3_ui/tests/test_navigation.py
```

---

## Why the Projects Are Structured This Way

The goal of this repository is not only to write passing tests, but also to practice:

- separation of concerns
- reusable validations
- maintainability
- debugging-friendly test structure
- negative testing
- gradual refactoring into a cleaner automation framework foundation

In the API project, tests keep the scenario and expected result, while validation helpers keep reusable contract / structure checks.

This keeps the suite easier to scale, debug, and maintain.

---

## Current Focus

I am using this repository to build toward:

**Manual QA → Automation QA → SDET-style work**

with emphasis on:

- API automation
- UI automation
- reusable test design
- maintainability
- clearer debugging
- cleaner project structure