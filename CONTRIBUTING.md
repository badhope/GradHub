# Contributing to ScholarLib-EM

Thank you for helping grow this open-access academic library! 🎉

## 📋 How to Submit a Paper

### Prerequisites

- The paper must be **open-access** (freely available as a full-text PDF)
- The paper must be related to **Economics or Management**
- You must have the right to share the paper (check the paper's license)

### Submission Steps

1. **Fork** this repository
2. **Navigate** to `papers/{year}/{category}/`
3. **Create a folder** named after the paper (use `kebab-case`, e.g., `market-frictions-in-crypto`)
4. **Add the following files** inside the folder:

```
market-frictions-in-crypto/
├── market-frictions-in-crypto.pdf    # Full-text PDF
├── market-frictions-in-crypto.bib    # BibTeX citation
└── metadata.json                     # Structured metadata
```

### File Templates

#### BibTeX Template (`.bib`)

```bibtex
@article{author2025keyword,
  title   = {Paper Title Goes Here},
  author  = {Lastname, Firstname and Lastname, Firstname},
  journal = {Journal Name},
  year    = {2025},
  volume  = {1},
  number  = {1},
  pages   = {1--20},
  doi     = {10.xxxx/xxxxx},
  url     = {https://doi.org/10.xxxx/xxxxx},
  keywords = {keyword1, keyword2, keyword3}
}
```

#### Metadata Template (`metadata.json`)

```json
{
  "title": "Paper Title Goes Here",
  "authors": ["Firstname Lastname", "Firstname Lastname"],
  "year": 2025,
  "journal": "Journal Name",
  "doi": "10.xxxx/xxxxx",
  "url": "https://doi.org/10.xxxx/xxxxx",
  "abstract": "A brief abstract of the paper...",
  "keywords": ["keyword1", "keyword2", "keyword3"],
  "category": "finance",
  "submitted_by": "Your GitHub Username",
  "date_added": "2025-01-01"
}
```

### Category Reference

| Directory | Field |
|-----------|-------|
| `microeconomics/` | Microeconomics |
| `macroeconomics/` | Macroeconomics |
| `finance/` | Finance |
| `accounting/` | Accounting |
| `marketing/` | Marketing |
| `strategic-management/` | Strategic Management |
| `operations-management/` | Operations Management |
| `innovation-entrepreneurship/` | Innovation & Entrepreneurship |
| `human-resources/` | Human Resources |
| `public-economics/` | Public Economics |

### Naming Conventions

- **Folder name**: `kebab-case` (e.g., `digital-transformation-in-banking`)
- **File names**: Match the folder name (e.g., `digital-transformation-in-banking.pdf`)
- **BibTeX key**: `{firstauthorlastname}{year}{keyword}` (e.g., `smith2025digital`)

### Pull Request Checklist

- [ ] Paper is open-access
- [ ] Paper is in Economics or Management field
- [ ] All 3 files are included (PDF, BibTeX, metadata.json)
- [ ] BibTeX entry is valid and complete
- [ ] metadata.json is valid JSON with all required fields
- [ ] Files are placed in the correct `year/category/` directory
- [ ] Folder and file names follow naming conventions

## 📜 License

By contributing, you agree that your submissions comply with the original paper's license and that the repository structure files are released under the MIT license.

---

Thank you for making academic research more accessible! 🙏
