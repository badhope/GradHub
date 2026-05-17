<div align="center">

# 📚 ScholarLib-EM

**Scholar Library for Economics & Management**

*A curated, open-access collection of research papers in Economics & Management — browse, download, and cite. Stop digging, start writing.*

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Paper Count](https://img.shields.io/badge/Papers-10%2B-green.svg)](papers/)

[English](#english) · [中文](#中文)

</div>

---

## English

### 🎯 What is This?

**ScholarLib-EM** is a systematically organized repository of open-access research papers focused on **Economics & Management**. Every paper comes with a ready-to-use **BibTeX citation** — just copy, paste, and keep writing.

**No more hunting through Google Scholar, juggling tabs, or wrestling with paywalls.**

### 📂 How Papers Are Organized

Papers are organized by **Year → Field → Journal Tier**:

```
papers/
├── 2020-2025/                     # By publication year
│   └── {field}/                   # By research field
│       └── paper-name/
│           ├── paper-name.bib     # BibTeX citation (copy-paste ready)
│           └── metadata.json      # Title, authors, abstract, DOI, keywords
│
├── 2026/                          # Latest papers — enhanced structure
│   ├── microeconomics/
│   │   ├── FT50-UTD24/           # 🏆 Financial Times Top 50 & UTD 24
│   │   ├── SSCI-Q1/              # SSCI Q1 journals
│   │   ├── SCI-Q1/               # SCI Q1 journals
│   │   ├── CSSCI/                # 中文社会科学引文索引
│   │   └── Other-Top/            # ABS 3/4, ABDC A*, etc.
│   ├── finance/
│   ├── human-resources/
│   │   ├── FT50-UTD24/           # AMJ, JAP, ASQ, Personnel Psychology...
│   │   │   ├── ceo-pay-ratios-income-inequality-wellbeing/
│   │   │   ├── generative-ai-creativity-field-experiment/
│   │   │   ├── passion-contagion-differentiated-theory/
│   │   │   └── relationship-splintering-repair-marginalization/
│   │   ├── SSCI-Q1/              # HRM, JOB, JVB, Leadership Quarterly...
│   │   │   ├── ai-double-edged-sword-service-performance/
│   │   │   ├── common-good-hrm-meaningfulness-thriving/
│   │   │   ├── meta-analysis-flexible-working-arrangements/
│   │   │   ├── meta-analysis-hr-attributions-hpws/
│   │   │   ├── star-advantage-employee-value-ai/
│   │   │   └── work-family-conflict-career-outcomes/
│   │   └── ...
│   └── ...
```

### 🏅 Journal Tier System (2026+)

| Tier | Description | Examples |
|------|-------------|----------|
| **FT50-UTD24** 🏆 | Financial Times Top 50 & UTD Dallas 24 | AMJ, AMR, ASQ, JAP, SMJ, JIBS, Personnel Psychology |
| **SSCI-Q1** | SSCI Q1 (Social Sciences, top quartile) | HRM, JOB, JVB, Human Relations, Leadership Quarterly |
| **SCI-Q1** | SCI Q1 (Science, top quartile) | Journal of Vocational Behavior, Work & Stress |
| **CSSCI** | 中文社会科学引文索引 | 管理世界, 南开管理评论, 心理学报, 管理科学学报 |
| **Other-Top** | Other highly regarded journals | ABS 3/4, ABDC A*, Scopus Q1 |

### 🚀 Quick Start

1. **Find your paper** → Browse `papers/{year}/{field}/{tier}/` or use `Ctrl+F` / `GitHub Search`
2. **Grab the citation** → Open the `.bib` file and copy the BibTeX entry into your LaTeX/BibTeX bibliography
3. **Access the paper** → Click the DOI link in `metadata.json` to access the full text
4. **Done** ✅ — Back to writing!

### 📋 Research Fields Covered

| Field | Topics |
|-------|--------|
| **Microeconomics** | Consumer theory, industrial organization, behavioral economics, game theory |
| **Macroeconomics** | Monetary policy, economic growth, international trade, business cycles |
| **Finance** | Corporate finance, asset pricing, derivatives, financial markets, fintech |
| **Accounting** | Financial reporting, auditing, managerial accounting, ESG disclosure |
| **Marketing** | Consumer behavior, digital marketing, branding, pricing strategy |
| **Strategic Management** | Competitive strategy, corporate governance, M&A, business model innovation |
| **Operations Management** | Supply chain management, logistics, production optimization |
| **Innovation & Entrepreneurship** | Technology innovation, startup strategy, venture capital, open innovation |
| **Human Resources** | Organizational behavior, leadership, labor economics, talent management |
| **Public Economics** | Public policy, taxation, welfare economics, health economics |

### 🤝 Contributing

We welcome contributions! If you have a paper to share:

1. Read [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines
2. Use the [paper template](templates/paper-template/) to format your submission
3. Submit a Pull Request

### 📜 License

This collection is released under the [MIT](LICENSE) license. Individual papers retain their original copyright.

---

## 中文

### 🎯 这是什么？

**ScholarLib-EM** 是一个系统整理的**经济与管理类**开放获取论文库。每篇论文都附带可直接使用的 **BibTeX 引用**——复制、粘贴、继续写作。

**不用再翻遍 Google Scholar，不用再纠结付费墙，写论文从此省心。**

### 📂 论文如何组织

论文按 **年份 → 领域 → 期刊等级** 三级分类：

```
papers/
├── 2020-2025/                     # 按发表年份
│   └── {领域}/                    # 按研究领域
│       └── 论文名称/
│           ├── paper-name.bib     # BibTeX 引用（直接复制使用）
│           └── metadata.json      # 标题、作者、摘要、DOI、关键词
│
├── 2026/                          # 最新论文 — 增强版分类
│   ├── human-resources/           # 人力资源管理
│   │   ├── FT50-UTD24/           # 🏆 金融时报50本 + UTD24顶级期刊
│   │   │   ├── ceo-pay-ratios-income-inequality-wellbeing/  # JIBS
│   │   │   ├── generative-ai-creativity-field-experiment/   # JAP
│   │   │   ├── passion-contagion-differentiated-theory/      # ASQ
│   │   │   └── relationship-splintering-repair-marginalization/ # AMJ
│   │   ├── SSCI-Q1/              # SSCI 一区期刊
│   │   │   ├── ai-double-edged-sword-service-performance/    # JOB
│   │   │   ├── common-good-hrm-meaningfulness-thriving/      # HRM
│   │   │   ├── meta-analysis-flexible-working-arrangements/  # JOB
│   │   │   ├── meta-analysis-hr-attributions-hpws/           # HRM
│   │   │   ├── star-advantage-employee-value-ai/             # HRM
│   │   │   └── work-family-conflict-career-outcomes/         # JVB
│   │   ├── SCI-Q1/               # SCI 一区期刊
│   │   ├── CSSCI/                # 中文社会科学引文索引
│   │   └── Other-Top/            # ABS 3/4, ABDC A* 等
│   └── ...
```

### 🏅 期刊等级体系（2026年起）

| 等级 | 说明 | 代表期刊 |
|------|------|---------|
| **FT50-UTD24** 🏆 | 金融时报50本 + UTD 24本 | AMJ, AMR, ASQ, JAP, SMJ, JIBS, Personnel Psychology |
| **SSCI-Q1** | SSCI 一区（社会科学引文索引） | HRM, JOB, JVB, Human Relations, Leadership Quarterly |
| **SCI-Q1** | SCI 一区（科学引文索引） | Journal of Vocational Behavior, Work & Stress |
| **CSSCI** | 中文社会科学引文索引 | 管理世界, 南开管理评论, 心理学报, 管理科学学报 |
| **Other-Top** | 其他权威期刊 | ABS 3/4, ABDC A*, Scopus Q1 |

### 🚀 快速使用

1. **找论文** → 浏览 `papers/{年份}/{领域}/{期刊等级}/` 或使用搜索功能
2. **取引用** → 打开 `.bib` 文件，复制 BibTeX 条目到你的参考文献库
3. **读全文** → 点击 `metadata.json` 中的 DOI 链接访问论文全文
4. **完成** ✅ — 继续写论文！

### 📋 涵盖的研究领域

| 领域 | 研究方向 |
|------|---------|
| **微观经济学** | 消费者理论、产业组织、行为经济学、博弈论 |
| **宏观经济学** | 货币政策、经济增长、国际贸易、经济周期 |
| **金融学** | 公司金融、资产定价、衍生品、金融市场、金融科技 |
| **会计学** | 财务报告、审计、管理会计、ESG 披露 |
| **市场营销** | 消费者行为、数字营销、品牌管理、定价策略 |
| **战略管理** | 竞争战略、公司治理、并购、商业模式创新 |
| **运营管理** | 供应链管理、物流、生产优化 |
| **创新与创业** | 技术创新、创业策略、风险投资、开放式创新 |
| **人力资源管理** | 组织行为、领导力、劳动经济学、人才管理 |
| **公共经济学** | 公共政策、税收、福利经济学、卫生经济学 |

### 🤝 参与贡献

欢迎投稿！如果你有好的论文想要分享：

1. 阅读 [CONTRIBUTING.md](CONTRIBUTING.md) 了解详细指南
2. 使用 [论文模板](templates/paper-template/) 格式化你的投稿
3. 提交 Pull Request

### 📜 许可证

本论文库采用 [MIT](LICENSE) 许可证发布。各篇论文保留其原始版权。

---

<div align="center">

**⭐ If this repository helps your research, consider giving it a star!**

Made with ❤️ for the academic community

</div>
