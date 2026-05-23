### Wizardry Variants Daphne Store Autocollector

\[English | [繁體中文](readme.zh-TW.md)\]

This is just a small bit of code to autocollect Wizardry Variants Daphne weekly free rewards from the online store.

To execute, the imports need settled:

```
pip install selenium
```

Then execute `python main.py [your_Wizardry_ID]` on the command line.

This file should work across environments, locales, and operating systems; it just requires the Chrome webdriver. Should also be compatible with `cron` (see the GitHub Actions workflow for an example).

### Running on GitHub Actions

The included workflow at `.github/workflows/python-app.yml` runs weekly (Mondays at 11:00 UTC) and can also be triggered manually.

The `WIZARDRY_USER_ID` repository secret **must be set** before the workflow can run — both scheduled and manual runs will fail-fast otherwise.

1. In your fork, go to **Settings → Secrets and variables → Actions → New repository secret**.
2. Add a secret named `WIZARDRY_USER_ID` with your Wizardry user ID as the value.