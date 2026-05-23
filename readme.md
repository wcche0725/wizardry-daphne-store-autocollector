### Wizardry Daphne Store Autocollector

This is just a small bit of code to autocollect Wizardry Daphne weekly free rewards from the online store.

To execute, the imports need settled:

```
pip install selenium
```

Then execute `python main.py [your_Wizardry_ID]` on the command line.

This file should work across environments, locales, and operating systems; it just requires the Chrome webdriver. Should also be compatible with `cron` (see the GitHub Actions workflow for an example).

### Running on GitHub Actions

The included workflow at `.github/workflows/python-app.yml` runs weekly (Mondays at 11:00 UTC) and can also be triggered manually.

1. In your fork, go to **Settings → Secrets and variables → Actions → New repository secret**.
2. Add a secret named `WIZARDRY_USER_ID` with your Wizardry user ID as the value.
3. (Optional) Trigger a manual run from the **Actions** tab — you can override the ID for that run via the `user_id` workflow input.