# Prompt: docs/index.html Landing Page

docs/index.html 必須包含 (按順序)：
1. Title + 一句話 Tagline（與 README 一致）。
2. Goal / 目標 — 一段 1–3 句的研究問題敘述。
3. Procedure / 過程 — 條列 4–6 個關鍵步驟（e.g., 資料來源、清理規則、分析方法、視覺化選擇）。不要貼 code，要寫成讀者看得懂的句子。
4. Outcome / 結果 — 兩張圖嵌入（從 reports/ 複製到 docs/ 內，路徑要相對於 docs/），每張圖配 1–2 句結論。
5. Caveats / 侷限 — 至少 2 點：取樣偏誤、心理測驗自陳資料的限制、推論範圍等。
6. Repo link / GitHub — 連回 repo 首頁。
7. Author + Date。

顏色風格：以 RGB 設定，第一種：R21, G53, B95；第二種：R252, G251, B245；第三種：R21, G108, B154。

此外，有兩點不允許：
1. 直接把 notebook nbconvert 成 HTML 當 index.html — 那是分析過程，不是成果頁。可以另外放成 docs/notebook.html 並從 index.html 連過去。
2. 預設如黑底深灰字、字體 < 14px、圖片寬度溢出視窗等對讀者不友善的設計。
