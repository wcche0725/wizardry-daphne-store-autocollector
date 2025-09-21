### Wizardry Daphne Store Autocollector

This is just a small bit of code to autocollect Wizardry Daphne weekly free rewards from the online store.

To execute, the imports need settled:

```
pip install python-dotenv
pip install selenium
```

Then just create a .env file contasining simply:

```
USER_ID="your_Wizardry_ID"
```

Then execute `python main.py` on the command line.

This file should work across environments, locales, and operating systems, it just requires the Chrome webdriver. Should also be compatible with `cron` (which is what I plan to do).