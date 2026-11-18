# observatory · 地方报刊扫描覆盖和词表命中底账

使用 Python 3.11 标准库，不需要联网、第三方包或数据库。输入示例使用本地合成记录。

```sh
python3 -m observatory quarter data/sample.json
python3 -m unittest discover -s tests -v
```

输出为 UTF-8 JSON。输入文件不可读、业务引用无效或记录不符合口径时退出码为 2，同时报告原因。

## 记录口径

`issues` 中 `eligible` 是该期已发行且纳入观察的版面编号；`scans` 保留每页的 `layout`、扫描批次和已识别 `tokens`，没有扫描行不是无词。`glossaries` 以版本及议题编号保存同义词集合，`edition` 是目前使用的版本。
`checks` 的键为版面和词表版本，`mentions` 是人工检查的该议题实际出现与否；`kind` 区分 random 与 targeted，随机记录的 `probability` 来自同版式和机器命中层内无放回抽查。`annotations` 保存点校派工，`archive` 是已发布报告的资料期、词表版本和出处索引。
