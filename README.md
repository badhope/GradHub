# 🎓 GradHub - 毕业项目导航站

<div align="center">

![GradHub](https://img.shields.io/badge/GradHub-v1.0-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)

**专为计算机专业学生设计的毕业项目导航平台**

*从选题到实现,一站式解决方案*

</div>

---

## ✨ 特性

### 🎯 核心功能
- 🗂️ **多级导航系统** - 专业分类、技术栈、项目类型三级导航
- 🔍 **智能搜索** - 快速定位所需项目和技术栈
- 📊 **项目展示** - 清晰展示项目信息、技术栈、难度等级
- 📱 **响应式设计** - 完美支持桌面、平板、移动端
- 🎨 **唯美UI** - 现代简洁的亮色调设计

### 🎨 视觉特色
- ✨ **唯美亮色调** - 白色背景 + 科技蓝渐变
- 🎯 **圆润卡片设计** - 16px大圆角 + 柔和阴影
- 🚀 **流畅动画** - 卡片悬浮、渐入渐出、触摸反馈
- 📱 **移动优先** - 完美适配所有设备

### 🗂️ 内容分类
#### 专业分类
- 🖥️ 软件工程 - Java后端、Web全栈、移动开发
- 📊 数据科学 - 数据分析、数据可视化、BI报表
- 🤖 人工智能 - 机器学习、深度学习、NLP、计算机视觉
- 🔐 网络安全 - 渗透测试、安全开发、密码学
- 📡 物联网工程 - 嵌入式开发、智能家居
- ☁️ 云计算 - 容器化、云原生、DevOps
- 🎮 游戏开发 - Unity、Unreal、游戏AI
- 📱 计算机基础 - 算法、操作系统、计算机网络

#### 技术栈
- ⚛️ 前端: React、Vue、Angular、TypeScript
- ☕ 后端: Java、Python、Go、Node.js
- 🗄️ 数据库: MySQL、MongoDB、Redis
- 🐳 DevOps: Docker、K8s、CI/CD

#### 项目类型
- 🌐 Web应用 - 企业级、电商、社交
- 📱 移动应用 - iOS、Android、跨平台
- 🖥️ 桌面应用 - Electron、Qt
- 📈 数据分析 - 可视化、BI、报表

---

## 🚀 快速开始

### 方式一: 直接打开
```bash
# 直接在浏览器中打开 index.html
open gradhub/index.html
```

### 方式二: 本地服务器
```bash
# 使用Python服务器
cd gradhub
python -m http.server 8080

# 或使用Node.js
npx serve .

# 访问 http://localhost:8080
```

### 方式三: GitHub Pages (推荐)
项目已配置GitHub Pages,访问:
```
https://yourusername.github.io/final-year-project/
```

---

## 📂 项目结构

```
final-year-project/
├── gradhub/
│   ├── index.html          # 🎯 主页面
│   ├── README.md           # 📖 项目说明
│   ├── css/
│   │   ├── variables.css   # 🎨 CSS变量(颜色、间距、动画)
│   │   ├── base.css       # 📐 基础样式重置
│   │   ├── components.css # 🧩 组件样式(按钮、卡片、标签)
│   │   ├── layout.css    # 📐 布局样式(导航、页脚)
│   │   ├── animations.css # ✨ 动画效果
│   │   └── responsive.css # 📱 响应式设计
│   └── js/
│       └── main.js        # ⚙️ 交互逻辑
│
├── .github/
│   └── workflows/
│       └── deploy.yml     # 🚀 GitHub Actions部署配置
│
├── .gitignore             # 📝 Git忽略配置
├── README.md              # 📖 项目说明(本文件)
└── LICENSE                # 📄 MIT许可证
```

---

## 🎨 技术栈

### 前端技术
- **HTML5** - 语义化标记
- **CSS3** - CSS Variables、Flexbox、Grid、Animations
- **JavaScript** - ES6+、DOM操作、事件处理
- **Google Fonts** - Noto Sans SC、Inter字体

### 设计工具
- **CSS Variables** - 统一管理样式变量
- **Flexbox & Grid** - 现代布局系统
- **CSS Animations** - 流畅交互动画
- **Responsive Design** - 移动优先设计

### 可选升级
- [ ] React/Vue 版本
- [ ] TypeScript 重构
- [ ] PWA 支持
- [ ] 国际化(i18n)

---

## 📖 使用指南

### 1️⃣ 浏览项目
- 点击顶部导航栏的分类菜单
- 使用侧边栏筛选不同方向
- 点击卡片查看项目详情

### 2️⃣ 搜索功能
- 在搜索框中输入关键词
- 支持项目名称、技术栈、描述搜索
- 实时显示搜索结果

### 3️⃣ 贡献项目
- 点击右上角"贡献项目"按钮
- 填写项目信息和链接
- 提交审核后即可展示

---

## 🔧 自定义开发

### 修改颜色主题
编辑 `css/variables.css`:
```css
:root {
  --color-primary: #007AFF;      /* 主色调 */
  --color-secondary: #5856D6;  /* 辅助色 */
  --color-accent: #34C759;      /* 强调色 */
  /* ... 其他变量 */
}
```

### 添加新分类
编辑 `js/main.js` 中的导航数据结构:
```javascript
const navigationData = {
  major: {
    "new-category": {
      label: "新分类",
      icon: "🆕",
      children: {
        // 子分类...
      }
    }
  }
};
```

### 添加项目卡片
在 `index.html` 中添加新的 `<article class="project-card">` 元素

---

## 🚀 部署

### GitHub Pages
项目已配置自动部署,推送到main分支后自动生效:

```bash
git push origin main
# 访问 https://yourusername.github.io/final-year-project/
```

### Vercel / Netlify
```bash
# Vercel
vercel --prod

# Netlify
netlify deploy --prod
```

### 自定义域名
1. 在GitHub仓库设置中添加自定义域名
2. 创建 `CNAME` 文件
3. 配置DNS解析

---

## 🤝 贡献指南

欢迎贡献项目!

### 贡献方式
1. ⭐ Star 本项目
2. 🍴 Fork 本项目
3. 🔀 创建分支 (`git checkout -b feature/AmazingFeature`)
4. ✔️ 提交更改 (`git commit -m 'Add AmazingFeature'`)
5. 📤 推送到分支 (`git push origin feature/AmazingFeature`)
6. 🔃 创建 Pull Request

### 项目规范
- 使用语义化的HTML标签
- 遵循CSS变量命名规范
- 保持代码简洁清晰
- 添加适当的注释说明

---

## 📊 数据统计

| 指标 | 数值 |
|------|------|
| 专业分类 | 8个 |
| 项目总数 | 100+ |
| 技术栈 | 50+ |
| 项目类型 | 4大类 |

---

## 🐛 问题反馈

如果您发现任何问题或有改进建议:
- 📝 [提交Issue](https://github.com/badhope/final-year-project/issues)
- 💬 [Discussion](https://github.com/badhope/final-year-project/discussions)
- 📧 发送邮件: badhope@example.com

---

## 📄 许可证

本项目采用 [MIT License](LICENSE) 许可证。

---

## 🙏 致谢

- [Google Fonts](https://fonts.google.com/) - 提供了优质的字体
- [GitHub](https://github.com/) - 代码托管和Pages服务
- 所有贡献者和用户

---

<div align="center">

**Made with ❤️ for Computer Science Students**

**为计算机专业学生而生** 🎓

</div>
