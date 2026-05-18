<div align="center">

# 📚 ScholarLib-EM

**Scholar Library for Economics & Management**

*A curated, open-access collection of research papers in Economics & Management — browse, download, and cite. Stop digging, start writing.*

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Paper Count](https://img.shields.io/badge/Papers-20%2B-green.svg)](papers/)
[![Fields](https://img.shields.io/badge/Fields-18-blue.svg)](#-research-fields-covered)

[English](#english) · [中文](#中文)

</div>

---

## English

### 🎯 What is This?

**ScholarLib-EM** is a systematically organized repository of open-access research papers focused on **Economics & Management**. Every paper comes with a ready-to-use **BibTeX citation** — just copy, paste, and keep writing.

**No more hunting through Google Scholar, juggling tabs, or wrestling with paywalls.**

### 📂 How Papers Are Organized

Papers are organized by **6 levels**: `Year → Field → Topic → Journal Tier → Method → Industry Scenario`

```
papers/
├── 2020-2025/                          # Legacy: Year → Field → Paper
│
├── 2026/                               # Enhanced 6-level structure
│   ├── {field}/                        # 18 research fields
│   │   ├── {topic}/                    # 3-5 topics per field
│   │   │   ├── {journal-tier}/         # 5 journal tiers
│   │   │   │   ├── {method}/           # 5 research methods
│   │   │   │   │   ├── {scenario}/     # 10 industry scenarios
│   │   │   │   │   │   └── {paper}/   # Paper entry
│   │   │   │   │   │       ├── paper.bib
│   │   │   │   │   │       └── metadata.json
│   │   │   │   │   │
│   │   │   │   │   ├── cross-industry/              # Cross-industry
│   │   │   │   │   ├── technology-internet/         # Tech & Internet
│   │   │   │   │   ├── manufacturing/               # Manufacturing
│   │   │   │   │   ├── finance-banking/             # Finance & Banking
│   │   │   │   │   ├── healthcare-pharma/           # Healthcare & Pharma
│   │   │   │   │   ├── education/                   # Education
│   │   │   │   │   ├── government-public/           # Government & Public Sector
│   │   │   │   │   ├── retail-consumer-goods/       # Retail & Consumer Goods
│   │   │   │   │   ├── energy-utilities/            # Energy & Utilities
│   │   │   │   │   ├── real-estate-construction/    # Real Estate & Construction
│   │   │   │   │   ├── consulting-professional-services/  # Consulting & Professional
│   │   │   │   │   └── agriculture-food/            # Agriculture & Food
│   │   │   │   │
│   │   │   │   ├── FT50-UTD24/        # 🏆 AMJ, JAP, ASQ, SMJ...
│   │   │   │   ├── SSCI-Q1/           # HRM, JOB, JVB...
│   │   │   │   ├── SCI-Q1/            # JVB, Work & Stress...
│   │   │   │   ├── CSSCI/             # 管理世界, 南开管理评论...
│   │   │   │   └── Other-Top/         # ABS 3/4, ABDC A*...
│   │   │   │
│   │   │   │   ├── empirical/         # Empirical studies
│   │   │   │   ├── theoretical/       # Theory building
│   │   │   │   ├── meta-analysis/     # Meta-analyses
│   │   │   │   ├── review/            # Literature reviews
│   │   │   │   └── experimental/      # Experiments
│
│   ├── human-resources/               # Example: most populated field
│   │   ├── ai-work/                   # AI & Work
│   │   │   ├── FT50-UTD24/experimental/technology-internet/
│   │   │   │   └── generative-ai-creativity-field-experiment/  # JAP
│   │   │   └── SSCI-Q1/empirical/
│   │   │       ├── technology-internet/
│   │   │       │   ├── ai-double-edged-sword-service-performance/  # JOB
│   │   │       │   └── star-advantage-employee-value-ai/           # HRM
│   │   │       └── cross-industry/
│   │   │           └── ...
│   │   ├── leadership/                # Leadership
│   │   ├── compensation-rewards/      # Compensation & Rewards
│   │   ├── diversity-dei/             # Diversity, Equity & Inclusion
│   │   ├── employee-wellbeing/        # Employee Wellbeing
│   │   └── talent-management/         # Talent Management
│   │
│   ├── finance/                       # Finance
│   │   ├── corporate-finance/
│   │   ├── asset-pricing/
│   │   ├── derivatives/
│   │   ├── fintech/
│   │   └── financial-markets/
│   │
│   ├── digital-economy/               # 🆕 Digital Economy
│   │   ├── platform-economy/
│   │   ├── e-commerce/
│   │   ├── digital-transformation/
│   │   └── data-economy/
│   │
│   ├── esg-sustainability/            # 🆕 ESG & Sustainability
│   │   ├── corporate-social-responsibility/
│   │   ├── green-finance/
│   │   ├── sustainable-supply-chain/
│   │   └── climate-risk/
│   │
│   ├── behavioral-economics/          # 🆕 Behavioral Economics
│   ├── labor-economics/               # 🆕 Labor Economics
│   ├── international-business/        # 🆕 International Business
│   ├── health-economics/              # 🆕 Health Economics
│   ├── tourism-hospitality/           # 🆕 Tourism & Hospitality
│   ├── real-estate-urban-economics/   # 🆕 Real Estate & Urban Econ
│   └── ... (18 fields total)
```

### 🏅 Journal Tier System

| Tier | Description | Examples |
|------|-------------|----------|
| **FT50-UTD24** 🏆 | Financial Times Top 50 & UTD Dallas 24 | AMJ, AMR, ASQ, JAP, SMJ, JIBS |
| **SSCI-Q1** | SSCI Q1 (Social Sciences, top quartile) | HRM, JOB, JVB, Human Relations, LQ |
| **SCI-Q1** | SCI Q1 (Science, top quartile) | Journal of Vocational Behavior |
| **CSSCI** | 中文社会科学引文索引 | 管理世界, 南开管理评论, 心理学报 |
| **Other-Top** | Other highly regarded journals | ABS 3/4, ABDC A*, Scopus Q1 |

### 🔬 Research Method Classification

| Method | Description |
|--------|-------------|
| **empirical** | Quantitative/qualitative empirical studies using real-world data |
| **theoretical** | Theory building, conceptual frameworks, mathematical models |
| **meta-analysis** | Systematic meta-analyses and meta-analytic reviews |
| **review** | Literature reviews, systematic reviews, critical analyses |
| **experimental** | Lab experiments, field experiments, randomized controlled trials |

### 🏭 Industry Scenario Classification

| Scenario | Description |
|----------|-------------|
| **cross-industry** | Cross-industry, generalizable findings |
| **technology-internet** | Tech companies, internet platforms, AI, software |
| **manufacturing** | Manufacturing, production, supply chain |
| **finance-banking** | Banking, insurance, investment, fintech |
| **healthcare-pharma** | Hospitals, pharma, healthcare systems |
| **education** | Schools, universities, edtech |
| **government-public** | Government agencies, public administration |
| **retail-consumer-goods** | Retail, e-commerce, FMCG |
| **energy-utilities** | Energy, oil & gas, utilities |
| **real-estate-construction** | Real estate, construction, infrastructure |
| **consulting-professional-services** | Consulting, law, accounting firms |
| **agriculture-food** | Agriculture, food industry |

### 📋 Research Fields Covered (18 Fields)

| # | Field | Topics |
|---|-------|--------|
| 1 | **Microeconomics** | Consumer theory, industrial organization, game theory, behavioral experiments |
| 2 | **Macroeconomics** | Monetary policy, economic growth, international trade, business cycles |
| 3 | **Finance** | Corporate finance, asset pricing, derivatives, fintech, financial markets |
| 4 | **Accounting** | Financial reporting, auditing, managerial accounting, ESG disclosure |
| 5 | **Marketing** | Consumer behavior, digital marketing, branding, pricing strategy |
| 6 | **Strategic Management** | Competitive strategy, corporate governance, M&A, business model innovation |
| 7 | **Operations Management** | Supply chain, logistics, production optimization, quality management |
| 8 | **Innovation & Entrepreneurship** | Tech innovation, startup strategy, venture capital, open innovation |
| 9 | **Human Resources** | AI & work, leadership, compensation, DEI, wellbeing, talent management |
| 10 | **Public Economics** | Public policy, taxation, welfare economics, education economics |
| 11 | 🆕 **Behavioral Economics** | Prospect theory, nudging, decision bias, neuroeconomics |
| 12 | 🆕 **Labor Economics** | Unemployment, wage dynamics, labor market, immigration |
| 13 | 🆕 **Digital Economy** | Platform economy, e-commerce, digital transformation, data economy |
| 14 | 🆕 **ESG & Sustainability** | CSR, green finance, sustainable supply chain, climate risk |
| 15 | 🆕 **International Business** | Cross-cultural, MNE strategy, global supply chain, foreign entry |
| 16 | 🆕 **Health Economics** | Health policy, pharmaceutical economics, health insurance, aging |
| 17 | 🆕 **Tourism & Hospitality** | Tourism management, hotel management, destination marketing |
| 18 | 🆕 **Real Estate & Urban Economics** | Housing market, urban development, RE finance, smart city |

### 🚀 Quick Start

1. **Find your paper** → Navigate `papers/2026/{field}/{topic}/{tier}/{method}/{scenario}/`
2. **Grab the citation** → Open the `.bib` file and copy into your `.bib` file
3. **Access the paper** → Click the DOI link in `metadata.json`
4. **Done** ✅ — Back to writing!

### 🤝 Contributing

1. Read [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines
2. Use the [paper template](templates/paper-template/)
3. Submit a Pull Request

### 📜 License

[MIT](LICENSE) license. Individual papers retain their original copyright.

---

## 中文

### 🎯 这是什么？

**ScholarLib-EM** 是一个系统整理的**经济与管理类**开放获取论文库。每篇论文附带可直接使用的 **BibTeX 引用**——复制、粘贴、继续写作。

### 📂 论文如何组织

**6级分类**：`年份 → 领域 → 主题 → 期刊等级 → 研究方法 → 应用场景`

```
papers/2026/
├── {领域}/              # 18个研究领域
│   ├── {主题}/          # 每个领域3-5个主题
│   │   ├── {期刊等级}/  # 5个期刊等级
│   │   │   ├── {方法}/  # 5种研究方法
│   │   │   │   ├── {场景}/  # 12个行业场景
│   │   │   │   │   └── {论文}/
```

### 🏅 期刊等级体系

| 等级 | 说明 | 代表期刊 |
|------|------|---------|
| **FT50-UTD24** 🏆 | 金融时报50本 + UTD 24本 | AMJ, AMR, ASQ, JAP, SMJ, JIBS |
| **SSCI-Q1** | SSCI 一区 | HRM, JOB, JVB, Human Relations, LQ |
| **SCI-Q1** | SCI 一区 | Journal of Vocational Behavior |
| **CSSCI** | 中文社会科学引文索引 | 管理世界, 南开管理评论, 心理学报 |
| **Other-Top** | 其他权威期刊 | ABS 3/4, ABDC A*, Scopus Q1 |

### 🔬 研究方法分类

| 方法 | 说明 |
|------|------|
| **empirical** | 实证研究（定量/定性） |
| **theoretical** | 理论构建、概念框架 |
| **meta-analysis** | 元分析 |
| **review** | 文献综述、系统综述 |
| **experimental** | 实验（实验室/现场/随机对照） |

### 🏭 行业应用场景分类

| 场景 | 说明 |
|------|------|
| **cross-industry** | 跨行业、普适性研究 |
| **technology-internet** | 科技公司、互联网平台、AI、软件 |
| **manufacturing** | 制造业、生产、供应链 |
| **finance-banking** | 银行、保险、投资、金融科技 |
| **healthcare-pharma** | 医院、制药、医疗系统 |
| **education** | 学校、大学、教育科技 |
| **government-public** | 政府机构、公共管理 |
| **retail-consumer-goods** | 零售、电商、快消品 |
| **energy-utilities** | 能源、油气、公用事业 |
| **real-estate-construction** | 房地产、建筑、基础设施 |
| **consulting-professional-services** | 咨询、法律、会计师事务所 |
| **agriculture-food** | 农业、食品行业 |

### 📋 18个研究领域

| # | 领域 | 主题 |
|---|------|------|
| 1 | **微观经济学** | 消费者理论、产业组织、博弈论、行为实验 |
| 2 | **宏观经济学** | 货币政策、经济增长、国际贸易、经济周期 |
| 3 | **金融学** | 公司金融、资产定价、衍生品、金融科技、金融市场 |
| 4 | **会计学** | 财务报告、审计、管理会计、ESG披露 |
| 5 | **市场营销** | 消费者行为、数字营销、品牌管理、定价策略 |
| 6 | **战略管理** | 竞争战略、公司治理、并购、商业模式创新 |
| 7 | **运营管理** | 供应链、物流、生产优化、质量管理 |
| 8 | **创新与创业** | 技术创新、创业策略、风险投资、开放式创新 |
| 9 | **人力资源管理** | AI与工作、领导力、薪酬激励、DEI、员工福祉、人才管理 |
| 10 | **公共经济学** | 公共政策、税收、福利经济学、教育经济学 |
| 11 | 🆕 **行为经济学** | 前景理论、助推、决策偏差、神经经济学 |
| 12 | 🆕 **劳动经济学** | 失业、工资动态、劳动力市场、移民 |
| 13 | 🆕 **数字经济** | 平台经济、电子商务、数字化转型、数据经济 |
| 14 | 🆕 **ESG与可持续发展** | 企业社会责任、绿色金融、可持续供应链、气候风险 |
| 15 | 🆕 **国际商务** | 跨文化、跨国企业战略、全球供应链、海外进入 |
| 16 | 🆕 **卫生经济学** | 卫生政策、医药经济学、健康保险、老龄化 |
| 17 | 🆕 **旅游与酒店管理** | 旅游管理、酒店管理、目的地营销 |
| 18 | 🆕 **房地产与城市经济学** | 住房市场、城市发展、房地产金融、智慧城市 |

### 🚀 快速使用

1. **找论文** → `papers/2026/{领域}/{主题}/{期刊等级}/{方法}/{场景}/`
2. **取引用** → 复制 `.bib` 文件内容
3. **读全文** → 点击 `metadata.json` 中的 DOI 链接
4. **完成** ✅

### 🤝 参与贡献

1. 阅读 [CONTRIBUTING.md](CONTRIBUTING.md)
2. 使用 [论文模板](templates/paper-template/)
3. 提交 Pull Request

---

<div align="center">

**⭐ If this repository helps your research, consider giving it a star!**

Made with ❤️ for the academic community

</div>
