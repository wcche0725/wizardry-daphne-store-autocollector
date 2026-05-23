### Wizardry Variants Daphne 商店自動領取工具

\[[English](readme.md) | 繁體中文\]

這是一段用來自動領取 Wizardry Variants Daphne 線上商店每週免費獎勵的小程式。

執行前需先安裝相依套件：

```
pip install selenium
```

接著在命令列執行 `python main.py [你的 Wizardry ID]`。

本程式可在不同環境、語系與作業系統下運作，僅需 Chrome webdriver。亦可搭配 `cron` 使用（範例請見內附的 GitHub Actions 工作流程）。

### 在 GitHub Actions 上執行

內附的工作流程 `.github/workflows/python-app.yml` 每週執行一次（每週一 UTC 時間 11:00），亦可手動觸發。

執行工作流程前**必須**先設定 `WIZARDRY_USER_ID` 儲存庫密鑰（repository secret），否則排程與手動觸發都會立即失敗。

1. 在你 fork 的儲存庫中前往 **Settings → Secrets and variables → Actions → New repository secret**。
2. 新增一個名為 `WIZARDRY_USER_ID` 的密鑰，值為你的 Wizardry ID。
