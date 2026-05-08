# 🎓 GradHub 贡献指南

感谢您对 GradHub 的关注!我们欢迎所有形式的贡献。

---

## 🤝 如何贡献

### 1. 报告问题 (Bug Reports)
如果您发现了任何问题,请创建 Issue:
- 使用清晰的问题描述
- 包含复现步骤
- 提供浏览器和操作系统信息
- 添加截图或录屏(如适用)

### 2. 提出功能建议 (Feature Requests)
我们欢迎新的功能建议:
- 描述您的功能需求
- 解释为什么这个功能对用户有帮助
- 提供使用场景示例

### 3. 代码贡献 (Code Contributions)

#### 开发环境
```bash
# 克隆仓库
git clone https://github.com/badhope/final-year-project.git

# 进入项目目录
cd final-year-project/gradhub

# 直接在浏览器中打开
open index.html
```

#### 开发流程
1. **Fork 仓库** - 点击右上角的 Fork 按钮
2. **克隆您的 Fork**
   ```bash
   git clone https://github.com/YOUR_USERNAME/final-year-project.git
   ```
3. **创建分支**
   ```bash
   git checkout -b feature/AmazingFeature
   ```
4. **进行更改** - 编辑 `index.html`、`css/` 或 `js/` 中的文件
5. **提交更改**
   ```bash
   git commit -m "Add: 添加了某个酷炫的功能"
   ```
6. **推送到您的 Fork**
   ```bash
   git push origin feature/AmazingFeature
   ```
7. **创建 Pull Request** - 在 GitHub 上发起 PR

---

## 📝 代码规范

### HTML
- 使用语义化标签 (`<header>`, `<main>`, `<article>`, `<section>`)
- 保持良好的可访问性 (ARIA 标签)
- 添加适当的注释

### CSS
- 使用 CSS 变量 (`var(--variable-name)`)
- 遵循 BEM 命名规范
- 保持选择器的简洁性
- 注释说明复杂样式

```css
/* ✅ 正确示例 */
.project-card {
  background: var(--color-bg-primary);
  border-radius: var(--radius-lg);
}

/* ❌ 避免 */
.project-card { background: #FFFFFF; border-radius: 12px; }
```

### JavaScript
- 使用 ES6+ 语法
- 添加适当的注释
- 保持函数简洁单一职责
- 避免全局污染

```javascript
// ✅ 正确示例
function initializeNavigation() {
  // 初始化导航逻辑
}

// ❌ 避免
function init() { /* 大量代码 */ }
```

---

## 🎨 设计规范

### 颜色系统
遵循 `css/variables.css` 中定义的颜色变量:
- 主色调: `--color-primary: #007AFF`
- 辅助色: `--color-secondary: #5856D6`
- 背景色: `--color-bg-primary: #FFFFFF`

### 圆角
- 小圆角: `--radius-sm: 8px`
- 中圆角: `--radius-md: 12px`
- 大圆角: `--radius-lg: 16px`

### 间距
使用 8px 基础间距系统:
- `--spacing-xs: 4px`
- `--spacing-sm: 8px`
- `--spacing-md: 16px`
- `--spacing-lg: 24px`

---

## 🔍 测试

在提交 PR 前,请确保:

- [ ] HTML 通过 W3C 验证
- [ ] CSS 没有语法错误
- [ ] JavaScript 在控制台无错误
- [ ] 响应式布局在移动端正常显示
- [ ] 所有链接都可正常访问

---

## 📜 许可证

通过贡献代码,您同意将您的代码按照 [MIT License](LICENSE) 许可证发布。

---

## 💬 讨论

欢迎加入我们的讨论:
- [GitHub Discussions](https://github.com/badhope/final-year-project/discussions)
- [Issues](https://github.com/badhope/final-year-project/issues)

---

## 🙏 感谢

感谢所有贡献者的付出! 🎉

---

<div align="center">

**让毕业设计不再困难** 💪

</div>
